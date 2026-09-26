# Flujo editorial de *El dispositivo caldereño* — versión 1

Fijada el 26/09/2026. Unifica los proyectos «BOLETINES CALDERA» y «EL DISPOSITIVO CALDEREÑO» en uno solo, con un único estado y un único punto de entrada.

**La meta:** que los 119 años de 1908 a 2026 estén leídos a nivel imagen e incorporados al libro. Los que no tienen PDF cuentan como límite declarado, no como pendiente.

---

## 0 · Qué cambia respecto del plan original, y por qué

El plan tenía cinco pasos:

1. leer el Boletín por año;
2. OCRizarlo;
3. completar el libro;
4. puntuarlo;
5. mejorarlo.

Proponía tres rúbricas: DESCARGA (1 y 2), AMPLÍA (3) y MEJORA (4 y 5). Se mantiene la idea con un ajuste: **el OCR no puede hacerse en una sesión**. La rúbrica LEE v16 lo midió en todas las sesiones de 1911 a 1932: un solo núcleo y un Tesseract sin español. Por eso el trabajo se reparte según quién puede hacerlo:

| Paso | Quién | Palabra clave o comando |
|---|---|---|
| Bajar el año, OCR, pre-informe y subir las salidas | **La máquina**, sin supervisión | `2-descargar.bat` o `noche.bat` |
| Leer el año con juicio: fichas, tablas, ausencias | **Una sesión** | `LEE <año>` |
| Completar el libro con lo leído | **Una sesión** | `AMPLÍA <años>` |
| Puntuar y corregir | **Una sesión** | `MEJORA` (acepta también `CORRIGE`) |
| Poner cada entrega en su lugar y actualizar el estado | **La máquina** | `3-registrar.bat` |
| Decir qué sigue | **La máquina** | `1-siguiente.bat` |

**DESCARGA no es un prompt: es un comando.** Una sesión no la puede hacer. Si alguien la escribe en el chat, la sesión responde con el comando que corresponde.

---

## 1 · Instrucciones del proyecto

Esto se pega **tal cual** en las instrucciones del proyecto de Claude y reemplaza a las instrucciones de los dos proyectos anteriores.

```
FLUJO EDITORIAL — fuente única

Las reglas, el estado y los registros viven en el repositorio público
ediedrich/corrige. No se usan copias de conversaciones anteriores, de la
memoria ni de los archivos del proyecto. Antes de trabajar, según la palabra
clave del mensaje, se bajan estos archivos (primera acción de la respuesta):

  B=https://raw.githubusercontent.com/ediedrich/corrige/main
  curl -fsSL $B/flujo-editorial.md     -o /home/claude/flujo.md      (siempre)
  curl -fsSL $B/estado/estado.json     -o /home/claude/estado.json   (siempre)
  LEE:      curl -fsSL $B/rubrica-lee-v16.md    -o /home/claude/lee-v16.md
            curl -fsSL $B/config/lee_config.json -o /home/claude/lee_config.json
  AMPLÍA:   git clone --depth 50 https://github.com/ediedrich/dispositivo-caldereno
  MEJORA/CORRIGE:
            curl -fsSL $B/rubrica-corrige.md     -o /home/claude/rubrica.md
            curl -fsSL $B/registro-cobertura.md  -o /home/claude/registro-cobertura.md
            git clone --depth 50 https://github.com/ediedrich/dispositivo-caldereno

Palabras clave: ESTADO · LEE <año> · LEE <año> complemento <ediciones> ·
LEE lote <a>-<b> · LEE cruce <a>-<b> · AMPLÍA <años> · MEJORA (= CORRIGE).
Lo que cada una hace está en flujo.md (§2 y siguientes); se lee entero.

Reglas:
1. Si una descarga falla, se dice en una línea y NO se trabaja con una
   versión recordada. Sin rubrica.md no hay nota. Sin registro-cobertura.md
   la cobertura acumulada es cero. Sin la rúbrica LEE no hay informe LEE.
2. Si el mensaje trae pegada una versión de una rúbrica, vale la del mensaje
   y se dice que no es la del repositorio.
3. La primera línea de la salida nombra la rúbrica, su versión y el tipo de
   trabajo: «Rúbrica 3.x — ronda de auditoría», «LEE v17 — 1951», «AMPLÍA v1
   — 1947-1949».
4. Las entregas llevan los nombres fijos de flujo.md §9, porque una máquina
   las registra sin leerlas. Un archivo con otro nombre se pierde.
5. Nadie escribe en los repositorios desde la sesión. Eduardo baja las
   entregas y corre 3-registrar.bat, que las pone en su lugar.
6. No se pide confirmación para empezar. Si el trabajo no cabe en un turno,
   se entrega lo hecho con sus nombres fijos y se dice qué falta.
7. DESCARGA <año> no se hace en sesión: se contesta con el comando
   «2-descargar.bat <año>».
```

