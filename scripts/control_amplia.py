#!/usr/bin/env python3
"""control_amplia.py — control automático de un AMPLÍA antes de entregarlo.

Corre sobre el diff entre la base clonada y el commit del AMPLÍA y marca, línea
por línea agregada o modificada, las seis clases de error que las rondas MEJORA
84 a 102 encontraron en el material de los AMPLÍA (diagnóstico del 14/10/2026):

  CITA    cadena entre comillas «...» que no está tal cual en la capa del año
          (NO-ENCONTRADA) o sólo está sin tildes (TILDES): se mira en la imagen.
  FECHA   fila de la cronología con asterisco cuya fecha es la de la edición
          que cita (fecha de publicación dada como fecha del acto), y fechas
          de «sanción»/«promulgación»/«publicación» para cotejar.
  CIFRA   número de tres o más dígitos, o escrito con punto o coma, que no está
          ni en el informe LEE del año ni en la capa: recuento o cálculo propio,
          que se rehace sobre la transcripción y se declara.
  IDENT   identidad entre personas («el mismo», «la misma persona»): el Boletín
          tiene que decirla; si no, se rotula como no afirmada.
  ALCANCE ausencias, unicidad y primacía («ningún», «nunca», «no se publica»,
          «el primero», «único», «sólo»): cada una con su universo (año entero,
          ediciones conservadas, ediciones leídas).
  VENTANA superlativos y ausencias de las frases vecinas de cada cambio (cinco
          líneas antes y después), que el dato nuevo puede desmentir.
  VERBO   verbos que deciden un acto (concede, renunció, nombra, remata, aprueba,
          adjudica, crea...): se cotejan con el verbo del acto en la ficha.
  ARRASTRE [ronda 118] la primera fórmula de remisión («también con pendientes»,
          «del mismo modo», «con la misma reserva», «como 1963») que sigue, en la
          misma línea, a un cambio que sube un año a «leído entero sobre la imagen».

No corrige nada. Entrega un informe; la sesión resuelve cada marca (corrige o
justifica) y lo resume en el .json del AMPLÍA, clave "control". Una marca
resuelta antes de compilar cuenta como «atrapada» (rúbrica CORRIGE 3.6).

Uso:
  python3 control_amplia.py --repo dispositivo-caldereno --base <sha> \
      --anio 1924 --textos lee_textos_1924.zip --informe BO-Salta-1924_...txt \
      [--anio 1925 --textos ... --informe ...] > control-amplia.txt
"""
import argparse, json, re, subprocess, sys, unicodedata, zipfile, collections

MESES = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6, 'jul': 7,
         'ago': 8, 'sep': 9, 'set': 9, 'oct': 10, 'nov': 11, 'dic': 12}
MESES_L = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
           'julio': 7, 'agosto': 8, 'setiembre': 9, 'septiembre': 9, 'octubre': 10,
           'noviembre': 11, 'diciembre': 12}

def sin_tildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def compacto(s, tildes=True):
    """Texto para buscar citas: une cortes, quita espacios y guiones de corte."""
    s = re.sub(r'\u00ad[ \t]*\n[ \t]*', '', s).replace('\u00ad', '')
    s = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', s)
    if not tildes:
        s = sin_tildes(s)
    s = s.lower()
    return re.sub(r'[\s\-—–\.,;:«»"\'`´’‘\(\)\[\]¡!¿?]+', '', s)

def latex_a_texto(s):
    s = re.sub(r'\\index\{[^}]*\}', '', s)
    s = re.sub(r'\\(?:textbf|textit|emph|texttt)\{', '', s)
    s = s.replace('\\ ', ' ').replace('~', ' ').replace('---', '—').replace('--', '–')
    s = s.replace('\\$', '$').replace('\\&', '&').replace('\\%', '%')
    s = re.sub(r'\\[a-zA-Z]+\*?(\{[^}]*\})?', '', s)
    return s.replace('{', '').replace('}', '')

