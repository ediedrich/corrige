# RÚBRICA LEE v16 — barrido documental forense, modo híbrido por año

Reemplaza a v1–v15. Fechada el 22/09/2026.

**De dónde viene.**
- v4 (12/09/2026) sobre los barridos de 1935, 1940, 1941, 1945, 1951, 1980, 2002, 2015, el Decreto 1889/16, el Plan de Manejo y el Expte. INC-23860/1.
- v5 a v11, sobre los once barridos de 1946 (N° 2465 a 2744).
- v12 fijó el modo híbrido (1908 y 1909); v13 pasó las imágenes a GitHub; v14 se escribió tras 1911; v15 tras 1912 y corrigió la unión de cortes.

**Qué cambia en v16.** Se escribe tras **veinte años barridos seguidos, de 1913 a 1932**, y tras el primer cruce de esos veinte informes entre sí. Su corrección mayor no es de lectura sino **de salida**: los informes son correctos uno por uno y **no son cruzables entre sí**, porque los marcadores de sección cambian de año en año y porque el recuento final no es legible por máquina. Todo lo marcado **[v16]** es nuevo; lo anterior se conserva aunque ya no lleve marca.

**Los cinco defectos que motivan v16, con su caso:**

1. **Las listas que el informe transcribe no se recuentan.** Los informes de 1922 y de 1923 declararon los dos «veinticinco parajes» del Colegio Electoral; sus propias transcripciones traen **treinta y cuatro**. Dos años seguidos, el mismo error, y nada en v15 lo pedía. → §4.1bis.
2. **Los marcadores de sección no son estables.** Entre 1913 y 1932 conviven `§A ·`, `§A -`, `§A —`, `§D · INDICE`, `§D - INDICE` y `§D, la cadena anual`. Un script que quiera cruzar los veinte años falla en ocho. → §10.1.
3. **El config del Release puede estar atrasado y el barrido no lo comprueba.** Los barridos de 1930, 1931 y 1932 encontraron que el asset del Release cierra en 1915 (180 actores, 70 términos de anillo 2) mientras el vigente llega a 1928 (388 y 139). Lo declararon —bien— pero ninguna regla lo obligaba. → §15.4.
4. **El anillo 2 no se coteja contra la toponimia ya establecida.** Diecisiete topónimos del corpus ya fichado no están en el anillo 2, entre ellos «candelaria», que es justamente la forma con que 1922 imprime Calderilla; y diez apellidos están dentro de la lista de lugares. → §5.1bis.
5. **Un control muestral se declara como si fuera completo.** En 1925 la cabecera «Pág. N» se leyó en 24 de 746 hojas interiores y el informe habló de control de paginación sin decir el denominador hasta que se le preguntó. → §8.19.

---

## §0 · INVOCACIÓN

| Lo que se escribe | Lo que se hace |
|---|---|
| `LEE <año>` | Informe final del año: PDF del Release + resultados de `lee_auto.py` (§14) |
| `LEE <año> revisión` | Sólo la primera tanda (§14.4) |
| `LEE` | Si hay un solo año disponible, conmuta y lo declara. Corpus sin salidas del script: barrido completo en sesión (§16) |
| `LEE <término>` / `LEE <t1>, <t2>` | Acota los términos |
| `LEE índice` / `LEE todo` / `LEE planos` / `LEE ausencias` | Como en v11 |
| **[v16]** `LEE cruce <año1>-<año2>` | No barre: cruza los informes ya entregados de ese rango y entrega el §X (§17) |

**Reglas generales:**
- Nunca se pide confirmación.
- El informe va siempre a `/mnt/user-data/outputs/` como `.txt`, nunca en el chat.
- Los informes LEE anteriores no se barren: son referencia de actores, números de acto y saldos.
- Si el término satura el corpus (más del 30 % de las hojas), el §A pasa a modo `LEE todo` y se declara.

**Si el trabajo no cabe en un turno:** partes en `/home/claude/lee/partes/`, fichas en `notas.txt`; lo mirado se anota en la misma llamada o en la siguiente; al cerrar un turno se dice qué quedó sin anotar y si hubo entrega; el informe se rehace entero cada vez, con `armar.py` parcheado.

**COMPLETO frente a CON PENDIENTES.** **Pendiente** es trabajo que la sesión todavía puede hacer; **límite** es lo que el corpus o los insumos no permiten. Un informe cuyo único faltante son límites se declara **COMPLETO, con N límites declarados**, y los desarrolla en E.10.

Al cerrar un informe COMPLETO se dice, en una línea, **qué agregaría cada insumo que faltó**.

---

## §1 · HECHOS DEL ENTORNO

**Máquina del usuario** (Windows, carpeta `boletines` en OneDrive):

```
boletines\
  boletines\<año>\*.pdf
  salidas txt\<año>\*.txt
  lee_config.json
  lee_trabajo\<año>\<edición>\   N.jpg (300 dpi), N.prev.txt, N.prop.txt,
                                 N.prop.tsv; EXTRAIDO.json por edición
  lee_informes\<año>\            pre-informe, resultados_<año>.csv,
                                 decretos_<año>.csv, log.txt, recortes\
```

- `python lee_auto.py --anios 1913 --workers 6`, o `--solo-busqueda`.
- Tesseract en `C:\Program Files\Tesseract-OCR\tesseract.exe`, idioma `spa`.
- `gh` instalado; tras instalarlo hay que abrir otra ventana de PowerShell.

**Sesión** (se verifica al empezar):

```bash
file /mnt/project/* /mnt/user-data/uploads/* 2>/dev/null | cut -c1-120
nproc; python3 -c "import pymupdf" 2>/dev/null || pip install pymupdf --break-system-packages -q
tesseract --version; tesseract --list-langs
```

- **Núcleos.** `nproc` = 1 en todas las sesiones medidas: el OCR de un año entero no se hace en sesión.
- **PyMuPDF** no viene instalado; se instala desde pypi en segundos.
- **Tesseract viene sólo con `eng` y `osd`, sin `spa`**, en todas las sesiones medidas de 1911 a 1932. Se comprueba **antes** de prometer OCR. Sin `spa`, el §3 y el §16 no son aplicables y se declara en el §0.
- **Herramientas.** Hay `convert`, `montage`, `identify`, `unzip`, `git`, `curl`, `python3` con PIL y numpy. No hay `jq`, `exiftool` ni `gh`.
- **Red.** Alcanzables: `github.com`, `codeload`, `raw.githubusercontent`, `release-assets.githubusercontent`, pypi, npm. `api.github.com` responde 403. **No** alcanzables: el sitio del Boletín, Google Drive, OneDrive.
- **Trampas del `sh`:** no expande llaves ni acepta `<(…)`; `awk` cuenta bytes; un `grep` con UTF-8 roto hace fallar la herramienta; `ls … | xargs convert … salida.png` sobrescribe; `time` no existe.
- **Formatos.** Se corre `file` primero, siempre.

### 1.1 · Cómo llegan las imágenes

Un **Release por año** en `github.com/ediedrich/boletines-salta`, con los PDF sueltos como assets. Publicación desde `boletines` con el bucle de `gh release create` / `upload --clobber` de v15 (`.FullName`, `"${a}:"` con llaves).

**Qué hay en el Release, sin token:**

```bash
curl -sL https://github.com/ediedrich/boletines-salta/releases/expanded_assets/1913 -o exp.html
python3 -c "
import re
h=open('exp.html',encoding='utf-8',errors='replace').read()
print(sorted(set(re.findall(r'/releases/download/1913/([^\"\']+)',h))))"
```

Ese listado también dice **qué insumos NO llegaron**, y eso decide el modo de trabajo entero (§2.1). Se escribe en el §0 antes de prometer nada.

Bajada: `seq <a> <b> | xargs -P 8 -I{} curl -sL -o pdf/{}.pdf …`. Un año de esta época tarda segundos (1930: 51 PDF, 85 MB; 1932: 54 PDF, 145 MB, en una llamada).