---

## 2 · Palabras clave

| Palabra clave | Qué hace | Qué entrega (nombres en §9) |
|---|---|---|
| `ESTADO` | Lee `estado.json` y responde: cuántos años en cada nivel, qué sigue y qué pendientes están abiertos. No trabaja sobre el libro. | Nada, sólo la respuesta |
| `LEE <año>` | Informe LEE completo del año (§5) | Informe LEE y, si cambió, `lee_config.json` |
| `LEE <año> complemento <ediciones>` | Informe sólo de las ediciones nuevas de un año ya leído | Informe LEE del complemento |
| `LEE lote <a>-<b>` | Varios años de pocos candidatos en una sesión, con un informe por año | Un informe por año |
| `LEE cruce <a>-<b>` | Cruce de informes ya entregados (v16 §17) | Archivo `LEE-cruce-…` |
| `AMPLÍA <años>` | Incorpora al libro lo leído en esos años (§6) | `amplia-….patch` y `amplia-….json` |
| `MEJORA` o `CORRIGE` | Ronda CORRIGE con fase 6 (§7) | `ronda-N.patch`, `registro-cobertura.md` y `mejora-ronda-N.json` |

`1-siguiente.bat` elige la palabra clave que toca y la deja en el portapapeles.

---

## 3 · El ciclo y su orden

```
  noche.bat ──► Release del año con OCR, textos y pre-informe
      │
      ▼
  LEE <año> (sesión) ──► 3-registrar ──► estado: año leído
      │  (cada 3 años leídos)
      ▼
  AMPLÍA <años> (sesión) ──► 3-registrar ──► parche aplicado al libro
      │  (después de cada AMPLÍA)
      ▼
  MEJORA (sesión) ──► 3-registrar ──► ronda registrada, nota
      │
      └──► 1-siguiente.bat vuelve a empezar
```

**Prioridades de `siguiente`**, de mayor a menor:

1. **Entregas sin registrar.** Primero se registra.
2. **Un AMPLÍA sin MEJORA posterior.** Lo nuevo se audita antes de seguir sumando: es el material donde la rúbrica CORRIGE encuentra la mayoría de los errores.
3. **Complementos.** Son las ediciones recién obtenidas de años ya leídos: 1913, 1915, 1917, 1920 y 1922. Van primero porque tocan afirmaciones que el libro ya hace.
4. **AMPLÍA** en cuanto hay 3 años leídos sin incorporar, o antes si no queda nada para leer.
5. **LEE** del primer año procesado sin informe. Se usa `LEE lote` si hay 3 o más años seguidos con 3 candidatos o menos cada uno.
6. **Descargar** los años siguientes.

**Orden de los años** (`orden_anios` en `proyecto.json`, se puede cambiar):

- **1947 a 1950.** Pasan de barrido a imagen, y 1947 y 1948 tienen 157 ediciones nuevas.
- **1951 a 2026.** Es terreno nuevo.
- **1933 a 1945.** El libro ya los leyó por imagen, pero sin informe LEE formal. Se regularizan al final.
- **1908 a 1932.** Ya tienen informe; sólo entran por complemento.

**Por qué AMPLÍA cada tres años y no cada uno.** Un parche de tres años es chico, así que choca poco con las rondas MEJORA. Además, el repaso de superlativos y ausencias que exige la rúbrica al crecer la ventana se hace una vez por tramo y no una vez por año.

---

## 4 · Niveles de cobertura de un año

`estado.json` lleva un nivel por año, `libro.nivel`, y AMPLÍA lo sube:

| Nivel | Qué significa | Qué puede afirmar el libro sobre ese año |
|---|---|---|
| `imagen` | Todas las ediciones leídas, y las fichas miradas en la imagen | Presencias y **ausencias** («no aparece en ninguna edición de…») |
| `barrido` | Barrido completo por texto o pre-informe, sin lectura sobre la imagen | Presencias; **ninguna ausencia** |
| `puntual` | Consultas sueltas | Sólo lo citado, con su edición |
| `ninguno` | Nada | Nada |