def cargar_textos(zpath):
    hojas = {}
    with zipfile.ZipFile(zpath) as z:
        for n in z.namelist():
            m = re.match(r'(\d+)/(\d+)\.(prev|prop)\.txt$', n)
            if m:
                k = (int(m.group(1)), int(m.group(2)))
                hojas.setdefault(k, '')
                hojas[k] += '\n' + z.read(n).decode('utf-8', 'replace')
    return hojas

def fechas_de_edicion(hojas, anio):
    """Fecha de cada edición, leída de la tapa en la capa (texto sin espacios)."""
    out = {}
    for (ed, h), t in hojas.items():
        if h != 1:
            continue
        s = sin_tildes(re.sub(r'\s+', '', t[:1500])).lower()
        m = re.search(r'(\d{1,2})de(' + '|'.join(MESES_L) + r')de' + str(anio), s)
        if m:
            out[ed] = (int(m.group(1)), MESES_L[m.group(2)])
    return out

def _frases(linea):
    """Corta una línea en frases, con su posición (las líneas del libro pueden
    ser párrafos enteros)."""
    out, i = [], 0
    for m in re.finditer(r'(?<=[\.;:])\s+(?=[A-ZÁÉÍÓÚ\\«(¿¡]|---)|\s*\\\\\s*$', linea):
        out.append((i, m.end(), linea[i:m.end()]))
        i = m.end()
    if i < len(linea):
        out.append((i, len(linea), linea[i:]))
    return out

def _cambiado(viejo, nuevo):
    """Frases de la línea nueva que contienen texto que no estaba en la vieja."""
    import difflib
    tok = [(m.start(), m.end()) for m in re.finditer(r'\S+', nuevo)]
    sm = difflib.SequenceMatcher(None, viejo.split(), [nuevo[a:b] for a, b in tok], autojunk=False)
    pos = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('replace', 'insert'):
            pos += [tok[j][0] for j in range(j1, j2)]
    return [f for (a, b, f) in _frases(nuevo) if any(a <= p < b for p in pos)]

def diff_lineas(repo, base, head):
    """(archivo, línea, texto a controlar): la línea entera si es nueva; si es
    una línea modificada, sólo las frases que cambiaron."""
    import difflib
    d = subprocess.run(['git', '-C', repo, 'diff', '-U0', base, head, '--', 'cap', 'ape'],
                       capture_output=True, text=True, check=True).stdout
    out, f, n, viejas, nuevas = [], None, 0, [], []
    def cerrar():
        for (nn, l) in nuevas:
            mejor, r = None, 0
            for v in viejas:
                q = difflib.SequenceMatcher(None, v, l, autojunk=False).quick_ratio()
                if q > r:
                    mejor, r = v, q
            if mejor is not None and r > 0.6:
                for fr in _cambiado(mejor, l):
                    out.append((f, nn, fr))
            else:
                out.append((f, nn, l))
    for l in d.split('\n'):
        if l.startswith('+++ ') or l.startswith('@@') or l.startswith('diff '):
            cerrar(); viejas, nuevas = [], []
            if l.startswith('+++ '):
                f = l[6:]
            elif l.startswith('@@'):
                n = int(re.search(r'\+(\d+)', l).group(1))
        elif l.startswith('-') and not l.startswith('---'):
            viejas.append(l[1:])
        elif l.startswith('+'):
            nuevas.append((n, l[1:])); n += 1
    cerrar()
    return out

PAT_ARR = re.compile(r'\b(también,? (?:leíd[oa]s? )?con pendientes|también leíd[oa]s?|leíd[oa]s? del mismo modo|del mismo modo|de la misma manera|con la misma reserva|leíd[oa]s? igual|como (?:de )?\d{4}\b)', re.I)
PAT_NIVEL = re.compile(r'(entero|enteros|entera|enteras) sobre la imagen|leíd[oa]s? enter[oa]s?|cerrad[oa]s?', re.I)