---

## §2 · ÁRBOL DE DECISIÓN: ¿LEER EL TEXTO O OCRIZAR?

Se decide midiendo, nunca por época ni por analogía.

| Contenedor | Capa previa | Qué es |
|---|---|---|
| ZIP, `has_visual_content` = false, txt > 0 | nativa | Texto nativo: cifras fiables |
| ZIP o PDF, imagen + txt > 0 | OCR previo | Se valida con §2.3 |
| PDF sólo imagen, txt = 0 | ninguna | Sólo existe la versión propia |
| texto plano con extensión .pdf | — | Sumario u otro texto suelto: se declara |

### 2.1 · Reconstruir la capa previa en sesión

Cuando el año está en el Release y **no llegaron los `.txt`**, la sesión extrae en una llamada con PyMuPDF (`page.get_text()` por hoja) y mide, por hoja: caracteres, U+0002, U+00AD, número de imágenes y ppi de la imagen incrustada.

**Da:** las cuatro pasadas, anillo 2, actores, números, reemplazos, tapas, calendario, paginación, §A y §B completos.
**No da:** segunda versión, confianza por hoja, md5, dhash ni tinta. Se declara en §0 y en E.10.

### 2.3 · Validación del OCR previo

1. **Marca de corte U+0002.** Se cuenta qué la sigue antes de fijar la unión. En 1946 iba dentro de la palabra; en 1908–1932 no aparece.

2. **Guion blando U+00AD: se quita JUNTO CON EL SALTO DE RENGLÓN**, no como carácter suelto:

   ```python
   t = re.sub(r'\u00ad[ \t]*\n[ \t]*', '', t)   # primero: corte de renglón
   t = t.replace('\u00ad', '')                  # después: los sueltos
   ```

   Escrito al revés, «Cal␍dera» se vuelve «cal\ndera» y la mención se pierde en silencio. En 1912 escondió tres hojas durante dos turnos; en 1923 el mismo mecanismo escondía el decreto 349 sobre la comisaría.

3. **Corte con signos intercalados.** `Cal-,\n¡dera`. La unión tolera hasta dos caracteres de puntuación a cada lado del salto.

4. **Densidad y ruido.** Menos de 500 B por hoja es sospechoso; más del 25 % de caracteres no alfabéticos indica OCR roto, salvo sumarios, tapas y tablas.