**Regla:** un año sube a `imagen` sólo si el informe LEE está COMPLETO y su §R dice `nivel_lectura: imagen` (§5.3). Un año sin PDF en el Release no puede pasar de `puntual`, y el libro lo declara como límite.

---

## 5 · LEE v17 — cambios sobre v16

**Fuente:** `rubrica-lee-v16.md` entera, más estos cambios. Donde este apartado dice otra cosa, rige esto. La primera línea de la salida es «LEE v17 — <año>».

### 5.1 · Insumos: todo sale del Release y de corrige

La máquina ya corrió `lee_auto.py` y subió todo al Release del año, así que la sesión no le pide nada a Eduardo:

```bash
Y=1951; R=https://github.com/ediedrich/boletines-salta/releases
curl -sL $R/expanded_assets/$Y -o exp.html     # inventario (v16 §1.1)
# todo lo que no es un PDF de edición: pre-informe(s), CSV, log, zips, config, avisos
grep -oE "releases/download/$Y/[^\"]+" exp.html | sed 's#.*/##' | sort -u \
  | grep -vE '^[0-9]+\.pdf$' | while read f; do
      curl -fsSL -o "$f" "$R/download/$Y/$f" || echo "no llegó: $f"; done
ls BO-Salta-${Y}_*PRE-INFORME*.txt | sort | tail -1   # el pre-informe vigente es el de fecha más nueva
# PDF: sólo los que hacen falta mirar, o el año entero:
# seq <a> <b> | xargs -P 8 -I{} curl -fsSL -o pdf/{}.pdf $R/download/$Y/{}.pdf
```

- **El pre-informe** se llama `BO-Salta-<año>_la-caldera_PRE-INFORME-LEE_<fecha>.txt`. Si hay más de uno (una corrida vieja y una nueva), **vale el de fecha más nueva**, y el §0 dice cuál se usó.

- **`lee_textos_<año>.zip`** trae los `.txt`, `.tsv` y `EXTRAIDO.json` de `lee_trabajo`. Con él hay **segunda versión y confianza por hoja**, así que ya no rige el límite de v16 §2.1.
- **Si falta** el zip de textos o el pre-informe, se trabaja como en v16 §2.1 y se declara en el §0. No se reclama.

### 5.2 · El config es uno solo

Reemplaza a v16 §15.4. **El único config válido es `corrige/config/lee_config.json`.** La copia que queda en cada Release es la foto del config con que se procesó ese año, y sirve sólo para saber con qué se barrió. En el §0 se escriben los dos, la `version` y el `hasta` de cada uno. Si la foto del Release es más vieja que el config de corrige, se agregan las búsquedas que falten y se dice.

**Si la sesión cambia el config** (v16 §15.3), entrega el `lee_config.json` completo, con `version` = fecha de hoy y `hasta` = año barrido. `registrar` rechaza cualquier config con una `version` más vieja que la del repositorio.

### 5.3 · Tres claves nuevas en el §R

Se suman a las de v16 §10.2:

```
nivel_lectura: imagen            (imagen | capa)
pdf_release: 236                 (PDF reales del Release, sin avisos)
avisos_release: 0                (avisos de «no se encontró»)
```

- `nivel_lectura: imagen` sólo si **toda** ficha del §A y del §B se miró en la imagen. Con una sola ficha leída sólo de la capa, el valor es `capa`.
- `registrar` lee el §R y lo copia en `estado.json`.

### 5.4 · Modos nuevos

- **`LEE <año> complemento <ediciones>`.** El corpus son sólo esas ediciones. Rigen todas las reglas, **más** una: el informe dice qué afirmaciones del informe anterior del año cambian con lo nuevo (ausencias, superlativos, recuentos, cadenas de saldos), cada una con su ficha. El nombre lleva el rango de ediciones del complemento.
- **`LEE lote <a>-<b>`.** Sólo para años donde el pre-informe da 3 candidatos o menos. Cada año tiene su informe completo y su §R. Las pasadas de control (laxa espaciada, difusa, anillo de actores) se corren igual en todos: **un año sin menciones se afirma con las cuatro pasadas probadas, no con el pre-informe**. Si un año resulta tener más de lo que decía el pre-informe, sale del lote y se dice.

### 5.5 · Años con muchas ediciones (1944 en adelante)

A partir de 1944 hay entre 150 y 280 ediciones por año, contra 50 antes. El presupuesto de v16 §14.4 (cuatro turnos) se mide en los primeros años de esa época y se corrige en el §F. Si un año no cabe, se entrega **CON PENDIENTES** y el pendiente queda nombrado. Eso es preferible a un informe COMPLETO que no miró lo que dice haber mirado.