def arrastres(repo, base, head):
    """[v4.1] ARRASTRE (causa 5 del flujo §6.6): cuando un cambio sube un año a
    «leído entero sobre la imagen», la primera fórmula de remisión que le sigue
    en la misma línea («también con pendientes», «del mismo modo», «con la misma
    reserva», «como 1963») pasa a remitir al nivel nuevo. Se marca para releerla.
    Rondas 117 y 118: diez frases desfasadas así, ninguna marcada por las otras clases."""
    import difflib
    d = subprocess.run(['git', '-C', repo, 'diff', '-U0', base, head, '--', 'cap', 'ape'],
                       capture_output=True, text=True, check=True).stdout
    out, f, n, viejas, nuevas = [], None, 0, [], []
    def cerrar():
        for (nn, l) in nuevas:
            mejor, r = None, 0
            for v in viejas:
                q = difflib.SequenceMatcher(None, v, l, autojunk=False).quick_ratio()
                if q > r:
                    mejor, r = v, q
            vieja = mejor if (mejor is not None and r > 0.6) else ''
            tok = [(m.start(), m.end()) for m in re.finditer(r'\S+', l)]
            sm = difflib.SequenceMatcher(None, vieja.split(), [l[a:b] for a, b in tok], autojunk=False)
            pos = []
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op in ('replace', 'insert'):
                    pos += [tok[j][0] for j in range(j1, j2)]
            hechos = set()
            for p in pos:
                m = PAT_NIVEL.search(l, max(0, p - 40), p + 60)
                if not m or m.start() > p + 40:
                    continue
                s = PAT_ARR.search(l, m.end())
                if s and s.start() not in hechos:
                    hechos.add(s.start())
                    out.append((f, nn, latex_a_texto(l[max(0, s.start() - 120):s.end() + 60]).strip()))
    for l in d.split('\n'):
        if l.startswith('+++ ') or l.startswith('@@') or l.startswith('diff '):
            cerrar(); viejas, nuevas = [], []
            if l.startswith('+++ '):
                f = l[6:]
            elif l.startswith('@@'):
                n = int(re.search(r'\+(\d+)', l).group(1))
        elif l.startswith('-') and not l.startswith('---'):
            viejas.append(l[1:])
        elif l.startswith('+'):
            nuevas.append((n, l[1:])); n += 1
    cerrar()
    return out