5. **Columna perdida.** Modo de falla dominante; el script no la detecta. Se confirma con un renglón entero (`repr`) y la imagen. No se atribuye a columna perdida lo que no se miró. Con una sola versión el control es el cotejo columna por columna, **y se declara sobre cuántas columnas se miró**.

   **Lo que falla con una sola versión es la palabra suelta, y falla en silencio.** Casos medidos: «Tacones»/*Yacones*, «Cajdera», «Achejal» (1911); «Oaldfera», «Challe» (1912); «galdefa», «Cald#ra», «Masc-ief» (1922); «mivrua» y la desaparición de «Sosauya» (1932). **Toda palabra que decide una ficha se mira.**

6. **[v16] El nombre del departamento puede venir con las letras separadas, y entonces ninguna pasada literal lo devuelve.** En 1923 el original imprime «C A L D E R A» y «C ald era». La variante espaciada de la laxa (§5.2) **rescató tres actos que la literal no veía, y uno de ellos era el único acto de dominio del año**. No es una rareza de un año: es un modo de composición tipográfica de la época, y se prueba en todos.

**Cotejo sumario/cuerpo.** Números del sumario de **una** versión (la previa); cuerpo, la unión, excluidos los renglones de sumario de las hojas 1 a 4. Si no hay sumario con puntos guía o no hay capa previa, **«cotejo no aplicable»**: en 1908–1912 no hay sumario; de 1924 en adelante sí, y entonces el cotejo sumario/página citada es el control de completitud (§2.5bis).

**Unión de versiones**, obligatoria cuando existen las dos, con etiqueta `prev`, `prop` o `prev+prop`. El desempate es siempre la imagen.

### 2.5bis · Tapas, calendario, paginación y autoridad

- **Páginas.** «EDICIÓN DE N PÁGINAS» contra las hojas presentes.
- **Paginación corrida** (1908–1923): el folio impreso en la cabecera encadena de edición en edición dentro del año. Se lee desde la capa previa, en los primeros ~90 caracteres de la hoja. **No** se hereda entre años (1911 cierra en 1248, 1912 abre en 1152).
- El folio **distingue la edición corta de la edición incompleta**; el conteo de archivos no.
- La serie puede **avanzar de a uno donde debería avanzar de a cuatro**: se declara y no se explica.
- **[v16] Desde cierta época la foliatura reinicia en cada edición y el control cambia de naturaleza.** Medido: 1923 corre corrida hasta la edición 970 y **reinicia desde la 971**, con lo cual 322 de 673 hojas quedan sin ese control; 1924 a 1932 reinician siempre. Los dos reemplazos, por orden de fuerza:
  1. **Cotejo sumario/página citada.** El sumario de la hoja 1 remite a páginas; la más alta citada no puede superar las hojas presentes. En 1924 cerró en las 52 ediciones. **Es el control fuerte y se usa primero.**
  2. **Cabecera «Pág. N».** Vale cuando la capa la resuelve. En 1925 la resolvió en **24 de 746 hojas interiores**. Sirve, y **se declara con su denominador** (§8.19).
- **Calendario.** El día de la semana de cada tapa se coteja. Para los días de salida sin edición se buscan «feriado», «asueto», «Día del Pueblo», «adhiere/adherir/adhesión»; si no explican el hueco, se declara sin explicar y **no se busca la causa afuera**.
- **Los días de salida los declara la tapa** («Aparece Miércoles y Sábados», 1911 y 1912). **[v16] Pero puede no declararlos la tapa.** En 1927 la tapa no lleva la fórmula y **la declaración está en la tarifa del propio Boletín** («aparece los Viernes»). Antes de dar por indeterminados los días de salida se busca la tarifa.
- **La tapa puede fecharse en un día que su propia fórmula no admite** (cuatro casos en 1912). No es errata del OCR y no se concilia.
- **Ediciones dobles.** Antes de listar un día sin edición se mira la tapa vecina.
- **El año editorial se lee en la tapa, no en la capa previa.**
- **[v16] El nombre del gobernador tampoco se toma de la capa.** En 1926 la capa escribe «CORBACHO», «CORBfltón» y «CORBflltó» donde la tapa dice Corbalán. Autoridad y año editorial se leen en la imagen, siempre.
- **Las erratas de tapa se repiten por tandas** y se declaran una vez en E.9, no una por edición.
- **Autoridad por firmantes**, no sólo por la tapa: fórmulas de encabezado, decretos de apertura y cierre de ejercicio, interinatos, y quién firma el «Es copia». La fórmula varía dentro del mismo año y del mismo gobierno: se registran todas y no se normaliza.
- **Interinato sin cierre:** se declaran el último acto del interino y el primero del titular; no se fija el día del reintegro.

---

## §3 · RECETA DE OCR

- **Parámetros de `lee_auto.py`:** `-l spa --psm 3`, salidas `txt` y `tsv`, sin preprocesado; PDF rasterizados en gris a 300 dpi; ZIP desde su propio `jpeg`; corrida paralela, reanudable, con escritura atómica.
- **Confianza por hoja** (del `.tsv`): «pub» si la media ≥ 88 y ≤ 5 % debajo de 60; «ojos» si la media < 70 o más del 30 % debajo de 60; «ver» en el resto. **No sirven para 1908–1932.**
- **Lo que el OCR nunca resuelve:** texto en arco, cartelas, tablas y columnas desvaídas.
- **En sesión** el OCR se usa sólo para hojas sueltas y **sólo si hay `spa`**.

---

## §4 · LECTURA CON LOS OJOS — OBLIGATORIA

1. **Toda tabla escaneada** se mira y se recalculan sus totales.

   **Alcance.** Se recalculan completas: las tablas que nombran el término, el anillo 2 o un actor; los balances municipales del departamento; toda lista con total dentro de un acto del §A o del §B. De los balances de Tesorería se transcriben y encadenan los saldos; sólo se recalculan enteros los que no encadenan. Las demás van a E.8 como «no recalculadas», con hoja y criterio.
   - Cuando un acto toma un porcentaje de otro, se recalcula contra las dos bases posibles.
   - **Cuadro contra detalle:** si hay cuadro resumen y detalle en prosa, se suman las dos y se comparan. En 1926 los 44 renglones del detalle de la Ley 3610 cerraron exactos contra el total en cifras **y el que no cerró fue el total en letras**.
   - **Que la cadena de saldos cierre no prueba que el cuadro cierre:** se recalcula al menos un subtotal por cuadro publicado. En 1924, once de doce cuadros cerraron y el de marzo falló por exactamente dieciséis mil pesos, con el error en el detalle y no en el subtotal.
   - **Un año puede no tener ningún balance municipal**, y eso se declara como hecho del corpus, no como tabla sin mirar.
   - **La tabla que no se puede atribuir a una jurisdicción se declara sin atribuir.**

### 4.1bis · **[v16] Toda lista enumerada se recuenta sobre la propia transcripción**

Es la regla nueva más cara de haber faltado.

- **Qué se recuenta:** circuitos electorales, nóminas de parajes o partidos, listas de comisarios auxiliares, nóminas de autoridades de mesa, listas de localidades o departamentos, nóminas de encargados, enumeraciones de linderos, listas de expedientes.
- **Cómo:** se cuentan los elementos de la transcripción, no los del original «a ojo», y el resultado se escribe en la NOTA DE LECTURA como **RECUENTO PROPIO**.
- **Contra qué:** si el acto declara un número, se coteja; si no lo declara, se dice «el acto no declara número, de modo que no hay nada que cotejar» —que es lo que el informe de 1926 hizo bien—.
- **Dónde falla y cómo se evita.** El separador del original no es fiable: 1923 imprime «Cachanio. Despensa» con punto y «El Monte Las Garrapatas» sin coma; 1926 imprime «Campo Alegre Calderilla» sin coma. **Un elemento de cuatro palabras o más se marca como posible nombre pegado y se cuenta aparte**, de modo que el informe entrega un rango y no un número falso.
- **El caso.** Los informes de 1922 y 1923 declararon «veinticinco parajes» y sus transcripciones traen treinta y cuatro. Ninguno de los dos recontó. El error sobrevivió a dos barridos y sólo apareció al cruzar los años.

2. **Todo número que vaya a usarse** se mira: expediente, decreto, importe y fecha.
3. **Sellos, folios y firmas.** Un decreto puede imprimirse sin fórmula de promulgación y sin artículo 1°, otro sin cierre, fecha ni firma, y otro **saltar del artículo 1° al 3°** (1928, decreto 6958). Se transcribe lo que hay, se declara lo que falta, no se completa.
4. **Encabezados con fecha.**
5. **Hojas en blanco o con poca tinta** (menos del 5 %).
6. **Todo resultado de la laxa o la difusa** que no sea obviamente ruido.
7. **Sumarios con cotejo por acto.**
8. **Hojas «a ojos».** Sin `.tsv` no hay confianza por hoja y esta lista **no existe**: es un límite, va a E.10 con esas palabras, y se dice por qué vía se cubrieron las hojas.
9. **Decretos largos que traen a un actor:** todos los incisos.
10. **Listas de departamentos o localidades** que nombran el término: enteras.
11. **El encabezado de una lista se mira aunque esté en otra hoja.** También explica los renglones raros.

**Cómo mirar (modo híbrido):** `pymupdf`, `get_pixmap(dpi=250, colorspace=csGRAY, clip=Rect(...))`. Columnas por proyección vertical, medidas una vez por corpus con `page.get_text('words')`. **Recorte por el ancho entero de la columna + ~6 pt**, nunca por la coordenada de la palabra. Apilado de a dos en horizontal, nunca por encima de ~1.700 px de alto. Solape: el renglón repetido se declara. Cifras dudosas, 400 o 600 dpi.

---

## §5 · VOCABULARIO Y PASADAS

### 5.1 · Los tres anillos

- **Anillo 1:** «La Caldera», «Caldera» sin artículo, «La Calderilla» y variantes.
- **Anillo 2:** el vocabulario del config. Un topónimo del anillo 2 puede ser otra cosa: **se leen los contextos de TODOS los términos con acierto**, no sólo los que parecen del departamento.
- **Anillo 3:** limítrofes, con ficha y una línea.
- **Anillo de actores:** las personas de los actos del §A se buscan en todo el corpus, por nombre y apellido laxos, por nombre + inicial + apellido, y por apellido suelto agrupando por contexto; también las fórmulas de reemplazo.
  - La lista se arma con **todos** los informes anteriores.
  - Es también **la red de seguridad del anillo 1**: se corre siempre.
  - Se busca sobre el texto **con la puntuación suprimida**.
  - **Prohibido declarar ausente a un actor cuya búsqueda por nombre completo no devuelve ni siquiera su propio acto.** Eso es una falla de la búsqueda y se declara nombrando a los afectados.
  - Las ausencias del §B se escriben en tres grupos: los que sólo aparecen en su propio acto; los que aparecen en más de un acto del departamento; y los que aparecen también fuera de él. **El segundo grupo es el que arma la trama del año.**

### 5.1bis · **[v16] El anillo 2 se coteja contra la toponimia ya establecida, antes de barrer**

El anillo 2 crece por acumulación y nadie lo revisa. Medido sobre el config vigente al 22/09/2026 contra la toponimia establecida por los barridos:

- **17 topónimos ya establecidos no están en el anillo 2**, entre ellos **«candelaria»** —que es la forma con que 1922 imprime Calderilla en su propio circuito— y «estación f.c.c.n.a.», «mesada», «el sauce», «cañada ancha», «la helvecia», «getsemaní». **Un término que no está en el anillo no se ve pasar.**
- **10 apellidos están dentro de la lista de lugares**: apaza, aramayo, condori, chaile, isasmendi, murúa, nogales, toconas, castellanos, «burgos de yugra». Su acierto en el anillo 2 **no prueba vecindad territorial** y produce ruido en el §B.
- **44 términos no son ni topónimo establecido ni variante ni apellido**, y ahí conviven dos cosas distintas: topónimos de otros departamentos (betania, siancas, trancas, tabacal, cornisa) e **hidrónimos legítimos que la toponimia de parajes no cubre** (guaranguay, cuchimayo, cerro de buena vista, río de wierna, quebrada de lesser, arroyo castellanos). Los segundos no son basura: son la señal de que la lista de parajes no es la lista de lugares.

**Regla.** Antes de cada barrido se corre el cotejo y se declara su resultado en el §2 del informe, en tres líneas: cuántos términos establecidos faltan, cuántos son apellidos y cuántos quedan a revisar. **Los apellidos se mueven a `actores`; los faltantes se agregan; los de otros departamentos se conservan con la marca de su jurisdicción.**

### 5.1ter · **[v16] El anillo 2 no decide jurisdicción**

Que un topónimo esté en el anillo 2 no dice de qué departamento es, y el informe **no lo afirma sin fuente**. El caso: el informe de 1926 anotó que la nómina del «Vaqueros, Colegio Electoral N° 6» «es otro departamento». **Vaqueros fue parte de La Caldera hasta 1994**, y el propio decreto la imprime a continuación del Colegio 5 de La Caldera. La pertenencia de un lugar se toma del acto que lo atribuye —«Mojotoro (Caldera)», «Vaqueros (Caldera)», como los imprime el decreto de 1926— o se declara indeterminada.

### 5.2 · Las cuatro pasadas

| Pasada | Qué hace |
|---|---|
| Literal/normalizada | `cald` sobre NFD sin diacríticos, con los cortes unidos (U+0002, guion, **U+00AD + salto**, puntuación intercalada) |
| Laxa | `[gc][ao][l1i\|][dcl][ec][rnm][ao]`, más la **variante espaciada** |
| Difusa | ratio ≥ 0,78 contra `caldera` y `calderilla`, excluida la forma exacta |
| Anillo 2, actores, números, reemplazo | sobre la unión, o sobre la única versión |

- **[v16] La variante espaciada admite separador ENTRE CADA PAR DE LETRAS, no sólo «en el medio».** v15 decía «una variante que admite espacios y saltos de renglón en el medio», y así escrita no habría devuelto «C A L D E R A». La forma correcta intercala la clase entre todas las letras:

  ```python
  L = r'[\s\-]{0,3}'
  laxa_esp = L.join(list('caldera'))
  ```

  Y se escribe **con la clase de espacios en blanco**, nunca con un espacio literal, que no cruza el salto de renglón. En 1923 esta variante rescató tres actos del departamento de diecisiete, **uno de ellos el único de dominio del año**.
- **Una pasada que devuelve cero se prueba antes de darla por sana.** «Cero aciertos» puede querer decir «no hay nada» o «la pasada está rota». Se comprueba con otro patrón o contra otro corpus y se dice cuál de las dos es.
- Si el pre-informe dice «Ninguno» en el anillo 1, la sesión lo comprueba por su cuenta y con la difusa.
- **Difusa ampliada:** una vez por año, entre 0,70 y 0,78, restringida a palabras que empiezan con c, g u o.
- **La difusa rescata lo que la literal pierde:** «CaMera» (1909), «Cajdera» (1911), «Oaldfera» (1912). **[v16] Y puede no rescatar nada**: en 1923 sus seis formas fueron todas falsos positivos. Eso también se declara, porque decide si conviene correrla en la época siguiente.

### 5.3 · Identificadores múltiples

- **Toda ausencia se afirma con al menos dos identificadores.**
- Cuando los actos no llevan número, los identificadores son lugar, persona y organismo, y se declara que no hay numeración.
- **Un acto citado** se busca antes de listarlo como «citado y no acompañado».
- **Una vacante declarada sin nombrar al que la dejó es también un acto citado y no acompañado.** No se infiere quién era.
- **[v16] Un nombramiento que sólo consta porque otro acto lo revoca es el mismo caso, al revés, y se ficha igual.** En 1925 el decreto 2674 nombra subcomisario de Vaqueros «en reemplazo de D. Francisco S. Urquiza» y **el nombramiento de Urquiza no aparece en ningún tramo leído**. Lo que falta ahí es el principio y no el final, y se declara con esas palabras.

---

## §6 · DEDUPLICACIÓN Y SALDOS

- **Nivel 1:** md5 de las imágenes, nunca del contenedor.
- **Nivel 2:** dhash de 256 bits; pares a distancia ≤ 16. Sin las `.jpg` no hay md5 ni dhash: se declara y se controla por texto.
- **La marca de publicación de un aviso no prueba que se haya repetido.** La repetición se comprueba buscando el texto del aviso en el resto del corpus, y sólo así.
- **[v16] El número de aviso tampoco prueba nada, porque cambia entre apariciones del mismo acto.** En 1927 el remate de la finca Los Sauces sale **tres veces con tres números distintos** —(2188), (2233) y (2349)—, con el mismo texto, los mismos linderos y distinto día de remate. Cotejar números no lo habría reunido; cotejar texto sí. **La deduplicación por texto es el control primario y el número de aviso es sólo un indicio.** Y a la inversa: números repetidos suelen ser ruido del OCR en el paréntesis (1927: nueve de 387; 1928: seis de 249).
- **Tinta.** Menos de 0,5 % es hoja en blanco; menos de 5 % se mira. Sin las `.jpg` no hay medición: límite declarado. **[v16] Con PDF reales eso es falso y se corrige: la sesión rasteriza y mide.** En 1926, 1108 h16 dio 0,05 % de píxeles oscuros contra 6,79 % de su vecina, y quedó declarada hoja en blanco sin mirarla.
- **Nivel 3:** la misma serie numérica en actos distintos es un hallazgo y va a §A y E.9.
- **Saldos.** De todo balance se transcriben el saldo inicial y el de caja final; el final de un mes se coteja con el inicial del siguiente y contra los informes anteriores.
- **La cadena anual puede no existir: se cuentan los resúmenes antes de prometerla.** Medido: 1911, uno; 1912, cuatro; 1926, cinco no consecutivos con los que **no se puede armar ninguna cadena**; 1927, nueve; 1928, diez; 1929, once.
- **[v16] Una cadena puede armarse en tramos, y entonces se dice dónde se corta y con qué puente.** En 1927 faltan junio, julio, agosto y diciembre; el resumen de septiembre abre con «A Saldo del mes de Agosto $ 73.456,16», de modo que **el cierre de agosto queda registrado aunque su resumen no se publique**. La cadena se entrega en dos tramos y con un puente de una sola cifra, y así se declara. **[v16] Y un resumen puede no imprimir renglón de cierre**: entonces se encadena por la apertura del mes siguiente y se dice.
- **El rótulo del saldo puede mentir aunque la cifra sea correcta.** La cadena se arma **por la cifra, no por el rótulo**. Casos: 1912 («A saldo de Mayo» para el saldo de junio, y «1012» por 1912); 1922 («A SALDO DE JULIO DE 1922» para la cifra de mayo); 1926 (dos resúmenes rotulados «noviembre ppdo.», uno de ellos en abril, que es imposible).

---

## §7 · ESTRUCTURA DEL INFORME

`BO-Salta-<año>_<primera>-<última edición>_la-caldera_LEE-<año>_<AAAA-MM-DD>.txt`

**[v16] El nombre lleva la fecha en ISO (`2026-09-22`), no `21-09-2026` ni `_B` ni `__1_`.** Los veinte informes de 1913 a 1932 traen tres formatos distintos y dos sufijos de versión, y eso ya obligó a desambiguar a mano. Si hay una segunda entrega del mismo año, el sufijo es `_v2`, nunca `_b` ni `_B`.

- **§0 · Advertencia preliminar.** Estado: **COMPLETO** (con límites) o **CON PENDIENTES**. Versión y fecha de `lee_auto.py`, parámetros, config usado y errores del log; qué subió el usuario y qué no; de dónde salieron las imágenes y cómo se cotejaron; qué verificó la sesión; desvíos de §8.17.
- **§1 · Corpus revisado.** Tabla por edición con fecha, hojas contra declaradas, tipo y confianza. Las fechas leídas en la imagen, entre corchetes.
- **§2 · Criterio de búsqueda.** Versiones y etiquetas; pasadas; actores con su origen; números arrastrados; identificadores de las ausencias; **[v16] resultado del cotejo del anillo 2 (§5.1bis)**.
- **§A · Menciones explícitas.** Por aparición: FUENTE, FICHA, MODO DE LECTURA, TEXTO, NOTA DE LECTURA. Un aviso repetido es una sola entrada; un juicio publicado por entregas también, con tantas apariciones como entregas.
- **§B · Vecindad,** en cuatro bloques: B.1 núcleos ya fichados; B.2 núcleos del departamento en actos que **no** nombran el término; B.3 términos que ese año son otra cosa; B.4 ausencias del anillo de actores en tres grupos.
- **§C · Limítrofes. §P · Planos. §D · Índice.**
- **§E · Observaciones:** E.1 duplicación y saldos; E.2 cobertura; E.3 sin mención y no mirado; E.4 firmas y autoridad; E.5 cortes y columnas; E.6 repeticiones; E.7 falsos positivos y negativos; E.8 fidelidad numérica; E.9 contradicciones; E.10 límites.
- **§F · Corrección a la rúbrica.**
- **[v16] §R · RECUENTO LEGIBLE POR MÁQUINA** (§10.2).
- **Config actualizado**, si se entrega.

### 7.1 · **[v16] El §D se desglosa por materia, con una clasificación fija**

v15 pedía un índice y cada año lo escribió a su manera: 1929 por materia, 1927 y 1928 por edición, 1926 por edición con materia. **Cruzar los veinte años exige una clase fija.** Cada entrada del §D lleva **edición, hoja y una clase**, de esta lista cerrada:

`DOMINIO` · `HACIENDA-MUN` · `CARGOS` · `ELECTORAL` · `AGUAS` · `MINAS` · `OBRA-PUBLICA` · `ESCUELA` · `REGISTRO-CIVIL` · `JUSTICIA` · `NORMA` · `OTRO`

Un acto puede llevar dos clases separadas por `+`. La clase no sustituye a la línea de materia: va delante de ella.

```
  1169  h14  DOMINIO      Remate de la finca Los Sauces, base $50.000
  1170  h2   HACIENDA-MUN Decreto 5036, presupuesto municipal de 1927
```

---

## §8 · REGLAS DE FIDELIDAD

1. **Transcribir, no parafrasear.**
2. **No completar lo que falta.** Se escribe `[ilegible]`.
3. **No conciliar contradicciones.**
4. **No enriquecer.** Toda inferencia se rotula; toda remisión se comprueba; nada se declara ausente sin buscarlo.
5. **Separar lo leído de lo inferido, y lo leído en la imagen de lo leído en la capa**, en el MODO DE LECTURA de cada ficha.
6. **Las tablas se miran con los ojos.**
7. **Las cifras dudosas se marcan**, y cuando una lectura alternativa cerraría una columna, se escriben las dos.
8. **El nombre del archivo no es fuente.**
9. **Una ausencia se declara tras la co-ocurrencia y los identificadores múltiples.**
10. **El techo de resolución se declara.** Medido: 1909, 323–370 ppi; 1911, 329–370; 1912, 300–500; **1922, 150–192; 1923 a 1932, 150 ppi uniforme**. La caída a la mitad a partir de 1922 es el hecho material más importante de esa época y se declara en el §1 de cada informe.
11. **Ninguna cifra de hoja escaneada se publica sin mirarla.**
12. **El modo de lectura se declara en cada ficha.**
13. **Duplicado descartado es duplicado declarado.**
14. **Lo que no se pudo leer se escribe igual.**
15. **Fecha contra numeración**, sobre los vecinos ±3 de cada acto del §A y del §B.
16. **Dígitos contra una segunda versión.** Con una sola versión, la única prueba es la imagen.
17. **Ortografía original.** Tildes, eñes, «N.o», «1º», erratas con `[sic]`, guiones de fin de renglón, «m/n», renglones traspuestos.
18. **Una errata del original se transcribe y se declara dos veces:** en la nota de lectura y en E.9.
19. **[v16] Todo control muestral se declara con su denominador, en la misma frase en que se declara su resultado.** No se escribe «el control de paginación cierra»; se escribe «cierra en las 24 hojas interiores en que la capa resuelve la cabecera, sobre 746». Vale para: columnas cotejadas, cabeceras leídas, hojas miradas, subtotales recalculados, tapas leídas en la imagen y avisos cotejados por texto. **Un control sin denominador es una afirmación vacía**, y v15 ya lo pedía para las columnas: v16 lo generaliza.
20. **[v16] Un período imposible se transcribe y se declara, no se corrige ni se descarta.** En 1928 el decreto 9464 le reconoce a un ex-encargado del Registro Civil un período que «empieza el 9 de junio y termina el 13 de mayo», y ninguna de las dos fechas coincide con las de los otros actos del mismo año sobre la misma persona. Se transcribe, se dice contra qué no coincide y no se elige una lectura.
21. **[v16] Un salto de numeración grande se declara con su magnitud y sus dos extremos mirados, y no se explica.** En 1928 la serie de decretos pasa de **7097 a 8001 en la misma hoja y con la misma fecha**, con los dos tramos firmados por el mismo gobernador y el mismo ministro. Si el lector del informe tiene una hipótesis sobre el régimen de numeración, el informe **no la adopta ni la refuta**: declara el hecho y nombra la pieza que lo resolvería (el Registro Oficial del año).

---

## §9 · PLANOS

Si el corpus no tiene planos, §P lo dice en una línea y declara el techo de resolución. Un aviso que remite a un plano que no está se registra como **citado y no acompañado**. Se cuentan las hojas donde aparece la palabra y **cuántas de esas remisiones tocan al departamento**.

**[v16] Un año sin planos es un dato de serie y se escribe como tal.** Medido: 1929, 1930, 1931 y 1932 no publican **ni un solo plano** —las 1.321 hojas de 1931 son texto a dos columnas—, y 1931 sí publica el acto en que Obras Públicas «ratifica la necesidad de confeccionar el plano catastral de la Provincia en láminas, una por departamento», que es un plano citado y no acompañado de la clase más importante posible. La serie de años sin planos se arrastra de informe en informe y se cierra en el §R.

---

## §10 · FORMATO DE SALIDA

- **Un `.txt` UTF-8 en `/mnt/user-data/outputs/`:** ancho ≤ 80 **caracteres**, medido con `python3` después del último cambio y después de concatenar; sin markdown, sin backticks, sin escapes sueltos; la marca de corte se nombra `U+0002`.
- **Se arma por partes** y se ajusta con `textwrap` (`break_on_hyphens=False`). Las transcripciones llevan sangría de dos espacios y **no** pasan por `textwrap`.
- Una función `ficha()` con los cinco campos y otra `P()` para prosa.
- **El armador se conserva entre turnos y se parchea**, con `assert` antes de cada reemplazo:

  ```python
  def rep(a, b):
      global s
      assert a in s, a[:70]
      s = s.replace(a, b)
  ```

  Si un `assert` corta el script antes de escribir, **ningún parche de esa tanda se guarda**: se corrige el ancla y se vuelve a correr la tanda entera.
- **Las fichas viven en su propio módulo (`fichas.py`)**, ordenadas por edición al escribirlas.

### 10.1 · **[v16] Marcadores de sección fijos, byte a byte**

Es la corrección que hace cruzables los informes. Los veinte años de 1913 a 1932 usan `§A ·`, `§A -`, `§A —`, `§D · INDICE`, `§D - INDICE` y `§D, la cadena anual`, y un script que corta por sección **falla en ocho de los veinte**.

**Cada sección abre en su propio renglón, en la primera columna, con exactamente esta forma:**

```
§0 · ADVERTENCIA PRELIMINAR
§1 · CORPUS REVISADO
§2 · CRITERIO DE BUSQUEDA
§A · MENCIONES EXPLICITAS
§B · VECINDAD
§C · LIMITROFES
§P · PLANOS
§D · INDICE
§E · OBSERVACIONES
§F · CORRECCION A LA RUBRICA
§R · RECUENTO
```

- Separador: **espacio, `·` (U+00B7), espacio**. Nunca guion, nunca raya.
- Rótulo en **mayúsculas sin tildes**, como arriba: `MENCIONES EXPLICITAS`, no `Menciones explícitas`.
- Debajo, una línea de guiones del ancho del rótulo. Nada más entre el rótulo y el contenido.
- **Las subsecciones** (`E.1`, `B.2`, `A.7`) abren en primera columna con `<clave> · <título>` y el mismo separador.
- **El §0 no contiene ningún otro `§` en primera columna**: las remisiones a otras secciones se escriben dentro del renglón, nunca al principio. En 1930 y 1932 el §0 abría con `§16 de la rúbrica…` y eso rompía el corte por sección.

Se comprueba antes de entregar:

```python
import re
s=open(archivo,encoding='utf-8').read()
m=re.findall(r'(?m)^§(\S+) · ([A-ZÁÉÍÓÚÑ ]+)$', s)
assert [k for k,_ in m] == ['0','1','2','A','B','C','P','D','E','F','R'], m
```

### 10.2 · **[v16] §R · Recuento legible por máquina**

El recuento en prosa de v15 es correcto y no se puede sumar entre años. El §R lo repite en un bloque `clave: valor`, uno por renglón, al final del informe. Claves obligatorias:

```
§R · RECUENTO
-------------
anio: 1927
ediciones_desde: 1148
ediciones_hasta: 1199
ediciones_presentes: 52
ediciones_ausentes: 0
hojas_presentes: 745
hojas_declaradas: 0
hojas_ausentes_estimadas: 0
periodicidad: semanal-viernes
dias_salida_sin_edicion: 0
ediciones_dobles: 0
techo_ppi: 150
ocr_en_sesion: no
capa_previa: extraida-en-sesion
versiones: 1
actos_departamento: 24
actos_dominio: 3
actos_hacienda_municipal: 2
planos_publicados: 0
planos_citados_departamento: 0
balances_municipales: 0
cuadros_publicados: 9
subtotales_recalculados: 9
resumenes_tesoreria: 9
cadena_saldos: dos-tramos
columnas_cotejadas: 26
hojas_miradas: 45
avisos_repetidos_departamento: 1
falsos_positivos_anillo1: 5
limites_declarados: 4
estado: COMPLETO
```

- **Toda clave se escribe siempre**, aunque el valor sea `0` o `no-aplicable`. Una clave ausente no se distingue de un cero y rompe la serie.
- Los valores son enteros, `si`/`no`, o una palabra con guiones. **Nada de prosa dentro del §R.**
- Si una clave no aplica al año, su valor es `no-aplicable` y la razón va en E.10, no en el §R.
- **Esto es lo que permite el `LEE cruce`** (§17) y lo que habría permitido, sin leer veinte informes, ver de un vistazo que 1929 a 1932 no publican planos y que las cadenas de saldos se cortan a partir de 1926.

---

## §11 · BITÁCORA (selección vigente)

| Error | Cómo se resolvió |
|---|---|
| Suponer el formato por la serie anterior | `file` primero; medir capa y marca de corte en cada corpus |
| Reemplazar el OCR previo por el propio | Buscar sobre la unión y etiquetar la versión |
| Dar por «columna perdida» un truncado de pantalla | Renglón entero con `repr` y la imagen |
| Tomar los números del sumario de la unión | Sumario de una versión, cuerpo de la unión |
| Registrar la autoridad sólo por la tapa | Firmantes, fórmulas, apertura y cierre, interinatos |
| Heredar el régimen de numeración | Medirlo con pares contiguos mirados |
| Copiar la lista de actores del informe anterior | Armarla con todos los informes |
| Creer el número de un acto hallado en el OCR previo | Mirar la imagen |
| Aceptar «0 discrepancias» sin sumario o sin capa previa | Declarar «no aplicable» |
| Confiar en las cuatro pasadas como única red | El anillo de actores encuentra lo que ellas pierden |
| Listar un día sin edición sin mirar la tapa vecina | Puede ser una edición doble |
| Prometer OCR en sesión sin mirar los idiomas | `tesseract --list-langs` antes |
| Depender de `api.github.com` para listar un Release | `releases/expanded_assets/<tag>`, HTML sin token |
| Recortar por la coordenada de la palabra | Por el ancho entero de la columna + 6 pt |
| Leer el año editorial en la capa previa | En la tapa |
| Leer los contextos de anillo 2 «que parecen» | Todos los términos con acierto, uno por uno |
| Declarar ausente a un actor que el OCR parte | Buscar sin puntuación; si falla su propio acto, es la búsqueda |
| Prometer la cadena de saldos sin contar los meses | Contar los resúmenes publicados antes de prometerla |
| Llamar «pendiente» a lo que nadie puede hacer | Pendiente es trabajo; límite es imposibilidad |
| Quitar U+00AD como carácter y dejar el salto | Quitarlo **junto con** el salto |
| Escribir la laxa con un espacio literal | Con la clase de espacios en blanco |
| Dar por sana una pasada que devuelve cero | Probarla con otro patrón antes de creerle |
| Heredar la cadena de folios de un año al otro | Cierra dentro del año; entre años, no |
| Confundir edición corta con edición incompleta | El folio las distingue |
| Creer que la marca de publicación prueba repetición | Buscar el texto del aviso en el resto del corpus |
| No recalcular un cuadro porque la cadena cierra | Un subtotal por cuadro, siempre |
| Parchear el armador con `str.replace` a secas | `assert` antes de reemplazar |
| **[v16]** Declarar el número de elementos de una lista sin contarlos | Recuento propio sobre la transcripción (§4.1bis) |
| **[v16]** Contar una lista separando sólo por coma | El original usa punto y yuxtaposición: rango, no número |
| **[v16]** Escribir la laxa espaciada «con espacios en el medio» | Separador entre **cada par** de letras: «C A L D E R A» |
| **[v16]** Cambiar el separador de las secciones entre informes | `§X · ROTULO` fijo, byte a byte (§10.1) |
| **[v16]** Entregar el recuento sólo en prosa | §R en `clave: valor`, con todas las claves siempre (§10.2) |
| **[v16]** Heredar el config del Release sin mirar su fecha | Comparar recuentos antes de barrer (§15.4) |
| **[v16]** Dejar que el anillo 2 crezca sin cotejarlo | Cotejo contra la toponimia establecida (§5.1bis) |
| **[v16]** Atribuir jurisdicción por pertenecer al anillo 2 | La atribuye el acto, o queda indeterminada (§5.1ter) |
| **[v16]** Creer que el número de aviso identifica el acto | Cambia entre apariciones: se dedupe por texto (§6) |
| **[v16]** Declarar un control muestral sin su denominador | Resultado y denominador en la misma frase (§8.19) |
| **[v16]** Tomar el nombre del gobernador de la capa | En la imagen, como el año editorial (§2.5bis) |
| **[v16]** Dar por indeterminados los días de salida | Pueden estar en la tarifa y no en la tapa (§2.5bis) |
| **[v16]** Declarar «sin medición de tinta» con PDF reales | Rasterizar y medir: el límite era de la época del ZIP |

---

## §12 · FALSOS POSITIVOS YA JUZGADOS

Se descartan sin volver a discutirlos **dentro de su época**; en otra época se revalidan con el contexto.

- **1946, anillo 1:** «recalda»; «Calderón»; «MOTORES Y CALDERAS»; «Alderete»; «fiscalde»; «cal deno»; difusa: mercaderías, escalera, cuadrilla, caletera, carlera, cualdras.
- **1946, anillo 2:** Robles Wierna; El Manzano (Rosario de Lerma); Río Blanco (Payogasta); Los Nogales (Anta); El Durazno (Metán, Guachipas); El Cajón (La Candelaria); Campo Alegre (Rivadavia); Quintín Zuleta; Isasmendi y Castellanos como apellidos; Entre Ríos (calle y juez federal).
- **1908–1909, anillo 1:** Calderón; «S. de Alcalde»; «calavera»; finca «Camera»; Cuarteadero; San Agustín de La Merced; difusa: aldea, cuadrilla, escalera, mercaderías, cámara, cabrera, carrera.
- **1911:** «caldo»; Calderón; «Caldas»; «ca1 deno»; difusa: calavera, cadera, Escalera, cama camera, Candela. Anillo 2: Campo Alegre de Chicoana y Orán; Wierna de La Silleta; Castellanos; Isasmendi; Quintín; Lesser como apellido; Río Blanco de Cachi y Zenta; Entre Ríos finca y pedimento; Lagunilla y La Quesera de la Capital; El Manzano; Tabacal; «el cajón».
- **1912:** «una caldera tubular generadora á vapor»; Calderón de Rosario de la Frontera; difusa: caderia(s), balderrama, alera grande/chica, calavera, y las 33 formas de 0,70–0,78. Anillo 2: «trancas» = «arretrancas»; Castellanos (abogado, finca, río, arroyo y cinco personas); Isasmendi y Cía.; Wierna de Rosario de Lerma y Chicoana; Quintín; Tabacal de Orán; los Sauces de La Viña y la quebrada del Toro; Angosturas de Orán; Acheral fracción de Uchuype; Entre Ríos boratera, finca y calle; Río Blanco del Cerro Negro; El Manzano; Betania; Lesser y Nogales como apellidos; «el cajón».
- **[v16] 1913–1932, anillo de actores:** los homónimos de otros departamentos son el falso positivo dominante de esta época y se descartan **nombrando la jurisdicción**. Medidos: Nacianceno y Napoleón **Apaza** (Guachipas, Sevilar); Jorge **Mamani** (Carahuasi); Silverio **Aramayo** (Iruya); José María **Decavi** senador por la Capital leído como senador por Caldera en 1927 —**caso de columna traspuesta**, el único del año—. **La regla que los separa no es el apellido sino el acto que los atribuye**, y por eso se anotan con su departamento y no se borran del config.
- **[v16] 1923, anillo 1:** las seis formas de la difusa del año fueron todas falsos positivos, y se declara, porque decide si conviene correr la difusa en la época siguiente.
- **Ojo con los que ocultan:** un término del anillo 1 cuyo contexto contenga un falso positivo del config queda marcado `fp_conocido` y **sin recorte**, aunque sea real. Por eso «calera» salió del config, y por eso los falsos positivos de 1911 en adelante se listan en el informe y **no** se agregan al config.

---

## §13 · CHECKLIST DE CIERRE

- [ ] Verifiqué el entorno, **los idiomas de tesseract** y los insumos, y declaré lo que faltó.
- [ ] Miré el listado de assets del Release y dije qué insumos no llegaron.
- [ ] **[v16]** Comparé el config del Release con el del proyecto y declaré cuál usé y por qué (§15.4).
- [ ] **[v16]** Corrí el cotejo del anillo 2 contra la toponimia establecida y declaré sus tres líneas (§5.1bis).
- [ ] Bajé los PDF y los cotejé contra `EXTRAIDO.json`, o contra la cadena de folios, o contra el sumario.
- [ ] Leí el `log.txt`, o declaré que no hay log.
- [ ] Medí la marca de corte, el guion blando y los cortes con puntuación, **y comprobé que la unión pega las dos mitades a través del salto**.
- [ ] **[v16]** Corrí la laxa espaciada con separador **entre cada par de letras** y declaré qué rescató.
- [ ] Probé que ninguna pasada que devuelve cero está rota.
- [ ] Confirmé la columna perdida en la imagen, o la descarté **diciendo sobre cuántas columnas**.
- [ ] Rehice una búsqueda del anillo 1 sobre los textos y corrí la difusa ampliada.
- [ ] Revisé las tapas; las ilegibles, en la imagen; busqué ediciones dobles; leí el año editorial **y el nombre del gobernador** en la tapa.
- [ ] Revisé la paginación —corrida dentro del año, o por edición con el sumario o la cabecera— **y declaré su denominador**.
- [ ] Busqué los días de salida en la tapa **y, si no están, en la tarifa**.
- [ ] Resolví el cotejo sumario/cuerpo, o lo declaré no aplicable.
- [ ] Registré la autoridad, todas sus fórmulas, los refrendos, los «Es copia» y los interinatos.
- [ ] Miré cada candidato del anillo 1 y transcribí desde la página, con el encabezado de cada lista.
- [ ] **[v16]** Reconté toda lista enumerada sobre mi propia transcripción y marqué los nombres pegados (§4.1bis).
- [ ] Leí el contexto de **todos** los aciertos del anillo 2, y no atribuí jurisdicción sin acto.
- [ ] Busqué los actores sin puntuación; nombré a los que la búsqueda no devuelve ni en su propio acto.
- [ ] Armé las ausencias del §B en los tres grupos.
- [ ] Conté los resúmenes de Tesorería antes de prometer la cadena, encadené por la cifra y declaré los tramos.
- [ ] Inventarié los cuadros, recalculé al menos un subtotal de cada uno y declaré los demás con su motivo.
- [ ] Comprobé por el **texto** si los avisos se repiten, sin confiar en el número de aviso.
- [ ] Listé los citados y no acompañados, incluidas las vacantes sin nombre **y los nombramientos que sólo constan por su revocación**.
- [ ] Rotulé toda inferencia y comprobé toda remisión.
- [ ] Todo lo mirado está en `notas.txt`.
- [ ] Cada parche del armador pasó por `assert`.
- [ ] **[v16]** Los marcadores de sección pasan el `assert` de §10.1.
- [ ] **[v16]** El §R está completo, con todas sus claves, sin prosa (§10.2).
- [ ] **[v16]** El §D lleva clase fija en cada entrada (§7.1).
- [ ] El archivo tiene ≤ 80 caracteres por línea, sin markdown, con nombre en ISO.
- [ ] El §0 declara COMPLETO (con límites y con qué agregaría cada insumo) o CON PENDIENTES, y el cierre del turno dice si hubo entrega.

---

## §14 · MODO HÍBRIDO

### 14.1 · Reparto del trabajo

| `lee_auto.py`, en la máquina | Sesión |
|---|---|
| Extracción; rasterizado a 300 dpi | Verificar la corrida, o extraer la capa ella misma (§2.1) |
| OCR propio y confianza | Confirmar la columna perdida en la imagen |
| Tapas, días sin edición, páginas | Tapas ilegibles, dobles, año editorial y gobernador |
| Cuatro pasadas; anillo 2; actores; números; reemplazos | Juzgar cada candidato y transcribir desde la imagen |
| Destinos; cotejo sumario/cuerpo | Cruzar por texto; resolver o declarar no aplicable |
| Conteo de fórmulas de autoridad; lista de decretos | Autoridad y numeración con pares mirados |
| md5, dhash, tinta; recortes | Hojas «a ojos», tablas, saldos y **recuentos de listas** |
| Pre-informe + CSV | Informe final, §R, §F y config actualizado |

### 14.2 · Qué pone el usuario, por año

En el Release con el año como tag: los PDF y, como assets, el pre-informe, `resultados_<año>.csv`, `decretos_<año>.csv`, `log.txt`, `recortes.zip`, **el `lee_config.json` vigente** y el zip de los `.txt` de `lee_trabajo`.

**Qué pasa si no llega nada de eso.** Con el Release y el config solos, la sesión **cierra el §A, el §B, la autoridad, las tablas y los saldos** y entrega un informe **COMPLETO con sus límites**. Costo medido, todos con cuatro turnos: 1911, 87 ediciones y 347 hojas, 18 fichas; 1912, 77 y 307, 17 fichas; 1923, 52 y 673, 17 fichas; 1924, 52 y 792, 24 fichas; 1932, 54 ediciones, 29 fichas.

### 14.3 · Búsquedas en sesión sobre los textos

La sesión reconstruye `V[versión][(edición, hoja)]` y aplica `unir`, `norm`, `buscar`, `pasadas`, `destinos`, con la unión corregida. Se guardan `res_sesion.json`, `fechas.json`, el normalizado (`N.json`) y el texto sin puntuación (`P.json`): son lo que permite rehacer las pasadas enteras en una llamada cuando se corrige una función de unión.

### 14.4 · Orden de trabajo en sesión

**Primer turno:** entorno, idiomas, inventario de assets, **cotejo del config y del anillo 2**; bajar el año y extraer o verificar la capa; confianza; marca de corte, guion blando y cortes; techo de resolución; hojas por edición; paginación; tapas y dobles; búsqueda propia de `cald`; laxa espaciada; difusa ampliada; columna perdida; lista de trabajo.

**Turnos siguientes:** candidatos del anillo 1 con encabezados y **recuentos de listas**; anillo 2, actores y números; autoridad, numeración y vecinos ±3; tablas y cadena de saldos; repeticiones por texto, §D con clases, **§R**, redacción y entrega con el config actualizado.

**Presupuesto de turno.** Mirar una mención cuesta entre una y tres llamadas. Cuatro turnos han bastado en todos los años medidos de 1911 a 1932. En cada turno se entrega el informe entero.

**Un hallazgo de método puede aparecer en el tercer turno y obligar a volver al §A.** Por eso el informe se rehace entero cada vez y las fichas viven en su propio módulo.

---

## §15 · CONFIGURACIÓN (`lee_config.json`)

### 15.1 · Claves

| Clave | Qué es |
|---|---|
| `tesseract` | Ruta al ejecutable |
| `lang` / `psm` / `dpi` | `spa`, `3`, `300` |
| `anillo1` | `caldera`, `calderilla` |
| `anillo2` | Vocabulario de vecindad, normalizado y sin tildes |
| `actores` | `[nombres, apellido, origen]` |
| `numeros` | Números de acto arrastrados |
| `falsos_positivos` | Contextos que el script marca como `fp_conocido` |
| **[v16]** `version` | `AAAA-MM-DD` de la última actualización, y `hasta`, el último año incorporado |

### 15.2 · Cómo se escribe el estado

**Leyendo el config, no de memoria:**

```python
import json, collections
c=json.load(open('lee_config.json'))
print(c.get('version'), c.get('hasta'))
print(len(c['actores']), collections.Counter(a[2] for a in c['actores']))
print(len(c['anillo2']), len(c['numeros']), len(c['falsos_positivos']))
```

### 15.3 · Config por época

1. La primera corrida de una época usa el config vigente.
2. La sesión arma los actores y los números del §A y §B del año, los busca sobre los textos y entrega un config actualizado: **agrega** los de la época nueva con su origen, **conserva** los anteriores, **agrega** al anillo 2 los topónimos del departamento con otra forma —incluida la deformación del OCR, cuando sin ella no se encontrarían— y **agrega** a `falsos_positivos` sólo contextos inequívocos.
3. **Cuando una persona aparece con dos apellidos distintos en años distintos, se agregan los dos y se conserva el anterior.** No se unifican: el config es una red de búsqueda, no un padrón.
4. El usuario reemplaza el config y corre el año siguiente; los años ya procesados se repasan con `--solo-busqueda`. **Después de una corrección de método como la del guion blando o la de la laxa espaciada, se repasan TODOS los años de la época ya barridos.**
5. Si la sesión no recibe el config, entrega un archivo de **agregados** y lo dice; nunca inventa el contenido del vigente.
6. **[v16] `origen` se normaliza a año.** De las 388 entradas vigentes, 42 llevan por origen un número de edición de 1946 en lugar de un año, de modo que no se puede medir cuánto aporta cada tramo al anillo. El campo pasa a ser el **año** en cuatro dígitos, con la edición como cuarto elemento opcional: `["teofilo","reyes",1946,2465]`.

### 15.4 · **[v16] El config del Release se compara con el del proyecto antes de barrer**

Los barridos de 1930, 1931 y 1932 encontraron, los tres, que el asset del Release **cierra en 1915** —180 actores, 70 términos de anillo 2, 40 números, 12 falsos positivos— mientras el del proyecto llega a 1928 —388, 139, 112 y 24—. Los tres lo declararon y usaron el del proyecto: bien. Pero **ninguna regla lo obligaba**, y un barrido que sólo hubiera tenido el del Release habría perdido los 208 actores de 1916 a 1928, que son justamente los de la época más cercana.

**Regla.** En el primer turno se leen los dos configs y se escribe en el §0:

```
config del Release: version <x>, hasta <a>, actores <n>, anillo2 <m>
config del proyecto: version <y>, hasta <b>, actores <n>, anillo2 <m>
se usa: <cuál> — razón: <más nuevo / único disponible>
contenido: <el usado contiene al otro / difieren en N términos, listados>
```

Si el usado **no** contiene al otro, los términos que faltan se agregan antes de barrer y se dice. Y si el del Release está atrasado, el informe cierra pidiendo que se suba el vigente, con esa frase.

---

## §16 · MODO EN SESIÓN

Cuando el corpus viene como archivos del proyecto sin salidas de `lee_auto.py` (ZIP con N.jpeg a ~110 ppi, como 1946), rige el procedimiento de v11: OCR en segundo plano con `setsid nohup`, reanudable y atómico, esperando con `sleep 270–290`; orden por turnos; y las mismas reglas de este documento.

**Supone `spa` instalado.** Si no lo hay, el §16 no corre: con PDF reales se usa §2.1, y con ZIP de imágenes sin capa el barrido no se puede hacer en sesión y se declara.

---

## §17 · **[v16] §X · CRUCE ENTRE AÑOS**

`LEE cruce <año1>-<año2>` no barre nada: lee los informes ya entregados del rango y entrega un archivo aparte, `LEE-cruce-<a1>-<a2>_<fecha>.txt`. **Existe porque los veinte informes de 1913 a 1932 son correctos uno por uno y el cruce encontró cosas que ninguno podía ver solo.**

**Qué entrega, y nada más que eso:**

1. **La serie del §R**, una fila por año y una columna por clave, con los años que no la traen marcados `—`. Es el producto principal.
2. **Rachas de valor constante**: años seguidos con `planos_publicados: 0`, con `balances_municipales: 0`, con `cadena_saldos: no-armable`. Una racha de cuatro años sin planos es un hecho del corpus que un informe anual no puede afirmar.
3. **Actores por año de primera aparición y por años de reaparición**, con el acto de cada una. Esto es lo que muestra las carreras largas y las vueltas a un mismo cargo.
4. **Términos del anillo 2 con aciertos en todos los años y con aciertos en ninguno.** Los primeros suelen ser apellidos o falsos positivos estructurales; los segundos, candidatos a salir.
5. **Contradicciones entre informes**: un mismo acto, número o fecha descrito de dos maneras en años distintos.

**Tres reglas que el cruce no puede violar:**

- **El cruce no es una fuente.** Todo lo que afirme remite al informe y a la edición y hoja de origen. Si un dato sólo existe en el §R y no en una ficha, se marca `sin-ficha` y no se usa para afirmar nada sobre el departamento.
- **El alcance de una frecuencia se declara.** Contar un apellido «en el informe» no es contarlo «en el departamento»: el informe cubre todo el Boletín. Una frecuencia que no esté restringida al §A **se rotula como frecuencia de corpus**, y la diferencia se escribe en la misma frase.
- **El cruce no concilia.** Si dos informes se contradicen, los transcribe los dos y nombra la pieza que lo resolvería, como hace cualquier ficha.

**El caso que lo motiva.** Cruzados los veinte años, aparece que los apellidos de origen andino que un padrón de 1944 registra como titulares están en el archivo del departamento desde 1917 —una familia con terreno deslindado judicialmente en La Calderilla, un causante de sucesión ante el juez de paz en 1918, tres comisarios auxiliares en 1919 y un comisario de policía en 1929—. Ninguno de los veinte informes podía decirlo: cada uno tenía una pieza. **Y el mismo cruce descartó tres apellidos que parecían del departamento y eran de Guachipas, Carahuasi e Iruya** — el descarte vale tanto como el hallazgo, y por eso va en el mismo archivo.

---

*v16 fijada el 22/09/2026, tras los barridos de 1913 a 1932 —veinte años seguidos, ediciones N° 384 a 1461— y tras el primer cruce de esos veinte informes entre sí.*