---

## 6 · AMPLÍA v1 — completar el libro con lo leído

La primera línea de la salida es «AMPLÍA v1 — <años>».

### 6.1 · Qué es y qué no es

AMPLÍA lleva al libro lo que los informes LEE de esos años establecieron. Hace cuatro cosas:

1. entradas nuevas en la cronología;
2. correcciones de lo que el libro afirmaba y lo nuevo desmiente;
3. ausencias que dejan de serlo;
4. declaraciones de cobertura actualizadas.

**No** es una ronda CORRIGE: no puntúa. Tampoco reescribe capítulos. Toda frase nueva sale de una ficha de un informe LEE.

### 6.2 · Insumos

- El libro (`git clone` de `dispositivo-caldereno`), compilado antes de tocar nada.
- Los informes LEE de esos años, desde `corrige/lee/<año>/`, o desde el Release si no están ahí.
- De `estado.json`: los `pendientes` abiertos cuyo campo `anios` cae en el rango, más los de tipo `libro` sin año.

### 6.3 · Procedimiento

1. **Índice de afirmaciones del libro sobre esos años.** Se buscan por script en todo el manuscrito:
   - los años;
   - los números de edición del rango;
   - las fórmulas de ausencia: «no aparece», «ningún», «ninguna», «no registra», «no consta», «no encontró», «nunca»;
   - los superlativos: «el primero», «la primera», «único», «única», «el más», «por primera vez»;
   - las declaraciones de cobertura en la Advertencia, en el capítulo de método y en los apéndices F (fuentes) y D (pedidos).

   El índice se entrega con su **denominador**: cuántas coincidencias hubo y cuántas se revisaron.
2. **Clasificar cada ficha del §A y del §B** de los informes contra ese índice:

   | Clase | Qué es |
   |---|---|
   | NUEVO | El libro no lo tiene |
   | CONFIRMA | El libro ya lo dice |
   | PRECISA | Mismo hecho, mejor dato: fecha, número, hoja |
   | CONTRADICE | Lo nuevo desmiente al libro |
   | CAE-AUSENCIA | Una ausencia del libro deja de serlo |
   | CAE-SUPERLATIVO | Un «primero» o «único» deja de serlo |

3. **Dónde va cada cosa:**

   | Clase | Destino |
   |---|---|
   | NUEVO que toca al departamento | Una entrada en la cronología, con edición y hoja |
   | NUEVO que cambia un argumento o responde un pedido de D | Además, en el capítulo que corresponde, **en su sección existente**, sin crear secciones nuevas |
   | PRECISA | Se corrige el dato donde esté, en todas sus menciones |
   | CONTRADICE, CAE-AUSENCIA, CAE-SUPERLATIVO | Se corrige la frase, y si la frase sostenía un argumento, se dice en la entrega qué argumento cambia |
   | CONFIRMA | No se toca, pero se cuenta |

4. **Cobertura.** Hay que actualizar:
   - las ventanas de años y ediciones en la Advertencia, el capítulo de método y el apéndice F;
   - la lista de ausentes, con la constancia de los sondeos;
   - los pedidos de D que queden satisfechos.

   Un año que llega a `imagen` habilita ausencias sobre ese año. Uno que queda en `barrido`, no.
5. **Repaso de ventana** (regla de la rúbrica CORRIGE). Toda afirmación del índice del paso 1 cuyo universo incluye los años nuevos se vuelve a juzgar, aunque ninguna ficha la haya tocado.
6. **Pendientes.** Se trabajan los pendientes abiertos del rango. Los que se cierran van en `pendientes_cerrados`. Los que aparecen, en `pendientes_nuevos`.

### 6.4 · Reglas de escritura

- **Prosa del libro:**
  - castellano rioplatense, en el registro del libro;
  - sin listas nuevas en el cuerpo;
  - sin lenguaje de proceso («hasta ahora», «una versión anterior decía»), salvo en los apéndices metodológicos;
  - toda cita, con edición y hoja.
- **Si una frase se puede corregir sin agregar renglones, se corrige así**, para que no caduque la cobertura de CORRIGE sobre ese tramo. Si hace falta agregar renglones, se agregan, y la entrega lista los archivos que cambiaron de largo.
- **Remisiones a capítulos posteriores**, marcadas («más adelante»).
- **Nada de figuras nuevas sin script publicado.** Una tabla nueva de la cronología no es una figura.
- **Superlativos:** la sesión corre la búsqueda de superlativos sobre el texto agregado, y cada uno lleva su universo declarado.
- **Se compila al final:** tiene que compilar, sin referencias indefinidas, y el número de láminas del `.lof` tiene que coincidir con el que dice el texto.