PAT_IDENT = re.compile(r'\b(el mismo|la misma|los mismos|las mismas)\b(?!\s+(año|mes|día|edición|hoja|acto|decreto|cargo|cuerpo|partido|circuito|lista|finca|martillero|juez|ejecución|forma|fecha|número|lugar|paraje|nombre))', re.I)
PAT_ALCANCE = re.compile(r'\b(ningún|ninguna|ninguno|nunca|jamás|no se publica\w*|se publica\w* en|no se repite|en el año|en todo el año|no consta|no aparece|no trae|no hay|sin un solo|el primer[oa]?|la primera|los primeros|las primeras|únic[oa]s?|sólo|solamente|el más|la más|por primera vez|(?:el|la) (?:segund|tercer|cuart|quint)[oa]?|siempre|todos? los años)\b', re.I)
PAT_VERBO = re.compile(r'\b(concede\w*|renunci\w*|nombr\w*|design\w*|remat\w*|aprueb\w*|aprob\w*|adjudic\w*|cre[aó]\w*|interv[ie]n\w*|suprim\w*|declar\w*|vend\w*|expropi\w*|deroga\w*|acepta\w*|revoca\w*|deja sin efecto)\b', re.I)
PAT_FECHA_REL = re.compile(r'\b(sancionad\w*|promulgad\w*|publicad\w*|dictad\w*|fechad\w*)\b', re.I)
PAT_CITA = re.compile(r'«([^«»]{4,400})»')
PAT_NUM = re.compile(r'(?<![\w\\])(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+,\d+|\d{3,})(?![\w])')
PAT_ED = re.compile(r'N[ºo°]\s*\\?\s*(\d[\d\.]{1,6})')
PAT_FILA = re.compile(r'^(\d{1,2})(?:\s*y\s*\d{1,2})?\s+([a-z]{3})\.\\?\s*(?:(?:y|a|--)\s*\d{1,2}\s+[a-z]{3}\.\\?\s*)?(\d{4})\*\s*&')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--base', required=True)
    ap.add_argument('--head', default='HEAD')
    ap.add_argument('--anio', action='append', type=int, required=True)
    ap.add_argument('--textos', action='append', required=True)
    ap.add_argument('--informe', action='append', required=True)
    a = ap.parse_args()

    capa_t, capa_s, informes, fechas = '', '', '', {}
    for anio, zp, inf in zip(a.anio, a.textos, a.informe):
        h = cargar_textos(zp)
        txt = '\n'.join(h[k] for k in sorted(h))
        capa_t += compacto(txt)
        capa_s += compacto(txt, tildes=False)
        informes += open(inf, encoding='utf-8').read()
        for ed, f in fechas_de_edicion(h, anio).items():
            fechas[ed] = (f[0], f[1], anio)
        # respaldo: la tabla del §1 del informe LEE («939 [05-01]», «1017 [05-07*]»)
        ti = open(inf, encoding='utf-8').read()
        i1, i2 = ti.find('§1 · CORPUS'), ti.find('§2 · CRITERIO')
        eds = set(e for (e, hh) in h)
        for m in re.finditer(r'(?<!\d)(\d{1,5})\s+\[?(\d{2})-(\d{2})\*?\]?', ti[i1:i2] if i1 >= 0 else ''):
            ed = int(m.group(1))
            if ed in eds and ed not in fechas:
                fechas[ed] = (int(m.group(2)), int(m.group(3)), anio)
    inf_num = set(re.sub(r'[\.,]', '', x) for x in PAT_NUM.findall(informes))
    inf_c = compacto(informes)
    capa_num = set(re.sub(r'[\.,]', '', x) for x in PAT_NUM.findall(capa_t))
    anios_txt = set(str(y) for y in range(1880, 2031))

    marcas = collections.defaultdict(list)
    lineas = diff_lineas(a.repo, a.base, a.head)
    archivos = {}
    for f, n, raw in lineas:
        if raw.count('«') > raw.count('»'):
            # cita que sigue en las líneas siguientes: se completa hasta cerrar
            if f not in archivos:
                archivos[f] = subprocess.run(['git', '-C', a.repo, 'show', f'{a.head}:{f}'],
                                             capture_output=True, text=True).stdout.split('\n')
            sig = archivos[f][n:n + 8]
            extra = ''
            for l in sig:
                extra += ' ' + l
                if (raw + extra).count('«') <= (raw + extra).count('»'):
                    break
            raw = raw + extra
        t = latex_a_texto(raw)
        donde = f'{f}:{n}'
        for c in PAT_CITA.findall(t):
            if len(c.split()) < 2 and not re.search(r'[A-ZÁÉÍÓÚ]', c[:1]):
                continue
            ct, cs = compacto(c), compacto(c, tildes=False)
            if not ct:
                continue
            if ct in capa_t:
                continue
            if cs in capa_s:
                marcas['CITA'].append((donde, f'TILDES — «{c[:90]}» está en la capa con otras tildes: mirar en la imagen'))
            elif ct in inf_c:
                marcas['CITA'].append((donde, f'SOLO-INFORME — «{c[:90]}» está en el informe LEE y no en la capa: mirar en la imagen (el informe puede estar errado)'))
            else:
                marcas['CITA'].append((donde, f'NO-ENCONTRADA — «{c[:90]}»: no está en la capa ni en el informe; mirar en la imagen o quitar las comillas'))
        if f.endswith('A-cronologia.tex'):
            m = PAT_FILA.match(raw)
            if m and m.group(2) in MESES:
                dia, mes, anio = int(m.group(1)), MESES[m.group(2)], int(m.group(3))
                for e in PAT_ED.findall(raw):
                    ed = int(e.replace('.', ''))
                    if fechas.get(ed) == (dia, mes, anio):
                        marcas['FECHA'].append((donde, f'la fila con asterisco lleva la fecha de la edición Nº {ed}: ¿es la del acto o la de la publicación?'))
        for m in PAT_FECHA_REL.finditer(t):
            marcas['FECHA'].append((donde, f'«{t[max(0, m.start()-60):m.end()+60].strip()}»: cotejar sanción, promulgación, publicación y fecha del acto'))
        for x in PAT_NUM.findall(t):
            k = re.sub(r'[\.,]', '', x)
            if k in anios_txt or k in inf_num or k in capa_num:
                continue
            marcas['CIFRA'].append((donde, f'{x}: no está en el informe LEE ni en la capa; si es recuento o cálculo propio, rehacerlo sobre la transcripción y decirlo'))
        for m in PAT_IDENT.finditer(t):
            marcas['IDENT'].append((donde, f'«{t[max(0, m.start()-70):m.end()+70].strip()}»: identidad entre personas o actos; ¿la dice el Boletín?'))
        for m in PAT_ALCANCE.finditer(t):
            marcas['ALCANCE'].append((donde, f'«{t[max(0, m.start()-70):m.end()+70].strip()}»: declarar el universo (año entero, ediciones conservadas, ediciones leídas)'))
        for m in PAT_VERBO.finditer(t):
            marcas['VERBO'].append((donde, f'{m.group(0)}: cotejar con el verbo del acto en la ficha'))

    # VENTANA: superlativos y ausencias del párrafo que rodea cada cambio (5 líneas
    # antes y después), aunque esa frase no haya cambiado: el dato nuevo puede
    # desmentirlos (rúbrica CORRIGE, repaso de ventana).
    PAT_SUP = re.compile(r'\b(ningún|ninguna|ninguno|nunca|jamás|el primer[oa]?|la primera|los primeros|las primeras|únic[oa]s?|el más|la más|por primera vez|siempre|(?:el|la) (?:segund|tercer|cuart|quint)[oa]?)\b', re.I)
    tocadas = set((f, n) for f, n, _ in lineas)
    vistas = set()
    for f, n in sorted(tocadas):
        if f not in archivos:
            archivos[f] = subprocess.run(['git', '-C', a.repo, 'show', f'{a.head}:{f}'],
                                         capture_output=True, text=True).stdout.split('\n')
        for k in range(max(1, n - 5), n + 6):
            if (f, k) in tocadas or (f, k) in vistas or k > len(archivos[f]):
                continue
            vistas.add((f, k))
            t = latex_a_texto(archivos[f][k - 1])
            for m in PAT_SUP.finditer(t):
                marcas['VENTANA'].append((f'{f}:{k}', f'«{t[max(0, m.start()-70):m.end()+70].strip()}»: frase vecina de un cambio; ¿la desmiente lo agregado?'))

    for f, n, fr in arrastres(a.repo, a.base, a.head):
        marcas['ARRASTRE'].append((f'{f}:{n}', f'«{fr}»: remite a la frase anterior, cuyo año acaba de cambiar de nivel; ¿sigue valiendo?'))

    print(f'CONTROL AMPLÍA — base {a.base}, {len(set((x[0], x[1]) for x in lineas))} líneas agregadas o modificadas ({len(lineas)} frases controladas), años {a.anio}')
    print(f'fechas de edición leídas en la capa: {len(fechas)}')
    for cl in ['CITA', 'FECHA', 'CIFRA', 'IDENT', 'ALCANCE', 'VENTANA', 'VERBO', 'ARRASTRE']:
        print(f'\n== {cl}: {len(marcas[cl])}')
        for d, msg in marcas[cl]:
            print(f'  {d}  {msg}')
    json.dump({k: len(v) for k, v in marcas.items()}, sys.stderr)

if __name__ == '__main__':
    main()