### 6.5 · Entregables

- **`amplia-<a>-<b>.patch`** (o `amplia-<a>.patch` si es un solo año), hecho con `git format-patch -1` sobre el `HEAD` clonado. Un solo commit, con mensaje `AMPLÍA <años>: <n> entradas, <m> correcciones`.
- **`amplia-<a>-<b>.json`**:

  ```json
  {"anios": [1947, 1948, 1949], "nivel": "imagen",
   "nivel_por_anio": {"1949": "barrido"},
   "base": "<sha del HEAD clonado>",
   "indice": {"coincidencias": 412, "revisadas": 412},
   "fichas": {"NUEVO": 31, "CONFIRMA": 12, "PRECISA": 4, "CONTRADICE": 2,
              "CAE-AUSENCIA": 3, "CAE-SUPERLATIVO": 1},
   "archivos_que_cambian_de_largo": ["ape/A-cronologia.tex"],
   "pendientes_cerrados": ["P06"],
   "pendientes_nuevos": [{"id": "P15", "tipo": "libro", "anios": [1949],
                          "texto": "…", "abierto": "2026-10-01", "hecho": null}]}
  ```

- **En el chat:** hasta diez renglones con lo que cambió de fondo. No se repite el parche.

---

## 7 · MEJORA v1 — puntuar y corregir

MEJORA es una ronda CORRIGE. **La rúbrica es `rubrica-corrige.md` del repositorio y rige entera**: versión, cobertura, topes, fase 6, avance y calidad de la auditoría. Este apartado sólo agrega cuatro cosas:

1. **Prioridad de lectura.** Primero se audita el material que entró con el último AMPLÍA: el `.json` de ese AMPLÍA lista los archivos tocados, y `git log` da el diff. Después se lee lo necesario para subir la cobertura acumulada al escalón siguiente.
2. **Fase 6 siempre que la sesión alcance.** Si no alcanza, se entregan la nota inicial y los hallazgos, y se dice.
3. **Pendientes.** Los abiertos de `estado.json` se tratan como hallazgos ya conocidos. Se cierran si la fase 6 los resuelve, y se abren los nuevos.
4. **Entregables con nombre fijo:**
   - **`ronda-<N>.patch`**, un commit sobre el `HEAD` clonado.
   - **`registro-cobertura.md`**, con el bloque nuevo al final y sin tocar los anteriores. `registrar` lo rechaza si cambia un solo carácter de lo previo.
   - **`mejora-ronda-<N>.json`**:

     ```json
     {"ronda": 39, "tipo": "auditoria con fase 6", "rubrica": "3.6",
      "nota_inicial": 78.2, "nota_final": 86.0, "tope": 85, "cobertura": 31.4,
      "fecha": "2026-10-02", "hallazgos": 14, "aplicados": 14,
      "pendientes_cerrados": ["P03"], "pendientes_nuevos": []}
     ```

   - **`rubrica-corrige.md`**, sólo si la ronda propone una versión nueva.

---

## 8 · `estado.json`

Vive en `corrige/estado/estado.json`. **Nadie lo edita a mano**: lo escriben `caldera.py estado`, `descargar` y `registrar`. Las sesiones lo leen y no lo entregan.

```json
{
 "anios": {
  "1951": {
   "release":  {"pdf": 236, "avisos_pdf": 0, "avisos_txt": false,
                "preinforme": true, "textos": true, "informes_lee": [], "revisado": "…"},
   "descarga": {"fecha": "…", "lee_auto": "<sha1>", "config": "2026-09-22",
                "pdf_bajados": 236, "candidatos": 7, "subidos": ["…"]},
   "lee":      {"informe": "BO-Salta-1951_…txt", "fecha": "…", "estado": "COMPLETO",
                "R": {"…": "…"}, "complemento": null},
   "libro":    {"nivel": "puntual", "incorporado": null, "nota": "…"}
  }
 },
 "rondas":     [{"ronda": 38, "nota_inicial": 75.8, "nota_final": 83.9, "…": "…"}],
 "pendientes": [{"id": "P01", "tipo": "libro", "anios": [1922], "texto": "…",
                 "abierto": "2026-09-24", "hecho": null}],
 "control":    {"mejora_pendiente": false}
}
```

- **`libro.incorporado`**:
  - `"previo"` para lo que el libro ya tenía antes de este flujo;
  - el sha del commit de AMPLÍA para lo que incorporó el flujo;
  - `null` si el año tiene informe LEE nuevo sin incorporar.
- **`lee.complemento`** tiene las ediciones de un año leído que todavía no se leyeron. Se vacía cuando llega su informe.

---

## 9 · Nombres fijos de las entregas

`3-registrar.bat` reconoce estos nombres y nada más. El sufijo « (1)» que agrega el navegador se ignora.

| Nombre | Qué hace `registrar` |
|---|---|
| `BO-Salta-<año>_<ed1>-<ed2>_la-caldera_LEE-<año>_<AAAA-MM-DD>.txt` | Lo sube al Release del año, lo guarda en `corrige/lee/<año>/`, lee su §R, marca el año como leído y lo deja pendiente de AMPLÍA |
| `LEE-cruce-<a>-<b>_<AAAA-MM-DD>.txt` | Lo guarda en `corrige/lee/cruces/` |
| `lee_config.json` | Si su `version` no es más vieja, lo instala en `corrige/config/` y en la carpeta de `lee_auto.py` |
| `amplia-<a>[-<b>].patch` + `.json` | Aplica el parche al libro con `git am`, hace push, sube el nivel de esos años y pide MEJORA |
| `ronda-<N>.patch` | Lo aplica al libro y hace push |
| `mejora-ronda-<N>.json` | Registra la ronda y apaga el pedido de MEJORA |
| `registro-cobertura.md` | Lo reemplaza en corrige, sólo si conserva intactos los bloques anteriores |
| `rubrica-corrige.md`, `rubrica-lee-v<N>.md`, `flujo-editorial.md` | Los reemplaza en corrige |

Si un parche no aplica, `registrar` lo deja donde está, no toca nada del libro y dice por qué. Casi siempre es porque se registró otro parche entre medio: la sesión siguiente lo rehace sobre el `HEAD` nuevo.

---

## 10 · Qué corrés vos y en qué orden

**Una sola vez:**

1. Hacé públicos `corrige`, `dispositivo-caldereno` y `mapas_caldera`. Es el pendiente P14: hoy dan 404 y ninguna sesión los puede leer.
2. Descomprimí `caldera.zip` dentro de `00  - LA CALDERA`, así queda `00  - LA CALDERA\caldera`. Las rutas de `proyecto.json` ya apuntan a `LIBRO` (el libro, que tiene que ser un clon de git), a `boletines` (la carpeta de `lee_auto.py`), a `corrige` (se clona ahí) y a `entregas`.
3. Doble clic en `0-instalar.bat`. Revisa Python, git, gh y Tesseract con español, comprueba que `LIBRO` sea un clon del repositorio del libro (si no lo es, te da los comandos para convertirlo sin perder nada), clona `corrige` y siembra `estado.json` y este archivo.
4. Guardá tu rúbrica LEE v16 como `rubrica-lee-v16.md` en Descargas y corré `3-registrar.bat`.
5. Pegá el bloque del §1 en las instrucciones del proyecto de Claude.
6. Corré `4-estado.bat`, que recalcula el estado contra GitHub.

**Todos los días:**

1. **`1-siguiente.bat`** te dice qué toca y deja el prompt en el portapapeles.
2. **Si es un prompt**, abrí una conversación nueva del proyecto, pegalo y bajá lo que entregue la sesión a Descargas.
3. **`3-registrar.bat`** registra las entregas y te dice el paso siguiente.
4. **Si es un comando de la máquina**, `2-descargar.bat` procesa los años que te indica. Para dejarlo corriendo de noche, usá `noche.bat`, que hace los próximos 10 años, o programalo:

   ```
   schtasks /create /tn CalderaNoche /tr "\"C:\Users\edudi\OneDrive\Documentos\Autismo\00  - LA CALDERA\caldera\noche.bat\"" /sc daily /st 23:30
   ```

**Espacio en disco.** `descargar` baja un año, lo procesa, sube las salidas y **borra los PDF y las imágenes de ese año** antes de pasar al siguiente. Sólo quedan los textos, que son livianos. Nunca hay más de un año pesado en el disco.

---

*Versión 1, 26/09/2026. La próxima versión la propone una ronda MEJORA o un informe LEE en su §F, y se entrega como `flujo-editorial.md` completo.*
