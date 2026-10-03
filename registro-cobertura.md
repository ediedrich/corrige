# Registro de cobertura acumulada — *El dispositivo caldereño*

Archivo exigido por CORRIGE 3.6 («Cobertura acumulada»). **Se versiona en el repositorio del libro**, no en la conversación. Cada ronda agrega su bloque; una línea leída dos veces cuenta una vez; al reescribir sustancialmente un archivo, sus tramos anteriores caducan y se marcan `caduco`.

- Manuscrito al abrir el registro: **24.476 líneas** en 38 archivos `.tex` (commit base de la ronda 35).
- Rondas 1–34: **sin registro en archivo → cobertura acumulada 0** por regla. Lo leído entonces no se reconstruye de memoria.

## Ronda 35 — auditoría (23/09/2026)

### Lectura sobre el texto

| Archivo | Líneas | Nota |
|---|---|---|
| cap/00-advertencia.tex | 43, 68–78 | 43 es un párrafo largo; leído entero |
| cap/01-planteo.tex | 135–141 | refutadores de las tres tesis |
| cap/02-metodo.tex | 28, 81 | |
| cap/04-siglo.tex | 430–435, 2172–2177, 2263–2268, 2385–2389, 2801–2805, 3012–3016, 3140–3144, 3391–3395, 3548–3562, 4397–4400 | |
| cap/11-ribera.tex | 1055–1062 | epígrafe `fig:catastro` |
| cap/15-hacienda.tex | 74–78 | |
| cap/18-politica.tex | 409–412 | |
| cap/20-opacidad.tex | 714–718, 730–733 | |
| cap/21-ausencias.tex | 70–75 | |
| cap/21-conclusion.tex | 80–85 | |
| cap/22-prospectiva.tex | 270–282 | |
| ape/D-pedidos.tex | 1–35, 213, 217, 222, 240–245, 249, 251, 297 | más los ítems 161, 163, 165, 166, 192, 214, 263 |
| ape/F-fuentes.tex | 25–30, 42, 49–51, 106–112, 143, 199 | 42 leída en parte (una línea de varias páginas) |
| ape/G-propuestas.tex | 1–30, 775–804 | |

**Total aproximado: 265 líneas de 24.476 (1,1 %).** Acumulado: **1,1 %**.

### Controles por script (no cuentan como lectura; se declaran con su denominador)

| Control | Denominador | Resultado |
|---|---|---|
| Superlativos (*único, primero, más antiguo, nunca, jamás…*) | 24.476/24.476 líneas | 584 coincidencias; 98 referidas al archivo; 36 revisadas en contexto |
| Menciones de ventana y de número de tramos | 24.476/24.476 | 8 menciones; 7 desactualizadas |
| Pedidos con objeto ya obtenido | 278/278 ítems | 26 con «ya se obtuvo»; 8 leídos; 1 con el objeto principal satisfecho |
| Pedidos duplicados por destinatario (número de expediente/ley) | 278/278 | 1 duplicado real (3898-C, cuatro menciones); 2 falsos positivos |
| Recuento de láminas en el texto frente al `.lof` | 38/38 entradas; 5 menciones del total | 4 menciones desfasadas (36 por 38) y 1 recuento de propias (15 por 17) |
| Estado de script de figuras propias | 17/17 | 11 publicados; 6 no publicados y declarados en F (uno con script ajeno en el epígrafe) |
| `\pendiente{}` con pedido del mismo capítulo | 52/52 | sin faltas |

## Ronda 36 — auditoría con fase 6 (23/09/2026)

Base: commit `591b074` de `ediedrich/dispositivo-caldereno` (el manuscrito no cambió desde `7cd0477`, base de la ronda 35). **Denominador medido: 24.450 líneas** en los mismos 38 archivos `.tex` (`wc -l`); la ronda 35 declaró 24.476, y la diferencia de 26 no se explica con el commit. Las correcciones de esta ronda **no cambian el número de líneas de ningún archivo** y son de una frase cada una: ningún tramo anterior caduca.

### Lectura sobre el texto

| Archivo | Líneas | Nota |
|---|---|---|
| cap/00-advertencia.tex | 1–82 | entero |
| cap/01-planteo.tex | 1–180 | entero |
| cap/02-metodo.tex | 1–85 | entero |
| cap/04-siglo.tex | 582–592, 843–900, 1252–1262, 4395–4403 | Luque 1918, lámina de nóminas, escuela 1921, cierre 1947–1948 |
| cap/21-ausencias.tex | 1–351 | entero |
| cap/21-conclusion.tex | 1–130 | entero |
| cap/26-presencia.tex | 1–229 | entero |
| ape/A-cronologia.tex | 37 | |
| ape/F-fuentes.tex | 22–41 | tramos y 31 ediciones faltantes |

**Esta ronda: 1.167 líneas (4,8 %).** Superpuestas con la ronda 35: 43 (00: 43, 68–78; 01: 135–141; 02: 28, 81; 04: 4397–4400; 21-ausencias: 70–75; 21-conclusion: 80–85; F: 25–30). **Nuevas: 1.124.**

Acumulado: ronda 35 recalculada sobre su propia tabla = **260 líneas** (había declarado «aproximado 265») + 1.124 = **1.384 de 24.450 (5,7 %)**.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Superlativos (*el único, la primera, nunca, jamás, uno solo…*) | 24.450/24.450 líneas | 677 coincidencias; 41 en los archivos leídos, revisadas todas en contexto; 4 falsas (3 sobre Juana Luque, 1 «el único caso en que … llegó») |
| Número de tramos leídos | 24.450/24.450 | 6 menciones: 32 (00, 04:4399), 36 (02, F, 21-ausencias por suma), 15 (D:217) |
| Nóminas y topónimos de la lámina `fig:parajesnom` | 24.450/24.450 | 21-ausencias decía 7 nóminas y 23 de 51; 04 y 00 dicen 12 y 24 de 52 |
| Láminas en el texto frente al `.lof` | 38/38 entradas; 7 menciones del total | cierra en las 7 |
| `\lamina` + `figure` con `\caption` | 19 + 19 | 38, sin figuras sin epígrafe en el cuerpo |
| Propuestas del apéndice G | 26/26 | 6 ordenanzas, 15 leyes, 5 actos del Ejecutivo: cierra con «veintiséis» |
| `\pendiente{}` e ítems de D | 52 y 278 | mismos totales que la ronda 35; el emparejamiento no se rehízo |
| Expediente 3898-C en D | 4 menciones | 1 ítem (l. 251) y 3 remisiones: ya no es duplicado |
| Compilación | libro entero | compila; 753 págs.; 0 referencias indefinidas; `.lof` con 38 |

## Ronda 37 — mixta: incorporación y auditoría (24/09/2026)

Base: la de la ronda 36 con sus correcciones aplicadas. **Denominador medido después de esta ronda: 24.547 líneas** (`wc -l`, 38 archivos `.tex`). Tres archivos crecen: `20-opacidad` 1.006 → 1.042, `22-infraestructura` 724 → 773, `22-prospectiva` 462 → 474. **Sus tramos de rondas anteriores caducan** (ronda 35: 20-opacidad 714–718 y 730–733; 22-prospectiva 270–282), y quedan cubiertos por la lectura completa de esta ronda sobre la numeración nueva. `01-planteo` y `21-conclusion` cambian una frase cada uno sin cambiar su número de líneas: no caducan.

### Lectura sobre el texto (numeración posterior a esta ronda)

| Archivo | Líneas | Nota |
|---|---|---|
| cap/20-opacidad.tex | 1–1042 | entero |
| cap/22-infraestructura.tex | 1–773 | entero |
| cap/22-prospectiva.tex | 1–474 | entero |
| cap/09-defensas.tex | 440–460 | serie de la refacción de la comisaría |
| cap/04-siglo.tex | 3385–3392 | la misma serie; 3391–3392 ya leídas en la ronda 35 |

**Esta ronda: 2.318 líneas (9,4 %).** Superpuestas con rondas anteriores: 24 (las 22 caducas de la ronda 35 y 2 de 04-siglo). **Nuevas: 2.294.**

Acumulado **según este archivo**: ronda 35 (260) + ronda 36 (1.124) + ronda 37 (2.294) = **3.678 de 24.547 (15,0 %)**. Si la ronda 36 no se commitea, el acumulado es 260 + 2.294 = 2.554 (10,4 %).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Superlativos en los tres capítulos | 2.289/2.289 líneas | 63 coincidencias, todas revisadas en contexto; 1 desmentida por el propio libro («la única vez… que un organismo publica el criterio»), corregida |
| Menciones de «cinco mecanismos», «once ocurrencias», «serie de seis», «la única vez en este libro» | 24.547/24.547 | ninguna fuera de los tres capítulos |
| Remisiones a capítulos posteriores en el texto nuevo | 3 de 20-opacidad a 21-ausencias | marcadas «más adelante» antes de compilar |
| Compilación | libro entero | compila; 755 págs.; 0 referencias indefinidas; `.lof` con 38 |

## Ronda 38 — auditoría con fase 6 (24/09/2026)

Base: commit `5196df6` de `ediedrich/dispositivo-caldereno`, con tres incorporaciones posteriores al cierre de la ronda 37 (`8072c0e`, `5f220dc`, `5196df6`). **Denominador medido: 24.672 líneas** (38 archivos `.tex`, `wc -l`).

### Traslado y caducidad de los tramos anteriores

Los tramos de las rondas 35 y 36 (numeración de `591b074`) y de la 37 (numeración de `67d1dae`) se trasladaron a la numeración de `5196df6` por diff línea a línea: una línea sin cambios conserva su cobertura con su número nuevo, y **una línea modificada por las incorporaciones caduca**. Recalculado el acumulado de este archivo sobre sus propias tablas, da 3.678, igual que la ronda 37. Caducan **51**: F-fuentes 16, 04-siglo 8, 22-infraestructura 8, 21-ausencias 5, 00-advertencia 4, 26-presencia 4, 20-opacidad 2, 22-prospectiva 2, 02-metodo 1 y 11-ribera 1. **Quedan vigentes 3.627.**

Las correcciones de la fase 6 de esta ronda cambian una o varias frases en 13 archivos **sin cambiar el número de líneas de ninguno** (lo comprobó el script que las aplicó). Siguiendo el criterio de las rondas 36 y 37, no hacen caducar ningún tramo.

### Lectura sobre el texto (numeración de `5196df6`, igual a la de después de la fase 6)

| Archivo | Líneas | Leídas | Nuevas |
|---|---|---|---|
| main.tex | 1–398 | 398 | 398 |
| cap/00-advertencia.tex | 20, 43, 75, 78 | 4 | 4 |
| cap/02-metodo.tex | 28–44 | 17 | 17 |
| cap/04-siglo.tex | 847–848, 850, 853, 863–865, 877–901, 2869–2870, 3285–3304, 3370–3380, 3515–3524, 3540–3542, 3550–3555, 3760–3772, 3928–3937, 4165–4190, 4192–4200 | 142 | 119 |
| cap/06-pdua.tex | 1–190 | 190 | 190 |
| cap/11-ribera.tex | 1056 | 1 | 1 |
| cap/14-poblacion.tex | 782 | 1 | 1 |
| cap/15-hacienda.tex | 39–52, 150–165 | 30 | 30 |
| cap/17-aguabaja.tex | 1–456 | 456 | 456 |
| cap/18-politica.tex | 371 | 1 | 1 |
| cap/18-trabajo.tex | 1–400 | 400 | 400 |
| cap/20-opacidad.tex | 653–655 | 3 | 3 |
| cap/21-ausencias.tex | 47–48, 56–58, 65, 87, 270–285 | 23 | 23 |
| cap/22-infraestructura.tex | 213–216, 270, 466, 551, 762–763, 768–771 | 13 | 13 |
| cap/22-prospectiva.tex | 158–160 | 3 | 3 |
| cap/23-plan.tex | 1–326 | 326 | 326 |
| cap/26-presencia.tex | 157, 174, 217–218, 228–251 | 28 | 28 |
| ape/A-cronologia.tex | 21, 25–26, 28, 65, 82, 91, 100, 103, 111, 120–121, 125–126, 132–133, 140–142, 152, 156, 158, 173, 180, 183, 186–189, 193–194, 198–199, 204–206, 210–211, 216, 227–231, 236–237, 245–246, 250, 253–255, 286, 301, 305, 341, 346, 351, 359, 369, 375, 381, 394, 399, 407, 418, 421–422, 427, 445 | 70 | 70 |
| ape/B-matriz.tex | 1–120 | 120 | 120 |
| ape/D-pedidos.tex | 102, 184, 200 | 3 | 3 |
| ape/F-fuentes.tex | 29–55, 57, 82, 121, 124–125, 130–133, 157–158, 162–167, 181–195, 205–207, 209, 213–226 | 77 | 76 |
| ape/G-propuestas.tex | 31–774 | 744 | 744 |

**Esta ronda: 3.050 líneas leídas; 24 ya estaban (04-siglo 23, F 1); nuevas: 3.026 (12,3 %).** De esas, 2.924 son de bloques enteros o de líneas que cambiaron las incorporaciones, y 102 son de contexto (04-siglo 66, 15-hacienda 21, F 13, D 2), deduplicadas por el mismo script.

Acumulado: 3.627 vigentes + 3.026 = **6.653 de 24.672 (27,0 %)**. Sin las 102 de contexto: 6.551 (26,6 %).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 3.678/3.678 líneas registradas | 3.627 vigentes, 51 caducas |
| Recuentos de topónimos contra `tabla_parajes.py` | 52 filas y 13 columnas | 52, 46, 24, 21 y núcleo de 10 cierran; 04:4200 y 21-ausencias:56 no (corregidos) |
| Menciones de «doce/trece nóminas», «1.470/1.492», «treinta y una» | 24.672/24.672 | sin menciones desactualizadas |
| Láminas en el texto frente al `.lof` | 41 entradas; menciones en 00 y F | 41 en todas |
| Scripts declarados frente a `mapas_caldera` (público) | 20/20 láminas propias | 17 presentes; 3 declaradas sin script en F |
| Superlativos en el texto agregado por la fase 6 | 28 líneas cambiadas | 4 coincidencias, todas preexistentes o con universo declarado |
| Número de líneas por archivo antes y después de la fase 6 | 13/13 archivos tocados | sin cambios |
| Compilación | libro entero | compila; 763 págs.; 0 referencias indefinidas; `.lof` con 41 |

## Ronda 39 — auditoría con fase 6 (27/09/2026)

Base: commit `0c924bd` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1913, 1915, 1917), con la fase 6 de esta ronda en `ronda-39.patch`. **Denominador medido después de la fase 6: 24.692 líneas** (38 archivos `.tex`, `wc -l`); en `0c924bd` eran 24.698.

### Traslado y caducidad de los tramos anteriores

Los tramos de las rondas 35 a 38 se trasladaron por diff línea a línea a la numeración de `0c924bd`, pasando por `67d1dae`, `8072c0e`, `5f220dc`, `5196df6` y `ae1f0b7`. Criterio: en los commits de incorporación, una línea modificada caduca; en los de fase 6 (`67d1dae` y `ae1f0b7`), una línea reescrita por la misma auditoría conserva su cobertura. Resultado: **6.650 líneas vigentes en `0c924bd`**. La ronda 38 declaró 6.653 con el mismo método; la diferencia es de 3 líneas.

- Caducan por el AMPLÍA `0c924bd`: 00-advertencia 43 y dos líneas de A-cronologia y de 04-siglo.
- La fase 6 de esta ronda cambia el número de líneas sólo de dos archivos: `ape/E-personas.tex` (163 → 161, porque se quita la entrada duplicada de Augusto Regis) y `ape/H-dominio.tex` (230 → 226, porque se quitan tres filas duplicadas). Ninguno de los dos tenía tramos vigentes.
- En los otros ocho archivos tocados, las correcciones son frases dentro de líneas existentes, sin cambio de largo.
- El traslado a la numeración nueva no hace caducar ninguna línea.

### Lectura sobre el texto (numeración posterior a la fase 6)

| Archivo | Líneas | Leídas | Nuevas |
|---|---|---|---|
| cap/00-advertencia.tex | 43 | 1 | 1 |
| cap/02-metodo.tex | 28, 36–42 | 8 | 0 |
| cap/03-fincas.tex | 933–938, 1036 | 7 | 7 |
| cap/04-siglo.tex | 180–575, 1804–1810, 2054–2064, 2630–2670, 3548–3590, 3655–3659, 3776–3806, 3958–3992, 4340–4360, 4540–4552 | 603 | 560 |
| cap/17-aguabaja.tex | 340–366 | 27 | 0 |
| cap/26-presencia.tex | 225–240 | 16 | 0 |
| ape/A-cronologia.tex | 29–37, 55, 74, 88, 129, 250, 253, 255 | 16 | 13 |
| ape/D-pedidos.tex | 23, 195, 200, 215, 263–267 | 9 | 8 |
| ape/E-personas.tex | 1–78 | 78 | 78 |
| ape/F-fuentes.tex | 1–60 | 60 | 25 |
| ape/H-dominio.tex | 1–30, 105–111, 146–226 | 118 | 118 |

**Esta ronda: 943 líneas leídas, de las que 810 son nuevas.** En bytes equivalen a unas **49,5 páginas**: 158.775 bytes sobre 2.445.267 bytes y 763 páginas. Ese es el denominador del aspecto 7.

Acumulado: 6.650 vigentes + 810 = **7.460 de 24.692 (30,2 %)**.

### Cotejo sobre el facsímil (Release de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 1169 (1927) | 14 | Aviso 2188 de Los Sauces | Martillero Roberto del Carril; juicio sucesorio de Domingo Royo; base \$50.000. Coincide |
| 1174 (1927) | 11–12 | Aviso de julio de Los Sauces | **Martillero Antonio Forcada**; ejecución del Banco de la Nación contra la testamentaría; base \$14.000; remate el 16 de agosto; aviso **2240** (el libro decía 2233, que es el de otro aviso de la columna vecina) |
| 1182 (1927) | 14 | Aviso 2349 | Forcada, base \$14.000. Coincide con el de julio |
| 2403 (1945) | 7 | Frente del terreno de Pfister | «ciento ocho metros con veinte y ocho centímetros»: 108,28 m. La fila de H que decía 108,20 estaba mal |
| 2030 (1943) | — | Si es una edición real | 31 hojas con texto de la Intervención; la capa no trae «Caldera». **No es lectura LEE**: la edición queda sin leer |

Son 4 datos cotejados sobre 4 ediciones. Con menos de 10 citas, el cotejo es parcial.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 6.650/6.650 líneas vigentes | 0 caducas |
| Filas de la tabla de dominio (longtable de H) | 61/61 filas después de la fase 6 | Ordenadas por fecha; 33 localizadas (de 1909 a 1945) y 28 sin localizar (de 1924 a 1945). Antes de la fase 6 eran 64 filas, con tres operaciones duplicadas y dos filas de 1945 entre 1926 y 1927 |
| Menciones del recuento de la tabla de dominio | 24.692/24.692 líneas | 5 menciones (H:7, 21, 195 y 223; 03:1036), todas corregidas |
| Menciones de las ediciones obtenidas después (837–838, 917–938, 2030, 2745–2868, 3027–3059) | 24.692/24.692 | 16 menciones en 00, 02, 04, A, D y F, todas corregidas |
| Índice de los Releases 1920, 1922, 1943, 1947 y 1948 | 5 ediciones sondeadas | Las 5 presentes (837, 917, 2030, 2745 y 3027); 1947 trae 282 PDF y 1948 trae 281 |
| Superlativos en el texto agregado por la fase 6 | 168 segmentos agregados | 2 coincidencias, las dos con su universo dicho |
| Largo de los archivos antes y después de la fase 6 | 10/10 archivos tocados | 8 sin cambios; cambian E (−2) y H (−4) |
| Muestra de 50 afirmaciones de hecho (aspecto 1), semilla 39 | 50 de 334 candidatas en los tramos leídos | 3 no son afirmaciones de hecho (un título, una cautela y una frase general de F); **45/47 tienen fuente localizable (95,7 %)**; las 2 sin fuente son entradas de E de 1908 y 1910 |
| Compilación | Libro entero | Compila; 763 páginas; 0 referencias indefinidas; `.lof` con 41 entradas |

## Ronda 40 — auditoría con fase 6 (27/09/2026)

Base: commit `5388e3c` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1920, 1922), con la fase 6 de esta ronda en `ronda-40.patch` (commit `c978aa9`). **Denominador medido después de la fase 6: 24.774 líneas** (38 archivos `.tex`, `wc -l`), igual que en `5388e3c`: la fase 6 no cambia el largo de ningún archivo.

### Traslado y caducidad de los tramos anteriores

Los tramos de las rondas 35 a 39 se trasladaron por script (`difflib`, línea a línea) por la cadena `591b074` → `67d1dae` → `8072c0e` → `5f220dc` → `5196df6` → `ae1f0b7` → `0c924bd` → `c0474ac` → `5388e3c`, con el criterio de la ronda 39: en los commits de incorporación una línea modificada caduca; en los de fase 6 (`67d1dae`, `ae1f0b7`, `c0474ac`) conserva su cobertura. El script reproduce los acumulados declarados por las rondas anteriores (3.678; 3.627; 6.653; 6.650; 7.460). **En `5388e3c` quedan 7.438 vigentes**: caducan 22 por el AMPLÍA 1920-1922 (04-siglo 5, 22-prospectiva 3, A-cronologia 3, 20-opacidad 2, F-fuentes 2, H-dominio 2, E-personas 2, 00-advertencia 1, 02-metodo 1, D-pedidos 1).

### Lectura sobre el texto (numeración de `5388e3c`, igual a la de después de la fase 6)

| Archivo | Líneas | Leídas | Nuevas |
|---|---|---|---|
| cap/00-advertencia.tex | 43 | 1 | 1 |
| cap/02-metodo.tex | 28, 94–98 | 6 | 1 |
| cap/03-fincas.tex | 958–972 | 15 | 15 |
| cap/04-siglo.tex | 10–33, 676–700, 744–752, 869–871, 955–957, 1250–2620, 2917–2932, 2993–2996, 3238–3244, 4619–4623 | 1.467 | 1.418 |
| cap/20-opacidad.tex | 879–880 | 2 | 2 |
| cap/22-infraestructura.tex | 512–518 | 7 | 0 |
| cap/22-prospectiva.tex | 208–212, 231–236 | 11 | 6 |
| cap/26-presencia.tex | 18–40 | 23 | 0 |
| ape/A-cronologia.tex | 24–25, 27, 33, 38, 55, 74, 83, 86–104, 108, 113, 115, 147, 150–151 | 33 | 28 |
| ape/D-pedidos.tex | 192, 217, 226, 229, 237 | 5 | 5 |
| ape/E-personas.tex | 42, 66, 68, 90 | 4 | 3 |
| ape/F-fuentes.tex | 57, 65 | 2 | 2 |
| ape/H-dominio.tex | 24 | 1 | 1 |

**Esta ronda: 1.577 líneas leídas, de las que 1.482 son nuevas.** En bytes equivalen a unas **54,5 páginas**: 174.731 bytes sobre 2.457.771 y 767 páginas. Ése es el denominador del aspecto 7. Además de estos tramos se leyó entero el diff del AMPLÍA `5388e3c` (132 líneas agregadas), cuyas líneas están incluidas en la tabla.

Acumulado: 7.438 vigentes + 1.482 = **8.920 de 24.774 (36,0 %)**.

### Cotejo sobre el facsímil (Release de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 961 (1923) | 12 | Aviso de remate de junio | Martillero Decavi, autos de división de bienes de los esposos Aramayo-Nogales: remata **sin base, muebles y semovientes**. No es acto de dominio: el libro decía que era «el único de dominio» del año (corregido en 04 y A) |
| 982 (1923) | 11 | Aviso de la finca Calderilla | Base \$7.000; la capa imprime «L a Caldera» con «Caldera» entero: no es uno de los actos con letras separadas |
| 918 (1922) | 4 | Decreto 192 | 27 de julio; renuncia «presentada por el señor Julio Royo Ortiz»; «atento las razones en que la funda». Coincide |
| 919 (1922) | 3 | Decreto 200 | «instalar en Mojotoro, departamento de Campo Santo, una escuela de la Ley 4874». Coincide |
| 927 (1922) | 5 | Decreto 345 | «don Francisco Urquiza», sin inicial; «con jurisdicción en Vaqueros»; «Santo Rufino». Coincide |
| 927 (1922) | 6 | Decreto 347 | «los que ha abonado de su peculio»; \$607 en efectivo; julio de 1921. Coincide |
| 931 (1922) | 5 | Decreto 442 | 31 de octubre; renuncia de Jorge A. Rauch «atento a los motivos en que la funda». Coincide; la frase del nombramiento de Royo cae fuera del recorte y no se cotejó |
| 931 (1922) | 7 | Decreto 446 | «al Comisario del departamento La Caldera, señor Julio Royo», reemplazado por Eustaquio Murúa. Coincide |
| 937 (1922) | 3 | Decreto 536 | Romelia Cáceres de Jerez; fianza del art. 77 de la Ley de Contabilidad. Coincide |

Son **8 citas cotejadas sobre 9 hojas**, sin correcciones silenciosas ni citas que cambien el sentido. Con menos de 10 citas, el cotejo es parcial.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 7.460/7.460 líneas vigentes en `c0474ac` | 7.438 vigentes, 22 caducas |
| Menciones desactualizadas de 1920 y 1922 («48 ediciones», «526 hojas», «917 a 938», «segundo semestre de 1922», «hasta el 21 de julio», «837 y 838») | 24.774/24.774 | 23 coincidencias; 1 desactualizada (02:97), corregida |
| Superlativos sobre mujeres con cargo, escuelas nacionales, apellidos de origen andino, actos fechados en el departamento y actos de dominio | 24.774/24.774 | 9 desmentidos por el propio libro (04:1265 no; 04:2019, 2239, 2326, 2407, 2421, 2525, 2614, 3242; A:93, 104, 113, 151; H:24; 22-infraestructura:517), todos corregidos |
| Remisiones a capítulos posteriores sin «más adelante» | 14/14 remisiones del tramo 04:1250–2620 | 14 sin marcar, marcadas |
| Muestra de 50 afirmaciones (aspecto 1), semilla 40 | 50 de 249 candidatas en 04:1250–2620 | 3 no son afirmaciones de hecho; **43/47 con fuente localizable (91,5 %)**; sin fuente: 04:1633 (caducidades de 1930), 04:1772 (disolución de Levilly y Cía., 1925), 04:1336 (edicto de 1921 a dos diarios), 04:2071 (ordenanza de 1983) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 280; 8/8 apéndices | sin cambios de recuento; el emparejamiento no se rehízo |
| Pedidos con objeto ya obtenido | 11 ítems con «ya se obtuvo» | los 11 piden un resto explícito; ninguno satisfecho entero |
| Superlativos en el texto agregado por la fase 6 | 79 segmentos agregados | 2 coincidencias, las dos con su universo dicho |
| Largo de los archivos antes y después de la fase 6 | 5/5 archivos tocados | sin cambios |
| Repositorios públicos | `corrige`, `dispositivo-caldereno`, `mapas_caldera` | los tres responden sin autenticación (P14) |
| Compilación | libro entero | compila (con `texlive-lang-spanish` instalado en el contenedor); 767 páginas; 0 referencias indefinidas; `.lof` con 41 entradas |

## Ronda 41 — auditoría con fase 6 (27/09/2026)

Base: commit `895e4d7` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1947, 1948, 1949), con la fase 6 de esta ronda en `ronda-41.patch` (commit `c7449a0`). **Denominador medido después de la fase 6: 24.883 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`), igual que en `895e4d7`: la fase 6 quita una línea de D (el pedido duplicado de la defensa de 1938) y agrega una a C (la Ley 1134).

### Traslado y caducidad de los tramos anteriores

Los tramos de las rondas 35 a 40 se trasladaron por script (`difflib`, línea a línea) por la cadena `591b074` → `67d1dae` → `8072c0e` → `5f220dc` → `5196df6` → `ae1f0b7` → `0c924bd` → `c0474ac` → `5388e3c` → `e1d4ada` → `895e4d7`, con el criterio de las rondas 39 y 40: en los commits de incorporación una línea modificada caduca; en los de fase 6 (`67d1dae`, `ae1f0b7`, `c0474ac`, `e1d4ada`) conserva su cobertura. El script incluye `main.tex`, que la ronda 38 registró, y reproduce los acumulados declarados (3.678; 3.627; 6.653; 6.650; 7.460; 8.921 en `e1d4ada`, uno más que los 8.920 que declaró la ronda 40). **En `895e4d7` quedan 8.874 vigentes**: caducan 47 por el AMPLÍA 1947-1949 (04-siglo 25, F-fuentes 5, A-cronologia 4, 26-presencia 3, 22-infraestructura 3, 20-opacidad 2, 17-aguabaja 2, 00-advertencia 1, 02-metodo 1, D-pedidos 1).

### Lectura sobre el texto (numeración de `895e4d7`; la fase 6 sólo corre una línea en D después de la 208 y agrega una en C después de la 105)

| Archivo | Líneas | Leídas | Nuevas |
|---|---|---|---|
| cap/03-fincas.tex | 1–1042 | 1.042 | 1.020 |
| cap/04-siglo.tex | 30–181, 608–862, 916–1251, 2890–4740 | 2.594 | 2.266 |
| cap/05-tierra.tex | 1–463 | 463 | 463 |
| cap/07-cot.tex | 1–368 | 368 | 368 |
| cap/08-vaqueros.tex | 1–317 | 317 | 317 |
| cap/09-defensas.tex | 360–400 | 41 | 41 |
| cap/10-expropiacion.tex | 1–567 | 567 | 567 |
| cap/22-infraestructura.tex | 498–512 | 15 | 0 |
| ape/A-cronologia.tex | 236–360 | 125 | 114 |
| ape/C-normativa.tex | 1–274 | 274 | 274 |
| ape/D-pedidos.tex | 30–209, 300–424 | 305 | 294 |
| ape/E-personas.tex | 85–160 | 76 | 75 |
| ape/F-fuentes.tex | 40–391 | 352 | 278 |
| ape/H-dominio.tex | 25–146 | 122 | 108 |

**Esta ronda: 6.661 líneas leídas, de las que 6.185 son nuevas.** En bytes equivalen a unas **221,3 páginas**: 709.434 bytes sobre 2.478.576 y 773 páginas. Ése es el denominador del aspecto 7. El diff entero del AMPLÍA `895e4d7` (226 líneas agregadas) cae dentro de estos tramos, salvo las líneas de 00, 02, 17, 18, 20, 22 y 26, que se leyeron en el diff y no se cuentan.

Acumulado: 8.874 vigentes + 6.185 = **15.059 de 24.883 (60,5 %)**.

### Cotejo sobre el facsímil (Release de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 2608 (1946) | 4 | Decreto 659-G | «Salta, Julio 6 de 1946»: da por terminada la intervención y nombra a Enrique Alejandro Pfister. El libro decía 6 de agosto en 04, 20 y 22-prospectiva (corregido); A ya decía 6 de julio |
| 2385 (1945) | 15 | Licitación Nº 1147 | «De conformidad con lo autorizado por el decreto N.o 8549 del 3 del mes en curso, llámase…», 25 de septiembre; \$2.515; propuestas hasta el 10 de octubre; «e|25|9|45 - v|11|10|45». El libro decía «Julio» y que el 8549 autorizaba la ejecución (corregido en 04 y A); el barrido de 2380–2412 da 15 ediciones con el aviso, no 16 |
| 1691 (1937) | 41 | Edicto Nº 3612 | Solicita el deslinde de La Helvecia «el señor Hermann Pfister»; perito Jorge de Bancarel. A decía que Pfister había sido perito en 1937 (corregido); 04 lo agrega. Cotejado en la capa, con la imagen del mismo pasaje ya transcripta en 03 |
| 3337 (1949) | 11 | Decreto 13793-E | 31 de enero; certificado Nº 1 por \$27.024,10; adjudicado por decreto 10668 del 29 de julio de 1948. Coincide; el art. 4º (Anexo I, Inciso III, Principal 1/c) se leyó en la capa |
| 3536 (1949) | 5 | Ley 1134 | Serrey, catastro 141, \$300.000, linderos. Coincide, salvo que la cita del art. 2º cortaba «y los gastos originados por la misma» (corregido) |
| 3514 (1949) | 23 | Decreto 17.056-G | La Caldera: un senador y un diputado en la imagen; «Intendente y Concejales» en el encabezado, leído en la capa. Coincide |
| 3431 (1949) | 7 | Decreto 15602-G | «Obras de defensa sobre los ríos Vaqueros y Wierna (Caldera)». Coincide |
| 3346 (1949) | 9 | Resolución de Minas 672 | 10 de febrero; «lugar denominado San José»; Exp. 44-L, 1929. Coincide |
| 3376 (1949) | 5 | Decreto 14548-G | 25 de marzo; petitorio de vecinos de Vaqueros. Coincide |
| 3540 (1949) | 10 | Decreto 17.557-G | Mojotoro «(Departamento de La Caldera)»; número y fecha en la capa. Coincide |
| 3547 (1949) | 10 | Decreto 17679-E | 4 de noviembre; certificado Nº 6 de la «Estación Sanitaria Tipo A de La Caldera», \$18.497,36. Coincide |
| 3397 (1949) | 12 | Decreto 14933-E | 21 de abril; Ebber, 5,71 l/s del Wierna, «8 Has. 3.800 m2», catastro 166. Coincide |
| 3414 (1949) | 5 | Resolución 806-E | 13 de mayo; setenta y cinco días a ECORM. El tercer dígito del número se lee 6 u 8 aun a 600 ppp; se deja 806 |

Son **13 citas cotejadas sobre 13 hojas**, 12 de ellas en la imagen. Una cita recortada que cambiaba el alcance (Ley 1134) y ninguna corrección silenciosa. Imágenes: `_sesion1949/_r41/c01.png` a `c15.png` en la máquina.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 8.921/8.921 líneas vigentes en `e1d4ada` | 8.874 vigentes, 47 caducas |
| Superlativos en las líneas que agregó el AMPLÍA | 54 coincidencias en 226 líneas | Todas dentro de los tramos leídos; 1 desmentida por el propio libro («una de las dos obras», 04:4563), corregida |
| Menciones desactualizadas de la ventana 1947-1950 («1947 a 1950 se barrieron», «termina en diciembre de 1946», «posterior a 1945», «las doce nóminas», «leyó edición por edición» en 1950) | 24.883/24.883 | 7 desactualizadas (01:139; 02:97, dos; 04:3548; 04:4546; 10:332; 22-infraestructura:545), todas corregidas |
| Cifras de la defensa de 1945 (\$2.515 y \$2.904,83) | 14 menciones en 04, 09, 20, 22, A y D | 3 de 04 daban \$2.515 como costo ejecutado (corregidas); 20:763, 22:501 y 22:509 lo dan como presupuesto, y quedan |
| Fecha del fin de la intervención de 1946 | 8 menciones | 7 decían agosto (04, cuatro; A:253; 20; 22-prospectiva), corregidas; A:254 ya decía julio |
| Remisiones a capítulos posteriores sin «más adelante» | 103 remisiones en los tramos leídos de 03, 04, 05, 07, 08 y 10 | 100 sin marcar, marcadas |
| Muestra de 50 afirmaciones (aspecto 1), semilla 41 | 50 de 636 candidatas en los tramos leídos de 03, 04, 05, 07, 08 y 10 | 3 no son afirmaciones de hecho; **41/47 con fuente localizable (87,2 %)**; sin fuente: 03:927 (deslinde de 1927), 04:3326 (gasto vial de 1937), 04:4022 (decreto 5466-E sin Boletín), 04:4205 (Res. 591 sin Boletín: agregado, B.O. 3104), 07:353 (comunicado municipal de 2020), 07:363 (declaración radial de 2026). Después de la fase 6, 42/47 |
| Muestra de 20 datos web o aportados (aspecto 9) | 20 en los tramos leídos | 9 trazables (IDESA, DOI de *Huellas*, *Construar*, Digesto de Vaqueros, visor, CNA, SNIH, ENARGAS); 11 sin URL o sin fecha (prensa y comunicados en 07, 08 y 10) |
| Lámina de cargos contra su texto | 1 lámina | 5 episodios de tutela dibujados; el texto decía 4 (corregido) |
| Pedidos de D satisfechos o duplicados | 305 líneas leídas de D | 1 satisfecho (por qué pide el Banco Provincial, que 04 ya explica) y 2 duplicados (defensa de 1938; constancia de los habitantes), corregidos |
| Largo de los archivos antes y después de la fase 6 | 15/15 archivos tocados | 13 sin cambios; D −1, C +1 |
| Compilación | Libro entero | Compila; 773 páginas; 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas de antes |

## Ronda 42 — auditoría con fase 6 (27/09/2026)

Base: commit `a647071` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1950), con la fase 6 de esta ronda en `ronda-42.patch` (commit `01915f3`). **Denominador medido: 24.964 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`), igual antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para los dos.

### Traslado y caducidad de los tramos anteriores

Los tramos de las rondas 35 a 41 se trasladaron por script (`difflib`, línea a línea) por toda la cadena, de `591b074` a `a647071`, con el criterio de siempre: en los commits de incorporación (`8072c0e`, `5f220dc`, `5196df6`, `0c924bd`, `5388e3c`, `895e4d7`, `a647071`) una línea modificada caduca; en los de fase 6 (`67d1dae`, `ae1f0b7`, `c0474ac`, `e1d4ada`, `4d89bcc`) conserva su cobertura. El script reproduce los acumulados declarados con una diferencia de una línea (7.459 por 7.460 en `c0474ac`, 8.873 por 8.874 en `895e4d7`, 15.058 por 15.059 después de la ronda 41). **En `a647071` quedan 14.997 vigentes**: la fase 6 de la ronda 41 (`4d89bcc`) deja 15.051, y el AMPLÍA 1950 hace caducar 54 (04-siglo, A, F, 00, 01, 02, 03, 10, 17-aguabaja, 20, 21, 22-infraestructura, 26, C y E).

### Lectura sobre el texto (numeración de `a647071`, igual a la de después de la fase 6)

Se leyeron **todas las líneas que no tenían cobertura vigente**. Los tramos marcados «auditor 1» a «auditor 7» los leyeron enteros siete subagentes de auditoría con un mismo encargo escrito (clases de defecto de la rúbrica 3.6, verificación antes de anotar, tramo leído declarado línea por línea); cada uno entregó sus hallazgos y sus correcciones, y **la sesión revisó en el diff cada corrección aplicada** antes de compilar. Los tramos «sesión» los leyó la sesión.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 1–20, 22–23, 39–54, 56–64, 66–73, 75–81, 84–85, 105–106, 109, 111–112, 114, 116–117, 119–126, 129–131, 134–135, 137–138, 141–146, 152–158, 160–162, 164, 166–179, 181–186, 188–189, 191–192, 197–199, 202–204, 207–210, 214–216, 219–222, 224–233, 273–278, 366–368, 370–373, 375–381, 383–391, 393–397, 399–403, 405–416, 418–421, 423–429, 431–440, 442–443, 446–449, 451–467, 469–490 | 272 | auditor 7 |
| ape/C-normativa.tex | 106 | 1 | sesión |
| ape/D-pedidos.tex | 102, 177–178, 180, 189–190, 209–213, 215, 217, 219–222, 224–226, 228–229, 231–237, 239–240, 247–249, 251, 253–263, 269–298 | 76 | auditor 7 |
| ape/E-personas.tex | 79–84 | 6 | sesión |
| ape/F-fuentes.tex | 26, 57, 64–66 | 5 | sesión |
| ape/G-propuestas.tex | 805–830 | 26 | auditor 7 |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 139 | 1 | sesión |
| cap/02-metodo.tex | 28 | 1 | sesión |
| cap/03-fincas.tex | 1016–1021, 1031 | 7 | sesión |
| cap/04-siglo.tex | 1–9, 576–598, 1330–1332, 2622–2701, 2743–2889, 2985–2990, 3637, 3658–3659, 3796–3798, 3888–3894, 4445–4447, 4449, 4451, 4555–4558, 4562–4575, 4578, 4581–4584, 4587–4589, 4593–4599, 4604–4612, 4623–4625, 4632–4669, 4737–4738 | 371 | sesión |
| cap/09-defensas.tex | 1–359, 401–439, 461–811 | 749 | auditor 6 |
| cap/10-expropiacion.tex | 115, 132 | 2 | sesión |
| cap/11-ribera.tex | 1–1054, 1063–1737 | 1729 | auditor 1 |
| cap/12-amparo.tex | 1–1254 | 1254 | auditor 2 |
| cap/13-loteo.tex | 1–820 | 820 | auditor 3 |
| cap/14-poblacion.tex | 1–781, 783–892 | 891 | auditor 4 |
| cap/15-hacienda.tex | 1–38, 53–80, 86–149, 166–548 | 513 | auditor 3 |
| cap/16-redes.tex | 1–885 | 885 | auditor 5 |
| cap/17-aguabaja.tex | 353, 365 | 2 | sesión |
| cap/17-tierrafiscal.tex | 1–667 | 667 | auditor 4 |
| cap/18-politica.tex | 1–370, 372–408, 413–724 | 719 | auditor 6 |
| cap/19-resistencias.tex | 1–955 | 955 | auditor 5 |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 213, 215–216, 545 | 4 | sesión |
| cap/26-presencia.tex | 157, 232–235, 245–246 | 7 | sesión |

**Esta ronda: 9,967 líneas nuevas.** En bytes equivalen a unas **350,4 páginas**: 1.125.063 bytes sobre 2.501.075 y 779 páginas. Ése es el denominador del aspecto 7. El diff entero del AMPLÍA `a647071` cae dentro de estos tramos.

Acumulado: 14.997 vigentes + 9,967 = **24.964 de 24.964 (100,0 %)**.

### Cotejo sobre el facsímil (Release 1950 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 3682 | 8 | Decreto 1477-E, recepción parcial | «constancia de la imposibilidad de someter a prueba las instalaciones sanitarias é instalación eléctrica, por carecer el edificio de provisión de aguas corrientes y energía eléctrica respectivamente»; «no han sido contempladas las provisiones de ambos flúidos». Coincide |
| 3646 | 8 | Decreto 883-E, visto | «de propiedad del señor Carlos Serrey», «con fines de colonización», «a favor de sus actuales arrenderos». Coincide |
| 3646 | 8 | Decreto 883-E, art. 1 | Fracción de 63 hectáreas 3.432 metros cuadrados «loteada en el año 1947 en lotes de dimensiones urbanas y para pequeñas quintas». Coincide, salvo que el libro escribía «N 17» donde la imagen dice «Nº 17» (corregido: corrección silenciosa) |
| 3864 | 4 | Decreto 4560-E | \$ 29.367.42; «con imputación a la cuenta especial "Depósi-tos en garantía"». Coincide |
| 3684 | 8 | Decreto 1503-E | «certificado final Nº 7 por un valor de \$ [7,54]»; la cifra cae fuera del recorte. Coincide en lo visible |
| 3601 | 3 | Decreto 22-E | Acta de recepción definitiva del 11 de octubre de 1949; «Cónrado» Marcuzzi. Coincide |
| 3773 | 4 | Decreto 3029-E | «Carlos Serrey y Manuel Serrey, inscripta a folio 123, asiento 15 del libro 1 del Registro de Inmuebles de La Caldera». Coincide |
| 3808 | 7 | Decreto 3533-E | «68 hectáreas 3432 mts. m2». Coincide |
| 3814 | 6 | Decreto 3712-E | «inventario de [cultivos, edificios, alam]brados, canales y mejoras»; el comienzo cae fuera del recorte |
| 3860 | 8 | Decreto 4490-E | «intensificar la producción hortícola de esa zona, para cumplimentar así uno de los aspectos o finalidad que motivó la expropiación». Coincide |
| 3767 | 5 | Decreto 2914-G | TRESCIENTOS PESOS. Coincide |
| 3793 | 9 | Decreto 3399-E | 1,14 l/seg para 2,1657 Ha; **en letras, «dos hectáreas un mil ciento cincuenta y siete metros cuadrados»**: discrepancia del original que el libro no declaraba (agregada en 04) |

Son **12 citas cotejadas sobre 11 hojas**, todas en la imagen: una corrección silenciosa («N 17») y ninguna cita que cambie el sentido. Recortes en `fac/` de la sesión (c_3682_8.png, v1.png, k_*.png).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 15.051/15.051 líneas vigentes en `4d89bcc` | 14.997 vigentes, 54 caducas por el AMPLÍA 1950 |
| Remisiones a capítulos posteriores sin «más adelante» | 312/312 `\ref{cap:…}` a capítulos posteriores (las de apéndices no se marcan, criterio de las rondas 35 a 41) | 189 sin marcar, todas marcadas; 0 al cerrar |
| Superlativos y ausencias en los tramos leídos | 311 revisados por los auditores | 20 desmentidos por el propio libro o sin sustento (corregidos); 3 sin universo en 11-ribera (401, 640, 1171) quedan sin corregir |
| Muestra de 50 afirmaciones (aspecto 1), semilla 42 | 50 de 2.271 candidatas en los tramos nuevos de 09 y 11 a 19 (8 descartadas por no ser afirmaciones de hecho) | **49/50 con fuente localizable (98 %)**; sin fuente: 19:839 (convocatoria de 2014 sin edición del Boletín) |
| Muestra de 20 datos web o de prensa (aspecto 9), semilla 42 | 20 de 117 frases con prensa o web en todo el libro; 12 son datos | **5/12 trazables** (IDESA ×3, ENARGAS, decretos); sin URL o fecha: El Tribuno (B:21, 14:389), Página/12 (18:654), sitio municipal (13:213, 17:55), nota periodística (14:27), carpeta técnica (05:58) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 281; 8/8 | los 52 con su pedido en D en los tramos auditados; un pedido faltante agregado (padrón «Baldío»); 3 pedidos satisfechos retirados (D:40, dos; 1950) |
| Lámina de cobertura del Boletín contra F | 1 lámina | la lámina pinta 1947 a 1950 como barrido automático; F los da leídos sobre la imagen (1947, 1949, 1950). Sin corregir: P37 |
| Largo de los archivos antes y después de la fase 6 | 29/29 archivos tocados | sin cambios |
| Compilación | libro entero | Compila; 779 páginas; 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas de antes |

## Ronda 43 — auditoría con fase 6 (28/09/2026)

Base: commit `86ee3b0` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1951), con la fase 6 de esta ronda en `ronda-43.patch` (commit `6f11387`). **Denominador medido: 24.983 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes de la fase 6 y **24.981** después: la fase 6 funde dos pares de filas duplicadas de `ape/A-cronologia.tex` (P38), que pasa de 500 a 498 líneas. **Ningún otro archivo cambia de largo.** La numeración de abajo es la de `86ee3b0`; en A, después de la fase 6, las líneas 156 a 164 bajan una y de la 166 en adelante bajan dos.

### Traslado y caducidad de los tramos anteriores

Los tramos de la ronda 42 se trasladaron por script (`difflib`, línea a línea) de `21f9a16` ---el commit de la fase 6 de la ronda 42 en el repositorio, `01915f3` en su sesión--- a `86ee3b0`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. En `21f9a16` estaban vigentes las 24.964 líneas (100,0 %). **El AMPLÍA 1951 hace caducar 95 líneas en 19 archivos** y deja **24.888 vigentes sobre 24.983 (99,6 %)**.

### Lectura sobre el texto (numeración de `86ee3b0`)

Se leyeron **las 95 líneas caducas, enteras, por la sesión**, sin subagentes. Además se releyeron como contexto 517 líneas que ya tenían cobertura vigente (04, 09, 10, 11, 16, 17, 18, 20, 21, 23, 26, A, C, D, F y H); no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 278–284, 286–291 (después de la fase 6: 276–282, 284–289) | 13 | sesión |
| ape/C-normativa.tex | 106 | 1 | sesión |
| ape/D-pedidos.tex | 102, 177, 180, 183, 189–190 | 6 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 64–66 | 6 | sesión |
| cap/00-advertencia.tex | 21, 43 | 2 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 1031 | 1 | sesión |
| cap/04-siglo.tex | 589–590, 3637, 3658–3660, 3894–3895, 3960, 4339, 4341, 4557–4558, 4599, 4638, 4669, 4738 | 17 | sesión |
| cap/09-defensas.tex | 499, 501, 509–510, 514, 526, 564–565 | 8 | sesión |
| cap/10-expropiacion.tex | 115, 332 | 2 | sesión |
| cap/16-redes.tex | 768–771, 773–775, 777, 780–785, 788–794 | 21 | sesión |
| cap/17-aguabaja.tex | 277–278, 281, 353, 364–365 | 6 | sesión |
| cap/18-politica.tex | 464 | 1 | sesión |
| cap/20-opacidad.tex | 655, 880 | 2 | sesión |
| cap/21-ausencias.tex | 58, 87 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 160 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

**Esta ronda: 95 líneas nuevas.** Con el contexto releído son 612 líneas y 137.098 bytes sobre 2.518.245, que en las 783 páginas de la base equivalen a **42,6 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `86ee3b0` cae dentro de estos tramos.

Acumulado: 24.888 vigentes + 95 = **24.983 de 24.983 (100,0 %)**. Después de la fase 6, que conserva la cobertura: **24.981 de 24.981 (100,0 %)**.

### Cotejo sobre el facsímil (Releases 1927, 1928, 1945 y 1951 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 3987 | 7 | Res. 953-A, visto | «el edificio del Hospital de la localidad de La Caldera que fuera cedido provisoriamente para sede de un hogar-escuela»; 25 de junio; \$669. Coincide |
| 3987 | 7 | Res. 953-A, detalle | «Gregorio M. García, Intendente de La Caldera», \$192; cuatro acreedores que suman \$669. Coincide |
| 4009 | 12 | Decreto 7637-E, considerando | «la Intendencia de Aguas respectiva informa que no tiene observación alguna que formular», inciso a) del art. 350. Coincide |
| 4009 | 12 | Decreto 7637-E, art. 2 | «Establécese que por no tenerse los aforos definitivos del río». Coincide |
| 4009 | 12 | Decreto 7637-E, cifras | 27 de julio; expte. 36/F/51; 10,5 l/s; 20 de 200 ha; catastro 136. Coincide |
| 3895 | 9 | Decretos 5268-E y 5269-E | **No coincide.** El 5268-E no se corta al pie de la columna: sigue en la cabeza de la tercera, con el art. 2 (ejecución «por vía administrativa») y el art. 3 (Obras de defensa permanente, Partida 7, «Rosario de Lerma, La Caldera, Capital, Cerrillos y Campo Santo», Ejercicio 1951). Corregido en A, 04, 09 y D |
| 4053 | 8 | Decreto 8701-E | \$281.800; depósito en el juicio de expropiación de la Finca Vaqueros; Banco de la Nación; juez Héctor Saravia Bavio; 8 de octubre. Coincide |
| 4074 | 14 | Decreto 9424-E | Emilio Ratel; Fracción de Finca «Entre Ríos»; catastro 165; 2 ha 9.637 m²; 0,75 l/s por ha. Coincide |
| 4102 | 9 | Decreto 10260-E | Carlos y Manuel Serrey; «SAUZAL» o «CURUZU»; catastro 126; 30 ha; 15,75 l/s. Coincide |
| 4058 | 5 | Ley 1402 | «que, por razones de domicilio y carencia de recursos, deban pernoctar en el pueblo»; \$150.000; cuarenta camas. Coincide, pero **está en la h. 5 y no en la 4**, que es sumario (26 y A corregidos) |
| 4048 | 4 | Ley 1356, incisos 9 y 10 | «40 varas de frente y fondo hasta el río», título de 1884; lotes 118, 119, 122 y 123 «en el plano número 17», título de 1950. Coincide, pero **en la h. 4** y no en la 5 (04 y D corregidos) |
| 3901 | 5 | Decreto 5445-E | «concluída»; \$40.767,50; Augusto E. Paladini, \$19.660. Coincide |
| 2429 | 5 | Decreto 9401-H (P32) | Es la liquidación de \$2.904,83 del 15 de noviembre de 1945, que cita el 9264-H del 31 de octubre; el libro le atribuía la autorización y transcribía «río de la Caldera» donde la imagen dice «La Caldera» (**corrección silenciosa**) |
| 1222 | 6 | Decreto 7095 (P41) | «Julio Royo Ortíz», con tilde. El libro normaliza «Ortiz» en la prosa; 18 lo declara |
| 1169 | 14 | Remate de Los Sauces (P17) | «extensión aproximada de 8.000 metros de Norte a Sud, por 17.000 metros de Naciente a Poniente»; base \$50.000. Coincide; el aviso es el **2190** y sigue en la h. 15 (04 y H decían 2188) |
| 1169 | 14 | Remate de Los Sauces, cita | «doctor Angel María Figueroa», sin tilde; el libro transcribía «Ángel» (**corrección silenciosa**) |

Son **16 citas cotejadas sobre 15 hojas**, todas en la imagen: dos correcciones silenciosas, ninguna cita que cambie el sentido, y un hecho que el libro daba por ausente del corpus (la imputación del 5268-E) y que está en la misma hoja. Recortes en `fac/` de la sesión.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 24.964/24.964 líneas vigentes en `21f9a16` | 24.888 vigentes, 95 caducas por el AMPLÍA 1951 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`) | 314/314 `\ref{cap:…}` a capítulos posteriores | 2 sin marcar: 04:4599 (del AMPLÍA 1951, corregida) y 26:6 (falso positivo: la marca está en la línea siguiente); 0 al cerrar, sobre 315 |
| Superlativos y ausencias con 1949, 1950 o 1951 en la misma oración (repaso de ventana) | 41 oraciones en todo el libro, todas leídas | 3 sin universo o sobre años no leídos (04:4338, 20:653, 21:64), 1 ausencia falsa que el propio párrafo desmiente (10:330); corregidas |
| Superlativos en el texto agregado por la fase 6 | 4 fragmentos | todos con universo declarado |
| Muestra de 50 afirmaciones (aspecto 1), semilla 43 | 50 de 212 oraciones con cifra en las 95 líneas nuevas | **49/50 con fuente localizable (98 %)**; sin fuente: 02:97 (cobertura del repositorio descargable, sin URL) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 95 líneas nuevas | no se rehízo; vale la de la ronda 42 (5/12) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 281; 8/8 | sin cambios; D:200 pedía lo que el capítulo 10 ya da (denegatoria de 1939) y D:263 contaba 31 filas donde H tiene 28 (recontadas por script): corregidos |
| Filas de H de 1924 a 1945 sin edición | 34 filas del tramo | 28 sin edición (D:263 decía 31) |
| Distancia 201/13–144/17 (`mapas_caldera/datos/ribera`) | 18 × 8 puntos | mínimo 13,51 m, de LRd18 a LRmd4a (último de la margen derecha de la ampliación): 11:506 corregido, 11:705 ya lo decía |
| Largo de los archivos antes y después de la fase 6 | 13/13 archivos tocados por la fase 6 | A: 500 → 498; los demás, sin cambios |
| Compilación | libro entero | Compila; 781 páginas (783 la base); 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas de antes |

## Ronda 44 — auditoría con fase 6 (28/09/2026)

Base: commit `570ed07` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1952), con la fase 6 de esta ronda en `ronda-44.patch` (commit `c48a739` en la sesión). **Denominador medido: 24.989 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos de la ronda 43 se trasladaron por diff de `3a6804b` (el commit de la fase 6 de la ronda 43 en el repositorio, `6f11387` en su sesión) a `570ed07`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. En `3a6804b` estaban vigentes las 24.981 líneas (100,0 %). **El AMPLÍA 1952 agrega 8 líneas en A y hace caducar 66 líneas en 20 archivos**, y deja **24.923 vigentes sobre 24.989 (99,7 %)**.

### Lectura sobre el texto (numeración de `570ed07`)

Se leyeron **las 66 líneas caducas, enteras, por la sesión**, sin subagentes. Además se releyeron como contexto 118 líneas que ya tenían cobertura vigente (04, 09, 16, 17, 20, 21, 22-prospectiva, 26 y A); no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 280, 290–297 | 9 | sesión |
| ape/C-normativa.tex | 106 | 1 | sesión |
| ape/D-pedidos.tex | 102, 177, 180, 183, 189–190 | 6 | sesión |
| ape/E-personas.tex | 84 | 1 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 64–66 | 6 | sesión |
| cap/00-advertencia.tex | 21, 43 | 2 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 1031 | 1 | sesión |
| cap/04-siglo.tex | 589–590, 3637, 3639, 3658–3660, 3894–3895, 3960, 4557–4558, 4599, 4612, 4669, 4738 | 16 | sesión |
| cap/09-defensas.tex | 526, 535 | 2 | sesión |
| cap/10-expropiacion.tex | 115, 332 | 2 | sesión |
| cap/16-redes.tex | 762, 787, 789–790, 794 | 5 | sesión |
| cap/17-aguabaja.tex | 281, 284, 353, 365 | 4 | sesión |
| cap/18-politica.tex | 464 | 1 | sesión |
| cap/20-opacidad.tex | 880 | 1 | sesión |
| cap/21-ausencias.tex | 65, 87 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 160 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído (no suma cobertura): 04:1826–1830, 2860–2866, 3955–3959, 3961, 4590–4598, 4600; 09:515–525, 527–534, 536; 16:760–761, 763–786, 788, 791–793, 795; 17:277–280, 282–283, 285; 20:876–879, 881–884; 21:60–64, 66, 85–86; 22-prospectiva:156–159, 161–164; 26:228–234; A:277.

**Esta ronda: 66 líneas nuevas.** Con el contexto releído son 184 líneas y 93.385 bytes sobre 2.537.845, que en las 787 páginas de la base equivalen a **29,0 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `570ed07` cae dentro de estos tramos.

Acumulado: 24.923 vigentes + 66 = **24.989 de 24.989 (100,0 %)**. La fase 6 toca 15 líneas, todas dentro de lo leído en esta ronda, y no cambia el largo de ningún archivo: **24.989 de 24.989 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1952 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 4201 | 6 | Decreto 13108-A, considerando | «recorriendo largas distancias a caballo». Coincide |
| 4201 | 6 | Decreto 13108-A, considerando | «Estación Sanitaria instalada en el mismo pueblo», tres veces por semana, médico y enfermera partera «con residencia permanente». Coincide |
| 4201 | 6 | Decreto 13108-A, considerando | «no es indispensable la habilitación de dicho edificio como Hospital general». Coincide |
| 4201 | 6 | Decreto 13108-A, arts. 1 a 3 | «por el corriente año lectivo», «Doctor Francisco Ortelli», «HOGAR EVITA», «ya terminado y equipado», Comisión «Pro-Hogar de La Caldera» presidida por el Intendente, \$3.000 por mes. Coincide |
| 4248 | 6 | Decreto 1001-E | «para dotar de iluminación», \$1.057 + \$230 = \$1.287. Coincide, pero el original dice «edificio **construído**» en el visto y en el art. 1; el libro transcribía «construido» (**corrección silenciosa**; A y 04 corregidos) |
| 4187 | 8 | Decreto 12744-E | «no son normales»; 40 km; 2/3 de viáticos. Coincide, pero el original imprime «los relevamientos **tos** topográficos» (sílaba repetida al cambio de renglón); el libro la suprimía (**corrección silenciosa**; A corregido con [sic]) |
| 4137 | 7 | Decreto 11303-E | «de inmediato», «estado deficiente», «varios pequeños predios rurales», margen izquierda aguas abajo del puente, vecinos de la localidad de Vaqueros. Coincide |
| 4116 | 9–10 | Decreto 10662-E | Turno de cuarenta horas semanales, 19/30 del río, dieciséis hectáreas, 0,75 l/s por hectárea. Coincide, pero **el encabezado está en la h. 9 y el artículo en la h. 10**; el libro citaba sólo la 9 (A y 04 corregidos) |
| 4238 | 12 | Decreto 804-E | «la Intervención de la Administración General de Aguas»; «la Intendencia de Aguas respectiva». Coincide |
| 4202 | 4 | Ley 1433 | «Caldera» en el grupo A, de once departamentos. Coincide |
| 4275 | 8 | Decreto 1663-E | «servicios públicos de pasajeros en automotor entre la ciudad de Salta y la localidad de Vaqueros»; permiso precario por un año. Coincide |
| 4333 | 6 | Decreto 2888-E | «hasta la localidad de La Caldera». Coincide |
| 4208 | 5 | Res. 2092-A | «con destino a la habilitación del Hospital de "LA CALDERA"»; 20 de mayo. Coincide |
| 4301 | 10 | Decreto 2291-E, cuadro | La Caldera, renglón 30, 0.947 bajo «PORCENTAJES %». Coincide, pero **el renglón está en la h. 10** y el libro citaba la 9 sin la unidad (A corregido) |
| 4308 | 8 | Decreto 2502-E, cuadro | La Caldera, \$24.362,97 y 0,235. Coincide |
| 4292 | 6 | Decreto 2026-E | «construcción de defensas sobre el Río Vaqueros», \$7.440. Coincide |
| 4128 | 16 | Decreto 11102-E | Julia Cruz de Salustri, 1,6 l/s, Wierna, 2,9640 ha, catastro 172. Coincide |

Son **17 citas cotejadas sobre 15 hojas de 14 ediciones**, todas en la imagen: dos correcciones silenciosas, ninguna cita que cambie el sentido y dos hojas mal citadas. Recortes en `fac/` de la sesión.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 24.981/24.981 líneas vigentes en `3a6804b` | 24.923 vigentes, 66 caducas por el AMPLÍA 1952 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`) | 315/315 `\ref{cap:…}` a capítulos posteriores | 0 sin marcar, antes y después de la fase 6 |
| Superlativos y ausencias con 1952, 1949–1952, «cuatrienio», «cuatro años» o 1953 en la misma oración (repaso de ventana) | 21 oraciones en todo el libro, todas leídas | ninguna desmentida; A:280 («único nombre… en los cuatro años leídos desde la convocatoria de 1949») cierra con 1952 |
| Superlativos con universo «años leídos», «serie», «archivo leído», 1949–1951 o 1951, sin 1952 | 36 oraciones en todo el libro, todas leídas | ninguna cuyo universo quede desmentido por 1952 |
| Superlativos en el texto agregado por la fase 6 | 19 fragmentos | ninguno |
| Muestra de 50 afirmaciones (aspecto 1), semilla 44 | 50 de 243 oraciones con cifra en las 66 líneas nuevas | **50/50 con fuente localizable** (30 con edición y hoja en la oración; 20 de método o cobertura, cuya fuente es el relevamiento que F describe, o con remisión a capítulo o apéndice) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 66 líneas nuevas | no se rehízo; vale la de la ronda 42 (5/12) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 281; 8/8 | sin cambios; ningún pedido de D satisfecho por 1952 |
| Recuento de dotaciones de 1952 contra A:296 | 8 decretos y 11 edictos | 04 y D decían «ocho reconocimientos»; 17 y D omitían Las Chuñas (y D el turno de Linares): corregidos |
| Largo de los archivos antes y después de la fase 6 | 8/8 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero | Compila; 787 páginas (787 la base); 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas de antes |

## Ronda 45 — auditoría con fase 6 (28/09/2026)

Base: commit `8182f9d` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1953), con la fase 6 de esta ronda en `ronda-45.patch` (commit `73d6374` en la sesión). **Denominador medido: 25.000 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos de la ronda 44 se trasladaron por diff de `70b1f1f` (el commit de la fase 6 de la ronda 44 en el repositorio, `c48a739` en su sesión) a `8182f9d`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. En `70b1f1f` estaban vigentes las 24.989 líneas (100,0 %). **El AMPLÍA 1953 agrega 11 líneas (8 en A y 3 en D) y hace caducar 70 líneas en 19 archivos**, y deja **24.930 vigentes sobre 25.000 (99,7 %)**.

### Lectura sobre el texto (numeración de `8182f9d`)

Se leyeron **las 70 líneas caducas, enteras, por la sesión**, sin subagentes. Además se releyeron como contexto 31 líneas que ya tenían cobertura vigente; no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 280, 297–305 | 10 | sesión |
| ape/C-normativa.tex | 106 | 1 | sesión |
| ape/D-pedidos.tex | 102, 177, 183, 189–193 | 8 | sesión |
| ape/E-personas.tex | 68, 84 | 2 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 64–66 | 6 | sesión |
| cap/00-advertencia.tex | 21, 43 | 2 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 389, 391–393, 1031 | 5 | sesión |
| cap/04-siglo.tex | 589–590, 1413, 3637, 3639, 3658–3660, 3894–3895, 4557–4558, 4599, 4669, 4738 | 15 | sesión |
| cap/09-defensas.tex | 526, 535 | 2 | sesión |
| cap/10-expropiacion.tex | 115, 332 | 2 | sesión |
| cap/16-redes.tex | 762, 789, 794 | 3 | sesión |
| cap/17-aguabaja.tex | 281, 284, 353, 365 | 4 | sesión |
| cap/18-politica.tex | 464 | 1 | sesión |
| cap/20-opacidad.tex | 880 | 1 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 41, 545 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído (no suma cobertura): 00:17–20, 22–24; 03:385–388, 390, 394–398; 04:3632–3636, 3638, 3640–3641; 22-prospectiva:286–291.

**Esta ronda: 70 líneas nuevas.** Con el contexto releído son 101 líneas y 104.053 bytes sobre 2.561.020, que en las 795 páginas de la base equivalen a **32,3 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `8182f9d` cae dentro de estos tramos.

Acumulado: 24.930 vigentes + 70 = **25.000 de 25.000 (100,0 %)**. La fase 6 toca 15 líneas: 14 dentro de lo leído en esta ronda y la 290 de 22-prospectiva, releída como contexto; no cambia el largo de ningún archivo: **25.000 de 25.000 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1953 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 4420 | 10 | Decreto 4825-E, encabezado y cláusula 1.ª | Manuel Serrey «por sí y en representación de su padre D. Carlos Serrey»; «que fueran propietarios». Coincide |
| 4420 | 10 | Decreto 4825-E, cláusulas 3.ª, 4.ª y 8.ª | Cinco hectáreas, diez para «las cuatro personas» que cultivan tabaco; «exclusivamente» a arrendatarios y medieros; \$3.000 la hectárea, \$281.800 y 8 % anual. Coincide, pero el precio es «excluídas las mejoras», que el libro omitía (A corregido) |
| 4420 | 10 | Decreto 4825-E, cláusulas 5.ª y 6.ª | «Las adjudicaciones de parcelas ya efectuadas y conformadas por nota por los beneficiarios, se respetarán»; los propietarios se reservan parte de la superficie a fraccionar, «de acuerdo al plano que se agrega»; excedentes y desistimientos vuelven a ellos «en libre disposición» (cl. 4.ª). **El libro no lo decía, y 10 afirmaba que el Estado no adjudicaba** (10, 04, A, C y D corregidos) |
| 4420 | 11 | Decreto 4825-E, cláusulas 9.ª a 12.ª y cierre | «La plena posesión del resto de la finca expropiada»; «Juzgado Nacional, expediente 26.489/1950»; «simple remisión de las actuaciones al archivo»; firmado el 16 de abril de 1953. Coincide. El informe LEE las había leído sólo en la capa (P57) |
| 4453 | 7 | Decreto 5564-E, visto y art. 1.º | Instituto Concepcionista «ubicado en el Departamento de La Caldera, Partido de Vaqueros»; Ley 968 (la de Obras Públicas); catastro 157; 736 ha 6.446 m²; título a folio 204, asiento 261 del libro 3 de La Caldera. Coincide; el título se suma a 03 y D |
| 4453 | 8 | Decreto 5564-E, linderos y art. 2.º | Finca Vaqueros de Carlos y Manuel Serrey, río Vaqueros, camino nacional a Jujuy, finca Lesser; \$60.000, «valor fiscal»; exceptúa las fracciones «transferidas a terceras personas». Coincide; la excepción se suma a 03 |
| 4419 | 6 | Decreto 4778-E | «Cerro de Buena Vista», catastro 182, en Vaqueros, de otros dueños. Coincide (el visto imprime el dígito del medio dudoso; la parte resolutiva, «182», limpio) |
| 4403 | 9 | Decreto 4431-E | 24 de marzo; resolución 661 del 27/11/1952 dejada sin efecto; 240 l/s de la «capa sub-alvea»; «de oficio»; «con destino al abastecimiento de la población de la ciudad de Salta»; art. 40 del Código de Aguas; planos de captación. Coincide |
| 4412 | 12 | Decreto 4655-E | «en mérito a que los mismos pasaron a depender de los usuarios»; dos tomeros de La Caldera y dos de Vaqueros. Coincide, pero **la baja es de los tomeros de toda la provincia** (unos treinta, de Orán a Cafayate); 17 decía «los tomeros de los ríos La Caldera y Vaqueros» (corregido) |
| 4373 | 5 | Res. 738 aprobada, Dina I. Lozano de Robles | «treinta y nueve decilitros por segundo»; 7556 m²; «acequia Municipal». Coincide |
| 4485 | 7 | Decreto 6216-A, art. 2.º | «Mucama del Hospital de La Caldera». Coincide, pero es un interinato **mientras dure la licencia de la titular**, no una vacante (A, 04 y D corregidos) |
| 4503 | 11 | Decreto 6553-A | «Mucama de la Estación Sanitaria» de La Caldera; reemplazo por licencia de la misma titular. Coincide (misma corrección) |
| 4552 | 6 | Decreto 7535-A, art. 3.º | «Mucama del Consultorio Externo de La Caldera», por la licencia reglamentaria de la titular. Coincide (misma corrección) |
| 4563 | 7 | Decreto 7738-E | \$12.646,55; juicio contra Mariano Sivila; «decreto 9817\|48», **legible** a 150 ppi. A y 04 decían que el dígito del año no se leía (corregidos) |
| 4350 | 5 | Decreto 3243-E, cuadro | «La Caldera ---Exprop. 1 manz. Estac. Sanitaria ... \$ 7.000». Coincide |
| 4474 | 9 | Decreto 6031-G | «ESTHER BLANCA REYES»; el decreto dice «de acuerdo al certificado de nacimiento» que corre en el expediente; A y E decían «partida» (corregidos) |
| 4559 | 5 | Decreto 7667-G | Vaqueros; *ad honorem*; «se encontraba a cargo de la Autoridad Policial del lugar». Coincide |
| 4438 | 8 | Decreto 5230-E | «art. 92, inc. b) de la Ley 775». Coincide |
| 4496 | 5 | Decreto 6418-E | El Angosto, catastro 60, 53 ha; «10\|30 avas partes del total del caudal». Coincide |
| 4532 | 7 | Decreto 7151-E | Getsemaní, catastro 61, 30 ha; «19\|30 avas partes», «turno de 216 horas quincenales». Coincide |
| 4522 | 11 | Edictos del 30 de septiembre | «S/C Ley 1627». Coincide |

Son **21 citas cotejadas sobre 19 hojas de 17 ediciones**, todas en la imagen: ninguna corrección silenciosa dentro de comillas, ninguna cita que cambie el sentido, y cinco paráfrasis que el facsímil corrige (mejoras, suplencia, certificado, alcance provincial de los tomeros, 9817|48) más una omisión que cambia una frase (adjudicaciones ya efectuadas). No se cotejaron: 4392 h8–10 (Plan Quinquenal), 4466 h11 (5859-A) ni 4541 h12 (7367-A).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 24.989/24.989 líneas vigentes en `70b1f1f` | 24.930 vigentes, 70 caducas por el AMPLÍA 1953 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`) | 316/316 `\ref{cap:…}` a capítulos posteriores | 0 sin marcar, antes y después de la fase 6 |
| Superlativos y ausencias con 1953, «quinquenio», «cinco años», 1949–1953 en la misma oración (repaso de ventana) | 12 oraciones en todo el libro, todas leídas | ninguna desmentida; A:280 («único nombre… en los cinco años leídos desde la convocatoria de 1949») cierra con 1953; 04:3636 («la lectura de 1947 a 1953 no encontró») incluye 1948, de barrido, y se deja porque dice «no encontró» |
| Superlativos con universo «cuatrienio», «cuatro años», 1949–1952, «años leídos», «archivo leído» o «serie», sin 1953 | 19 oraciones en todo el libro, todas leídas | ninguna cuyo universo quede desmentido por 1953 |
| Superlativos y ausencias en el texto agregado por la fase 6 | 22 reemplazos | cuatro ausencias («ningún acto leído publica», «ningún acto del año publica una adjudicación», «tampoco se publica ninguna», «que ningún acto publicado registra»), todas sobre 1949–1953, leídos sobre la imagen |
| Muestra de 50 afirmaciones (aspecto 1), semilla 45 | 50 de 292 oraciones con cifra en las 70 líneas nuevas | **49/50 con fuente localizable**; la que falta es D:183 (decreto 5466-E sin Boletín ni hoja), ya en P30 |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 70 líneas nuevas | no se rehízo; vale la de la ronda 42 (5/12) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 284; 8/8 | **22-prospectiva:290 decía «doscientos setenta y ocho pedidos» contra 284 `\item` de D** (desfase que venía de `895e4d7`, con 282): corregido |
| Recuento de hojas de 1950, 1951 y 1953 contra las tapas (F:57) | 3 años | 4.274 − 128 ≠ 4.156; 4.034 − 89 ≠ 4.025; 4.350 − 70 ≠ 4.305: faltaban las ediciones con hojas que la tapa no cuenta (10, 80 y 25, según los informes LEE): corregido |
| Largo de los archivos antes y después de la fase 6 | 10/10 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero | Compila; 795 páginas (795 la base); 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas de antes |

## Ronda 46 — auditoría con fase 6 (28/09/2026)

Base: commit `cef0e1d` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1954), con la fase 6 de esta ronda en `ronda-46.patch` (commit `2d942b0` en la sesión). **Denominador medido: 25.009 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos de la ronda 45 se trasladaron por diff de `3fb5644` (el commit de la fase 6 de la ronda 45 en el repositorio, `73d6374` en su sesión) a `cef0e1d`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. En `3fb5644` estaban vigentes las 25.000 líneas (100,0 %). **El AMPLÍA 1954 agrega 9 líneas (todas en A) y hace caducar 72 líneas en 18 archivos**, y deja **24.937 vigentes sobre 25.009 (99,7 %)**.

### Lectura sobre el texto (numeración de `cef0e1d`)

Se leyeron **las 72 líneas caducas, enteras, por la sesión**, sin subagentes, cotejadas ficha por ficha contra el informe LEE 1954 (`BO-Salta-1954_4587-4830_la-caldera_LEE-1954_2026-09-28.txt`, 67 fichas del §A y 11 de B.2). Además se releyeron como contexto 27 líneas que ya tenían cobertura vigente; no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 280, 298, 300, 302–303, 305–314 | 15 | sesión |
| ape/C-normativa.tex | 95, 106 | 2 | sesión |
| ape/D-pedidos.tex | 32, 102, 177–178, 183, 189–193 | 10 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 64–66 | 6 | sesión |
| cap/00-advertencia.tex | 21, 43 | 2 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 389, 938, 1031 | 3 | sesión |
| cap/04-siglo.tex | 589–590, 3637, 3639, 3658–3660, 3894, 4557–4558, 4599, 4669, 4738 | 13 | sesión |
| cap/09-defensas.tex | 526, 535 | 2 | sesión |
| cap/10-expropiacion.tex | 115, 332 | 2 | sesión |
| cap/16-redes.tex | 762, 789, 794 | 3 | sesión |
| cap/17-aguabaja.tex | 281, 284, 353, 365 | 4 | sesión |
| cap/18-politica.tex | 464 | 1 | sesión |
| cap/20-opacidad.tex | 880 | 1 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 223, 545 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído (no suma cobertura): 15-hacienda:200–214; 04:1826–1830; 21-ausencias:62–66; A:155, 175.

**Esta ronda: 72 líneas nuevas.** Con el contexto releído son 99 líneas y 117.317 bytes sobre 2.585.131, que en las 803 páginas de la base equivalen a **36,4 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `cef0e1d` cae dentro de estos tramos.

Acumulado: 24.937 vigentes + 72 = **25.009 de 25.009 (100,0 %)**. La fase 6 toca 10 líneas: 9 dentro de lo leído en esta ronda (A:298, 306, 307, 310, 314; F:57; 04:4599, 4669; 10:115) y la 214 de 15-hacienda, releída como contexto; no cambia el largo de ningún archivo: **25.009 de 25.009 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1953 y 1954 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 4593 | 5 | Decreto 8358-E, cuarto considerando | «no fué sin embargo plena»; «percibieron y perciben los arriendos correspondientes y la utilizan en su exclusivo beneficio». La cita coincide, pero **«en su exclusivo beneficio» califica el uso de la finca, no el cobro de los arriendos**, como la leía 04:4669 (corregido) |
| 4593 | 5 | Decreto 8358-E, séptimo considerando | «a pesar de la mediación del Poder Ejecutivo»; «una justa distribución de las tierras a fraccionarse». Coincide |
| 4593 | 5 | Decreto 8358-E, considerando de la disyuntiva | «una única solución»; «el régimen que rige los arrendatarios rurales» [sic]. Coincide; A y 04 lo parafrasean fuera de comillas |
| 4593 | 6 | Decreto 8358-E, último considerando y arts. 1.º y 2.º | «artículo 39 de la Ley 1336»; Carlos y Manuel Serrey; Escribano de Gobierno. Coincide |
| 4599 | 6 | Decreto 8475-A | «Hospital de La Caldera», cañerías, 14 de enero de 1954. Coincide |
| 4643 | 12 | Decreto 9333-A | «Oficial 3.º, Méd. Hosp. La Caldera, Dr. EUGENIO ROMANOV». Coincide |
| 4674 | 7 | Resolución 3132-A | «Consultorio Externo de la Caldera», con minúscula; el libro citaba «de La Caldera» en A y 04 (**corrección silenciosa**, corregida); «Dr. Eugenio Romanow», \$120. Coincide |
| 4650 | 8 | Decreto 9576-G, sección femenina | Circuito 5: mesas 1 y 3 en la Escuela Elemental Mixta, mesa 2 en la Iglesia Parroquial; circuito 6: Vaqueros y estación de Mojotoro. **La iglesia tiene una mesa por sexo**, no una en total, como sumaba A (corregido) |
| 4700 | 5 | Edicto 10954 | «Cerro Bueno Vista», catastro 112, Germán Peral, río Vaqueros, 1,05 l/s, hijuela Urquiza. Coincide |
| 4705 | 11 | Edicto 10994 | Ma. Elena Costas de Patrón Costas, «inscrip. aguas priv», Resolución 383/54, art. 183 del Código de Aguas. Coincide |
| 4720 | 13 | Decreto 10851-E, visto | «piedra embolsada», «Río La Caldera», \$88.928, Resolución 794 del 23 de diciembre de 1953. Coincide |
| 4726 | 5 | Decreto 10954-E | «los trabajos de relevamiento y plano regular de la localidad de La Caldera». Coincide |
| 4747 | 7 | Decreto 11380-G, art. 2.º | Designa interinamente al reemplazante del médico regional de Cerrillos–La Merced, «debiendo atender además los consultorios de Vaqueros», **desde el 11 de septiembre**. A lo ponía en simultáneo con mayo (corregido) |
| 4756 | 6 | Decreto 11505-E | «completamente inutilizado a consecuencia de las crecientes del Río Wie[r]na». Coincide |
| 4822 | 6 | Decreto 12575-E, considerandos 1.º a 3.º | \$100.000; pagaré a ciento ochenta días; «Concluir con el parcelamiento [a favor de] los arrendatarios de la finca» (el recorte corta el margen; el informe LEE lo da entero). Coincide |
| 4466 (1953) | 11 | Decreto 5859-A | Designa desde el 18 de junio de 1953 médico regional de La Caldera a Eugenio Romanow. **Es el médico que A:298 describía por su condición de extranjero** en la fila de 1953, y que el AMPLÍA 1954 nombra en la de 1954 (P58; corregido en A:298) |

Son **16 citas cotejadas sobre 15 hojas de 15 ediciones** (14 de 1954 y una de 1953), todas en la imagen: una corrección silenciosa dentro de comillas («La Caldera» por «la Caldera»), ninguna cita que cambie el sentido, y tres paráfrasis que el facsímil corrige (a qué califica «en su exclusivo beneficio», las mesas de la iglesia y la fecha del interinato de Cerrillos). No se cotejaron: 4609 h6–7 (8545-G), 4622, 4633, 4648, 4654 y 4656 h8–12 (decretos y edictos de agua), 4827 h10 (12687-E) ni 4663 h14 (9928-E).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.000/25.000 líneas vigentes en `3fb5644` | 24.937 vigentes, 72 caducas por el AMPLÍA 1954 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`) | 316/316 `\ref{cap:…}` a capítulos posteriores | 0 sin marcar, antes y después de la fase 6 |
| Superlativos y ausencias con 1954, 1955, «sexenio», «seis años» o 1949–1954 en la misma oración (repaso de ventana) | 19 oraciones en todo el libro, todas leídas | ninguna desmentida; A:280 («único nombre… en los seis años leídos desde la convocatoria de 1949») cierra con 1954 |
| Superlativos con universo «quinquenio», «cinco años», 1949–1953, «años leídos», «archivo leído» o «en toda la serie», sin 1954 | 12 oraciones en todo el libro, todas leídas | **una desmentida por 1954: 15-hacienda:213–214, «las dos únicas obligaciones que el archivo leído documenta», contra la deuda con la Caja de Jubilaciones de 1954 que A:314 ya traía** (corregida: universo 1932–1940 y la tercera nombrada) |
| Superlativos y ausencias en el texto agregado por la fase 6 | 11 reemplazos | uno, «las dos únicas… entre 1932 y 1940», con su universo declarado |
| Muestra de 50 afirmaciones (aspecto 1), semilla 46 | 50 de 317 oraciones con cifra en las 72 líneas nuevas | **50/50 con fuente localizable**: 21 no llevan la cita en la misma oración, y la tienen en el párrafo (04:4599, 4669; A:302) o son declaraciones de cobertura de F, 00, 01, 02, 09 y 20 cuya fuente es el propio apéndice F y el informe LEE |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 72 líneas nuevas | no se rehízo; vale la de la ronda 42 (5/12) |
| Dotaciones de 1954 recalculadas desde caudal y superficie | 11 cocientes de los 10 decretos y 8 de los 10 edictos | decretos 0,482 a 0,539 (el 0,482 es Vivas de Kelly); edictos 0,516 a 0,528; cierran A, D:102, 04:3894, 04:4738 y 17:353 |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 284; 8/8 | 22-prospectiva dice 284: cierra |
| Recuento de hojas de 1954 contra las tapas (F:57) | 244 ediciones | **4.634 − 96 + 7 ≠ 4.584: faltaban las 39 hojas de las dos ediciones cuya tapa no deja leer la cifra (4697, 17; 4811, 22)**; con ellas, 4.634 − 96 + 7 + 39 = 4.584 (corregido) |
| Rango de edictos citado en A (1954) | 10 edictos de agua del informe LEE | «edictos 10676 a 10680» incluía el 10679, que no es del departamento (corregido: 10676 a 10678 y 10680) |
| Privacidad: personas nombradas en las 72 líneas nuevas, cruzadas con atributos sensibles y contextos socioeconómicos en todo A | 72/72 líneas nuevas, leídas enteras, y búsqueda en todo el libro de cada nombre en contexto sensible | dos casos: el médico de 1953 descripto por su condición de extranjero en A:298, identificable por su nombre en A:306 y 04:4599 (tope 60), y un deudor de dos remates judiciales nombrado en A:314; los dos corregidos |
| Largo de los archivos antes y después de la fase 6 | 5/5 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero | Compila; 803 páginas (803 la base); 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:78; 2 cajas desbordadas, las mismas de antes |

## Ronda 46 — agregado (28/09/2026, después de registrar el bloque anterior)

El bloque anterior quedó registrado antes de que Eduardo leyera los recortes. Este agregado no lo modifica: lo completa y corrige tres cosas de él.

- **Commits.** En el libro, la fase 6 quedó en dos commits: `0debc30` (el `2d942b0` de la sesión, registrado) y `d397f08` (segunda parte, con este agregado). El árbol resultante es idéntico al `ecd8dc1` que `estado.json` registra para la ronda 46.
- **La fila de 4756 h6 del cotejo** decía «Coincide». Sobre el recorte, Eduardo lee «Río Wie_na»: falta la r en el original, y A y 22 citaban «Wierna» entre comillas. Es una **corrección silenciosa**, la segunda de la ronda, y se corrige a «Wie[r]na» en `d397f08`. Las citas cotejadas siguen siendo 16; las correcciones silenciosas pasan a dos.
- **El año de la patente de Arévalo** (Res. 564-E, 4699 h9): A decía «1948 o 1949» y ahora dice «de los años cuarenta, con el último dígito sobreimpreso» (`d397f08`). Es una cifra tomada del informe LEE sin decidir en la imagen (aspecto 3).
- **Notas.** Con estos dos hallazgos, la nota inicial sin tope es 76,8 (aspecto 3: 90; aspecto 4: 84). La nota inicial con tope (60,0) y la final (88,3) no cambian. Hallazgos: 12, todos aplicados; 11 en material del AMPLÍA 1954. Es lo que ya registra `mejora-ronda-46.json` en `estado.json`.
- **Largo.** `d397f08` toca A:311 y A:314 y 22-infraestructura:223, todas dentro de lo leído en la ronda; ningún archivo cambia de largo. La cobertura acumulada sigue en 25.009 de 25.009 (100,0 %). El libro compila: 803 páginas, 0 referencias indefinidas, `.lof` con 41 entradas.

### Lecturas humanas sobre el facsímil (Eduardo, 28/09/2026)

Las nueve dudas de lectura de 1954 (P63) se le mostraron recortadas de los PDF del Release, a 150 ppi de origen. No suman cobertura del libro: deciden datos del informe LEE 1954.

| Edición | Hoja | Duda | Sesión | Eduardo | Qué se hace |
|---|---|---|---|---|---|
| 4656 | 12 | Catastro del edicto 10680 (Portal) | 26 o 28 | 26 | Se toma 26; el libro no lo cita |
| 4699 | 9 | Año de la patente de Arévalo (Res. 564-E) | 1948 o 1949 | 1943 («1913» ampliado; el tercer dígito es un 4 claro, así que 1913 no) | Tres lecturas distintas del último dígito, que está sobreimpreso: **A decía «1948 o 1949» (corregido a «de los años cuarenta, con el último dígito sobreimpreso»)** |
| 4647 | 19 | Valor fiscal del remate 10627 | 2.450 | 2.400 | Se toma 2.400: la base, \$1.600, son sus dos tercios exactos; el libro no lo cita |
| 4822 | 6 | Decreto citado en el art. 1.º del 12575-E | «1154?\|54» | «116-304» | Queda ilegible. El 11630-E existe (4765 h6) y es una jubilación, así que no es ese. Candidato por inferencia, no por lectura: 11843, el reajuste general de valores fiscales que cita el 12687-E. El libro no lo cita |
| 4792 | 12 | Resolución de caducidad del 12148-E | 577?-J | 5772-J | Se toma 5772-J; el libro no lo cita |
| 4827 | 10 | Expediente del 12687-E | 6682 o 6683 | 6688 | Queda entre 6682, 6683 y 6688; el libro no lo cita |
| 4764 | 8 | Pensionado de Vaqueros (11627-E) | nombre ilegible, «Cleure» | Isidro o Isidoro Claure | Se registra; el libro no nombra a los pensionados |
| 4596 | 10 | Número del decreto de B.2.1 (Carmelo Lassi) | 8437-G por la capa | 8437-G | **Ninguno de los dos: el 8437-G empieza después del art. 2.º y las firmas del decreto de Lassi. El de Lassi es el 8436-G** («Reconócense los servicios prestados», fechado «enero 11 de 1953», errata por 1954), que empieza al pie de la columna anterior (4596 h10, recorte 08b). El libro no lo cita |
| 4756 | 6 | «Wie_na» | Wierna, casi seguro | Wie_na, errata del tipógrafo | **A y 22 corregidos a «Wie[r]na»** |

### Lecturas humanas 1951–1953 (Eduardo, 28/09/2026)

Doce dudas de los pendientes P48, P53 y P57, mostradas en una hoja de recortes a 150 ppi de origen. Cada lectura se contrastó con un control que no depende del ojo: los números de los decretos vecinos en la misma hoja (capa nativa del PDF), las otras apariciones del mismo aviso y el expediente. Ninguno de estos números lo cita el libro; lo que se decide corrige los informes LEE (P65).

| # | Edición y hoja | Duda | Sesión | Eduardo | Control | Queda |
|---|---|---|---|---|---|---|
| 1 | 3983 h4 | Decreto del Hogar Escuela | 70[6?]4-A | 7864-A | La misma hoja trae el 7062-A del mismo día (18/06/1951) | **7064-A**; el 8 de la lectura es un 0 |
| 2 | 4023 h8 | Decreto de índices municipales | 80[8?]3-E (número «en el borde») | 8063-E | El decreto siguiente, mismo día y expediente, es el 8064-E; el número sí está en la imagen | **8063-E** |
| 3–4 | 4002 h4 y 4033 h16 | Edicto sucesorio de La Caldera | 7249 o 7243 | 7249 y 7249 | Capa y sumario dan 7249; dos apariciones leídas | **7249** |
| 5 | 4235 h11 | Expediente y resolución del 706-A | 10.8??/952; 8?01 | 10.825/952; 820-J | Sin control externo | Lectura de Eduardo, sin confirmar: 10.825/952 y 820-J |
| 6 | 4371 h5 | Decreto de Manuel Condori | 376?-E | 3788-E | La hoja trae 3763, 3765 y 3766, y la siguiente 3770 a 3773: es un 376x. El 3768 no aparece en otra parte | **376[8]-E**, el último dígito por la lectura de Eduardo y compatible con la serie; el penúltimo 8 es un 6 |
| 7 | 4373 h4 | Decreto de Dina I. Lozano de Robles | 3809-E (3808 posible) | 3808-E | En la capa, el 3808-E encabeza el expediente 6691/R/52; el 3809-E de h5 es otro decreto (Vialidad, 31B/A/53) | **3808-E. El informe LEE 1953 (A.11) estaba mal** |
| 8 | 4373 h12 | Decreto de personal de Salubridad | 3840 o 3846 | 3840-A | Coinciden | **3840-A** |
| 9 | 4407 h7 | Decreto de pensiones | 45[2?]8-E | 4528-E | Coinciden | **4528-E** |
| 10 | 4470 h9 | Decreto del transporte Salta–La Caldera (Mompó) | 59[5?]6-E | 5988-E | El decreto anterior en la misma hoja y del mismo día es el 5955-E | Abierto: 5956-E por la serie, 5988-E por la lectura |
| 11 | 4479 h5 | Decreto del permiso a Donato Villa | número no leído; ¿6108? | expediente 3364 | La hoja trae 6104 y 6105, y la siguiente el 6107 | **6106-E** por la serie (sin lectura directa); expediente **3364/A/1953** |
| 12 | 4581 h6 | Decreto de la «Expropiación Serranía en La Caldera» | 8078-E por la capa | 8077-E | El 8077-E es el decreto de al lado (expediente 5605/R); el que corresponde al expediente 5441/F es el 8078-E | **8078-E**; la lectura tomó el decreto vecino |

Queda cerrada, además, la fecha del decreto 11.064 (P57): su encabezado dice «Enero 29 de 1952» (4128 h4). El «31 de enero» es el modo en que lo cita el 3243-E de 1953 (4350 h4): es una discrepancia entre fuentes, no una duda de lectura.

### Catálogo de confusiones de la tipografía de 1951–1954 (primera versión)

Sale de las 21 lecturas humanas de hoy (9 de 1954 y 12 de 1951–1953), comparadas con las de la sesión y con los controles.

- **Números de 150 ppi, en cursiva o negrita de encabezado.** 0, 3, 5, 6, 8 y 9 se confunden entre sí: 7064 leído 7864; 376x leído 378x; 5956 o 5988; 6682, 6683 o 6688; 1154?, 116-304 o 118?. Ni la sesión ni el ojo humano deciden uno de estos dígitos sin un control.
- **Controles que deciden**, por orden de fuerza: (1) la serie de números de los decretos vecinos de la misma hoja y la misma fecha; (2) la aritmética del propio acto (2.400 por la base de 1.600); (3) las otras apariciones del mismo aviso; (4) el sumario de la edición.
- **Lo que aporta más el ojo humano:** las letras y las palabras (Claure, Wie_na), las erratas del original y los dígitos que la capa destroza, pero que la imagen muestra enteros (3808, 4528, 5772, 26).
- **La falla típica de la lectura humana:** tomar el acto de al lado (8077 por 8078, y 8437 por 8436 en 1954). Las próximas hojas de dudas marcan el renglón exacto con un recuadro.
- **Sobreimpresión y tipos rotos:** cuando un dígito está sobreimpreso (la patente de Arévalo), ni tres lecturas lo deciden; se declara el dígito como ilegible.

## Ronda 47 — lecturas de Eduardo, 1909–1950 (28/09/2026)

Tipo: **incorporación** (CORRIGE 3.6), por la palabra clave `LECTURAS` (flujo v2 §5.6). Base: commit `508b191`; parche `ronda-47.patch` (commit `509f81a` en la sesión). Denominador: 25.009 líneas, sin cambios de largo.

### Traslado, lectura y cobertura

La ronda toca dos líneas, A:271 y 04:3891. La sesión las leyó enteras, y además 04:3886–3894 como contexto. Siguen vigentes las 25.009 líneas: **25.009 de 25.009 (100,0 %)**.

### Qué se decidió con controles, sin mostrarlo (§5.6.1)

| Año, edición y hoja | Duda del informe LEE | Control | Queda |
|---|---|---|---|
| 1950 · 3793 h9 | Decreto de Aquiles Casale, «3399-E» | La imagen dice 3339; los decretos de la misma edición fechados el 21 de septiembre van del 3370 al 3373, y el de Casale es del 20 | **3339-E. El libro decía 3399-E en A:271 y 04:3891 (corregido)** |
| 1948 · 3046 h8 | Fecha del 7886-E, «enero 22 (dudoso)» | El 7883-E y el 7885-E, en la hoja anterior, son del 22 de enero | 22 de enero de 1948 |
| 1948 · 3083 h6 | Decreto de coeficientes citado, «52^6» | La imagen dice 5276, y el 5276-E es el decreto de coeficientes de 1947 (2909 h5) | 5276 |
| 1948 · 3208 h8 | Número del decreto del Registro Civil, «no leído» | Se lee en la imagen | 11052-G |
| 1925 · 1066 h13 | Azúcar, ¿1.833,32 u 11.833,32? | Se lee en la imagen, y la columna cierra con ella | 1.833,32 |
| 1926 · 1122 h3 | Letra del expediente «7571 e» | En la imagen no hay letra después de 7571: la «e» es de la capa | 7571, sin letra |
| 1917 · 640 h6 | «Ruiloba [dudoso]» | Se lee en la imagen, y el decreto 1.564 de 1918 nombra a Venancio Ruiloba para el mismo partido | Ruiloba |

Se quitó de la hoja el renglón borrado de 1912 (362 h3), donde no hay nada que leer.

### Lecturas de Eduardo (hoja `dudas-1909-1950.html`, 15 recortes con el renglón marcado)

| # | Año, edición y hoja | Duda | Sesión | Eduardo | Control | Clase |
|---|---|---|---|---|---|---|
| 1 | 1909 · 113 h4 | Vacas con cría | «6[ilegible]» | 6 | Ninguno (el remate no imprime total) | Decidida por Eduardo: 6. La marca que sigue al 6 se toma como tinta |
| 2 | 1913 · 444 h4 | «Ma[?]ín» Lesser | lectura obvia no escrita | Martín | Ninguno | Decidida por Eduardo |
| 3 | 1917 · 640 h6 | «Chalcha-mio» y «Ruiloba» | Chalchamio; Ruiloba | Chalchamio; «Ralloba» | Cita cruzada: el decreto 1.564 de 1918 dice «Venancio Ruiloba» | Chalchamio, confirmada; **Ruiloba, corregida por el control** |
| 4 | 1921 · 844 h12 | «Fernández Auge…» | [ilegible] | «Fernandez Auge» | Ninguno | Abierta: el final del nombre no se lee |
| 5 | 1925 · 1066 h13 | Eventuales, ¿637,16 o 627,16? | 637,16 por la suma | 637,16 | La columna cierra con 637,16 | Confirmada |
| 6 | 1925 · 1079 h13 | Total de agosto, 486.135,5? | 486.135,58 por la suma | 486.135,58 | 469.300,80 + 16.834,78 = 486.135,58 | Confirmada |
| 7 | 1925 · 1083 h13 | Subtotal de septiembre, ¿,85 o ,89? | ,89 por la suma | 887.834,89 | 887.834,89 + 14.375,46 = 902.210,35, el total impreso | **Confirmada: el pie de septiembre de 1925 cierra y desaparece la diferencia de cuatro centavos del informe LEE 1925** |
| 8 | 1929 · 1268 h11 | «Rorcado» o «Rocado» | Rorcado | Rorcado | Ninguno | Confirmada |
| 9 | 1934 · 1560 h43 | Base del remate de San Jorge y San Félix unidas | «[1]0.000 [dudoso]» | $ 6.000 | Cita cruzada: el apéndice H del libro, leído sobre la imagen, da \$6.000 unidas | **6.000; el informe LEE 1934 decía [1]0.000** |
| 10 | 1934 · 1517 h39 | Saldo de noviembre de 1933 | 33.398,8? | 33.398,82 | Ninguno en el corpus (el resumen de noviembre de 1933 es de 1933) | Decidida por Eduardo |
| 11 | 1936 · 1617 h37 | Saldo de octubre de 1935 | 31.809,3? | 31.809,33 | Ninguno en el corpus | Decidida por Eduardo |
| 12 | 1947 · 2909 h5 | Coeficiente del renglón 10 | 1,578 o 1,576 | 1,576 | Los coeficientes suman 100,000 sólo con 1,576 | **Confirmada por control**; la impresión de la sesión sobre el recorte (1,578) era errónea |
| 13 | 1950 · 3596 h10 | Apellido del oficial 7.º | Ca[i]tuolo | Calluolo | Ninguno; no aparece en otro acto leído | Abierta: Caituolo o Calluolo |
| 14 | 1950 · 3678 h5 | Orden de pago del 1423-E | 662 o 682 | 662 | Ninguno | Decidida por Eduardo |
| 15 | 1950 · 3825 h8 | «RECHI» o «REGHI» | Rechi (la capa, reghi) | RECHI | Ninguno | Decidida por Eduardo |

Balance: de 15 lecturas, 7 confirmadas por un control, 6 decididas por Eduardo, 1 corregida por el control (Ralloba) y 2 abiertas (4 y 13). El ojo humano volvió a rendir más en palabras (Martín, Rorcado, Rechi) y en dígitos finales de cifras sin control (33.398,82; 31.809,33; 662). El error volvió a ser el de una lectura que un control desmiente (Ralloba). Se agrega al catálogo del §5.6: **en los saldos de Tesorería, el último dígito queda a menudo sobreimpreso por el signo de cierre; la cadena de saldos del mes siguiente es el control, y se busca antes de mandarlo a la hoja.**

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Menciones de los números y nombres decididos en el libro | 22 formas buscadas en los 38 archivos | 3399-E en A:271 y 04:3891 (corregidos); San Jorge y San Félix (H) ya daba \$6.000; ninguna otra mención |
| Remisiones, pedidos y aparato | sin cambios respecto de la ronda 46 | no se tocan |
| Compilación | libro entero | Compila; 803 páginas; 0 referencias indefinidas; `.lof` con 41 entradas |

## Ronda 48 — lecturas de Eduardo, 1957 (29/09/2026)

Tipo: **lecturas sin cambio en el libro** (CORRIGE 3.6), por la palabra clave `LECTURAS` (flujo v2 §5.6). Base: commit `5741b93`. No hay parche. 1957 no está incorporado (`libro.incorporado: null`), y ninguna de las formas decididas aparece en el libro. Denominador: 25.009 líneas, sin cambios. La cobertura acumulada sigue en **25.009 de 25.009 (100,0 %)**. Todo lo que sigue corrige sólo el informe `BO-Salta-1957_5317-5561_la-caldera_LEE-1957_2026-09-29.txt`, y queda como pendiente P68.

### Qué se decidió con controles, sin mostrarlo (§5.6.1)

| Edición y hoja | Duda del informe LEE | Control | Queda |
|---|---|---|---|
| 5511 h12 | Decreto de la concesión del río Vaqueros, «107[0?]3-E» (capa «107C3») | Serie: en la misma hoja están el 10702-E, también del 10 de octubre, y el 10704-E | **10703-E**. Se sacó de la hoja antes de entregarla |
| 5434 h1 | Tapa, «EDICIÓN DE 2? PÁGINAS»; el PDF tiene 24 hojas | Cadena de folios, y cotejo sobre la imagen: h21 repite a h19 (pág. 1303) y h22 repite a h20 (pág. 1304). La edición va de la pág. 1285 a la 1306: **22 páginas** | 22, confirmado por Eduardo (D3). El Release tiene **2 hojas duplicadas**. La 5433 termina en la pág. 1283, así que la 1284 no está en el Release o es un salto de numeración (abierto) |
| 5451 h1 | Tapa, «24?», débil; el PDF tiene 21 hojas | Cadena de folios: 5451 va de la pág. 1615 a la 1635, y la 5452 empieza en la 1637 | La tapa sigue ilegible (D4). La cadena da una edición de **22 páginas**, a la que le falta en el Release la última (pág. 1636). No se toma «24» |

### Lecturas de Eduardo (hoja `dudas-1957.html`, 4 casos con el renglón marcado)

| # | Edición y hoja | Duda | Sesión | Eduardo | Control | Clase |
|---|---|---|---|---|---|---|
| D1 | 5521 h15 y 5535 h7 | Presupuesto del puente sobre el río Caldera (A.74, licitación 593), 1.984.?88,50 | La capa da «088» en seis apariciones y «988» en una | 1.984.088,50 [seguro] | Ninguno decide (el aviso no trae desglose); la lectura coincide con seis de las siete apariciones | **Decidida por Eduardo: $ 1.984.088,50** |
| D2 | 5429 h22 | Expediente de la Res. 5718-A (A.35), ¿24.753 o 24.756? | «24.75g»; el informe transcribió 24.756/57 | 24.753/57 [seguro] | Cita cruzada: la Res. 5982-A (A.50), que aprueba el concurso autorizado por la 5718, lleva el 24.753/57. No la contradice | **Decidida por Eduardo, apoyada por la cita cruzada: 24.753/57. El informe decía 24.756/57** |
| D3 | 5434 h1 | Páginas declaradas en la tapa | «2?» | 22 [seguro] | Cadena de folios más duplicados: 22 páginas | **Confirmada por control** |
| D4 | 5451 h1 | Páginas declaradas en la tapa | «24?» | ilegible | Cadena de folios: 22 páginas, y falta la última | **Abierta en la tapa.** La extensión de la edición la decide la cadena |

Balance: de 4 lecturas, 1 confirmada por un control (D3), 2 decididas por Eduardo (D1, y D2 con una cita cruzada que la acompaña) y 1 ilegible (D4), que la cadena de folios deja acotada. No hubo lecturas corregidas por un control. Se suma al catálogo del §5.6: **cuando las hojas del PDF no coinciden con las páginas de la tapa, antes de mandar la tapa a la hoja se corre la cadena de folios y se buscan hojas repetidas. Una hoja duplicada no tiene folio nuevo; una faltante deja un salto entre ediciones.** La sesión lo aplicó después de entregar la hoja, y con eso D3 y D4 no hacían falta.

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Menciones en el libro de las formas decididas | 9 formas (1.984, 10703, 10702, 24.75, 5718, 5434, 5451, 1957, «Luis Linares» en 1957) en los 38 archivos | Ninguna del informe 1957; «1.984» sólo como matrícula en 19:935, ajena |
| Duplicados en 5434 | 24 hojas, comparadas de a pares por texto y luego sobre la imagen | 2 duplicados (h21 = h19, h22 = h20) |
| Cadena de folios 5433 a 5452 | 5 empalmes | Salto de 1 en 5433→5434 (pág. 1284) y en 5451→5452 (pág. 1636) |

## Ronda 49 — auditoría con fase 6 (29/09/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1955–1957. Base: commit `770bdd3` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1955–1957), con la fase 6 de esta ronda en `ronda-49.patch` (commit `aaea202` en la sesión). **Denominador medido: 25.032 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 48 (25.009 de 25.009 en `5741b93`, el commit de la ronda 47; la 48 no tuvo parche) se trasladaron por diff a `770bdd3`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1955–1957 agrega 23 líneas (21 en A y 2 en C) y hace caducar 74 líneas en 21 archivos**, y deja **24.958 vigentes sobre 25.032 (99,7 %)**.

### Lectura sobre el texto (numeración de `770bdd3`)

Se leyeron **las 74 líneas caducas, enteras, por la sesión**, sin subagentes, cotejadas contra los informes LEE 1955 (`BO-Salta-1955_4831-5073_la-caldera_LEE-1955_2026-09-29.txt`), 1956 (`BO-Salta-1956_5074-5316_la-caldera_LEE-1956_2026-09-29.txt`) y 1957 (`BO-Salta-1957_5317-5561_la-caldera_LEE-1957_2026-09-29_1.txt`, el nombre que da `estado.json`), en todas las fichas que las líneas citan. Además se releyeron como contexto 36 líneas con cobertura vigente; no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 280, 303, 315–335 | 23 | sesión |
| ape/C-normativa.tex | 106–107 | 2 | sesión |
| ape/D-pedidos.tex | 177, 183, 190, 192–193 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 64–66 | 6 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 389, 391–392, 475 | 4 | sesión |
| cap/04-siglo.tex | 3639, 3658–3660, 4557–4558, 4599, 4696–4697 | 9 | sesión |
| cap/09-defensas.tex | 526, 535 | 2 | sesión |
| cap/10-expropiacion.tex | 149, 332 | 2 | sesión |
| cap/13-loteo.tex | 727 | 1 | sesión |
| cap/14-poblacion.tex | 517 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 762, 789, 794 | 3 | sesión |
| cap/17-aguabaja.tex | 281, 284, 353 | 3 | sesión |
| cap/18-politica.tex | 464 | 1 | sesión |
| cap/20-opacidad.tex | 880 | 1 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 216, 223, 545 | 3 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído (no suma cobertura): 03-fincas:465–474; 22-infraestructura:205–215; 26-presencia:170–176; 20-opacidad:724–731.

**Esta ronda: 74 líneas nuevas.** Con el contexto releído son 110 líneas y 123.431 bytes sobre 2.624.415, que en las 815 páginas de la base equivalen a **38,3 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `770bdd3` cae dentro de estos tramos.

Acumulado: 24.958 vigentes + 74 = **25.032 de 25.032 (100,0 %)**. La fase 6 toca 10 líneas, todas dentro de lo leído en esta ronda (A:315, 318, 321, 323, 324; F:57; 03:475; 10:149; 16:794; 18:464), y no cambia el largo de ningún archivo: **25.032 de 25.032 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1955, 1956 y 1957 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 4880 | 6 | Decreto 13671-E, visto | «Construcción de Defensas de Piedra Embolsada sobre Rio La Caldera». Coincide; la tilde de «Río» no se decide a 150 ppi |
| 4880 | 11 | Decreto 13694-E, art. 1.º | Catastro Nº 26, José Ángel Portal, cinco mil metros cuadrados, «doscientos sesenta y dos milímetros por segundo». Coincide |
| 5032 | 5 | Decreto 247-G, considerando | **Dice «una mejor organización dentro del régimen municipal, con la designación de las nuevas autoridades»**. A:318 y 18:464 citaban entre comillas «para reorganizar el régimen municipal», que es la paráfrasis de la FICHA del informe LEE 1955 (A.45), no el texto (corregido) |
| 4842 | 7 | Decreto 12933-E, visto | Sastre y Giménez, «explotación irracional», «GETSEMANI». Coincide |
| 4945 | 4 | Decreto 14707-S, art. 2.º | «Estación Sanitaria de La Caldera». Coincide |
| 5091 | 5 | Decreto-ley 82-G, visto | Leyes 1741 y 1402; albergue para alumnos anexo a la escuela Juana Moro de López. Coincide |
| 5146 | 6 | Decreto 2382-E, visto y art. 1.º | **«Estudios Embalse en Campo Alegre»**, con mayúscula las dos veces; A:323 y 10:149 citaban «Estudios embalse» (**corrección silenciosa**, corregida) |
| 5160 | 8 | Decreto 2773-E | «con el objeto de proseguir los trabajos de perforación en la zona de Campo Alegre (Departamento La Caldera)». Coincide |
| 5225 | 5 | Decreto 3872-E, visto y art. 1.º | El visto dice «Servicio de Aguas Corrientes en La Caldera» y el art. 1.º **«Servicios de Aguas Corrientes en la Caldera»**; A:324 y 16:794 citaban «Servicios… en La Caldera», el plural de uno y la mayúscula del otro (**corrección silenciosa**, corregida a la forma del art. 1.º) |
| 5253 | 9 | Decreto 4489-G | «VISTA la vacancia»; «Interventor Municipal de la localidad de La Caldera», Cecilio Muñoz. Coincide |
| 5190 | 9 | Aviso 14050 | «EL DURAZNO», «herederos de Campero», Silvano Murúa al sud, Liborio Guerra «antes» de José María Murúa. Coincide |
| 5259 | 6 | Decreto 4576-G | «con motivo de contravenir a órdenes policiales en vigencia». Coincide |
| 5164 | 13 | Resolución 2635-S | «VISTO la necesidad de proveer de atención médica al pueblo de La Caldera». Coincide |
| 5513 | 17 | Decreto 10816-E, considerando | «uno de los tantos avasallamientos de la propiedad privada, efectuados por el régimen anterior, bajo el pretexto de la…». Coincide hasta el corte de renglón; el final, por el informe LEE |
| 5521 | 15 | Licitación 593 | Consorcio Caminero Nº 12, «puente de hormigón armado, sobre el río Caldera». Coincide |
| 5508 | 17 | Obra 517 | «Construcción Comparto Sistema de Riego, Vaqueros, La Calderilla y La Caldera». Coincide |
| 5461 | 8 | Decreto-ley 590-E, arts. 3.º y 4.º | «veinte (20) cuotas anuales, iguales y consecutivas, sin interés». Coincide |

Son **17 citas cotejadas sobre 17 hojas de 17 ediciones** (6 de 1955, 8 de 1956 y 3 de 1957), todas en la imagen: **una paráfrasis dentro de comillas** (247-G) y **dos correcciones silenciosas** de mayúscula («Embalse», «la Caldera»); ninguna cita que cambie el sentido. No se cotejaron: 4945 h4 (14705-S, las cifras de veinticinco y sesenta niños), 5039 h10–15 (450-E), 4968 h9 (15060-G, «Dpto. Capital»), 5051 h6 (681-G), 5147 h10 (2436-E, «Villa San Lorenzo») ni 5363 h6–8 (decreto-ley 408-E).

### Hallazgos (seis, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:318, 18:464 | Cita del 247-G que es la paráfrasis de la ficha, no el texto | 4 | Texto del considerando |
| 2 | A:323, 10:149 | «Estudios embalse» por «Estudios Embalse» | 4 | Mayúscula del original |
| 3 | A:324, 16:794 | «Servicios… en La Caldera» por «Servicios… en la Caldera» | 4 | Forma del art. 1.º |
| 4 | F:57 | 1957 «con las 244 tapas» en la misma oración que dice que la 5318 no trae tapa (el informe LEE 1957 arrastra la misma contradicción) | 7 | 243 tapas |
| 5 | A:315 | «En septiembre la tapa del Boletín cambia cuatro veces de titular»: según el E.4 del informe LEE 1955, las tapas nombran a Durand hasta el 19 de septiembre, a Pfister el 21, a Moschini el 26 y el 28 y a Lobo desde el 3 de octubre: **cuatro titulares y tres cambios**, uno de ellos en octubre | 3 | «Entre el 19 de septiembre y el 3 de octubre la tapa nombra cuatro titulares sucesivos» |
| 6 | 03:475 | «Que sea la misma finca lo sugieren el nombre y dos de los linderos»: coincide uno, el del oeste (Daniel Linares); el del norte es «herederos de Campero» contra «Campos», como la misma frase dice | 5 | El lindero del oeste, y el del norte sólo si Campero y Campos son la misma familia |

Observación de prosa, sin restar como error (aspecto 12): A:321 y 16:794 decían que «el pueblo licita» su servicio de aguas corrientes, y la misma frase de 16 dice que lo hace la Provincia y que el municipio no figura. Corregido a «la Provincia licita» (A) y «se licita» (16).

**Los seis están en material que la propia auditoría incorporó** (AMPLÍA 1955–1957, `770bdd3`); ninguno fue atrapado por un control automático antes de llegar al libro. Los hallazgos 1 a 3 los habría atrapado un control que busque cada texto entrecomillado nuevo en los bloques TEXTO del informe LEE, no en su FICHA: se corrió después de la lectura (tabla de abajo) y devuelve exactamente esos tres (P74).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.009/25.009 líneas vigentes en `5741b93` | 24.958 vigentes, 74 caducas por el AMPLÍA 1955–1957 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`) | 316/316 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| Superlativos y ausencias sobre los temas que tocan las fichas de 1955–1957 (usina, aguas corrientes, juez de paz, comisión municipal, intendente, intervención, Hogar, embalse, puente, defensas, Registro Civil, presupuesto, balance, tomeros, Obras Sanitarias, Cerro de Buena Vista, El Durazno, médico, consultorio, albergue, pensiones, becas, minas, entre otros), en oraciones que no nombran 1955–1957 (repaso de ventana) | 40.406 oraciones del libro; 148 coincidencias, todas leídas | Ninguna desmentida. 20:728 («el único balance con cifras de todo el período»), 22:212 (el puente de \$200.000 «no vuelve a aparecer… hasta 1946») y 26:172 (la estación sanitaria, 1923–1945) tienen universo declarado anterior a 1955 |
| Menciones de la ventana (1949–1954, «sexenio», tramos, 1955–2012, cincuenta y seis a cincuenta y ocho años) | 25.032/25.032 líneas | Ninguna desactualizada: 00, 01, 02, 04, 20, 22 y F dicen 1949–1957, cuarenta y dos de cuarenta y tres tramos y cincuenta y cinco años (1958–2012) |
| Citas entre comillas de las 74 líneas contra el TEXTO de los informes LEE 1955–1957 (búsqueda literal, sin mayúsculas en segunda pasada) | 85 citas; 38 de actos de 1955–1957 | 33 literales; 5 discrepan: los hallazgos 1 a 3 y dos falsos positivos por mayúscula de comienzo de oración («VISTO», «VISTA»). Las 47 restantes son de años anteriores y no se buscan en estos informes |
| Muestra de 50 afirmaciones (aspecto 1), semilla 49 | 50 de 340 oraciones con cifra en las 74 líneas | **50/50 con fuente localizable**: 27 no llevan la cita en la misma oración y la tienen en el párrafo o en la fila remitida, o son declaraciones de cobertura de F, 00, 01 y 02 cuya fuente es el propio apéndice F y los informes LEE |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 74 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Dotaciones de 1955–1957 recalculadas desde caudal y superficie | 4 decretos de 1955 (con la superficie exacta de San Cayetano, 38,175 ha), 3 actos de 1956 | 1955: 0,525 (San Cayetano, 20,04/38,175), 0,524 (Portal), 0,525 (Apaza), 0,525 (Somerville, 26,25/50 y 36,75/70); 1956: 0,525, 0,75 y 0,525. Cierran A:319, A:326 y 17:353. La cuenta sobre «38 hectáreas» redondeadas daría 0,527: no es error, porque el decreto da 38 ha 1.750 m² |
| Recuentos de hojas de 1955–1957 (F:57) | 3 años | 1955: 4.670 − 104 + 5 = 4.571, + 96 = 4.667; 88 = 66 + 2 + 20. 1956: 4.282 − 84 + 2 = 4.200, + 236 = 4.436; 79 = 55 + 2 + 22. 1957: 4.264 − 81 + 7 = 4.190, + 72 + 196 = 4.458; 71 = 36 + 35. Tapas: 237 + 6, 230 + 12, 240 + 3 + la 5318. Cierran. Hojas de poca tinta: 430 − 96 = 334; 108 − 30 = 78; 185 − 40 = 145. Cierran |
| Rangos de ediciones | 3 años | 4831–5073 = 243; 5074–5316 = 243 (242 sin la 5293); 5317–5561 = 245 (244 sin la 5334); 5037–5073 = 37 ediciones a 75 ppi. Cierran con A, F, 00 y 02 |
| Porcentajes de A | 1 (adjudicación de la obra 343) | 125.930,39 / 110.465,26 = 1,140: «un catorce por ciento más» cierra |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 284; 8/8 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Privacidad: personas nombradas en las 74 líneas, cruzadas con contextos sensibles | 74/74 líneas y búsqueda en todo el libro de «gobernanta», «regente», «cuidadora» | La gobernanta intervenida en 1956 y la regente y la cuidadora sancionadas en 1957 no se nombran en ningún lugar del libro; la menor de 1957 tampoco; los deudores de los remates de 1955 a 1957 no se nombran. Sin casos |
| Largo de los archivos antes y después de la fase 6 | 6/6 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero | Compila; 815 páginas (815 la base); 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:78; 2 cajas desbordadas, las mismas de antes |

## Ronda 50 — lecturas de Eduardo, 1959 (29/09/2026)

Tipo: **lecturas sin cambio en el libro** (CORRIGE 3.6), por la palabra clave `LECTURAS` (flujo v2 §5.6). Base: commit `770bdd3` (la fase 6 de la ronda 49, `aaea202`, no toca nada de 1959). No hay parche: 1959 está en `puntual`, sin informe registrado, y ninguna de las formas decididas aparece en el libro. Denominador: 25.032 líneas, sin cambios. La cobertura acumulada sigue en **25.032 de 25.032 (100,0 %)**. Como el informe `BO-Salta-1959_5806-6047_la-caldera_LEE-1959_2026-09-29.txt` todavía no está registrado, las lecturas se aplicaron sobre él y se entrega de nuevo con el mismo nombre: **no queda pendiente de tipo `lee`**.

### Qué se decidió con controles, sin mostrarlo (§5.6.1)

Antes de armar la hoja se decidieron por control, entre otros: el expediente del cateo de Marcelo Diez, 2847-D, por la serie (el 2848-S es del mismo día y hora, A de 5875); la base del remate 3176 por sus dos tercios; el decreto citado 4403/59 de A de 5841 por la cita cruzada con A de 5820, y los tres encabezados que la capa atribuía al acto vecino, por coordenadas y en la imagen.

### Lecturas de Eduardo (hoja `dudas-1959-1959.html`, 9 casos con el renglón marcado)

| # | Edición y hoja | Duda | Sesión | Eduardo | Control | Clase |
|---|---|---|---|---|---|---|
| D1 | 5826 h6 | Reproductores del Dto. 4630-E, «los 1? reproductores» | Segundo dígito roto (600 ppp) | 16 | El cuadro trae 16 prestatarios; no lo decide (el acto no dice uno por renglón), pero no lo contradice | **Decidida por Eduardo: 16** |
| D2 | 5857 h7 | Decreto del 31 de enero citado por el 5305-A, «4?89» | Segundo dígito roto | 4789 | Serie del año (`decretos_1959.csv`): del 4718 al 4831 son del 31 de enero; el 4689 es del 30 y el 4889 del 11 de febrero | **Decidida por control y confirmada: 4789.** No debió ir a la hoja |
| D3 | 5820 h8 | Ocho retenciones ajenas del cuadro del Dto. 4403-E (carta fianza de Imberti) | Centenas rotas | 6.030,59; 6.892,10; 3.662,96; 4.194,22; 4.749,17; 3.321,42; 3.617,35; 2.866,52 | Aritmética: con 3.645,30, 9.177,83 y 6.320,60 suman 54.478,06, y el total impreso es 55.021,06. Faltan 543,00. 150 combinaciones de 2 o 3 dígitos confundibles cierran la diferencia | **Abierta: el control rechaza la lectura y no elige otra.** Renglones de otras obras; el certificado 2 de La Caldera (6.320,60) lo cierra el art. 2 (55.021,06 − 6.320,60 = 48.700,46) y el art. 3 (10 % de 63.206,05) |
| D4 | 5867 h1 | Número impreso en la tapa | «5337» o «5367» | 5337 | La serie da 5867; decide sólo la errata impresa | **Decidida por Eduardo: la tapa imprime 5337** |
| D5 | 6024 h1 | Páginas declaradas | 20 o 26; el archivo trae 19 hojas | 20 | Ninguno la contradice; 19 hojas con 20 declaradas cuadra con una faltante | **Decidida por Eduardo: 20** |
| D6 | 5928 h8 | Expediente del Dto. 7163-E (convenio A.G.A.S.-Municipalidad) | Imagen «1563», capa «1533» | 1563-59 | Sin cita cruzada en el corpus | **Decidida por Eduardo: 1563-59**, igual que la imagen |
| D7 | 5837 h5 | «Moría» o «María» Polo de Herrera | «Moría» | Moría, errata del cajista | — | **Decidida por Eduardo: «Moría» [sic]** |
| D8 | 5964 h13 | Samora o Samara, pensión 1087 | Imagen «Samora», capa «Samara» | Samora | — | **Decidida por Eduardo: Samora** |
| D9 | 6009 h13 | Saldo en caja que pasa a agosto de 1959 | 19.624.971,70, tercer dígito inseguro | 19.624.971,70 | Sin control: agosto y septiembre no se publicaron | **Decidida por Eduardo: 19.624.971,70** |

Balance: de 9 lecturas, 1 decidida por control y confirmada (D2), 7 decididas por Eduardo (D1, D4 a D9) y 1 abierta porque la aritmética rechaza la lectura (D3). No hubo lecturas corregidas por un control con un valor propio. Se suma al catálogo del §5.6: **un número citado con un dígito roto se corre contra la serie de fechas de todo el año, no sólo contra la de la hoja; y un cuadro con total impreso se devuelve con la suma de la lectura hecha, para que la discrepancia se vea antes de aceptar la lectura.** En D3, la lectura de 4.749,17 donde la capa da «1.719.17» y la de 2.866,52 donde la capa da «2.366.52» son los renglones a mirar primero en un escaneo mejor.

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Menciones en el libro de las formas decididas | 17 formas (4789, 4630, 4403, 55.021, Imberti, 7163, 1563, 1533, Polo de Herrera, Moría, Samora, Samara, 8059, 5337, 6024, 19.624, 1959) en los 38 archivos | Ninguna del informe 1959: 4403 sólo dentro de «4431-E» (1953); 7163 como expediente de 1925 (cap. 4); 1959 en un expediente de 2010 y en un máximo de caudal (cap. 11), ajenas |
| Serie de decretos para D2 | 10 candidatos 4089 a 4989 contra `decretos_1959.csv` | Sólo el 4789 cae en el 31 de enero |
| Suma del cuadro de D3 | 11 renglones y el total | Diferencia de 543,00; 150 soluciones de 2 o 3 dígitos; ninguna única |
| Cita cruzada para D6 | Texto de las dos versiones, 242 ediciones | «1563-59» y «1533-59» sólo en 5928 h8 |

## Ronda 51 — auditoría con fase 6 (30/09/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1958–1960. Base: commit `1d33852` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1958–1960), con la fase 6 de esta ronda en `ronda-51.patch` (commit `d301f2a` en la sesión; aplica con `git am` sobre `1d33852`). **Denominador medido: 25.056 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 50 (25.032 de 25.032 en `841d6ce`, el commit de la ronda 49; la 50 no tuvo parche) se trasladaron por diff a `1d33852`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1958–1960 agrega 24 líneas (18 en A, 4 en C y 2 en F) y hace caducar 65 líneas en 20 archivos**, y deja **24.991 vigentes sobre 25.056 (99,7 %)**.

### Lectura sobre el texto (numeración de `1d33852`)

Se leyeron **las 65 líneas caducas, enteras, por la sesión**, sin subagentes, cotejadas contra los informes LEE 1958 (`BO-Salta-1958_5562-5805_la-caldera_LEE-1958_2026-09-29.txt`), 1959 (`BO-Salta-1959_5806-6047_la-caldera_LEE-1959_2026-09-29.txt`) y 1960 (`BO-Salta-1960_6048-6287_la-caldera_LEE-1960_2026-09-30.txt`), bajados de `corrige/lee/`, en todas las fichas que las líneas citan (las 183 del §A y las 34 de B.2 de los tres informes se listaron y se leyeron en su FICHA; en las citadas, también en TEXTO y NOTA). Además se releyeron como contexto 104 líneas con cobertura vigente; no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 330, 332, 336–353 | 20 | sesión |
| ape/C-normativa.tex | 109–112 | 4 | sesión |
| ape/D-pedidos.tex | 177, 190–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 64–65, 67 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 389, 391 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599, 4638, 4697 | 5 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332 | 1 | sesión |
| cap/13-loteo.tex | 725 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 45, 281, 284, 353 | 4 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 216, 223, 545 | 3 | sesión |
| cap/26-presencia.tex | 69, 98, 235 | 3 | sesión |

Contexto releído (no suma cobertura): D-pedidos:178; 04-siglo:1695–1725, 4203–4225 y 4525–4545 (la serie de la mina del expediente 44-L); 22-prospectiva:138–149; 22-infraestructura:528–533; 26-presencia:4–8 y 208–212.

**Esta ronda: 65 líneas nuevas.** Con el contexto releído son 169 líneas y 87.051 bytes sobre 2.661.710, que en las 831 páginas de la base equivalen a **27,2 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `1d33852` cae dentro de estos tramos.

Acumulado: 24.991 vigentes + 65 = **25.056 de 25.056 (100,0 %)**. La fase 6 toca 8 líneas, 7 dentro de lo leído en esta ronda (A:336, 340, 346, 353; 04:4638; 22:545; 26:235) y una del contexto releído (D:178), y no cambia el largo de ningún archivo: **25.056 de 25.056 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1958, 1959 y 1960 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 5826 | 6 | Decreto 4630-E, cuadro de prestatarios | **«Getcemani», sin tilde**; A:346 citaba «Getcemaní» entre comillas (**corrección silenciosa**, corregida; la FICHA del informe LEE 1959, A.5, pone la tilde y su TEXTO no) |
| 5569 | 8 | Decreto 12064-G, resolución transcripta | «considerando lo manifestado por la Administración General de A. G. A. S.»; 31,10, 29,90 y 48,30 %. Coincide |
| 5730 | 11 | Plan de obras electromecánicas | «LA CALDERA: Obra Municipal / Usina hidroeléctrica y licitada y adjudicada. Red … 300 300» (miles de pesos). Coincide |
| 5778 | 5 | Ley 3344, art. 1 | «una vez aprobada la adjudicación de los trabajos para la instalación de la usina de referencia». Coincide |
| 6003 | 6 | Decreto 8954-A, reglamento, art. 1 | «Niños o niñas que vivan en apartados lugares serranos». Coincide |
| 5840 | 12 | Remate 3176 | «"Villa Urquiza" (antes Cerro de Buena Vista)», lote 5, plano 21. Coincide |
| 6028 | 25 | Decreto 9878-E, considerando | «vendrá a complementar el importante puente construído sobre el Río La Caldera». Coincide |
| 5989 | 5 | Ley 3425, art. 3 | «a partir del puente sobre el río del mismo nombre». Coincide |
| 5908 | 10 | Decreto 6726-G, visto | «durarán un año en el desempeño de sus funciones, pudiendo los mismos ser designados nuevamente». Coincide |
| 5667 | 19 | Decreto 391-E | «los señores Intendentes Municipales que a continuación se detallan». Coincide |
| 6201 | 4 | Ley 3548, arts. 1 y 2 | «aprovechamiento integral del río Mojotoro»; «Dos Diques de toma y derivación en los ríos Wierna y Vaqueros». Coinciden las dos |
| 6240 | 5 | Ley 3566, art. 1 | «que forma parte del lote 1 del plano número 17»; **el artículo dice «Autorízase al Poder Ejecutivo a expropiar»**, como A:351 y C:111, y no «manda expropiar», como 04:4638 y 26:235 (hallazgo 5) |
| 5613 | 13 | Decreto 13090-G, art. 2 | «Déjase establecido, que la Municipalidad en cualquier oportunidad que deba realizar una obra municipal, deberá dar cumplimiento previamente con las exigencias legales». Coincide |
| 6197 | 9 | Decreto 13631-E | «los Intendentes Municipales». Coincide |
| 5629 | 18 | Decreto 13764-A, art. 4 | «Mucama del Hospital de La Caldera». Coincide |
| 5642 | 13 | Decreto 14043-A, art. 3 | «Enfermera de la Estación Sanitaria de La Caldera». Coincide |
| 5654 | 6 | Decreto 126-A, art. 1 | «Ayudante de Enfermera del Consultorio Externo de La Caldera». Coincide |
| 6231 | 12 | Decreto 14381-A, visto | «Médico Regional de la Estación Sanitaria de La Caldera». Coincide |

Son **19 citas cotejadas sobre 18 hojas de 18 ediciones** (8 de 1958, 6 de 1959 y 4 de 1960), todas en la imagen: **una corrección silenciosa** (la tilde de «Getcemani»); ninguna cita que cambie el sentido. Se cotejaron además en la capa del PDF, sin cita entre comillas, la descripción de la zona del edicto 3359 (5858 h12: el punto de referencia es «la confluencia del Río Ovejería con el Arroyo de las Tinajas o San José», que el informe LEE 1959 no transcribe y A:346 da bien) y las cláusulas del convenio del 7163-E (5928 h8: tres por ciento anual, quince anualidades, intervención de «La Usina», 4 de febrero de 1959). No se cotejaron: 5592 h16 y h22 (mesas de 1958), 6094 h6 y h11 (mesas de 1960), 6240 h8 (Ley 3575), 5734 h12–13 (2263-E) ni 6172 h8 (13171-E).

### Hallazgos (ocho, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:346 | «Getcemaní» entre comillas; el cuadro de 5826 h6 imprime «Getcemani» | 4 | Forma del original |
| 2 | A:336 | «un decreto nombra a Werfil Gallo como intendente municipal»: el 391-E designa a los intendentes municipales encargados de constituir las comisiones viales, y la fila siguiente (A:337) y 18:470 dicen justamente eso y que a Gallo se lo designa en 1959 y 1960 presidente de la comisión municipal. Contradicción a menos de diez páginas | 7 | «un decreto cuenta a Werfil Gallo entre los intendentes municipales encargados de las comisiones viales» |
| 3 | A:336 | «en 1958 … la usina hidroeléctrica se adjudica»: la adjudicación la resolvió la Intervención Municipal el 27/11/1957 y la aprobó el 12064-G del 30/12/1957, publicado en enero de 1958 (A:330 y A:338 lo dicen) | 3 | «se publica la adjudicación, aprobada el 30 de diciembre de 1957, y se autoriza a registrar la servidumbre» |
| 4 | 22:545 | «en 1958 la Provincia aprueba la adjudicación»: mismo caso | 3 | «en enero de 1958 se publica el decreto del 30 de diciembre anterior con que la Provincia aprueba…» |
| 5 | 04:4638, 26:235 | «la Ley 3566 manda expropiar»: el art. 1 autoriza (6240 h5), y A:351 y C:111 lo dicen | 7 | «autoriza a expropiar» |
| 6 | D:178 (con A:340) | El pedido del expediente 44-L pregunta «por qué caducó tres veces»; A:340 incorpora en 1958 la Resolución 2465, que declara caduca la mina «Caldera 1-2 y 3», expediente 44-L-1929, por deber el canon de 1951 a 1957 (Nº 5757, h. 12), y el pedido de mensura de 1955 (edicto 1990, Nº 5710, h. 11), sin enlazarlos con la serie. El libro contiene el dato que desmiente la cuenta | 7 | D:178 suma los dos actos de 1958 y dice «cuatro veces»; A:340 remite al pedido. La identidad de Valdés Torres (1954) con Valdez Villagrán (1955) no se afirma |
| 7 | 22:545 | «Los tres últimos años leídos muestran…» y enumera 1955 y 1957; la frase siguiente pasa a «los tres años siguientes, leídos con pendientes», 1958–1960, que son ahora los últimos leídos | 7 | «Los tres últimos años leídos sobre la imagen» |
| 8 | A:353 | «en junio Vialidad rebaja \$300.000»: el 12.603-E es del 30 de mayo y lo dicta el Ejecutivo a pedido de Vialidad (publicado el 6 de junio) | 3 | «a fines de mayo, a pedido de Vialidad, se rebajan» |

Restan: tres casos en el aspecto 3 (hallazgos 3, 4 y 8), una corrección silenciosa en el 4 (hallazgo 1) y cuatro errores de consistencia en el 7 (hallazgos 2, 5, 6 y 7).

**Los ocho están en material que la propia auditoría incorporó** (AMPLÍA 1958–1960, `1d33852`); ninguno fue atrapado por un control automático antes de llegar al libro. El hallazgo 1 lo habría atrapado el control de citas de P74 (texto entrecomillado contra el bloque TEXTO, no contra la FICHA): corrido después de la lectura, lo devuelve.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.032/25.032 líneas vigentes en `841d6ce` | 24.991 vigentes, 65 caducas por el AMPLÍA 1958–1960 |
| Citas con número de acto, edición y hoja de 1958–1960 contra las FUENTE de los informes LEE | 112 citas «número-letra, Nº, h.» y 175 citas «Nº, h.» con edición ≥ 5560 | Todas localizadas; las 6 que el script no resolvió de primera son rangos de hoja («h14 c2 a h23», «h11 c3 y h12 c1») y cierran al mirar la FUENTE. Observación sin restar: 9194-E y 5051-E se citan por la hoja del cuerpo (h12, h11) y no por la del encabezado |
| Citas entre comillas de las 65 líneas contra el TEXTO de los informes LEE 1958–1960 | 109 citas; 23 de actos de 1958–1960 | 22 literales o con diferencia sólo de mayúscula o corte de renglón («TERREÑO», «Buena Vis ta»); 1 discrepa: «Getcemaní» (hallazgo 1). Las 86 restantes son de años anteriores y no se buscan en estos informes |
| Superlativos y ausencias sobre los temas de las fichas de 1958–1960 (usina, A.G.A.S., servidumbre, destacamento, comisaría, juez de paz, intendente, comisión municipal, puente, consorcio, Registro Civil, Hogar, reglamento, Bernabé López, Villa Urquiza, Mojotoro, caza, censo, pensiones, cateo, mina, patio, Serrey, plano 17, Wierna, Chalchanio, tomero, subsidio, senador, Los Porongos, Los Peñones, Potrero de Castilla, San Alejo, entre otros), en oraciones que no nombran 1958–1960 (repaso de ventana) | 33.706 oraciones del libro; 237 coincidencias, todas leídas | Ninguna desmentida en su universo declarado. A:280 («el único nombre de un intendente … en los nueve años leídos desde la convocatoria de 1949») y 04:4372 («la primera vez que el archivo nombra una villa») conservan su universo. El repaso llevó a la serie de la mina 44-L (04:4203, D:178), donde la cuenta de caducidades no incorporaba 1958 (hallazgo 6) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 318/318 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| Dotaciones de 1958–1960 recalculadas desde caudal y superficie | 19 actos (7, 6 y 6) | 1958: 0,525; 0,524; 0,525; 0,50; 0,525; 0,524 (el 242-E no da caudal). 1959: 0,528; 0,524; 0,525; 0,525; 0,526; 0,525. 1960: 0,526 (dos veces); 0,525 (cuatro). Cierran A:339, A:345, A:352 y 17:353 («diecisiete de los diecinueve») |
| Recuentos de 1958–1960 (A, F, 00, 02, 17) | 3 años | Ediciones: 5562–5805 = 244 números, 243 distintas (la 5727 es la edición ausente del lunes 8 de septiembre y su archivo repite la 5728); 5806–6047 = 242; 6048–6287 = 240. Hojas: 4.129 − 15 = 4.114; 3.890 − 1 = 3.889; 3.523. Faltantes por tapa: 4.204 − 4.090 = 114 (57 de ellas por foliatura, en 51 ediciones); 116 en 97; 116 en 112. Fichas: 80 + 54 + 49 = 183 del §A y 10 + 10 + 14 = 34 de B.2. Mesas: 9 + 5 = 14 en 1958 y en 1960. Actos de agua con acequia municipal: 4. Intendentes confirmados en 1960: La Caldera y otros diez. Cierran |
| Cadenas de saldos (F:64, D:177) | 3 informes, §E.1 | 1958: tres resúmenes, cadena no armada; 1959: cuatro tramos; 1960: dos tramos, subtotales sin recalcular. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 51 | 50 de 227 oraciones con cifra en las 65 líneas | **50/50 con fuente localizable**: 27 con la cita en la oración, 18 en la fila o el párrafo, y 5 declaraciones de cobertura (F, 09, 20) o recapitulaciones (03:391) cuya fuente es el propio apéndice F, los informes LEE o el párrafo anterior |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 65 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 284; 8/8 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra. Ningún pedido de D satisfecho por 1958–1960 sigue en la lista (D:177 pide justamente lo que falta de esos años) |
| Privacidad: personas nombradas en las 65 líneas, cruzadas con contextos sensibles | 65/65 líneas | Deudores de los remates de 1958–1959 (Getsemaní, Villa Urquiza), pensionados, personal del Hogar, vecinos expropiados por la Ley 3425 y jueces de paz renunciantes: ninguno nombrado. Nombrados sólo funcionarios (Gallo, Muñoz), concesionarios de agua (Ortiz, Palazzolo), el contratista de la usina, los Serrey y Fiori en actos de dominio. Sin casos |
| Largo de los archivos antes y después de la fase 6 | 5/5 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero, base y fase 6 | Compilan las dos; 831 páginas; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:78; 2 cajas desbordadas, las mismas |

## Ronda 52 — auditoría con fase 6 (30/09/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1961–1962. Base: commit `d126594` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1961–1962), con la fase 6 de esta ronda en `ronda-52.patch` (commit `74c4226` en la sesión; aplica con `git am` sobre `d126594`). **Denominador medido: 25.068 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 51 (25.056 de 25.056, registrados sobre `d301f2a`, que entró al repositorio como `11d8d1f`) se trasladaron por diff a `d126594`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1961–1962 agrega 12 líneas (9 en A, 1 en C y 2 en F) y modifica 34 en 19 archivos: caducan 46**, y quedan **25.022 vigentes sobre 25.068 (99,8 %)**.

### Lectura sobre el texto (numeración de `d126594`)

Se leyeron **las 46 líneas caducas, enteras, por la sesión**, sin subagentes, cotejadas contra los informes LEE 1961 (`BO-Salta-1961_6288-6527_la-caldera_LEE-1961_2026-09-30.txt`) y 1962 (`BO-Salta-1962_6528-6768_la-caldera_LEE-1962_2026-09-30.txt`), bajados de `corrige/lee/`: las 123 fichas de los dos informes (61 + 35 del §A y 10 + 17 de B.2) se listaron y se leyeron en su FICHA, y en las que las líneas citan, también en TEXTO y NOTA; además, el §0, el §R, E.1 y E.4 de los dos. Se releyeron como contexto, enteras, 89 líneas con cobertura vigente; no suman cobertura, pero entran en el denominador del aspecto 7.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 354–362 | 9 | sesión |
| ape/C-normativa.tex | 113 | 1 | sesión |
| ape/D-pedidos.tex | 40, 177, 191–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 66–67, 69 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599, 4638 | 4 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332 | 1 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 45, 281, 284, 353 | 4 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/26-presencia.tex | 69, 98, 235 | 3 | sesión |

Contexto releído entero (no suma cobertura): 22-prospectiva:120–175 (la serie de intervenciones y la tercera condición); 18-politica:529–531 (Esteban Mogro en 1983); 10-expropiacion:325–331; 26-presencia:68 y 206–213; 04-siglo:4207–4212 (la mina de plomo y plata); 20-opacidad:750–756; D:193. Leídas en parte, para el repaso de ventana, y fuera del denominador: A:213, 216, 219, 225, 226, 233 y 320 (la serie de Augusto Regis) y E:30.

**Esta ronda: 46 líneas nuevas.** Con el contexto leído entero son 135 líneas y 76.518 bytes sobre 2.686.983, que en las 837 páginas de la base equivalen a **23,8 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `d126594` cae dentro de estos tramos.

Acumulado: 25.022 vigentes + 46 = **25.068 de 25.068 (100,0 %)**. La fase 6 toca 8 líneas, 6 dentro de lo leído en esta ronda (A:360; D:191; 04:4599; 18:470; 21:87; 26:235) y 2 del contexto releído entero (22-prospectiva:140 y 144), y no cambia el largo de ningún archivo: **25.068 de 25.068 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1961 y 1962 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 6421 | 6 | Decreto 18570-E, visto y art. 1 | «a fin de reforzar el caudal con que actualmente abastece de agua para bebida a la ciudad de Salta»; «art. 40 de la Ley Nº 755». Coincide (A:355, 17:45) |
| 6439 | 6 | Decreto 19119-A, visto | «siendo necesario normalizar la situación de dicho personal». Coincide |
| 6615 | 11 | Decreto 2382-G, visto y art. 2 | «por el que se declara en comisión a las autoridades municipales de la provincia»; Augusto Regis en el cuarto renglón, La Caldera. Coincide. En la misma hoja, el 2381-G lleva el mismo visto y otras siete localidades |
| 6718 | 10 | Decreto 4511-E, considerando | «disponer la rescisión del contrato, resultaría desfavorable»; «reducido porcentaje de obra faltante»; Resolución 414 del 6 de septiembre de 1962. Coinciden las dos citas |
| 6581 | 9 | Decreto 1522-A, art. 1 | «fenómenos atmosféricos». Coincide |
| 6440 | 7 | Decreto 19157-E, visto y art. 1 | «Manufactura de Tabacos Particulares V. F. Greco S. A.»; «la actual propietaria del predio»; «Getsemaní»; setenta y cinco centilitros por hectárea. Coinciden |
| 6334 | 8 | Edicto 7831 | «Manufactura de Tabacos Particular V. F. Grego Sociedad Anónima»; 216 horas, 19/30 partes, 0.75 l/s. Coincide |
| 6367 | 6 | Decreto 17.362-G, resolución 189 | «(Departamento La Caldera)»; II Zona con asiento en Campo Quijano, 1 cabo y 2 agentes. Coincide |
| 6394 | 8 | Decreto 18.079-E, planilla | «Edificio Policial en La Caldera», H I III 6 D III 7, \$300. Coincide |
| 6438 | 5 | Decreto 19.077, art. 1 | \$812.516,85; «de fs. 13 a fs. 16 de estas actuaciones». Coincide |
| 6671 | 12 | Decreto 3634-E, art. 1 | Arturo René Fernández; «Campo Alegre», Dpto. La Caldera. Coincide |
| 6610 | 17 | Decreto 2166-A, nómina | «Médico Regional — La Caldera»; **«Auxiliar 5º — Enf. La Caldera — Señorita Corina Adela Bustamante», sin consultorio externo** (hallazgo 3) |
| 6360 | 8 | Decreto 17.219-A, nómina | «Médico Reg. La Caldera, Dr. Juan C. Martearena»; «Médico Reg. Vaqueros y San Lorenzo, Dr. Dardo Frías». Coincide |
| 6552 | 12 | Decreto 941-A, art. 1 | Servicios de Frías «desde el 6 de noviembre al 1º de diciembre de 1961», mientras Martearena es encargado del Hospital de Cafayate (hallazgo 2) |
| 6288 | 10 | Decreto 15839-G | Decreto del 27/12/1960; Resolución 898 del Consejo General de Educación del 14/12/1960 (hallazgo 1) |
| 6585 | 5 | Decreto 1565-G, art. 1 | «que corre de fojas 2, a fojas 5, de este expediente»; \$1.002.736,82; firma Escobar Cello. Coincide |

Son **13 citas entre comillas del libro cotejadas en la imagen, sobre 11 hojas de 11 ediciones** (6421, 6439, 6615, 6718, 6581, 6440, 6334, 6367, 6394, 6438, 6671), **ninguna corrección silenciosa y ninguna cita que cambie el sentido**; más la cita que la fase 6 agrega («Enf. La Caldera», 6610 h17) y **5 datos sin comillas** (6610 h17, 6360 h8, 6552 h12, 6288 h10, 6585 h5), de donde salen los hallazgos 1, 2 y 3. En total, 16 hojas de 16 ediciones (9 de 1961 y 7 de 1962). No se cotejaron: 6573 h11–13 (zonas de 1962), 6406 h5–6 (zona D de 1961, sólo localizado), 6512 h5–6 (decretos 1-G y 7-G, que los informes leen en la capa), 6547 h3–5 (896-G) ni los certificados de la escuela.

### Hallazgos (cuatro, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 26:235 | «En 1961 y 1962 … la obra se hace: se adjudica a Walter Lerario»: la adjudicación es la Resolución 898 del Consejo General de Educación del 14/12/1960, aprobada por el 15839-G del 27/12/1960 y publicada en enero de 1961 (Nº 6288, h. 10); A:359 lo dice bien | 3 | «en enero de 1961 se publica la adjudicación a Walter Lerario, resuelta en diciembre de 1960» |
| 2 | A:360 | En la fila de 1962, «dos médicos reemplazan al regional de La Caldera»: el reemplazo del 941-A es del 6/11 al 1/12/1961 (Nº 6552, h. 12); el del 1047-A, del 16/1 al 12/2/1962 | 3 | «se reconocen los servicios de dos médicos que reemplazaron al regional…, uno en noviembre de 1961…, y otro en enero y febrero de 1962» |
| 3 | 04:4599, D:191, 21:87 | Los tres atribuyen el consultorio externo también a 1962: el 2166-A dice «Enf. La Caldera» sin consultorio (Nº 6610, h. 17), como trae A:360 y el informe LEE 1962 (A.17); ningún acto de 1962 del informe nombra el consultorio externo | 7 | 04: «a la enfermera ---en 1961, la del consultorio externo; en 1962, sólo «Enf. La Caldera»---»; D y 21: consultorio externo sólo en 1961 |
| 4 | 22-prospectiva:140–144 | «Y la serie no termina ahí: llega hasta 1946»: cierre de serie desmentido por el propio libro, que registra la intervención de la Municipalidad de octubre de 1955 (247-G, D:193, 18) y, desde este AMPLÍA, la puesta en comisión de noviembre de 1961 y los comisionados interventores de 1962 (A:356, 18:470). Sobrevivió al cierre de las ventanas 1955–1957 y 1961–1962 | 5 | «en el archivo temprano llega hasta 1946»; y una frase que sigue la serie fuera de esa ventana (1955, 1961–1962), con remisión al capítulo de política |

Restan: dos casos en el aspecto 3 (hallazgos 1 y 2), un error de consistencia en el 7 (hallazgo 3) y un superlativo de cierre desmentido por el propio libro en el 5 (hallazgo 4, −10).

**Tres de los cuatro están en material que la propia auditoría incorporó** (AMPLÍA 1961–1962, `d126594`: hallazgos 1, 2 y 3); el cuarto es una frase anterior que el repaso de ventana de las rondas 49 y 51 y el del AMPLÍA no revisaron. Ninguno fue atrapado por un control automático antes de llegar al libro: el control de citas de P74 no los ve (no son citas), y los hallazgos 1 y 2 los vería un control de fechas que compare el año de la fila con las fechas de la FICHA (P86, nuevo).

**Mejora sin hallazgo.** 18:470 suma que el Esteban Mogro de la ordenanza de 1983 renuncia en noviembre de ese año como juez de paz titular (18:529, B.O. Nº 11.868): el cargo de 1961 y el de 1983 son de la misma clase. La identidad sigue sin afirmarse.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.056/25.056 líneas vigentes en `11d8d1f` | 25.022 vigentes, 46 caducas por el AMPLÍA 1961–1962 |
| Citas con número de acto, edición y hoja de 1961–1962 contra las FUENTE de los informes LEE | 132 citas «número-letra, Nº, h.» y «Nº, h.» con edición ≥ 6288 en las 46 líneas | Todas localizadas; las 10 que el script no resolvió de primera son rangos de hoja («h5 c2 a h10 c1», «h11 c1 a h18»), el «[1]7763» del 17763-A y tres citas de 6512 h5–h6 que los informes dan en E.4 y en B y no en una ficha del §A; cierran al mirar la FUENTE y las notas |
| Citas entre comillas de las 46 líneas contra el TEXTO de los informes LEE 1961–1962 (P74) | 91 citas | 43 aparecen en el TEXTO de los informes 1961–1962: 40 literales y 3 que difieren sólo por el espacio de TeX («Dr.\ Luis Linares», dos veces, y «fs.\ 13»); ninguna cita de un acto de 1961–1962 discrepa. Las 46 restantes son de actos de años anteriores y no se buscan en estos informes; 2 de menos de cuatro caracteres no se controlan |
| Superlativos, cierres y ausencias sobre los temas de las fichas de 1961–1962 (Obras Sanitarias, Getsemaní, destacamento, Los Yacones, Registro Civil, juez de paz, comisionado, interventor, Gallo, Regis, presupuesto, Bernabé López, Chalchanio, zona, Hogar, Campo Alegre, mina, cateo, pensión, San Cayetano, senador, Ley 3192, edificio policial, receptor, elección, Mogro, Fernández, médico regional, consultorio, usina, Wierna, entre otros), en oraciones que no nombran 1961 ni 1962 (repaso de ventana) | 263 coincidencias en el libro entero, todas leídas | Una desmentida por el propio libro: 22-prospectiva:140 (hallazgo 4). Conservan su universo: A:280 («nueve años leídos desde la convocatoria de 1949»), 04:4209 («la única sustancia metalífera que el archivo temprano asocia»: las minas de 1955 y 1961 son también de plomo y plata), 26:212 (1923–1945), 20:754 y 22-prospectiva:144 («veintiocho años») |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 319/319 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 (la nueva remisión de 22-prospectiva va a un capítulo anterior) |
| Sumas de los certificados de la escuela de Vaqueros (A:359, 26:235) | 19 certificados (6 de 1961 y 13 de 1962) | \$934.343,32 + \$1.882.910,81 = \$2.817.254,13. Faltan el parcial 3 y los ajustes provisorios 3 y 5. Cierran |
| Dotaciones de 1961–1962 recalculadas (A:357, A:361, 17:353) | 4 actos con caudal y superficie | 25,25/50 = 0,505; 1,57/3 = 0,523; 0,79/1,5 = 0,527; Getsemaní, 0,75 como máximo. Cierran |
| Recuentos de 1961–1962 (A, F, 00, 02) | 2 años | Ediciones: 6288–6527 = 240; 6528–6768 = 241 archivos y 240 de contenido. Hojas: 4.663 (223 de suplemento) y 4.619 (112). Faltantes por tapa: 118 en 76 ediciones y 167 en 127. Fichas: 61 + 35 = 96 del §A y 10 + 17 = 27 de B.2. Actos de agua: 4 y 4. Pensiones de 1961: 5 a la vejez (1 sin lugar, 1 Los Yacones, 3 Vaqueros), 2 a la invalidez, 1 rehabilitación. Tramos: 42 + 1 + 5 = 48. Hueco 1963–2012: 50 años. Cierran |
| Cadenas de saldos (F:66) | 2 informes, E.1 | 1961: un tramo, febrero con cien pesos de más y diciembre de 1960 sin recalcular; 1962: dos tramos cortados por enero, enlaza con 1961. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 52 | 50 de 172 oraciones con cifra en las 46 líneas | **50/50 con fuente localizable**: 32 con la cita en la oración, 8 en la fila o el párrafo, y 10 declaraciones de cobertura (00, 02, 04, F) cuya fuente es el apéndice F o los informes LEE |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 46 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| `\pendiente{}`, ítems de D y `\label` de apéndices | 52; 284; 8/8 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra. Ningún pedido de D satisfecho por 1961–1962 sigue en la lista (D:191 sigue pidiendo el otorgamiento de 1953, que 1961 no trae) |
| Privacidad: personas nombradas en las 46 líneas, cruzadas con contextos sensibles | 46/46 líneas | Pensionados, personal del Hogar, la empleada denunciante, el agente cesante, la titular del Registro Civil en licencia y los deudores de los remates: ninguno nombrado. Nombrados sólo funcionarios (Gallo, Regis, Escobar Cello, Mogro), el contratista de la escuela y el destinatario del préstamo de un toro (Fernández), sin contexto sensible. Sin casos |
| Largo de los archivos antes y después de la fase 6 | 7/7 archivos tocados por la fase 6 | ninguno cambia de largo |
| Compilación | libro entero, base y fase 6 | Compilan las dos; 837 páginas; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:75 y 00:78; 2 cajas desbordadas, las mismas |

## Ronda 53 — incorporación de la respuesta del ENReGE (30/09/2026)

Tipo: **incorporación** (CORRIGE 3.6), a pedido de Eduardo, de un documento aportado: la nota NO-2026-95453797-APN-UDG\#ENREGE del 30/09/2026 (Unidad Distribución de Gas del ENReGE, firmada por Guillermo Lanzillotti), respuesta a la presentación IF-2026-90610845-APN-USDG\#ENREGE, con dos adjuntos embebidos en el PDF: la presentación de Naturgy NOA S.A. IF-2025-131212725-APN-SD\#ENARGAS y el informe intergerencial IF-2026-41299939-APN-GD\#ENARGAS (23/04/2026). Base: commit `74c4226` (fase 6 de la ronda 52, en `ronda-52.patch`); parche `ronda-53.patch` (commit `20bb7d4` en la sesión; aplica con `git am` después de `ronda-52.patch`, y los dos sobre `d126594`). **Denominador: 25.071 líneas** (25.068 + 3: dos filas nuevas en A y un ítem nuevo en F).

### Lectura de la fuente

La sesión leyó la nota entera (2 hojas) y los dos adjuntos por su capa de texto: la presentación de Naturgy entera y, del informe, la apertura, el cierre y los pasajes sobre «Comitente», la oportunidad de la evaluación económica y las propuestas de FESUBGAS (la búsqueda da 40 renglones con «Comitente» y 21 con «NOA» o «Naturgy»; se leyeron en contexto los que tratan la definición del Comitente, la oportunidad de la evaluación económica y la captación de usuarios, y el resto no se leyó). Ni la nota ni los adjuntos nombran La Caldera.

### Qué establece y qué cambia en el libro

| Dato de la fuente | Clase | Dónde | Corrección |
|---|---|---|---|
| El marcador azul del mapa interactivo es la función «Mi Ubicación» | CONTRADICE | 16:190, 196, 216 y 219 | La lámina del mapa interactivo deja de contarse como testimonio de la red: epígrafe y ficha lo dicen, y «las tres dicen lo mismo» pasa a «dos permiten responderlo». El libro había leído el marcador como capa de localidades abastecidas, y lo había declarado como lectura propia |
| El mapa de Salta del «Sistema de Transporte y Distribución de Gas» se actualizó por última vez en 2024 | PRECISA | 16:194 y 206; F:241 | «sin fecha» pasa a «sin fecha impresa; última actualización en 2024, según el Ente» |
| Nota ENRG/GAL/GDyE/GD/D Nº 2896/99, del 08/07/1999: el ENARGAS autoriza a Gasnor el proyecto «Provisión de gas natural en el Valle de Lerma», cuyas zonas incluyen Vaqueros y Lagunilla y no La Caldera | NUEVO | A:382; 16:261 | Fila nueva en la cronología. 16:261 decía que la consulta al Ente no se había hecho; ahora dice que se hizo y qué contestó, con dos cautelas: la nota no dice que no haya otra autorización, y sólo las obras de magnitud la requieren |
| Presentación de Naturgy NOA e informe intergerencial | NUEVO; CAE-PEDIDO | 16:257; D:336 | Lo que dicen para el corredor: captación real lejos de la conexión completa a cinco años (La Viña, «un 8\% de la potencialidad total»), objeción al «Comitente», rechazada por el informe, y evaluación económica al pedir la factibilidad. En D:336 salen los dos documentos y la consulta al Ente, y entran, en el mismo ítem, el expediente de la autorización de 1999 y la consulta a Naturgy sobre solicitudes de factibilidad para La Caldera |
| Fecha del atlas y leyenda del marcador | CAE-PEDIDO | D:355 | Salen del ítem; queda la extensión de la red dentro de Vaqueros |
| La respuesta misma | NUEVO | A:562; F:242 | Fila del 30/09/2026 y la nota con sus adjuntos entre las fuentes |
| Régimen de 2026 | PRECISA | 23:183; 00:75 | 23: los terceros pueden ser futuros usuarios o comitentes, y el cálculo se hace al pedir la factibilidad. 00: «tres mapas de la red de gas del ENARGAS» pasa a «tres mapas del ENARGAS» |

Recuento: 2 NUEVO con fila propia, 1 CONTRADICE, 3 PRECISA y 3 pedidos satisfechos que salen de D (dentro de dos ítems, que siguen siendo 284).

### Traslado, lectura y cobertura

La ronda toca 16 líneas: 16:190, 194, 196, 206, 216, 219, 257 y 261; 23:183; 00:75; D:336 y 355; F:241 y 242 (nueva); A:382 y 562 (nuevas). **La sesión releyó enteras las 16 después de escribirlas**, contra la nota y sus adjuntos, como en la ronda 47, y releyó además 16:192–262 como contexto. Siguen vigentes las 25.055 líneas que no se tocaron, y las 16 quedan leídas en esta ronda: **25.071 de 25.071 (100,0 %)**. Un auditor que no las escribió las leerá en la próxima `MEJORA`, que empieza por este parche.

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Citas entre comillas agregadas, contra la nota y los adjuntos | 5 («Mi Ubicación», dos veces; «Provisión de gas natural en el Valle de Lerma», dos veces; «actualmente lleva conectado un 8\% de la potencialidad total») | Las 5 literales. «Comitente» es el término definido, no una cita |
| Repaso de lo que dependía del marcador o de la consulta no hecha | 7 formas («tres mapas», «las tres dicen», «marcador azul», «consulta al ENARGAS», «consultar al ENARGAS», «nadie pidió», «nadie solicitó») en los 38 archivos | 00:75 y 16:190, 196, 216, 219 y 261 corregidos; 16:259 («nadie solicitó que se calculara el Valor de Negocio», hasta donde alcanza el relevamiento) sigue en pie: la nota no informa ninguna solicitud para La Caldera |
| Ítems de D | 284 antes y después | Cierra con 22-prospectiva |
| Remisiones a capítulos posteriores sin «más adelante» | 319/319 | 0 sin marcar (las dos remisiones nuevas, de 23 a 16 y de F a 16, van hacia atrás o desde un apéndice) |
| Privacidad | 16 líneas | Sólo organismos, la distribuidora y el número de la presentación; ni el nombre ni el correo del presentante. Sin casos |
| Compilación | libro entero, con las rondas 52 y 53 aplicadas sobre `d126594` | Compila; 839 páginas; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:75 y 00:78 |

## Ronda 54 — auditoría con fase 6 (01/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1963 y, como lo pedía el bloque de la ronda 53, sobre las 16 líneas de esa incorporación, que esta vez lee un auditor que no las escribió. Base: commit `32ad712` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1963, sobre `3304c70`, la ronda 53), con la fase 6 en `ronda-54.patch` (commit `4f39e11` en la sesión; aplica con `git am` sobre `32ad712`, probado en un clon limpio: árbol `18a0989`). **Denominador medido: 25.080 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 53 (25.071 de 25.071, sobre `3304c70`) se trasladaron por diff a `32ad712`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1963 agrega 9 líneas (6 en A, 1 en C y 2 en F) y modifica 35 en 22 archivos: caducan 44**, y quedan **25.036 vigentes sobre 25.080 (99,8 %)**. La ubicación de cada línea se tomó con `git blame` sobre `32ad712` (44 líneas del commit `32ad712` y 16 del `3304c70`).

### Lectura sobre el texto (numeración de `32ad712`)

Se leyeron **las 44 líneas caducas, enteras, por la sesión**, sin subagentes, contra el informe LEE 1963 (`BO-Salta-1963_6769-7009_la-caldera_LEE-1963_2026-10-01.txt`, bajado de `corrige/lee/1963/`): el §0, el §1 con la tabla por edición, las 40 fichas del §A y las 6 de B.2 enteras (FICHA, TEXTO y NOTA), B.1, B.3, B.4, §C y §P; y, para las remisiones a otros años, el informe 1962 (aviso 12441), el 1959 (Ley 3425 y la fracción de Manuel Condori), el 1958 (A.69, «La Milagrosa») y el 1955 (minas San Fernando y Abra de Mayo). Se leyeron además, enteras, **las 16 líneas de la ronda 53**, que su propia sesión había dado por leídas; suman a la cobertura sólo como relectura, porque ya estaban vigentes, pero entran en el denominador del aspecto 7. La nota del ENReGE y sus adjuntos no están en un repositorio que la sesión pueda bajar (P87): esas 16 líneas se leyeron por su consistencia interna y con el resto del libro, no contra la fuente.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 306, 359, 363–368 | 8 | sesión |
| ape/C-normativa.tex | 114, 142 | 2 | sesión |
| ape/D-pedidos.tex | 40, 177, 191–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 68–69, 71 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 1010 | 1 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/08-vaqueros.tex | 85 | 1 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332 | 1 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 50, 235 | 2 | sesión |

Relectura de la ronda 53 (ya vigentes, no suman): A:388 y 568; D:336 y 355; F:243–244; 00:75; 16:190, 194, 196, 206, 216, 219, 257 y 261; 23:183. Contexto releído entero (no suma cobertura): 16:186–200 (la ficha de las tres cartografías) y las filas A:320, 340, 344 y 358 (las minas de 1955, 1958 y 1961 y la Ley 3425).

**Esta ronda: 44 líneas nuevas.** Con la relectura de la ronda 53 y el contexto son 76 líneas y 89.814 bytes sobre 2.709.375, que en las 845 páginas de la base equivalen a **28,0 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `32ad712` cae dentro de estos tramos.

Acumulado: 25.036 vigentes + 44 = **25.080 de 25.080 (100,0 %)**. La fase 6 toca 10 líneas, todas dentro de lo leído en esta ronda (A:359, 364, 365, 366 y 368; C:114; D:253; 04:4599; 13:248; 15:185), y no cambia el largo de ningún archivo: **25.080 de 25.080 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1963 de `boletines-salta`)

Imágenes de los PDF del Release, a 200–500 ppp, recortadas por coordenadas o por la posición de la capa.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 6917 | 5 | Decreto 8519, vistos y arts. 1 a 3 | «La Caldera» o «Getsemani», Ley 1030\|48: coinciden (A:365, 13:248). El considerando funda en el convenio la apertura, el enripiado y la cañería, y en el art. 174 de la Ley 1030 el arbolado; **el art. 3, que el informe no transcribe, impone las tres cosas** (hallazgo 1) |
| 6959 | 7 | Decreto-ley 429, vistos, considerando y art. 1 | Art. 1, leído en la imagen y no sólo en la capa: «Ratifícanse con fuerza de **Ordenanza**» (hallazgo 6). El considerando: convenios «de cláusulas similares» a uno aprobado por el «Decreto Ley Nº 309\|63», que el informe daba sin número |
| 6774 | 5 | Decreto 5127-E | «Salta, 31 de Octubre de 1962» es la fecha del decreto; el certificado no lleva fecha (hallazgo 2). \$162.373: coincide |
| 7008 | 13 y 14 | Resoluciones de minas 16093 y 16088 | «SALTA, Noviembre 29 de 1963» y «SALTA, Diciembre 3 de 1963», publicadas el 30 de diciembre (hallazgo 3); «ABRA DE MAYO», seis pertenencias; «SAN FERNANDO», cinco: coinciden |
| 6976 | 7 | Decreto 365, art. 2 | «en vacante por renuncia del Dr. Juan C. Martearena»: coincide. Las localidades son «Las Moras, San Fernando de Escoipe y **Pulares**»: el informe y el libro, por la capa, decían «Fulares» (hallazgo 5) |
| 6903 | 18 | Decreto 8271, art. 1 | «Consultorio Externo de la localidad de La Caldera»; del 8 de abril al 7 de mayo. Coincide |
| 6888 | 13 | Decreto 7945, art. 1 | «corre a fojas 15**.** 17, 19 y 21»: a 500 ppp, punto después del 15 y comas después del 17 y del 19 (hallazgo 7); \$909.695,17 coincide |
| 6823 | 9 | Decreto 6751-G, visto | «La Cal-» al fin del renglón y «lera;» al principio del siguiente: la errata es «Callera», y el guion es el corte de renglón (hallazgo 8). «JULIO CATALAN ARRELLANO»: coincide |
| 6993 | 9 | Decreto 959, art. 1 | «Sub Comisaría de La Caldera»; seis meses en comisión por el 6542 del 19-II-1963. Coincide |
| 6850 | 5 | Decreto 150 de la Municipalidad de la Capital, considerando | «en los campos comprendidos entre La Caldera y Los Sauces». Coincide |
| 6846 | 6 | Decreto 7173-G, vistos | «dirección libre» (entre comillas en el original). Coincide |
| 6965 | 6 | Decreto 32, art. 2 | «señor Mario García». Coincide |
| 6969 | 10 | Decreto 184, art. 1 | Manuel José Hernández desde el 11 de septiembre, por treinta días hábiles. Coincide |
| 6908 | 11 | Decreto 8410, arts. 1 y 2 | Esteban Mogro, juez de paz propietario, y Pastor Lizondo, suplente, por dos años. Coincide |

Son **10 citas entre comillas del libro cotejadas en la imagen, sobre 9 hojas de 9 ediciones** («La Caldera» y «Getsemani», 6917; «con fuerza de ordenanza», 6959, dos veces en el libro; «Consultorio Externo de la localidad de La Caldera», 6903; «en vacante por renuncia», 6976; «corre a fojas 15, 17, 19 y 21», 6888; «La Cal-lera», 6823; «Sub Comisaría de La Caldera», 6993; «en los campos comprendidos entre La Caldera y Los Sauces», 6850; «dirección libre», 6846): **tres con diferencias** —una mayúscula corregida en silencio en dos lugares, un punto cambiado por coma y un guion de fin de renglón transcripto como parte de la palabra—, **ninguna que cambie el sentido**. Más **7 datos sin comillas** (6774 h5, 7008 h13–14, 6976 h7 —las localidades—, 6917 h5 —el art. 3—, 6965 h6, 6969 h10, 6908 h11), de donde salen los hallazgos 1, 2, 3 y 5. En total, 15 hojas de 14 ediciones. No se cotejaron: 6776 (5966-A y 6015-E), 6793 (236-G), 6823 h7 y 6858 (partida de la Ley 3192), 6907 (8394), 6909 (decreto-ley 360), 6975 (traslado de la Escuela 310) ni 7009 h8. Las 16 líneas de la ronda 53 no tienen facsímil en el corpus (P87).

### Hallazgos (ocho, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 13:248 | «por un convenio con la Municipalidad se obliga a abrir y enripiar las calles, prolongar la cañería de agua potable y arbolar calles y plazas»: el decreto funda el arbolado en el art. 174 de la Ley 1030, no en el convenio, como dicen A:365 y 08:85. El error viene de la FICHA A.26 del informe, que atribuye las tres cosas al convenio (el TEXTO lo transcribe bien) | 7 | el convenio para calles y cañería, el art. 174 para el arbolado; y se agrega que el art. 3 del decreto le impone las tres cosas (también en A:365) |
| 2 | A:359 | «el certificado parcial 6, del 31 de octubre de 1962»: el 31 de octubre es la fecha del decreto 5127-E; el certificado no está fechado (26:235 lo dice bien: «aprobado en octubre de 1962») | 3 | «por \$162.373, aprobado por un decreto del 31 de octubre de 1962» |
| 3 | A:368 | «el 30 y el 31 de diciembre las resoluciones que declaran caducas…»: son las fechas de publicación; las resoluciones son del 29 de noviembre (16093) y del 3 de diciembre (16088), y la de «La Milagrosa» no da fecha en la parte leída. El control de fechas de P86 compara sólo el año | 3 | «el 30 y el 31 de diciembre se publican las resoluciones ---dos de ellas del 29 de noviembre y del 3 de diciembre--- que…» |
| 4 | A:368 | La confluencia de los ríos Nieve y Wierna, «el punto de partida del cateo de 1962»: en los dos edictos (14658 y 12441) es el punto de referencia, y el de partida está 4.000 m al oeste | 3 | «que el edicto toma, como el del cateo de 1962, por punto de referencia: el de partida, el mismo en los dos, está cuatro kilómetros más al oeste» |
| 5 | 04:4599 | «San Fernando de Escoipe y Fulares»: la imagen (6976 h7) dice «Pulares»; «Fulares» es la lectura de la capa que el informe (A.34) dio por buena | 3 | «Pulares» |
| 6 | A:366, 15:185 | «con fuerza de ordenanza» entre comillas: el original imprime «Ordenanza» con mayúscula. El informe leyó el art. 1 sólo en la capa | 4 (dos casos) | «con fuerza de Ordenanza» en las dos citas; C:114, 01:139 y 22-infraestructura:545 lo dicen sin comillas y no cambian |
| 7 | 15:185 | «corre a fojas 15, 17, 19 y 21» entre comillas: el original pone punto después del 15 | 4 | la frase pasa a paráfrasis, sin comillas |
| 8 | A:364 | «La Cal-lera» ---así, en el visto---: el guion es el corte de renglón; la errata del original es «Callera» | 4 | «La Callera» ---así, en el visto, partido al fin del renglón--- |

Restan: un error de consistencia en el aspecto 7 (hallazgo 1: 1 en 28,0 páginas = 3,6 por cada 100, escalón ≤ 4 → 50), cuatro casos en el 3 (hallazgos 2 a 5, −20) y cuatro casos en el 4 (hallazgos 6 a 8, −12).

**Los ocho están en material que la propia auditoría incorporó** (AMPLÍA 1963, `32ad712`), y **ninguno fue atrapado por un control automático** antes de llegar al libro. Cuatro (5 a 8) vienen de renglones que el informe LEE leyó en la capa o transcribió con el corte de renglón, y el control de citas de P74 los dio por literales porque compara contra el TEXTO del informe, no contra la imagen; dos (2 y 3) los habría visto un control de fechas que compare también el mes y que distinga la fecha del acto de la de lo que aprueba (P86 compara sólo el año). Las dieciséis líneas de la ronda 53 no dan hallazgos.

**Mejoras sin hallazgo.** El art. 3 del decreto 8519 (A:365, 13:248) y el considerando del decreto-ley 429, que remite a un convenio de cláusulas similares aprobado por el decreto-ley 309/63 (A:366, C:114, y se pide en D:253, dentro del mismo ítem). C:114 pasa a declarar el art. 1 leído sobre el facsímil.

**Descartados (falsos positivos, 4).** «Diecisiete años de servicios» de 1920 a 1938 (A:368): es literal del 7883, que no explica la diferencia. Que el vecino del juicio ejecutivo sea uno de los dos de la Ley 3425 (A:368): el informe 1959 da a Manuel Condori como titular de una de las dos fracciones. «Con los expedientes de sus manifestaciones o mensuras de 1955, 1958 y 1961» (A:368): cierra con las filas de esos años (manifestaciones de San Fernando y Abra de Mayo en 1955, mensura de San Fernando y manifestación de La Milagrosa en 1958, mensura de Abra de Mayo en 1961). «Los dos primeros» mapas (16:219): son el atlas y el mapa nacional, en el orden de la ficha; el interactivo es el tercero.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff y `git blame` | 25.071/25.071 líneas vigentes en `3304c70` | 25.036 vigentes, 44 caducas por el AMPLÍA 1963 |
| Superlativos, cierres y ausencias sobre los temas de las fichas de 1963 (comisionado, comisión municipal, convenio, Agua y Energía, fraccionamiento, Catastro, cesiones, donación, peluquero, minas, caducidad, Escuela 310, San Alejo, encuesta, Fomento Ganadero, juez de paz, médico regional, consultorio, Linares, Hogar, cateo, Wierna, Getsemaní, Martell, San Cayetano, presupuesto, pensiones, Ley 3192, electromecánicas, intervención, subcomisaría, destacamento), en oraciones que no nombran 1963 ni un año posterior (repaso de ventana) | 80 coincidencias en el libro entero, todas leídas | Ninguna desmentida por 1963. Conservan su universo: 04:1702, 1718 y 1761 («la única mina registrada del departamento», 1908–1941), 04:4209 (plomo y plata; La Milagrosa es de cloruro de plata, sustancia de plata), 08:83, 15:457, 20:728, 22-infraestructura:545 («la usina ya no aparece por su nombre», 1961–1962) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 322/322 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 (las tres nuevas del AMPLÍA, 01→13, 01→22 y 08→13, llevan la marca) |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra. El decreto-ley 309/63 entra dentro de un ítem existente (D:253) |
| Recuentos de 1963 (A:363, F:68, 00:43, 02:28, D:177) contra el §0 y el §1 del informe | 1 año | 241 ediciones (6769–7009), 4.359 hojas, 229 del suplemento; 4.306 páginas declaradas, cuatro manchadas; 119 ediciones con 183 hojas de menos; 228 de 240 pares de foliatura; 6893 mil más bajo; cuatro tapas cien más bajas; 734 y 392 hojas sin mirar. Tramos: 42 + 1 + 6 = 49; hueco 1964–2012: 49 años. Cierran |
| Aritmética de 1963 | 4 cuentas | Certificados: 2.817.254,13 + 162.373 = 2.979.627,13. Superficies del 8519: 163.568,95 m² = 16 ha 3.568,95 m², cinco plazoletas. Ley 3192: 1.400.000 + 450.000 = 1.850.000. Comisionado: 12/10 a 15/10, tres días. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 54 | 50 de 174 oraciones con cifra en las 44 líneas | **50/50 con fuente localizable**: 39 con la cita en la oración, 10 en la fila o el párrafo, y 1 declaración de cobertura (04:3659) cuya fuente es el apéndice F |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 44 líneas; los de las 16 de la ronda 53 son de una nota oficial aportada | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 44 líneas, cruzadas con contextos sensibles | 44/44 líneas | El regente cesante y deudor del fisco, la empleada que renuncia, el empleado de la encuesta, el oficial confirmado, el agente cesante de Vaqueros, el vecino que demanda a la Provincia y los pensionados: ninguno nombrado, y lo que se dice del regente se atribuye a los actos. Nombrados: funcionarios (Regis, Catalán Arellano, García, Mogro) y el propietario del fraccionamiento (Martell), sin contexto sensible. Sin casos |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `32ad712` y fase 6 | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 845 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:75; 2 cajas desbordadas, las mismas |

## Ronda 55 — auditoría con fase 6 (01/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1964-1965. Base: commit `ff46efc` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1964-1965, sobre `c3a2761`, la ronda 54), con la fase 6 en `ronda-55.patch` (commit `adaf402` en la sesión; aplica con `git am` sobre `ff46efc`, probado en un clon limpio de GitHub: árbol `7e4bafc`). **Denominador medido: 25.096 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 54 (25.080 de 25.080, sobre `c3a2761`) se trasladaron por diff a `ff46efc`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1964-1965 agrega 16 líneas (11 en A, 3 en C y 2 en F) y modifica 39 en 22 archivos: caducan 55**, y quedan **25.041 vigentes sobre 25.096 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `ff46efc`)

Se leyeron **las 55 líneas caducas, enteras, por la sesión**, sin subagentes (una, F:71, es un renglón en blanco), contra los informes LEE 1964 (`BO-Salta-1964_7010-7251_la-caldera_LEE-1964_2026-10-01.txt`) y 1965 (`BO-Salta-1965_7252-7494_la-caldera_LEE-1965_2026-10-01.txt`), bajados de `corrige/lee/`: el §0 y el §1 de los dos, las 38 fichas del §A de 1964 y las 52 de 1965 enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, E.1 a E.3 y §R; y, para las remisiones a 1963, el informe 1963 (A.22, A.31 y A.34: el nombre entero de Martearena y el decreto 365).

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 363, 368–379 | 13 | sesión |
| ape/C-normativa.tex | 115–117, 145 | 4 | sesión |
| ape/D-pedidos.tex | 40, 177, 191–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 70–71, 73 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/03-fincas.tex | 475 | 1 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/08-vaqueros.tex | 85 | 1 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332 | 1 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470, 531, 704 | 3 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 145, 182 | 3 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 50, 235 | 2 | sesión |

Contexto releído entero (no suma cobertura): 16:283–292 y 314–332 (el Abra de Lesser de 1939 y 1942, por la remisión de 17:281) y la búsqueda de «Concejo» y «Consejo Deliberante» en el libro entero (por 18:470 y A:375).

**Esta ronda: 55 líneas nuevas**, 92.965 bytes sobre 2.742.710, que en las 855 páginas de la base equivalen a **29,0 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `ff46efc` cae dentro de estos tramos.

Acumulado: 25.041 vigentes + 55 = **25.096 de 25.096 (100,0 %)**. La fase 6 toca 7 líneas, todas dentro de lo leído en esta ronda (A:371, 373 y 379; C:117; F:70; 03:475; 22-prospectiva:144), y no cambia el largo de ningún archivo: **25.096 de 25.096 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1963, 1964 y 1965 de `boletines-salta`)

Imágenes de los PDF del Release, a 220–300 ppp, recortadas por la posición de la capa o, donde la hoja no tiene capa, por coordenadas sobre una vista entera a 75–80 ppp.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 7100 | 6 | Decreto 3162, considerando | «se estima que el lugar más apropiado y conveniente sería la localidad de La Caldera, lo que por otra parte contaría con el beneplácito de los vecinos y autoridades de ese lugar». Coincide (A:372) |
| 7118 | 7 | Decreto 3550, visto | «H. Consejo Deliberante de la Municipalidad de La Caldera», con *s*. Coincide (18:470, A:375) |
| 7453 | 7 | Decreto 10619, visto | «H. Concejo Deliberante de la Municipalidad», con *c*. Coincide (18:470, A:375) |
| 7378 | 6 | Decreto 9239, art. 3 | El informe lo leyó en la capa; en la imagen: «Director Zonal del Hospital "Dr Rafael Villagrán"», «debiendo desempeñar funciones en las localidades de La Isla y San Luis», «en base a un pedido formulado por el citado profesional». Coincide (A:373) |
| 7430 | 6 | Ley 4032, art. 1 y «Por tanto» | «con asiento en la cabecera del mismo»: coincide (A:376, 17:281). El «Por tanto» del 23 de setiembre dice «Encontrándose vencido el plazo establecido por el Artículo 98 de la Constitución Provincial, téngase por Ley»: **no es una promulgación** (hallazgo 3). La 4031, en la columna anterior, igual |
| 7317 | 10 | Decreto 7968, visto | «"Cristo Monumental"», «a erigirse en los aledaños del pueblo de La Cal-dera». Coincide (A:372) |
| 7452 | 14 | Decreto 10600, arts. 1 a 3 | «"YEYSEMANI" o "GETSEMANI"», plano 101, 48.002,88 m² y 698,96; el art. 3, que el informe leyó en la capa: «apertura de calles, arbolados y pavimentación de calles». Coincide (A:377, 13:248) |
| 7407 | 6 | Aviso 21253 | «Finca el Durazno», «herederos de Liborio Guerra», catastro 93, valor fiscal \$420.000, base \$280.000. Coincide (03:475, A:379) |
| 7099 | 8 | Aviso 17187, linderos | «Norte, propiedad de Martín Borja y Eusebio Palma»; «cumbre del cerro "El Puchete" o "El Pucheta", que lo separa de la finca "Potrero de Valencia"»; oeste, el río. Coincide; **Borja está en este aviso, que la fila de 1964 no nombraba** (hallazgo 8) |
| 7438 | 5 | Decreto 10353 (capa del PDF, legible) | «Intendencia de Aguas de La Caldera», jornal de los intendentes sin título habilitante, partida de la A.G.A.S. «hasta tanto la mencionada repartición concurse el cargo». Coincide con A:376 y C:117 |
| 6976 (1963) | 7 | Decreto 365, art. 4 | Designa al Dr. Oscar Hugo Brandan «para que tenga a su cargo la Dirección del Hospital "Dr. Rafael Villagrán" de la localidad de Chicoana», en vacante de Dousset. Coincide con 04:4599 (el informe 1963 no transcribe el art. 4) |

Son **12 citas entre comillas del libro cotejadas en la imagen, sobre 8 hojas de 8 ediciones** (la del 3162; «H. Consejo Deliberante…» y «H. Consejo Deliberante»; «H. Concejo Deliberante de la Municipalidad», dos veces; «debiendo desempeñar funciones…»; «con asiento en la cabecera del mismo», dos veces; «Cristo Monumental»; «en los aledaños del pueblo de La Caldera»; «YEYSEMANI» y «GETSEMANI», dos veces cada una en A y 13 y contadas una vez; «Finca el Durazno»; «herederos de Liborio Guerra»): **ninguna con diferencias**. Más **datos sin comillas en 4 hojas** (7430 h6, el «Por tanto»; 7099 h8; 7438 h5; 6976 h7), de donde salen los hallazgos 3 y 8. No se cotejaron: 7347 h18 (8560, «artículo 178»), 7409 h9 (9774, el art. 3 de Pineda, leído en la capa por el informe: «abrir, abovedar y arbolar» queda sin cotejo), 7285 h6 (cifras y letras del presupuesto), 7457 h7 (mejoras de San Roque), 7224 h7, 7248 h12–15, 7049 h13, 7305 h8 y 7477 h5.

### Hallazgos (ocho, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 22-prospectiva:144 | «y en 1965, cuando **ese presidente** es electo senador, designa a otro»: identifica al presidente que el decreto 32 de 1963 llama Mario García con el Gregorio M. García que renuncia en 1965, y A:375 y 18:470, del mismo AMPLÍA, dicen que eso no consta. Y «el juez de paz del pueblo»: Mogro había renunciado al juzgado una semana antes | 7 | «cuando renuncia el presidente, Gregorio M. García, electo senador ---si es el que el decreto de 1963 llama Mario García, los actos no lo dicen---, designa a otro: el que hasta una semana antes era juez de paz del pueblo» |
| 2 | A:373, F:70 | 1965: «3.902 hojas de las 3.930 páginas» y «faltan 37 páginas por la cadena»: 3.930 − 3.902 = 28, no 37. El informe (§1) lo explica: de las 3.902 hojas, 9 no son páginas distintas (seis repetidas en la 7319 y tres blancas en la 7348); 3.930 − 3.893 = 37. El libro omitía las nueve | 7 | 3.893 páginas distintas, con la razón, en A y en F |
| 3 | C:117 | Ley 4032 «Promulgada el 23/09/1965, según el decreto 10353»: el «Por tanto» (7430 h6, imagen) la tiene por ley por vencimiento del plazo del art. 98, como a la 4031; el decreto 10353 la llama promulgada. La ficha A40 del informe la da por promulgada; su propia nota de A39 decía, por el sumario, que toda la tanda 4030–4034 fue tácita | 3 | «Tenida por ley el 23/09/1965 por vencimiento del plazo del artículo 98 de la Constitución, como la 4031 ---el decreto 10353 la da por promulgada en esa fecha---» |
| 4 | F:70 | «se miraron sobre la imagen … al menos en sus renglones del departamento, los 105 actos … y los 11 de sus núcleos»: en 1965 el informe leyó en la capa los renglones del departamento del 8631 (A26), del 10462 y el 11303 (A42), del 10588 (A45) y la sentencia de B2-05. Declaración de cobertura importada del informe sin rehacer | 3 | «salvo cinco de 1965 cuyos renglones del departamento se leyeron sólo en la capa de texto», con los cinco |
| 5 | A:371 | El deudor del Banco Provincial en la ejecución de San Antonio o San Roque, nombrado («ejecuta a Ernesto Mesples»): registro de 1964, persona que puede estar viva, en contexto socioeconómico | 15 | «ejecuta al propietario» |
| 6 | A:379 | El ejecutado del remate de derechos y acciones sobre Potrero de Valencia, nombrado (1965) | 15 | «de un particular» |
| 7 | 03:475 | El ejecutado del remate de El Durazno, nombrado (1965) | 15 | «contra un particular que el aviso no da como titular» |
| 8 | A:376 | «un Martín Borja era en 1964 lindero de la finca San Antonio o San Roque (fila de 1964)»: la fila de 1964 no nombraba a Borja; está en el aviso 17187 (7099 h8). La nota de A44 del informe 1965 da otra fuente, equivocada («lindero en el aviso de agua de los Trucco, A34») | 1 (no resta fuera de la muestra) | la fila de 1964 (A:371) pasa a decir que el segundo aviso pone al norte a Martín Borja y Eusebio Palma |

Más una errata sin aspecto propio, corregida: «no veían. en 1964» con minúscula (F:70).

Restan: dos errores de consistencia en el aspecto 7 (hallazgos 1 y 2: 2 en 29,0 páginas = 6,9 por cada 100, escalón ≤ 8 → 40); dos casos en el 3 (−10); tres en el 15 (−60, desde 100: 40, como en la ronda 46 con un deudor nombrado); y la errata, en la escala general del 12 (95).

**Los ocho están en material que la propia auditoría incorporó** (AMPLÍA 1964-1965, `ff46efc`), y **ninguno fue atrapado por un control automático** antes de llegar al libro. Los controles de P74, P86 y P94 corrieron y funcionaron sobre lo que miran (citas, fechas): ninguna de las 12 citas cotejadas tiene diferencias. Lo que se escapó es de otra clase: una identidad afirmada en un capítulo y negada en el apéndice (1), una resta de recuentos (2), el tipo de promulgación (3), una declaración de cobertura copiada del informe (4), tres deudores nombrados (5 a 7), que la sesión de AMPLÍA no buscaba, y una remisión a una fila que no traía el dato (8).

**Descartados (falsos positivos, 5).** «Juan Carlos Martearena» (04:4599, A:363 y 369): el decreto 365 dice «Juan C.», pero el 8271 y el 184 de 1963 lo nombran entero (informe 1963, A.22 y A.31). Que el decreto 365 le dé a Brandan la dirección del hospital de Chicoana (04:4599): es su art. 4 (6976 h7, imagen). «Las mismas que en 1939 y 1942 sigue el capítulo» (17:281): 16:283–332, Dr. Lucio Ortiz y el arroyo del Abra. «Dos veces en veinte meses» (04:4599): noviembre de 1963 a julio de 1965. «Aparece … un cuerpo que la convocatoria no elige» (18:470): el libro no nombra antes de 1964 ningún concejo deliberante de La Caldera (búsqueda en el libro entero).

**Pendientes nuevos.** P101 (lee, 1964-1965): corregir el informe LEE 1965 —A44, Borja es lindero del aviso 17187 de 1964 (A37) y no del de los Trucco; A40, la Ley 4032 se tuvo por ley por vencimiento del plazo (7430 h6, imagen), y A39 lo anticipaba; §R, `nivel_lectura` es `capa` y no `imagen` según flujo §5.3, porque A26, A42 (10462 y 11303), A45 (10588) y B2-05 se leyeron en la capa—. P102 (herramientas): control de privacidad para AMPLÍA (y para la rúbrica AMPLÍA v2): todo nombre propio que una frase nueva pone junto a «ejecuta», «ejecución», «remate», «juicio ejecutivo», «contra», «deudor» o «embargo», en un registro de 1945 o posterior, se reemplaza por su papel antes de entregar (tres casos en esta ronda, uno en la 46).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.080/25.080 líneas vigentes en `c3a2761` | 25.041 vigentes, 55 caducas por el AMPLÍA 1964-1965 |
| Superlativos, cierres y ausencias sobre los temas de las fichas de 1964 y 1965 (Cristo, juez y juzgado de paz, concejo, intendente de riego, Intendencia de Aguas, defensas, loteo, fraccionamiento, Getsemaní, Pineda, Durazno, receptor, odontólogo, médico regional y zonal, Tolaba, puesto sanitario, Gallinato, Casa Parroquial, El Palenque, rabia, La Silleta, ómnibus, Calderilla, San Roque, Potrero de Valencia, Lucio Ortiz, Abra de Lesser, Trucco, Martell, Mogro, comisión municipal, Brandan, Torrens, escuela nacional, Registro Civil), en oraciones que no nombran 1964 ni un año posterior (repaso de ventana) | 106 coincidencias en el libro entero, todas leídas | Ninguna desmentida por 1964-1965. Conservan su universo: 04:2327 y A:113 (primer acto sobre una escuela nacional «que el relevamiento encuentra», en el tramo que esa fila fecha), 18:505 («no había Concejo», 1982–1983), 09:526 (1953, 1956 y 1957 sin defensas), 08:83 (la ley orgánica) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 323/323 `\ref{cap:…}` de un capítulo a uno posterior (una más que en la ronda 54: la de 01:139 a `cap:aguabaja`) | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Recuentos de 1964 y 1965 (A:369 y 373, F:25 y 70, 00:43, 02:28, D:177) contra el §0, el §1 y el §R de los informes | 2 años | 1964: 242 ediciones (7010–7251), 4.408 hojas, 4.536 páginas, 128 faltantes, 577 a ojos, seis seguidas en la 7118. 1965: 243 ediciones (7252–7494), 3.902 hojas, 3.893 distintas, 3.930 por la cadena, 3.950 por las tapas, 37 y 57 faltantes, 347 a ojos, 118 hojas con dos versiones; 7290 con 24 declaradas y 10 hojas. Tramos: 42 + 1 + 8 = 51; hueco 1966–2012: 47 años; las 262 a 764 hojas sin mirar por año siguen cubriendo 347 y 577. Cierran después de la fase 6 (hallazgo 2 antes) |
| Aritmética de 1964 y 1965 | 9 cuentas | Bases de San Roque: 99.000 × 3/2 × 2 × 2/3 = 198.000. El Durazno: 420.000 × 2/3 = 280.000. Presupuesto 1964/65: 1.595.148,56 − 1.595.118,56 = 30. Obra 127: 7.039.095 × 0,88 = 6.194.403,60. Obra 283: 3.210.326 × 1,147 = 3.682.244 (el decreto 3.682.245). Obra 280: 1.278.666 × 1,135 = 1.451.286. Obra 290: 3.268.586 × 0,959 = 3.134.574. Convenio del Cristo: 500 + 500 + 500 + 400 + 300 = 2.200 mil. Martearena a Brandan: noviembre de 1963 a julio de 1965, veinte meses. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 55 | 50 de 232 oraciones con cifra en las 54 líneas con texto | **49/50 con fuente localizable**: 35 con la cita en la oración, 10 en la fila o el párrafo, 4 declaraciones de cobertura cuya fuente es el apéndice F; sin fuente, 02:97 («se crea el municipio de Vaqueros, se expropia el Campo Alegre, se dicta el régimen de loteos de 1973…»), texto anterior al AMPLÍA. 98 % → 82 |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 55 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 55 líneas, cruzadas con contextos sensibles | 55/55 líneas y búsqueda en el libro entero de los ejecutados de los remates de 1964 y 1965 | Tres ejecutados nombrados (hallazgos 5 a 7; tras la fase 6, ninguno en el libro). Sin nombre: el subcomisario cesante, el sargento y los agentes que renuncian, la auxiliar de servicio, los pensionados, el jubilado de la Municipalidad, las enfermeras. Nombrados sin contexto sensible: funcionarios (Mogro, García, Brandan, Torrens Santigosa, Villada, Satue, Hernández, Muños, Borja, Mangogña), el párroco, los escultores y la comisión del Cristo, contratistas, el loteador, los solicitantes de agua y de posesión, el presidente del centro gaucho y el transportista del préstamo (como en la ronda 52). Las licencias «por enfermedad» de Torrens Santigosa no pasan al libro |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `ff46efc` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 855 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:75; 2 cajas desbordadas, las mismas |

## Ronda 56 — auditoría con fase 6 (01/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1966. Base: commit `0d141b6` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1966, sobre `21f94c5`, la ronda 55), con la fase 6 en `ronda-56.patch` (commit `2d89b02` en la sesión; aplica con `git am` sobre `0d141b6`, probado en un clon limpio de GitHub: árbol `4916b6a`). **Denominador medido: 25.105 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 55 (25.096 de 25.096, sobre `ff46efc` con la fase 6, que es `21f94c5`) se trasladaron por diff a `0d141b6`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1966 agrega 9 líneas (5 en A, 2 en C y 2 en F) y modifica 29 en 19 archivos: caducan 38**, y quedan **25.067 vigentes sobre 25.105 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `0d141b6`)

Se leyeron **las 38 líneas caducas, enteras, por la sesión**, sin subagentes (una, F:73, es un renglón en blanco), contra el informe LEE 1966 (`BO-Salta-1966_7495-7734_la-caldera_LEE-1966_2026-10-01.txt`), bajado de `corrige/lee/1966/`: el §0, el §1 con su tabla de 239 ediciones, el §2, las 25 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, E.1 a E.10, §F y §R; y el `amplia-1966.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 380–384 | 5 | sesión |
| ape/C-normativa.tex | 118–119 | 2 | sesión |
| ape/D-pedidos.tex | 177, 191–192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 26, 72–73, 75 | 4 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470, 531 | 2 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 50, 235 | 2 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): F:22–27 (la declaración de los tramos), 04:3655–3658, 22-prospectiva:141–143, 26:69, 21:64, 04:2960 y A:385 (fila de 1970); y, por búsqueda, los pasajes de las filas de A que las líneas nuevas citan (358, 362, 368, 371, 373, 375 y 379).

**Esta ronda: 38 líneas nuevas**, 72.774 bytes sobre 2.758.692, que en las 861 páginas de la base equivalen a **22,7 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `0d141b6` cae dentro de estos tramos.

Acumulado: 25.067 vigentes + 38 = **25.105 de 25.105 (100,0 %)**. La fase 6 toca 9 líneas: ocho dentro de lo leído en esta ronda (A:381, 382 y 383; F:72; 04:4599; 17:281; 18:470; 21:182) y F:25, vigente desde rondas anteriores y releída entera en ésta; no cambia el largo de ningún archivo: **25.105 de 25.105 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1965 y 1966 de `boletines-salta`)

Imágenes de los PDF del Release, a 200–400 ppp, recortadas por la posición de la capa o, donde la hoja no tiene capa (casi todo 1966), por coordenadas sobre una vista entera a 60 ppp.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 7708 | 10 | Decreto 1684, considerando | «resulta insuficiente para un efectivo bombeo ya que la napa freática en el período máximo de crecimiento se encuentra aproximadamente a 25 metros». Coincide (A:380, 26:235) |
| 7705 | 9 | Decreto 1597, considerando | «las medidas de la base a cuya construcción se había obligado eran de menores dimensiones que el pedestal de la estatua»; 6,10 x 5,20 m. Coincide (A:381) |
| 7705 | 8 | Decreto 1597, visto y primer considerando | La prórroga se funda «en la serie de inconvenientes que impidieron el normal cumplimiento del plan de trabajo originario», «en la falta de pago de certificados» y en las medidas de la base: **tres razones, y A:381 daba una** (hallazgo 6) |
| 7576 | 8 | Decreto 13341, considerando | «se han presentado diversos casos» de rabia paresiante. Coincide (A:384) |
| 7529 | 7 | Decreto 12389, art. 1 | «en reemplazo del doctor Alfredo Satué, en uso de licencia reglamentaria»: **«Satué», con tilde**; 04:4599 lo citaba sin ella (hallazgo 3) |
| 7529, 7530, 7518, 7519 | 2, 17, 2, 18, 22, 3 | Cabeceras de folio | 7529 h2 «PAG. 426» y h17 «PAG. 441» (la edición va de la 425 a la 442); 7530 h2 «PAG 414» y h18 «PAG. 430» (va de la 413 a la 432); 7518 h22 «PAG. 286»; 7519 h3 «PAG. 301». **La 7530 repite treinta números, del 413 al 442, y no doce** (hallazgo 1). Con treinta la cadena cierra: 5.038 − 10 + 30 = 5.058 = 4.975 + 65 + 18 |
| 7675 | 5 | Edicto 24647 | «tiene solicitado agua para abastecimiento de población», sin fecha del pedido (expediente 6231/U/66); 6.000 personas, 10,41 l/s, Mercurio S. A., decreto 9877 del 26-XI-59. **El edicto no fecha el pedido** (hallazgo 4); lo demás coincide (A:383, 17:281) |
| 7666 | 7 | Decreto 777 | Empieza al pie de la columna 1 y termina en la 2 de la misma hoja (pág. 3271); la hoja 8 trae los decretos 779 a 782. **No ocupa la hoja 8** (hallazgo 5) |
| 7601 | 14 | Decreto 13811 | \$416.078, tres pagarés de \$50.000, \$1.050.000, \$483.922, artículos 5 y 6 del convenio, cinco miembros. Coincide (A:381) |
| 7732 | 8 | Decreto 2081, arts. 1 y 2 | \$400.000 por la tercera y cuarta secciones; \$216.078 de la cuenta especial y \$183.922 del plan de obras. Coincide (A:381) |
| 7672 | 9 | Decreto 973 | Renuncia del juez de paz titular de La Caldera. Coincide (A:382, 18:470) |
| 7520 | 8 | Decreto 12169 | Columnas 1 y 2 de la hoja. Coincide (A:383) |
| 7477 (1965) y 7527 | 5 y 5 | Grafía del contratista de la base (P106, punto 2) | La 7477 imprime «Bressannutti» dos veces (considerando y art. 1 del 11307); la 7527, «BRESSANUTTI» (12275). **La fila de 1964--1965 transcribe bien su fuente**; la grafía cambia entre ediciones del original. Sin cambio en el libro |

Son **4 citas entre comillas del libro cotejadas en la imagen** —las cuatro con texto que agregó el AMPLÍA; la del 1684 está dos veces, en A y en 26, y se cuenta una—, **una con diferencias** (la tilde de «Satué»), y **datos sin comillas en 9 hojas** más las cabeceras de folio de 4 ediciones, de donde salen los hallazgos 1, 4, 5 y 6. Con 4 citas el cotejo es parcial (la rúbrica pide 10). No se cotejaron: 7557 h6, h7 y h10 (pensiones, cooperadoras, contratos de Tolaba y Campos), 7558 h13–14, 7582 h6 y h13, 7551 h11, 7554 h8, 7579 h12, 7585 h10, 7590 h15, 7598 h7–8, 7638 h14, 7649 h14, 7583 h6–7, 7616 h16–17 y h19, 7625 h3, 7690 h5, 7692 h12–13, 7696 h10, 7717 h7, 7724 h12 y 7518 h16–17.

### Hallazgos (seis, todos aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | F:72 | «con un salto de diez números tras la 7518 y doce repetidos en la 7530»: la 7530 vuelve a la página 413 cuando la 7529 había llegado a la 442, y repite treinta números. Con doce la cadena no cierra con lo que el mismo párrafo dice (5.038 − 10 + 12 = 5.040, contra 4.975 hojas + 65 faltantes + 18 de la 7553 = 5.058); con treinta, sí. El dato viene del §1 del informe (425 − 413) | 7 | «treinta repetidos ---la 7530 vuelve a la 413 cuando la 7529 había llegado a la 442---» |
| 2 | F:25 | «Cincuenta y un tramos se relevaron de otro modo», en la frase anterior a la que suma 42 + 1 + 9 y a la del «tramo quincuagésimo segundo»; 00:43 y 02:28 dicen cincuenta y dos. El índice del AMPLÍA registra las formas «cincuenta y un» de 03, 04, 18 y 22, y no ésta | 7 | «Cincuenta y dos tramos» |
| 3 | 04:4599 | Cita del 12389 con «Alfredo Satue»: la imagen dice «Satué». El TEXTO del informe va sin tildes (desvío declarado en su §0), y el control de citas del AMPLÍA (P74) no puede verlas | 4 | «Satué» dentro de la cita; la prosa del libro conserva «Satue» |
| 4 | A:383, 17:281 | «en octubre la Universidad Católica de Salta pide»: octubre es la publicación del edicto, que no fecha el pedido («tiene solicitado», expediente de 1966) | 3 | «en octubre se publica un pedido de la Universidad Católica de Salta, que el edicto no fecha» |
| 5 | A:382, 18:470 | Decreto 777 citado «h. 7 y 8»: está entero en la hoja 7 (7666, pág. 3271). La FUENTE de la ficha A18 del informe dice «h7 col. 1 y h8 col. 2 (pag. 3271)» | 1 (no resta fuera de la muestra) | «h. 7» en los dos lugares |
| 6 | A:381 | «amplía en 150 días el plazo de la base, porque al pedir datos el contratista había observado…»: el 1597 da tres razones de Arquitectura y una es la falta de pago de certificados, que la fila callaba | 10 (escala general; no baja el aspecto, que está en 70 por su criterio) | «con tres razones de Arquitectura: los inconvenientes del plan de trabajo, la falta de pago de certificados y que, al pedir datos, el contratista había observado…» |

Más una precisión sin aspecto propio: 21:182 decía que en 1966 la Provincia «paga el taselaje»; paga dos cuotas, \$750.000 de los \$1.050.000 adeudados (14052 y 2081), y pasa a decir «paga dos cuotas del taselaje».

Restan: dos errores de consistencia en el aspecto 7 (hallazgos 1 y 2: 2 en 22,7 páginas = 8,8 por cada 100, escalón > 8 → 30); un caso en el 3 (−5); una corrección silenciosa en el 4 (−3, por debajo del techo de 90 del cotejo parcial).

**Los seis están en material que la propia auditoría incorporó** (AMPLÍA 1966, `0d141b6`; el 2 es una línea que el AMPLÍA debía actualizar y no actualizó), y **ninguno fue atrapado por un control automático** antes de llegar al libro. Los controles de P74 (citas literales en el TEXTO del informe) y P102 (nombres junto a remates y cesantías) corrieron y funcionaron sobre lo que miran: ninguna persona privada nombrada en contexto sensible. Se escaparon un recuento copiado del informe sin rehacer la cadena (1), una mención del total de tramos con mayúscula inicial (2), una tilde que el TEXTO del informe no transcribe (3), una fecha de publicación leída como fecha del pedido (4), una hoja copiada de la FUENTE del informe (5) y una causa elegida entre tres (6).

**Descartados (falsos positivos, 5).** Que el Satue de 1966 sea el interino de 1965 (04:4599, A:380): mismo nombre en la misma plaza a siete meses, y el 12389 lo da como titular en licencia. «Tres cateos de dos mil hectáreas» (A:384): dos edictos no declaran la superficie, pero los tres polígonos cierran en 4.000 × 5.000 m (recalculado). «Cuatro órdenes de servicio» de la obra 127 (A:380, 26:235): el 13563 aprueba las órdenes 2 y 1 de las obras 127 y 174 «respectivamente», y la 1 de la 127 es la del 13397. «Es el único acto hallado del año sobre las autoridades del municipio» (A:382): el 973 es de la justicia de paz y el 13049 y el 13484, del fisco municipal. «El presupuesto … vuelve a ser del año» (15:185): el 13484 dice «correspondiente al año 1966» y el anterior era del ejercicio 1964/65.

**Pendientes nuevos.** P107 (lee, 1966): corregir el informe LEE 1966 —§1, la 7530 repite treinta números (413 a 442) y no doce, con lo que la cadena cierra (7529 h17 «PAG. 441»; 7530 h2 «PAG 414», h18 «PAG. 430»); A18, la FUENTE del 777 es 7666 h7 cols. 1-2 (pág. 3271), no h8; A04, el TEXTO pierde la tilde de «Satué» (imagen), que es parte de la grafía del original; B2-03, el edicto no fecha el pedido («tiene solicitado»); A03, la NOTA debería registrar que el 1597 da tres razones a la prórroga—. P108 (herramientas): tres controles más para AMPLÍA (y para la rúbrica AMPLÍA v2), extensión de P74, P86, P94 y P102: (1) toda cita que lleve una palabra con tilde o un nombre propio se coteja en la imagen, porque el TEXTO del informe va sin tildes; (2) la búsqueda de los recuentos de tramos y ventanas corre sin distinguir mayúsculas («Cincuenta y un»); (3) toda cifra de la cadena de folios que el libro copia se comprueba con la cuenta del año (último folio − saltos + repetidos = hojas + faltantes + ediciones ausentes) y un edicto se fecha por su publicación salvo que el texto fije la del pedido.

**Pendientes revisados sin cerrar.** P106: su punto 2 queda resuelto sin cambio en el libro (7477 h5 imprime «Bressannutti» y 7527 h5 «BRESSANUTTI»: la grafía varía entre ediciones del original, y la fila de 1964--1965 transcribe la suya); siguen abiertos sus puntos 1, 3, 4 y 5. P54 (1966 no nombra el establecimiento de salud del pueblo). P100 (1966 queda en barrido con el criterio de F). P103, P104 y P105 (láminas, H y E, pedidos de D de 1966: fuera del alcance de una ronda de auditoría).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.096/25.096 líneas vigentes en `21f94c5` | 25.067 vigentes, 38 caducas por el AMPLÍA 1966 |
| Superlativos, cierres y ausencias sobre los temas de las fichas de 1966 (Cristo, taselaje, Iramain, Trucco, rabia, Correos, cooperadora, San Cayetano, Linares, Registro Civil, Mogro, juez y juzgado de paz, comisión municipal, intervención federal, pensiones, cateo, Juanita, «Argentina», Nieve, Hoygaard, Satue, médico zonal, consultorio externo, Vialidad, Gallinato, chapas, fiestas patronales, ordenanza impositiva, presupuesto de la Municipalidad, Universidad Católica, Castañares, Tolaba, obra 127, escuela nacional, Mojotoro, Calderilla, Lesser, Yacones, D'Andrea, Durand), en oraciones que no nombran 1966 ni un año posterior (repaso de ventana) | 66 coincidencias en el libro entero, todas leídas | Ninguna desmentida por 1966. Conservan su universo: A:369 (El Gallinato, la única de las veintidós localidades de la Ley 3930), 04:2327 (escuela nacional, archivo temprano), 18:513 (urna anulada de un año), A:382 y 04:4599 («hallado del año») |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 323/323 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Recuentos de 1966 (A:380, F:26 y 72, 00:43, 02:28, D:177) contra el §0, el §1 y el §R del informe | 1 año y la tabla de 239 ediciones | Tabla del §1: 239 ediciones, tapas 5.038, hojas 4.975, faltantes 65 en 30 ediciones (19 de una, 8 de dos, 7605 de cuatro, 7647 de ocho, 7629 de dieciocho). Cadena: tres discontinuidades (7518→7519, +10; 7529→7530, −30; 7552→7554, la 7553 con 18). Cierra con 30 repetidos y no con 12 (hallazgo 1). Tramos: 42 + 1 + 9 = 52 (hallazgo 2 antes de la fase 6); hueco 1967–2012: 46 años; hojas sin mirar por año en 1958–1966: de 171 a 764. Cierran después de la fase 6 |
| Aritmética de 1966 | 9 cuentas | Chapas: 150 × 445 = 66.750. Cristo: 416.078 + 3 × 50.000 = 566.078; 1.050.000 − 566.078 = 483.922; 566.078 − 350.000 = 216.078; 216.078 + 183.922 = 400.000; pagado en el año 350.000 + 400.000 = 750.000 de 1.050.000. Cateos: 2.900 + 2.100 = 5.000 al norte contra 5.000 al sur, 4.000 × 5.000 m = 2.000 ha (los tres). Cadena de folios: 5.038 − 10 + 30 = 5.058 = 4.975 + 65 + 18. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 56 | 50 de 169 oraciones con cifra en las 36 líneas con texto que las tienen | **49/50 con fuente localizable**: 31 con la cita en la oración o en el párrafo, 15 declaraciones de cobertura cuya fuente es el apéndice F y 3 de método o de contexto con la fuente en el párrafo; sin fuente, otra vez 02:97 («se crea el municipio de Vaqueros, se expropia el Campo Alegre, se dicta el régimen de loteos de 1973…»), texto anterior al AMPLÍA. 98 % → 82. El hallazgo 5 cae fuera de la muestra |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa en las 38 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 38 líneas, cruzadas con contextos sensibles (P102) | 38/38 líneas | Ningún nombre junto a remate, ejecución, cesantía, pensión o embargo. Sin nombre: la auxiliar cesanteada por abandono de servicio, la regente, los pensionados, la enfermera promovida, el titular del Registro Civil en licencia, el juez de paz que renuncia, el firmante de los pagarés. Nombrados sin contexto sensible: funcionarios (Hoygaard, Satue, Mogro, Julio González, D'Andrea, Durand), los escultores del Cristo, la empresa contratista y los concesionarios de agua (como en las rondas 52 y 55) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `0d141b6` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 861 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 41 entradas, las cuarenta y una que dice 00:75; 2 cajas desbordadas, las mismas |

## Ronda 57 — auditoría con fase 6 (02/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1967-1968. Base: commit `3b5be9e` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1967-1968, sobre `187bc6d`, la ronda 56), con la fase 6 en `ronda-57.patch` (commit `8cdeb54` en la sesión; aplica con `git am` sobre `3b5be9e`, probado en un clon limpio de GitHub: árbol `7ed9447`). **Denominador medido: 25.120 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 56 (25.105 de 25.105, sobre `0d141b6` con la fase 6, que es `187bc6d`) se trasladaron por diff a `3b5be9e`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1967-1968 agrega 15 líneas netas (10 en A, 3 en C y 2 en F) y deja 50 líneas nuevas o modificadas en 21 archivos: caducan 50**, y quedan **25.070 vigentes sobre 25.120 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `3b5be9e`)

Se leyeron **las 50 líneas caducas, enteras, por la sesión**, sin subagentes (una, F:75, es un renglón en blanco), contra los informes LEE 1967 (`BO-Salta-1967_7735-7972_la-caldera_LEE-1967_2026-10-01.txt`) y 1968 (`BO-Salta-1968_7973-8217_la-caldera_LEE-1968_2026-10-01.txt`), bajados de `corrige/lee/<año>/`: el §0, el §1, las 23 y 35 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, E.2, E.4 y E.7; y el `amplia-1967-1968.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 385–394, 396 | 11 | sesión |
| ape/C-normativa.tex | 120–122 | 3 | sesión |
| ape/D-pedidos.tex | 177, 191–192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 74–75, 77 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 97 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 149, 332, 513 | 3 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 463 | 1 | sesión |
| cap/18-politica.tex | 470, 531 | 2 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 15-hacienda:46–50, 09-defensas:546–550, 26-presencia:59–61, 22-prospectiva:140–143 y 10-expropiacion:511–515.

**Esta ronda: 50 líneas nuevas**, 103.237 bytes sobre 2.797.039, que en las 873 páginas de la base equivalen a **32,2 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `3b5be9e` cae dentro de estos tramos.

Acumulado: 25.070 vigentes + 50 = **25.120 de 25.120 (100,0 %)**. La fase 6 toca 9 líneas, todas dentro de lo leído en esta ronda (A:385, 386, 387, 392 y 394; 10:149; 17-aguabaja:281; 18:531; 26:235), y no cambia el largo de ningún archivo: **25.120 de 25.120 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1967 y 1968 de `boletines-salta`)

Imágenes de los PDF del Release (sin capa de texto en 1967) a 300 ppp, recortadas por la posición que da un reconocimiento propio con tesseract `eng` sobre la hoja entera; cada recorte se miró.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 7783 | 20 | Decreto 3240: considerando y art. 2 | «por no existir de energía eléctrica en la zona» y «las condiciones topográficas de los terrenos a donde han de emplazarse las obras, antes de proyectar las mismas». Coinciden (A:385, 26:235) |
| 7783 | 20 | Decreto 3240: fecha y visto | El decreto es del 9 de marzo de 1967 y aprueba la Resolución 706 de Arquitectura **del 18 de noviembre de 1966**, que es la que aprueba la orden de servicio 5: **la orden no es de marzo** (hallazgo 1) |
| 7951 | 16 | Decreto 7012, considerando | «por la proximidad de un lecho de río que ofrecía peligro de inundación». Coincide; la lista de trabajos es «cisterna, lechos filtrantes, desarenador y toma» (precisión b) |
| 7915 | 7 | Decreto 6103, considerando | «dada la proximidad de una ala de la base a la barranca del cerro que podía sufrir desmoronamientos en épocas de lluvias». Coincide; la orden suma cuatro rubros, uno de ellos la pintura y el silitón de los muros de piedra, que A:386 no traía (precisión a) |
| 7772 | 8 | Decreto 3033, considerandos | Única proponente en anteriores llamados «para realizar trabajos de idéntica naturaleza»; «necesarios para regularizar un normal abastecimiento de agua potable a la ciudad de Salta e incrementar el sistema de riego de la zona de influencia». Coinciden (A:387, 10:149, C:120) |
| 7909 | 6 | Decreto 6011 | «Defensa s/Río La Caldera», \$4.219.029, «se protegería al pueblo de La Caldera, que se encuentra ubicado en la ribera derecha del río», y el art. 1 autoriza a licitar. Coinciden (A:387, 09:535) |
| 7969 | 5–6 | Decreto 7314 | Obra D-16, Galindo, \$3.555.418, 15,72 %. Coincide (09:535) |
| 7961 | 7 | Decreto 7179, considerando | «se habrían realizado patentamientos de automotores en forma irregular». Coincide (A:388, 15:185, 18:470) |
| 7860 | 7 | Decreto 4850 | «La Caldera-Santa Clara (Límite con la Prov. de Jujuy)», con tilde en el original. Coincide (A:389) |
| 7859 | 11 | Decreto 4837 | «Abra de Lesser Yacone y Laguna». Coincide (A:387) |
| 7932 | 8 | Decreto 6569 | «Embalse en Campo Alegre». Coincide (A:387) |
| 7843 | 12 | Decreto 4474 | «Intendente Municipal» y «Médico Regional», los dos en la hoja 12. Coinciden (18:470, 04:4599) |
| 8204 | 6 | Decreto 2866 | «reconocimientos geográficos para la instauración del Plan de Salud». Coincide (A:390) |
| 8167 | 7 | Decreto 2162 | «…no pueden concurrir a dichos establecimientos por falta de asientos». Coincide (A:390, 26:235); el 2163 de la misma hoja dice «dicho establecimiento», y no es el citado |
| 8114 | 8 | Decreto 1229 | «Construcción Cristo Monumental», «a erigirse en la localidad de La Caldera», «la erección de este monumento constituirá un motivo ponderable de atracción turística». Coinciden (A:391, 21:182) |
| 8180 | 9 | Decreto 2362, contratos | «ya depositados en el lugar de emplazamiento»; Iramain «ejercerá la supervisión general» y Ávila «la dirección técnica necesaria para el armado del taselaje». Coinciden (A:391) |
| 8124 | 8 | Decreto 1408 | «actual Interventor de la Municipalidad de La Caldera». Coincide (A:392) |
| 8178 | 12 | Decreto 2308 | «de su propiedad», «Getsemaní», catastro 1463. Coincide (A:393, 13:248) |
| 8090 | 12 | Decreto 800 | «atento al pedido de los regantes de la zona». Coincide (A:393, 17:281) |
| 8175 | 5 | Ley 4266 | «Sanciona y Promulga con fuerza de LEY»; «Defensas sobre Río La Caldera». Coinciden (A:393, C:122, 09:535) |
| 8161 | 31 | Edicto 31615 | «Andrés Rodó hoy Julio González», con tildes en el original. Coincide (A:394) |

Son **24 citas entre comillas del libro cotejadas en la imagen**, **ninguna con diferencias**, y datos sin comillas en 4 hojas (7783 h20, 7915 h7, 7969 h5–6 y 8180 h9), de donde salen el hallazgo 1 y las precisiones a y b. No se cotejaron: 8070 h7 (393, «Rvdo. Padre Requena de La Caldera»: el reconocimiento no ubicó el renglón), 8099 h27–28 (escritura 279), 7993 h12, 8119 h7, 8124 h27, 8129 h26, 8053 h14–15, 8062 h16, 8109 h18, 8183 h6, 8201 h8 y h11, 8114 h12, 8000 h14, 8027 h9, 8036 h8, 8021 h8, 8147 h5, 7999 h12 y h14, 8047 h20 y h24, 8006 h22, 7988 h10, 7983 h11, 7989 h9 y 8166 h14, ni de 1967 7755 h21–24, 7762 h19–20, 7774 h7 y h12–13, 7803–7806, 7827, 7835, 7876, 7885, 7895, 7908, 7925, 7933, 7964 y los avisos.

### Hallazgos (tres, todos aplicados en la fase 6) y cuatro precisiones

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:385 | «en marzo una orden de servicio de la obra 127 suprime los materiales eléctricos»: la orden de servicio 5 la aprueba la Resolución 706 de Arquitectura del 18 de noviembre de 1966; marzo es el decreto que aprueba la resolución (7783 h20, imagen; la FICHA del informe lo trae bien) | 3 | «una orden de servicio de la obra 127, aprobada por Arquitectura en noviembre de 1966, suprime … y el decreto que en marzo la aprueba manda…» |
| 2 | A:387, 10:149 | «para llamar a licitación a principios de noviembre» y «con vistas a licitar la obra en noviembre»: el contrato del 5539 fija los primeros días de noviembre para **entregar la documentación** del llamado, y ése es el plazo que el 7448 extiende a fin de diciembre | 3 | «para entregar a principios de noviembre la documentación del llamado a licitación»; «con la documentación para licitar la obra a entregar a principios de noviembre» |
| 3 | A:385, 18:531, A:392 | «en diciembre renuncia el suplente», «renuncia en diciembre» (7232) y «En julio Julio González renuncia» (1196): los decretos aceptan renuncias cuya fecha no dan; el mes es el de la aceptación | 3 | «en diciembre se acepta la renuncia del suplente»; «en diciembre se le acepta la renuncia»; «En julio se acepta la renuncia de Julio González» |

Precisiones sin aspecto propio (escala general del 10 y del 1; no bajan la nota): (a) A:386 enumeraba como completos los rubros de la orden de servicio 4 de la base del Cristo y omitía la pintura y el silitón de los muros de piedra (6103, 7915 h7): se agrega «por la pintura de los muros de piedra»; (b) A:385 y 26:235 omitían el desarenador entre los trabajos de la escuela 250 (7012, 7951 h16): se agrega; (c) 26:235 decía que en 1967 se reciben «los edificios de la obra 127»: el 2745 recibe los de las escuelas 160 y 332, como dice A:385; (d) A:394 ponía «en octubre y noviembre» la 58 y la 61 en ese orden, cuando la 61 se aprueba en octubre (2432) y la 58 en noviembre (2814): se invierte el orden; y en 17-aguabaja:281 la canalización del 5983 iba «desde la primera toma del Wierna hasta la junta», sin «la última del Mojotoro» que el decreto nombra: se agrega.

Restan: tres casos en el aspecto 3 (−15). Ninguno en el 7: **0 errores de consistencia en 32,2 páginas** → 100.

**Los tres hallazgos y las cuatro precisiones están en material que la propia auditoría incorporó** (AMPLÍA 1967-1968, `3b5be9e`), y **ninguno fue atrapado por un control automático**. Los controles de P74 (citas literales; esta vez las 24 en la imagen) y P102 (privacidad) funcionaron: ninguna cita difiere del original. Se escaparon tres fechas de un acto dadas por el acto que lo aprueba o lo acepta, que es la falla de la ronda 56 (hallazgo 4) en otra forma, y listas de trabajos recortadas.

**Descartados (falsos positivos, 5).** «La búsqueda laxa devolvió un sumario que el reconocimiento lee "La Galdera"» (F:74): la NOTA de A05 del informe 1967 dice «sólo la difusa», pero el §2 y E.7 del mismo informe registran que la laxa lo devuelve; el libro sigue al §2 (pendiente nuevo P114, sobre el informe). «La empresa que en 1967 había estudiado el vaso» (10:513): el 8164 de 1968 paga intereses por mora a Rodio por los «Sondeos de reconocimiento embalse en Campo Alegre», de modo que el trabajo se hizo. «Ese presidente» (22-prospectiva:144) es el designado en septiembre de 1966, Julio González, como dice 18:470. «En diciembre se rematan … dos lotes» y «en marzo se rematan» (A:389 y 394): es la convención de la cronología para los avisos de remate (seis casos anteriores). Julio González nombrado junto a la suspensión del 7179 (A:388, 18:470): funcionario en su función, con la afirmación atribuida al acto en condicional y el resultado del sumario declarado ausente.

**Pendientes nuevos.** P114 (lee, 1967): en el informe LEE 1967, la NOTA de A05 dice que el sumario «La Galdera» de 7808 h3 lo devuelve «sólo la difusa», contra el §2 (línea 367) y E.7, que dan la laxa y la difusa; corregir la nota. P115 (libro): 10:513 da la capacidad, el espejo, la profundidad y la cota del embalse Campo Alegre, el comienzo de la obra en 1972 y la adjudicataria sin fuente localizable en el párrafo (muestra del aspecto 1 de esta ronda); dar la fuente o marcarla como pedido. P116 (herramientas): extensión de P108 para AMPLÍA (y para la rúbrica AMPLÍA v2): (1) una orden de servicio, una resolución o una renuncia se fecha por su propio acto, y si el decreto no da esa fecha se escribe «se aprueba» o «se acepta», no el verbo del acto aprobado; (2) toda enumeración de trabajos, causas o rubros tomada de un considerando va completa o con «entre otros».

**Pendientes revisados sin cerrar.** P54 (1967-1968 no nombran el establecimiento de salud del pueblo). P100 (1967 y 1968 quedan en barrido con el criterio de F). P109, P110, P111 y P113 (láminas, H y E, pedidos de D y la coincidencia de D'Andrea: fuera del alcance de una ronda de auditoría).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.105/25.105 líneas vigentes en `187bc6d` | 25.070 vigentes, 50 caducas por el AMPLÍA 1967-1968 |
| Superlativos, cierres y ausencias sobre los temas de las fichas de 1967-1968 (Cristo, intervención, Rodio, Campo Alegre, defensas, Borja, cooperadora, Getsemaní, juez y juzgado de paz, Serrey, Lavaque, Chalchanio, Berejnoi, Farfán, Centro Agrario, Bernabé López, Juana Moro, tabaco, coparticipación, Registro Civil, Hurtado, patentamientos, médico zonal, Brandan, Álvarez César, Satué, San Cayetano, Iramain, presupuesto municipal, ordenanza impositiva, escuela 250, Yacones, Gallinato, Lesser), en oraciones que no nombran 1967, 1968 ni un año posterior (repaso de ventana) | 63 coincidencias en el libro entero, todas leídas | Ninguna desmentida por 1967-1968. Conservan su universo: 09:550 (primera defensa de hormigón, 1980), 26:61 (escuela de 1911), 15:50 (renta 1918-1946), 22-prospectiva:142 (archivo temprano), A:369 (Ley 3930) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 326/326 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Recuentos de 1967-1968 (A:385 y 390, F:25–26 y 74, 00:43, 01:119, 02:28 y 97, D:177) contra el §0, el §1, E.2 y el §R de los informes | 2 años | Tramos: 42 + 1 + 11 = 54. Hojas sin mirar en 1958-1968: 306, 364, 262, 764, 290, 734, 577, 347, 171, 69 y 258 (00:43, «entre sesenta y nueve y setecientas sesenta y cuatro»). Páginas faltantes 1964-1968: 128, 37, 65, 111 y 109. 1967: 6.128 + 147 (111 + 36 de la 7780) = 6.275 contra el folio 6.270, con los saltos sin páginas de siete ediciones que E.2 declara (F:74 dice siete). 1968: 6.792 − 21 repetidas + 109 = 6.880 = último folio. Hueco 1969-2012: 44 años. Rovaletti asume el 15 de abril (E.4); los decretos 57 y 58 son del 19: cuatro días. Cierran |
| Aritmética de 1967-1968 | 8 cuentas | 1 − 3.555.418/4.219.029 = 15,729 % (el acto imprime 15,72). 210.135 + 241.732 = 451.867. Siete integrantes de la cooperadora además del presidente y el vicepresidente (9 − 2). 26,25/50 = 7,35/14 = 15,75/30 = 0,525 l/s por ha. 200.000 + 4 × 150.000 = 800.000; 200.000 + 4 × 200.000 = 1.000.000. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 57 | 50 de 246 oraciones con cifra en las 50 líneas | **48/50 con fuente localizable**: 34 con la cita en la oración, 11 declaraciones de cobertura cuya fuente es el apéndice F y 3 de método o inferencia con su remisión; sin fuente, dos oraciones de 10:513 (datos físicos del embalse; obra de 1972 y adjudicataria), texto anterior al AMPLÍA (P115). 96 % → 74 |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 50 líneas (10:513 no da URL) | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 50 líneas, cruzadas con contextos sensibles (P102) | 50/50 líneas | Ningún particular nombrado junto a remate, ejecución, cesantía, pensión o embargo: los remates de 1967 y 1968 van sin nombres de las partes, el subcomisario cesanteado y los pensionados sin nombre. Nombrados: funcionarios (D'Andrea, Rovaletti, Julio González, Gómez, Serrey, Satué, Álvarez César, Brandan, Borja, Durand), los escultores, la contratista, los concesionarios de agua y los que promueven juicios de dominio (como en las rondas 52, 55 y 56) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `3b5be9e` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 873 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 41 entradas; 2 cajas desbordadas, las mismas |

## Ronda 58 — incorporación de dos láminas (02/10/2026)

Tipo: **incorporación** (CORRIGE 3.6), a pedido de Eduardo: series de datos para `mapas_caldera` y láminas para el libro. Base: commit `ea71712` de `ediedrich/dispositivo-caldereno` (la ronda 57 registrada); parche `ronda-58.patch` (commit `359d4a9` en la sesión; aplica con `git am` sobre `ea71712`, probado en un clon limpio de GitHub: árbol `bf0f723`). Acompaña un parche de `mapas_caldera` (`mapas_caldera-cobertura-y-agua.patch`, commit `9e72a33` sobre `876f8fb`), que `registrar` no reconoce y se aplica a mano: **el libro nombra dos scripts que sólo están publicados cuando ese parche se sube**. **Denominador: 25.139 líneas** (25.120 + 19: 16 en 17-aguabaja, 2 en 02-metodo y 1 en F).

### Qué se incorporó

| Lámina | Datos | Script | Dónde |
|---|---|---|---|
| `fig:boletin`, rehecha: **1908–2026** en dos paneles | A: `datos/boletin/ediciones_por_anio.csv`, ediciones por año en los *Releases* de `boletines-salta`, copiadas de `estado/estado.json` de `corrige` (actualizado el 02/10/2026 a las 00:10); B: el índice de 1910–1943 de siempre. `estado_lectura.csv` pasa a seguir el apéndice F entero: 1947 y 1949–1957 sobre la imagen, 1948 barrido con lectura parcial, 1958–1968 con hojas sin mirar enteras, 1969–2012 y 2016–2026 puntuales, 2013–2015 por término | `scripts/grafico_boletin.py` | 02-metodo:33–44 (epígrafe nuevo); F:195 |
| `fig:aguaserie`, **nueva**: los actos sobre derechos de agua del departamento, 1951–1968, y el municipio | `datos/agua/actos_agua_1951_1968.csv`: dieciocho filas, transcriptas de 16-redes:768–794 y 17-aguabaja:281, con la línea de cada una; 134 actos, ninguno con el municipio; 1956 sin desglose | `scripts/grafico_agua_serie.py` (comprueba que decretos más edictos den el total y que la columna del municipio sume cero) | 17-aguabaja:281 (remisión) y 282–297 (figura); F:196 |

No se hicieron mapas: ningún dato nuevo de 1949–1968 se puede ubicar en el catastro vigente sin inferencia (los catastros de los actos son los de la época, y el libro no afirma su correspondencia con las partidas de hoy).

**Recuentos del aparato que cambian**: 41 → 42 láminas (00:75 dos veces, 00:78, F:94 y F:237); 20 → 21 propias, 9 → 10 gráficos y 17 → 18 reproducibles (00:75, F:133, 136–137, 208, 218–221). La lámina de los actos de agua cuenta como reproducible **una vez subido el parche de `mapas_caldera`**.

### Lectura y controles

La sesión escribió y releyó enteras las **43 líneas** que toca la ronda (F:94, 133, 136–137, 195–196, 208, 218–221 y 237; 00:75 y 78; 02-metodo:33–44; 17-aguabaja:281–297), contra las dos tablas y las dos figuras. Siguen vigentes las 25.096 que no se tocaron: **25.139 de 25.139 (100,0 %)**. Un auditor que no las escribió las leerá en la próxima `MEJORA`, que empieza por este parche.

| Control | Denominador | Resultado |
|---|---|---|
| Filas de `actos_agua_1951_1968.csv` contra el libro | 18/18 | Cada total y cada desglose coinciden con 16-redes y 17-aguabaja; 1956, «tres» sin desglose en los dos capítulos |
| Hitos de la franja inferior de `fig:aguaserie` | 6 actos | 5230-E (Nº 4438), 4655-E (Nº 4412), 9566-E y 9541-E (Nº 5469), 18570-E (Nº 6421), Ley 4032 (Nº 7430) y 800 (Nº 8090), con la cita que les da el libro |
| Ediciones por año contra `estado.json` | 119 años | 103 con *Release* y 16 sin él (1989–2001, 2003, 2004, 2006); 2005 con 123 |
| `control_figuras.py` sobre el libro | 21 láminas propias | 18 con script declarado, 3 sin él (las mismas de siempre, P10) |
| Remisiones, `\pendiente{}`, ítems de D | — | Sin cambios: 52 y 284 |
| Compilación | libro entero, base `ea71712` más este parche, en un clon limpio | 875 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas de antes (una tercera, del ítem nuevo de F, se corrigió antes de compilar la versión entregada) |

**Atrapados por control**: 1 (la caja desbordada del ítem de F, detectada por la compilación y corregida antes de entregar). Nota final (rúbrica, tipo incorporación, sin tope de cobertura y sin aspecto 7): **87,5**, igual a la de la ronda 57; ninguna nota por aspecto cambia, y el aspecto 13 sigue en 94 hasta que se suba `mapas_caldera`.

**Pendientes que cierra** (en la parte de `fig:boletin` de cada uno: marcar los años leídos y extender el título): P37, P44, P51, P55, P60, P69, P75, P81, P88, P95, P103 y P109 quedan **resueltos en su punto sobre `fig:boletin`** y siguen abiertos en lo demás (fig:agua, fig:parajesnom, fig:votado). **Pendientes nuevos**: P117 (fuentes): subir el parche de `mapas_caldera` (`git am` y `git push`), o agregar el repositorio a las fuentes de la sesión para que una sesión pueda subirlo; hasta entonces dos láminas citan un script que no está publicado. P118 (herramientas): `estado.json` da a 1950 `libro.nivel: barrido` y a 1947 y 1949 `imagen`, mientras el apéndice F da 1947 y 1949–1957 leídos sobre la imagen; la lámina sigue a F.

## Ronda 59 — auditoría con fase 6 (02/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1969. Base: commit `44c7495` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1969, sobre `bb9b63c`, la ronda 58), con la fase 6 en `ronda-59.patch` (commit `684723e` en la sesión; aplica con `git am` sobre `44c7495`, probado en un clon limpio de GitHub: árbol `fd0621d`). **Denominador medido: 25.154 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 58 (25.139 de 25.139, sobre `bb9b63c`) se trasladaron por diff a `44c7495`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1969 agrega 15 líneas netas (5 en A, 4 en C, 2 en F, 2 en 06-pdua y 2 en 07-cot) y deja 49 líneas nuevas o modificadas en 24 archivos: caducan 49**, y quedan **25.105 vigentes sobre 25.154 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `44c7495`)

Se leyeron **las 49 líneas caducas, enteras, por la sesión**, sin subagentes (una, F:77, es un renglón en blanco), contra el informe LEE 1969 (`BO-Salta-1969_8218-8461_la-caldera_LEE-1969_2026-10-02.txt`), bajado de `corrige/lee/1969/`: el §0, las 39 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, E.1 a E.4; y el `amplia-1969.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 390, 395–399 | 6 | sesión |
| ape/C-normativa.tex | 123–126 | 4 | sesión |
| ape/D-pedidos.tex | 177, 191–192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 76–77, 79 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/05-tierra.tex | 290 | 1 | sesión |
| cap/06-pdua.tex | 55–56 | 2 | sesión |
| cap/07-cot.tex | 249–250 | 2 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 149, 332 | 2 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 463 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 07-cot:244–252 (la ficha de las leyes 4365 y 4987), A:364 y A:400 (Catalán Arellano en 1963 y en 1970), y las dos láminas de la ronda 58 con sus epígrafes, 02-metodo:30–45 y 17-aguabaja:283–297, contra `img/fig-agua-serie.png` (las dieciocho barras, los ceros del municipio y los seis hitos coinciden con 16-redes y 17-aguabaja: 134 actos). Las demás líneas de la ronda 58 (F:94, 133, 136–137, 195–196, 208, 218–221 y 237; 00:75 y 78) se leyeron sólo en el diff, sin el contexto entero: siguen contando por la ronda 58.

**Esta ronda: 49 líneas nuevas**, 103.737 bytes sobre 2.822.763, que en las 879 páginas de la base equivalen a **32,3 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `44c7495` cae dentro de estos tramos.

Acumulado: 25.105 vigentes + 49 = **25.154 de 25.154 (100,0 %)**. La fase 6 toca 8 líneas, todas dentro de lo leído en esta ronda (A:395 y 398; 01:139; 04:4599; 09:535; 18:470; 21:182; 26:235), y no cambia el largo de ningún archivo: **25.154 de 25.154 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1969 de `boletines-salta`)

Imágenes de los PDF del Release (150 ppp de origen) renderizadas a 300 ppp con PyMuPDF y recortadas por la posición que da un reconocimiento propio con tesseract `eng` sobre la hoja entera, o por cuartos de hoja donde el reconocimiento no ubicó el renglón (8344 h17); cada recorte se miró.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 8281 | 13 | Decreto 4133, art. 1 y firmas | «son para la localidad de Vaqueros, jurisdicción del citado municipio». Coincide (A:396, C:123, 07:249). Firman Rovaletti, Díaz Villalba **y Museli**, como dice C:123; la FICHA del informe da sólo los dos primeros (pendiente P124) |
| 8361 | 18 | Decreto 5928, visto y considerando | «Defensas sobre el Río La Caldera - Zona La Calderilla» y «Que la construcción de las dos defensas en que consiste la obra citada, vendría a proteger la zona de cultivos de La Calderilla, la toma principal y acueductos del lugar». Coinciden (A:398, 09:535); el sujeto de «vendría» es la construcción, no las defensas (precisión a) |
| 8308 | 17 | Decreto 4584, visto | «el volumen de trabajo y el escaso movimiento demográfico que se registra en la misma, no justifica su funcionamiento». Coincide (A:395, C:124, 26:235) |
| 8308 | 12 | Decreto 4574, art. 1 | «ESCUELA "GUSTAVO MARTINEZ ZUVIRIA", de la localidad de El Gallinato», sin tildes en el original. Coincide (A:395, 17-tierrafiscal:463, 26:235) |
| 8332 | 10 | Decreto 5283, art. 1 | «por la acequia Municipal», con mayúscula. Coincide (A:398, 01:139, 17-aguabaja:281) |
| 8424 | 11 | Decreto 6938, art. 1 | «con todo el caudal de la acequia municipal», en minúscula. Coincide (A:398, 17-aguabaja:281) |
| 8421 | 12 | Decreto 6882, art. 1 | Serrey «Intendente Municipal», Álvarez César «Médico Regional», Catalán Arellano «Agricultor», Mogro «Comerciante», Arturo René Fernández en el órgano de fiscalización. Coinciden (A:396, 04:4599, 18:470, 22-prospectiva:144) |
| 8387 | 11 | Decreto 6407, cláusula primera | «I - Estudio de La Caldera y su zona de influencia desde el punto de vista turístico. — II - Plan piloto de desarrollo urbano y vinculación con la estructura general de comunicaciones». Coincide (A:399, 06:56, 21:182) |
| 8387 | 12 | Decreto 6407, planos | «3.1. Zonificación» y «3.4. Delimitación del perímetro urbano». Coinciden (A:399, 06:56) |
| 8225 | 9 | Resolución 647 en el decreto 3253 | \$7.638.730 y «con una disminución del 19% del», con «presupuesto oficial» en el renglón siguiente, que el recorte no alcanzó. Coincide hasta ahí (A:395) |
| 8347 | 7 | Decreto 5603, refuerzos | «Construcción Cristo Monumental en La Caldera», \$3.000.000. Coincide (A:397, 21:182) |
| 8328 | 18 | Licitación privada 3/69 de Vialidad | «En alquiler de un tractor con topadora destinado a la ejecución de trabajos en el camino de acceso al Cristo de La Caldera». Coincide la cita (A:397); se licita el alquiler, no el tractor (precisión b, 21:182) |
| 8340 | 5 | Decreto 5445, visto | «Director del Plan de Salud del Departamento de La Capital y La Caldera». Coincide (A:395, 04:4599) |
| 8234 | 5 | Decreto 3500, visto | «los municipios de: San Lorenzo, Cerrillos, Campo Quijano, Vaqueros…» y «leche procesada». Coinciden (A:396, 07:249) |
| 8344 | 17 | Acta 6 de Lerma S.A.C.I.F.I.M.A. | «Aprobación adquisición "Finca Getsemaní" en La Caldera», «la extensión de la misma, mejoras existentes, agua de riego» y «particularmente por tratarse de zona afectada por la garrapata»; protocolización del 23 de mayo. Coinciden (13:248) |

Son **22 citas entre comillas del libro cotejadas en la imagen** (la de 6407 cuenta tres veces, una por pasaje, y la de 4584 dos, en A y en C), **ninguna con diferencias**, y datos sin comillas en 4 hojas (8281 h13, firmas; 8361 h18, sujeto del considerando; 8328 h18, objeto de la licitación; 8421 h12, oficios), de donde salen el pendiente P124 y las precisiones a y b. No se cotejaron: 8227 h6–7, 8278 h24–25, 8455 h21–22 (Campo Alegre), 8288 h6, 8318 h5 y h15, 8325 h8 y h19–21, 8352 h23–24, 8327 h20, 8338 h9, 8363 h12, 8457 h16 (ordenanzas), 8296 h5–6, 8304 h9–10, 8310 h14 (obra 283), 8308 h11 (distritos), 8317 h14, 8443 h20 (agua), 8351 h8–9, 8353 h7, 8355 h9–10 (hogar), 8320 h15, 8421 h10–11, 8371 h13–14 y h16, 8380 h6, 8392 h6, 8393 h9–10, 8399 h8, 8401 h20–21, 8434 h8, 8444 h17, 8455 h40, 8456 h21, 8460 h4–5, 8346 h8–9, 8364 h24 y 8260 h12.

### Hallazgos (tres, todos aplicados en la fase 6) y cinco precisiones

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:395 | El resumen del año dice que la Provincia «licita una defensa en La Calderilla»; la fila de 1969 de agua y río da la obra D-3/69, «Defensas…», y 01:139, 17-aguabaja:281 y 22-infraestructura:508 dicen «dos defensas», que es lo que dice el considerando del 5928 (8361 h18, imagen) | 7 | «licita una obra de dos defensas en La Calderilla» |
| 2 | A:398, 01:139 | «En ninguno de esos actos figura el municipio» y «el municipio no figura en ninguno de esos actos», en el mismo pasaje que cita «por la acequia Municipal» (5283) y, en A, «con todo el caudal de la acequia municipal» (6938): el municipio figura como nombre de la acequia y no interviene, que es la fórmula de 17-aguabaja:281 para 1958–1960 y para 1969. Contradicción dentro del mismo pasaje | 7 | A: «En ninguno de esos actos interviene el municipio, que figura sólo como nombre de la acequia por la que riegan dos de ellos»; 01: «el municipio no interviene en ninguno de esos actos» |
| 3 | A:395 | «el 21 de agosto renuncia Hugo Alberto Rovaletti y deja el mando»: el decreto 6262 del 21 de agosto pone en posesión del mando al ministro «con motivo de la renuncia», cuya fecha no da (E.4 del informe). Es la falla de la ronda 57 (hallazgo 3, P116): la fecha del acto que acepta o ejecuta dada como la del acto aceptado | 3 | «el 21 de agosto, por su renuncia, Hugo Alberto Rovaletti pone en posesión del mando al ministro de Gobierno» |

Precisiones sin aspecto propio (escala general del 4, del 10 y del 12; no bajan la nota): (a) 09:535 ponía «cuyas dos defensas, según el decreto, «vendría a proteger…»», con un plural que concuerda con la cita en singular: en el original el sujeto es «la construcción»; pasa a «cuya construcción, en dos defensas, según el decreto «vendría a proteger…»»; (b) 21:182 decía que la Provincia «licita un tractor con topadora»: Vialidad licita su alquiler (8328 h18); (c) 04:4599 decía que en 1969 Álvarez César es «ya «Médico Regional»», cuando el mismo párrafo cita el 4474 de 1967 que ya lo llama así: «otra vez»; (d) 26:235 decía que el cese de la oficina de Vaqueros rige «a partir del mismo día», sin que el párrafo dé la fecha del 8365: «a partir del día de aquel decreto, el 29 de febrero de 1968»; (e) 18:470: el inciso de 1969 sobre Arturo René Fernández y Arturo Fernández cortaba la oración «Arturo René Fernández, a quien…, coincide con el de su presidente»: va entre rayas.

Restan: un caso en el aspecto 3 (−5) y dos errores de consistencia en el 7: **2 en 32,3 páginas = 6,2 por cada 100** → escalón de ≤ 8 (40), y uno más abajo porque el hallazgo 2 contradice material del mismo pasaje → **30**. Los dos se aplicaron: 100 en la nota final.

**Los tres hallazgos y las cinco precisiones están en material que la propia auditoría incorporó** (AMPLÍA 1969, `44c7495`), y **ninguno fue atrapado por un control automático**. Los controles de P74 (citas literales: las 22 cotejadas coinciden) y P102 (privacidad) funcionaron. Se escaparon un resumen de año que no repite lo que dicen sus filas (hallazgo 1), una fórmula de ausencia que el propio pasaje desmiente (hallazgo 2) y otra fecha de un acto tomada del que lo ejecuta (hallazgo 3, la regla 1 de P116 todavía no corre como control).

**Descartados (falsos positivos, 5).** «Firman Rovaletti, Díaz Villalba y Museli» (C:123): la FICHA del informe no trae a Museli, pero la imagen sí (8281 h13). «Un año antes de la ley, la localidad de Vaqueros era todavía del municipio de La Caldera» (07:249): la Ley 4365 de 1970 la crea, y el 4133 la llama «jurisdicción del citado municipio»; el 3500 que la llama municipio está dicho en la misma oración. «Los expedientes … son de 1955 y de 1948, y las resoluciones … de 1957 y de 1960» (17-aguabaja:281): A15 y A33 dan la Res. 1208 del 7-11-1957 y la 684 del 1-6-1960. «La serie entera, de 1951 a 1968» (17-aguabaja:281): el universo está declarado, y la frase nueva pone 1969 «fuera de la lámina». «Lo firma el gobernador interino» (C:125): el 6407 es del 28 de agosto, con Díaz Villalba interino del 21 al 29 (E.4).

**Pendientes que cierra.** **P117**: el parche de `mapas_caldera` está subido (commit `a027898`, «Lámina de cobertura 1908-2026 y serie de actos de agua 1951-1968»; `scripts/grafico_boletin.py` y `scripts/grafico_agua_serie.py` en el repositorio público).

**Pendientes nuevos.** P123 (herramientas): extensión de P116 para AMPLÍA (y rúbrica AMPLÍA v2): (1) la fórmula «no figura el municipio» no se usa en un pasaje que cita una «acequia municipal» o «del Pueblo»: se escribe «no interviene» y se dice que figura como nombre; (2) la línea de resumen de una fila de año se coteja por script contra las filas de detalle del mismo año (números, cuántas obras, cuántas ordenanzas); (3) un cambio de gobernador se fecha por el decreto de traspaso y la renuncia no se fecha si el decreto no la fecha. P124 (lee, 1969): corregir el informe LEE 1969 A04: el 4133 lo refrendan Rovaletti, Díaz Villalba y Museli (8281 h13, imagen), y el TEXTO da sólo los dos primeros.

**Pendientes revisados sin cerrar.** P54 (1969 tampoco nombra el establecimiento de salud del pueblo). P100 y P118 (1969 queda en barrido con el criterio de F, como dice `amplia-1969.json`). P115 (10:513 sigue sin fuente). P119, P120, P121 y P122 (láminas, H y E, pedidos de D y correcciones del informe LEE 1969: fuera del alcance de una ronda de auditoría).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.139/25.139 líneas vigentes en `bb9b63c` | 25.105 vigentes, 49 caducas por el AMPLÍA 1969 |
| Superlativos, cierres y ausencias en las líneas agregadas por el AMPLÍA (*el único*, *la única*, *el primero*, *la primera*, *por primera vez*, *el más*, *nunca*, *jamás*, *ningún*, *ninguna*, *no aparece*, *no consta*, *tampoco*) | 93 coincidencias en las 49 líneas (casi todas en texto anterior de las líneas modificadas), todas leídas | Una desmentida por el propio pasaje (hallazgo 2). «El primero» de 05:290, A:395 y 04:4599 es el orden del artículo del 7557 y del 4572; «el primer intendente de Vaqueros» remite a la fila de 1970; las demás conservan su universo («lo hallado del año», «los actos hallados») |
| Repaso de ventana: afirmaciones que cierran en 1968 (*a 1968*, *--1968*, *hasta 1968*, *1949 a 1968*, *1958 a 1968*, *1961 a 1968*, *1964 a 1968*, *1951 a 1968*) | 7 coincidencias en el libro entero, todas leídas | Ninguna desmentida: 00:75 y 17-aguabaja:281–291 son la lámina, que declara su universo 1951–1968; 04:4599 y F:76 nombran los años |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 326/326 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Recuentos de 1969 (A:395, F:25–26 y 76, 00:43, 02:28 y 99, 01:119, D:177) contra el §0, E.1, E.2 y el §R del informe | 1 año | Tramos: 42 + 1 + 12 = 55. Hojas sin mirar en 1958-1969: 306, 364, 262, 764, 290, 734, 577, 347, 171, 69, 258 y 191 (00:43, «entre sesenta y nueve y setecientas sesenta y cuatro»). Páginas faltantes 1964-1969: 128, 37, 65, 111, 109 y 75. 1969: 6.928 − 47 repetidas + 75 = 6.956 = último folio; 18 + 27 = 45 de las 75 en la 8337 y la 8365. Capa útil: 110 hojas en 5 ediciones; segunda versión en 10; 38 hojas a 300 ppp. Hueco 1970–2012: 43 años. Cierran |
| Aritmética de 1969 | 7 cuentas | 9.430.531 × 0,81 = 7.638.730,11. 95.764 + 64.045 + 464.910 = 624.719. 1,5 × 0,525 = 0,7875 (0,79); 2 × 0,525 = 1,05; 1 × 0,525 = 0,525; 3 × 0,525 = 1,575. Tres vehículos en la 109 (2 + 1). Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 59 | 50 de 232 oraciones con cifra en las 49 líneas | **50/50 con fuente localizable**: 37 con la cita en la oración o en la anterior del mismo período, 9 declaraciones de cobertura cuya fuente es el apéndice F, 2 recuentos de 17-aguabaja con la lámina y su planilla, y 2 de inferencia con su remisión. 100 % → 90 |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 49 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 49 líneas, cruzadas con contextos sensibles (P102) | 49/49 líneas | Ningún particular nombrado junto a remate, ejecución, cesantía, jubilación o embargo: el remate del catastro 116 va sin las partes, la encargada del Registro Civil sin nombre, la jubilada y el camión de A24 no entran. Nombrados: funcionarios (Rovaletti, Díaz Villalba, Ponce Martínez, Serrey, Álvarez César), los concesionarios y peticionarios de agua (como en las rondas 52 y 55 a 57), el arquitecto contratado y los integrantes de la cooperadora asistencial con el oficio que da el decreto |
| `mapas_caldera` | 2 scripts que el libro cita desde la ronda 58 | publicados en `a027898` (P117) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `44c7495` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 879 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

## Ronda 60 — auditoría con fase 6 (02/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1970-1972. Base: commit `d628fd6` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1970-1972, sobre `5533413`, la ronda 59), con la fase 6 en `ronda-60.patch` (commit `074fadf` en la sesión; aplica con `git am` sobre `d628fd6`, probado en un clon limpio de GitHub: árbol `55f57fb`). **Denominador medido: 25.176 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 59 (25.154 de 25.154, sobre `5533413`) se trasladaron por diff a `d628fd6`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1970-1972 agrega 22 líneas netas (11 en A, 9 en C y 2 en F) y deja 71 líneas nuevas o modificadas en 26 archivos: caducan 49 líneas anteriores**, y quedan **25.105 vigentes sobre 25.176 (99,7 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `d628fd6`)

Se leyeron **las 71 líneas, enteras, por la sesión**, sin subagentes (una, F:79, es un renglón en blanco): las nuevas de A y C completas en el diff por palabras, y las modificadas del resto en su texto entero, no sólo en el fragmento cambiado. Se cotejaron contra los tres informes LEE (`BO-Salta-1970_8462-8701_la-caldera_LEE-1970_2026-10-02.txt`, `BO-Salta-1971_8702-8942_la-caldera_LEE-1971_2026-10-02.txt` y `BO-Salta-1972_8943-9180_la-caldera_LEE-1972_2026-10-02.txt`, bajados de `corrige/lee/<año>/`): §0, las 143 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, E.1 a E.10 y §R de cada uno; y el `amplia-1970-1972.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 315, 364, 380, 396, 400–413 | 18 | sesión |
| ape/C-normativa.tex | 98, 103, 127–135 | 11 | sesión |
| ape/D-pedidos.tex | 177, 191–192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 78–79, 81 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/03-fincas.tex | 1010 | 1 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/05-tierra.tex | 290 | 1 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/07-cot.tex | 249, 251 | 2 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 18, 149, 332, 513 | 4 | sesión |
| cap/13-loteo.tex | 248 | 1 | sesión |
| cap/14-poblacion.tex | 517 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 463 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 03:1009 (el comienzo de la oración de 03:1010), 10:14–40 (la ficha de la Ley 4486, contra las superficies dudosas del informe 1972: 167,4139, 1,8036 y 363,0718 son compatibles con 4.13[8?],82, 8.03[?],[?] y 3[6?]3 ha 0717,6[6?], y suman 686,1871), la fila de 1967 de A:387 (Carmelo Galindo, contratista de la defensa del pueblo de 1967, que A:403 nombra por su reajuste de 1970) y las líneas de 14-poblacion con la cifra de 2022 (12.299: 12.299 / 3.671 = 3,35 → «3,4»; 12.299 / 2.831 = 4,34 → «4,3»).

**Esta ronda: 71 líneas nuevas**, 145.082 bytes sobre 2.869.431, que en las 891 páginas de la base equivalen a **45,1 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `d628fd6` cae dentro de estos tramos.

Acumulado: 25.105 vigentes + 71 = **25.176 de 25.176 (100,0 %)**. La fase 6 toca 15 líneas, todas dentro de lo leído en esta ronda (A:400, 402, 405, 409 y 410; C:134; D:177; F:78; 04:4599; 07:251; 10:149 y 513; 17-aguabaja:281; 21:182; 22-infraestructura:508), y no cambia el largo de ningún archivo: **25.176 de 25.176 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1970, 1971 y 1972 de `boletines-salta`)

Imágenes de los PDF del Release (150 ppp de origen en 1970 y 1971; 96 ppp en las hojas de 1972 miradas) renderizadas a 100–300 ppp con PyMuPDF (600 en la 9040 h5), primero la hoja entera y después el recorte del renglón; cada recorte se miró. Se bajaron 33 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 8929 | 25 | Decreto 2486, art. 1 | Tres publicaciones de «Democracia», cada una con su fecha: «Otra Riqueza Salteña…, el día 11 de setiembre/71», «Reactivación de las Obras Públicas Municipales…, el día 31 de agosto de 1971» y «Iniciación de Obras de Construcción del Dique Campo Alegre, el 1º de setiembre de 1971». La cita coincide (A:409, 10:149); **el 1.º de septiembre es el día en que aparece el aviso, no una fecha de comienzo que el aviso anuncie** (hallazgo 1) |
| 8860 | 11–12 | Ordenanza impositiva 1971 (decreto 370), art. 74 y radio urbano | «de los ríos del Municipio, o sea de los ríos Wierna, La Caldera y Mojotoro» coincide (A:406, 07:251, C:130). En h12, col. 1: «La avenida General Martín Miguel de Güemes desde el comienzo del loteo del Ing. Martell» y «Calle Cristo Redentor… hasta el monumento al Cristo y las lomas de Getsemaní que están al frente»: coinciden (13:248); no están en el TEXTO del informe 1971, cuyo B.4 da a Getsemaní dos apariciones en el año (pendiente P129) |
| 8842 | 13 | Decreto 939, considerando y art. 1 | «Que a la subasta se presentó como único proponente la Empresa Sollazzo Hnos. S.A.» y «Embalse Campo Alegre - Etapa "A" - Departamento de La Caldera (Salta)». Coinciden (A:409, 10:149); el informe tenía el considerando sólo en la capa |
| 8714 | 13 | Decreto 1279, considerando y art. 3 | «tiende a solucionar el agudo problema de provisión de agua potable a la Ciudad de Salta, localidades aledañas y del Departamento de General Güemes» y la serie de inversiones hasta 1975. Coinciden (A:409, 10:149, C:127) |
| 8768 | 5 | Decreto 2051, considerando y art. 1 | «per- / tenecía y estaba atendida por la Municipalidad de La Caldera», «de la jurisdicción que ahora se desmembra», «en forma provisoria», 66,67 y 33,33, 22 de marzo. Coinciden (A:406, 07:249, 15:185, C:128) |
| 8773 | 13 | Decreto 2161, considerando | «se preve su iniciación en breve plazo» y «debe impedirse el uso discrecional de las mismas y su fraccionamiento arbitrario». Coinciden (A:407, 06:56) |
| 8928 | 12 | Decreto 2447 y ordenanza 173 | «LA CALDERA, es un pueblo aut nticamente histórico y colonial» (falla de impresión, P128) y «reemplazándose las pantallas comunes con faroles de tipo colonial». Coinciden (06:56, C:132) |
| 8991 | 14 | Ordenanza 1 de Vaqueros (decreto 3677), art. 81 | «de los ríos del municipio o sea de los ríos Wierna, La Caldera y Mojotoro» y «citados ríos del Municipio de La Caldera». Coinciden (A:411, 07:251, C:133) |
| 9040 | 5 | Ley 4474, art. 1 | La imagen (96 ppp, recorte a 600) dice «estará circunscripto al actual éj'do del mu- / nic'p'o de la citada localidad»: **«éjido», con tilde, y «municipio», con minúscula**; A:410 y C:134 citaban «ejido del Municipio» (hallazgo 4) |
| 9152 | 6 | Decreto 6307, art. 1 | «con atención de las localidades de La Caldera, La Calderilla y Vaqueros». Coincide (A:410, 04:4599, C:135) |
| 8671 | 11 | Resolución 149, art. 1 | «el Consultorio Externo de La Caldera» (el visto dice «de la Caldera»). Coincide (A:400, 04:4599, 21:87) |
| 8931 | 10 | Decreto 2530, considerando | «el sistema de captación de agua corriente y a la propia localidad de La Caldera», y «margen derecho» en el original. Coincide (09:535) |
| 8585 | 15 | Decreto 9372, visto | La Municipalidad «eleva terna para la designación de Juez de Paz Titular»: la terna de A:400 vale también para Avilés |
| 8785 | 12–15 | Decreto 2378, plan de Vialidad 1971 | El acceso al Cristo tiene \$30.000 en «5) Fondos de Administración Central» del plan de contado (h13) y \$170.000 en el mismo fondo del «Plan Financiado» (h15), con la misma estructura que el dique: 21:182 decía «da a Vialidad \$200.000» (precisión e) |
| 8758 | 15–16 | Aviso 6372, postergación de la licitación del embalse | Lleva la nueva apertura al 5 de mayo de 1971; A:409 y 10:149 citaban sólo el llamado del 31 de marzo (aviso 5836) para la apertura del 5 de mayo (precisión b) |
| 9178 | 13 | Decreto 6866, considerando | «el reacondicionamiento total de la red distribuidora de agua corriente, con previsión a un crecimiento vegetativo por un período de 20 años, sumada a la zona de influencia del dique Campo Alegre». Coincide (A:410, 22-infraestructura:545; el informe lo tenía en la capa) |

Son **39 citas entre comillas del libro cotejadas en la imagen** (20 distintas, contadas una vez por pasaje), **una con diferencias** (la de la Ley 4474, en dos pasajes), y datos sin comillas en 5 hojas (8929 h25, el sentido de la fecha; 8585 h15, la terna; 8785 h13 y h15, el acceso al Cristo; 8758 h15–16, la postergación; 9178 h13, la red de agua). No se cotejaron: 8546 h12 (8641 a 8643), 8616 h23 (563), 8620 h16 y 8690 h14–15 (D-3-69), 8622 h8 y 8700 h12 (iluminación), 8628 h5–6 (22), 8660 h15 (censo), 8712 h29 y 8750 h16 (Getsemaní en 1971), 8715 h14 (1335), 8743 h5 (1797), 8811 h15, 8815 h9, 8817 h14–16, 8823 h13, 8883 h5, 8887 h8, 8892 h11, 8893 h27, 8899 h22, 8907 h8–9, 8910 h20–23, 8925 h6–9, 8957 h11–12, 9007 h9 y h11–12, 9011 h13–14, 9031 h7, 9055 h8, 9058 h13, 9059 h5–6, 9072 h9, 9077 h9–10, 9087 h5, 9089 h8, 9092 h10–11, 9099 h12, 9119 h9–12, 9122 h15, 9140 h38, 9141 h19, 9143 h11, 9148 h18, 9154 h12, 9155 h16–17, 9158 h15, 9161 h21–22, 9167 h5, 9171 h15 y h17, 9176 h21, 9179 h11–12, 9180 h12.

### Hallazgos (cuatro, todos aplicados en la fase 6) y seis precisiones

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:409, 10:149, 10:513 | «La única fecha de comienzo que publica el Boletín es la de un aviso pagado… el 1.º de septiembre» y «el único comienzo de obra que publica el Boletín es el que anuncia un aviso pagado para el 1.º de septiembre de 1971»: el decreto 2486 paga tres publicaciones de «Democracia» y da de cada una el día en que salió (8929 h25, imagen); el 1.º de septiembre es la fecha del aviso, y qué fecha de comienzo anunciaba no consta. La fecha de una publicación dada como fecha del hecho | 3 | A y 10:149: «el Boletín no publica el acta de inicio: sólo el decreto que paga al diario «Democracia» un aviso, «Iniciación de Obras…», aparecido el 1.º de septiembre, sin decir qué fecha de comienzo anunciaba»; 10:513: «del comienzo de obra el Boletín no da más que un aviso de «Iniciación de Obras» aparecido en un diario el 1.º de septiembre de 1971»; F:78: «la fecha en que apareció el aviso» |
| 2 | 04:4599 | «Los de 1970 a 1972 lo nombran otra vez, pero sólo como consultorio»: en el mismo párrafo los de 1961 nombran «el consultorio externo» y se dicen «sin nombrar el establecimiento», y D:191 y 21:87, del mismo AMPLÍA, dicen que los de 1970 a 1972 nombran «sólo un consultorio externo» sin nombrar el establecimiento. Contradicción dentro del mismo pasaje | 7 | «Los de 1970 a 1972 vuelven a nombrar sólo el consultorio» |
| 3 | D:177, F:78 | «seis dígitos de sus superficies» de la Ley 4486 que la imagen no decide: de los seis dígitos entre corchetes del informe 1972 (A19, E.8), cinco son de superficies y uno del número de un plano de expropiación («0013[6?]»). Recuento importado del informe sin rehacerlo sobre la ficha | 3 | «seis dígitos que la imagen no decide, cinco de sus superficies y uno del número de un plano» (D); «seis dígitos de la Ley 4486, cinco de sus superficies y uno del número de un plano» (F) |
| 4 | A:410, C:134 | Cita de la Ley 4474 con dos correcciones silenciosas: «ejido del Municipio» donde el original dice «éjido del municipio» (9040 h5, imagen); el TEXTO del informe 1972 (A18) trae la misma forma | 4 | «…al actual éjido del municipio de la citada localidad» en los dos pasajes |

Precisiones sin aspecto propio (escala general del 1, del 5, del 12 y del 13; no bajan la nota): (a) A:400 y A:405 daban los traspasos de gobernador de 1970 y 1971 sin fuente, el único dato de las dos filas fuera de la muestra que no la tenía: se agregan los decretos 1 de cada serie (Nº 8581, h.\ 9; Nº 8625, h.\ 5; Nº 8790, h.\ 5, por E.4 de los informes); (b) A:409 y 10:149 citaban para la apertura del 5 de mayo sólo el llamado del 31 de marzo: se agrega el aviso de postergación 6372 (Nº 8758, h.\ 16); (c) 17-aguabaja:281 llamaba «concesión» al edicto 12751, que publica un pedido: «un pedido de concesión temporal-eventual»; (d) A:402 titulaba «El Cristo, iluminado» una fila que sólo trae legajo, licitación y adjudicación: «La iluminación del Cristo»; (e) 21:182 decía que en 1971 la Provincia «da a Vialidad \$200.000 para el acceso»: el plan de Vialidad asigna \$30.000 de contado y \$170.000 financiados (8785 h13 y h15, imagen); (f) 22-infraestructura:508 había perdido la coordinación («adjudicada en 1967 dos en La Calderilla»), A:410 decía «el archivo no tiene» donde F, 00, 02 y D dicen «el repositorio», y 07:251 llamaba «las dos primeras impositivas» a las primeras posteriores a la ley de 1970: se corrigen las tres.

Restan: dos casos en el aspecto 3 (−10), dos correcciones silenciosas en una cita, en dos pasajes, en el 4 (−6; el aspecto ya está en 90 por cotejo parcial) y un error de consistencia en el 7: **1 en 45,1 páginas = 2,2 por cada 100** → escalón de ≤ 4 (50), y uno más abajo porque contradice material del mismo párrafo → **40**. Los cuatro se aplicaron: 100 en la nota final del 3 y del 7.

**Los cuatro hallazgos y las seis precisiones están en material que la propia auditoría incorporó** (AMPLÍA 1970-1972, `d628fd6`), y **ninguno fue atrapado por un control automático**. Los controles de P74 (citas literales) y P108 (1) (citas con tilde cotejadas en la imagen) no se corrieron como script en el AMPLÍA para la Ley 4474: la cita copia el TEXTO del informe, que ya traía la forma corregida. El de P102 (privacidad) funcionó.

**Descartados (falsos positivos, 6).** «Por terna de la Municipalidad» para los tres jueces de 1970 (A:400): la ficha del 9372 no lo decía, pero la imagen sí (8585 h15). «La impositiva … describe una calle «hasta el monumento al Cristo y las lomas de Getsemaní»» (13:248): no está en el informe, pero la imagen la da (8860 h12). «Dos de ellas decretadas a fines de 1971» (A:411): el 2767 es del 10 de noviembre y el 3677 del 31 de diciembre. «De 1970 a 2022 … por 3,4» (14:517): 12.299 / 3.671 = 3,35. «El contratista de la defensa del pueblo de 1967» (A:403): Carmelo Galindo, como en A:387 y 09:535. «Su primer intendente» (03:1009), que el AMPLÍA cambió por «presidente de la comisión municipal» en A y en 18 y no aquí: la oración sigue diciendo en la línea 1010 que el decreto 135 lo designa presidente, y «intendente» es el nombre que los propios actos de 1971 dan al cargo (1797, A16 del informe 1971).

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P129 (lee, 1970-1972): corregir los informes con lo mirado en esta ronda: 1971 A24 (y P128), la fecha del 2486 es la de aparición del aviso, como las otras dos publicaciones del mismo decreto, y la nota «única fecha de iniciación de la obra en lo leído» cae; 1971 A11, la postergación es el aviso 6372 (8758 h15–16); 1971 A26, el acceso al Cristo queda decidido por la imagen (\$30.000 en el plan de contado y \$170.000 en el financiado de Vialidad, 8785 h13 y h15); 1971 A42 y B.4, Getsemaní aparece una tercera vez en el año, en el radio urbano de la ordenanza impositiva (8860 h12: «las lomas de Getsemaní» y «el loteo del Ing. Martell»); 1972 A18, la Ley 4474 dice «éjido del municipio» (9040 h5). P130 (herramientas): controles para AMPLÍA (y rúbrica AMPLÍA v2), extensión de P123 con la ronda 60: (1) la fecha que da un decreto que paga publicaciones es la de aparición del aviso, nunca la del hecho que el aviso nombra; (2) un recuento de dígitos o lecturas dudosas se describe por lo que es cada uno (superficie, plano, expediente), no por la mayoría; (3) una fecha de apertura postergada se cita con el aviso de postergación; (4) el título en negrita de una fila de año no afirma más que sus actos (una obra adjudicada no está hecha).

**Pendientes revisados sin cerrar.** P54 (los actos de 1970 a 1972 tampoco nombran el establecimiento). P100 y P118 (1970 a 1972 en barrido con el criterio de F, como dice `amplia-1970-1972.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; ningún acto de 1970-1972 los da). P125 a P128 (láminas, H y E, pedidos de D y correcciones de los informes: fuera del alcance de una ronda de auditoría; P128 queda corregido en su primer punto por P129).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.154/25.154 líneas vigentes en `5533413` | 25.105 vigentes, 49 caducas por el AMPLÍA 1970-1972 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*el único*, *la única*, *único*, *única*, *el primero*, *la primera*, *el primer*, *por primera vez*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*), sobre 8.173 palabras agregadas | 30 coincidencias, todas leídas | Una cae (hallazgo 1, «la única fecha de comienzo» y «el único comienzo de obra»); una lleva universo implícito (07:251, «las dos primeras impositivas», precisión f); «el primer renglón de expropiación del embalse que la lectura halla» (A:407) declara su universo; «única proponente» y «único proponente» son del considerando del 939; las demás conservan su universo («lo hallado», «ningún acto hallado del año») |
| Repaso de ventana: afirmaciones que cierran en 1969 (*a 1969*, *hasta 1969*, *--1969*, *1958 a 1969*, *1961 a 1969*, *1964 a 1969*, *1949 a 1969*) y que abren el hueco en 1970 (*1970--2012*, *1970 a 2012*, *de 1970 en adelante*, *cuarenta y tres años*, *cincuenta y cinco tramos*, *los trece*, *y doce*) | libro entero | Quedan dos, las dos correctas: 21:87 («hasta 1969», seguido de 1970 y 1972 en la misma oración) y F:78 («como 1958 a 1969»); las demás coincidencias son otros trece y otros cincuenta y cinco (partidos de 1909, localidades de 1919, ediciones de 1946) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente) | 328/328 `\ref{cap:…}` de un capítulo a uno posterior (326 en la ronda 59, más dos del AMPLÍA en 01:139) | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Recuentos de 1970-1972 (F:25–26 y 78, 00:43, 02:28 y 99, 01:119, 04:3659–3660, D:177, A:400, 405 y 410) contra el §0, E.1, E.2 y el §R de los informes | 3 años | Tramos: 42 + 1 + 15 = 58; fuera de las ventanas, 1948 y 1958-1972 = 16. Hojas sin mirar 1961-1972: 764, 290, 734, 577, 347, 171, 69, 258, 191, 132, 211 y 545 (00:43, «entre sesenta y nueve y setecientas sesenta y cuatro»: cierra). Páginas faltantes 1964-1972: 128, 37, 65, 111, 109, 75, 32, 18 y 104. Cadenas: 1970, 6.858 − 2 repetidas + 32 = 6.888; 1971, 8.109 − 3 + 18 = 8.124; 1972, 8.157 + 104 + unas 140 de las cuatro ausentes ≈ 8.404. Ediciones: 8462–8701 = 240; 8702–8942 = 241 − 1 = 240; 8943–9180 = 238 − 4 = 234. Hueco 1973–2012: 40 años. Seis dígitos dudosos de la Ley 4486: cinco de superficie y uno de plano (hallazgo 3) |
| Aritmética de 1970-1972 | 14 cuentas | 81.105,94 − 44.137,49 = 36.968,45 (45,6 %). 1.500.000 + 3.500.000 + 1.783.257 = 6.783.257. 51.507 / 73.282,41 = 0,7029. 13.898,76 / 15.443,06 = 0,900. 11.148.148,69 / 8.186.398,01 = 1,362. 9.000 + 11.713 = 20.713; 4.000 + 24.258 = 28.258. 117.389,16 / 81.463,68 = 1,441; 149.868,73 / 81.463,68 = 1,840. 4.110.000 / 12.817.000 = 0,32. 66,67 + 33,33 = 100. 30.000 + 170.000 = 200.000. Superficies de la Ley 4486: 686,1871. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 60 | 50 de 354 oraciones con cifra en las 71 líneas | **49/50 con fuente localizable**: 37 con la cita en la oración o en la anterior del mismo período, 9 declaraciones de cobertura cuya fuente es el apéndice F, 3 de texto anterior con su fuente en el párrafo; sin fuente, los traspasos de gobernador de A:405 (precisión a, aplicada). 98 % → 82 en la inicial; 50/50 después de la fase 6 |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 71 líneas (el aviso de «Democracia» llega por el decreto que lo paga) | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 71 líneas, cruzadas con contextos sensibles (P102) | 71/71 líneas | Ningún particular nombrado junto a remate, ejecución, sumario, cesantía, jubilación, rescisión o embargo: los remates de la finca Mojotoro, Potrero de Gallinato, el lote 77, San Antonio o San Roque y Villa Urquiza van sin las partes; el enfermero sumariado, la empleada del hogar, las encargadas del Registro Civil y los interventores de la guardería, sin nombre. Nombrados: funcionarios (gobernadores, Serrey, Lizondo, Catalán Arellano, jueces de paz), contratistas (Moyano, Marcuzzi, Galindo, Sollazzo Hnos., Clitori Hnos.) y sociedades (Lerma S.A., Cuesta del Obispo S.A.) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `d628fd6` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 891 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

## Ronda 61 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1973-1974. Base: commit `d99ba07` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1973-1974, sobre `b21a592`, la ronda 60), con la fase 6 en `ronda-61.patch` (commit `498ee5b` en la sesión; aplica con `git am` sobre `d99ba07`, probado en un clon limpio de GitHub: árbol `5860f5d`). **Denominador medido: 25.200 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 60 (25.176 de 25.176, sobre `b21a592`) se trasladaron por diff a `d99ba07`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1973-1974 agrega 24 líneas netas (9 en A, 11 en C, 2 en F y 2 en 08-vaqueros) y deja 66 líneas nuevas o modificadas en 24 archivos: caducan 42 líneas anteriores**, y quedan **25.134 vigentes sobre 25.200 (99,7 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `d99ba07`)

Se leyeron **las 66 líneas, enteras, por la sesión**, sin subagentes (dos, F:81 y 08:23, son renglones en blanco): las nuevas de A, C, F y 08 completas, y las modificadas del resto en su texto entero, no sólo en el fragmento cambiado. Se cotejaron contra los dos informes LEE (`BO-Salta-1973_9181-9415_la-caldera_LEE-1973_2026-10-02.txt` y `BO-Salta-1974_9416-9654_la-caldera_LEE-1974_2026-10-02.txt`, bajados de `corrige/lee/<año>/`): §0, §1, las 45 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, E.1 a E.10 y §R de cada uno; y el `amplia-1973-1974.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 414–417, 419–424 | 10 | sesión |
| ape/C-normativa.tex | 99, 105, 136–146 | 13 | sesión |
| ape/D-pedidos.tex | 191–192, 253 | 3 | sesión |
| ape/F-fuentes.tex | 25–26, 80–81, 83 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/03-fincas.tex | 1010 | 1 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/05-tierra.tex | 290 | 1 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/07-cot.tex | 246, 249, 253 | 3 | sesión |
| cap/08-vaqueros.tex | 22–23 | 2 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 61, 332, 362, 372–373, 513 | 6 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 03:1009 (el comienzo de la oración de 03:1010), 08:18–21 (la ficha del Código de Vaqueros con las superficies mínimas por zona), 10:355–371 (el plan de 1980 que 10:362 y 10:372 corrigen), D:177 y F:78 (los dos renglones que la fase 6 toca fuera de las 66 líneas), la fila de 1970 de 18-politica sobre la designación de Lizondo (8641 a 8643) y la de 1958 a 1962 sobre Werfil Gallo.

**Esta ronda: 66 líneas nuevas**, 128.100 bytes sobre 2.907.165, que en las 901 páginas de la base equivalen a **39,7 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `d99ba07` cae dentro de estos tramos.

Acumulado: 25.134 vigentes + 66 = **25.200 de 25.200 (100,0 %)**. La fase 6 toca 10 líneas: ocho dentro de lo leído en esta ronda (A:414, C:145, F:80, 03:1010, 04:4599, 06:56, 09:535 y 18:470) y dos vigentes de rondas anteriores, releídas enteras en ésta (D:177 y F:78), y no cambia el largo de ningún archivo: **25.200 de 25.200 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1973 y 1974 de `boletines-salta`)

Imágenes de los PDF del Release (96 a 200 ppp de origen en 1973; 300 en 1974) renderizadas a 40–300 ppp con PyMuPDF (600 y 1.200 en la 9363 h9), primero la hoja entera y después el recorte del renglón, ubicado con el reconocimiento `eng` de la sesión; cada recorte se miró. Se bajaron 27 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 9363 | 9 | Decreto 1265, VISTO | «a partir del día 3 de mayo ppdo. y mien- / tras se desempéñe como Legislador (Diputado / Provincial)»: **el original imprime «desempéñe», con tilde en la segunda e** (recorte a 1.200 ppp; la capa nativa del PDF lee lo mismo). A:414, 04:4599 y 18:470 citaban «desempeñe» (hallazgo 1). «Murúa», con tilde, no se nombra en el libro |
| 9518 | 5–7 | Ley 4834, art. 1 del convenio, sanción y promulgación | La cita de A:422, 17:281 y 10:513 coincide («destinadas a reforzar la provisión de agua potable a la Ciudad de Salta y al eventual suministro a las demás poblacio- / nes comprendidas en el recorrido del acueduc- / to», con el corte de h5 a h6), y «"ACUEDUCTO EMBALSE CAMPO ALEGRE"». La ley sigue en la h7: «Dada en la Sala de Sesiones … a los veinti- / trés días del mes de mayo», y «Salta, 29 de mayo de 1974 … MIGUEL RAGONE»; la edición es del 31 de mayo. **C:145 daba el 29/05/1974, la promulgación, en la columna de la sanción, y la ley en h.\ 5 y 6** (hallazgo 2) |
| 9346 | 37 | Aviso 15589, Centro Vecinal Vaqueros | «Convocatoria a Asamblea Extraordinaria para el día 17 de setiembre de 1973, a las 18 horas en el local Municipal de Vaqueros», y la cita del punto a). Coinciden (A:416, 22-infraestructura:545); el informe 1973 (B.2.5) daba el local sólo para las dos asambleas ordinarias (falso positivo 1) |
| 9183 | 10 | Decreto 6986, resolución 238 | «por intermedio del Mu- / nicipio de La Caldera» y «Contralor Municipal». Coinciden (A:414, C:136, 07:253) |
| 9195 | 8 | Decreto 7348, considerando | «alimentar el Embalse de Campo Alegre, captando / las aguas de los ríos San Alejo y Santa Rufina / en su confluencia». Coincide (A:415) |
| 9218 | 10 | Decreto 121, arts. 1 y 2 | «Desígnase por un nuevo perío- / do legal de dos años». Coincide (A:414, 18:470) |
| 9276 | 28 | Decreto 753, VISTO | «estas últimas ya no se fabrican». Coincide (A:415) |
| 9289 | 7 | Decreto 80, art. 2 | La lista de renuncias termina en «JULIO CATALAN ARELLANO, Vaqueros.» (A:414, 18:470, 03:1010) |
| 9335 | 10 | Decreto 819, art. 1 | «a partir de la fecha que tome posesión de sus fun- / ciones». Coincide (A:414) |
| 9344 | 18 | Aviso 15547 | «Bernabé Aráoz - Vaqueros, Dpto. La Caldera.» Coincide (A:414) |
| 9380 | 6 | Decreto 1563, considerando | «por razones de índole presupuestario». Coincide (A:416, 22-infraestructura:545) |
| 9384 | 5–6 | Decreto 1599, arts. 2 y 5 del contrato | El art. 2 financia «las obligaciones pen- / dientes … provenientes de las certi- / ficaciones correspondientes a partir del primero / de mayo de 1973, como las obligaciones que / emerjan de futuras certificaciones» en siete tramos, y el 5 dice «la interrupción en la normal entrega de docu- / mentos». Coinciden (A:415, C:141) |
| 9384 | 22 | Aviso 16232 | «compra de / 16 lotes de terreno en el Departamento de / La Caldera (Salta)». Coincide (A:414) |
| 9456 | 17 | Ley 4597, arts. 1 y 2 | «Declárase de interés provincial la / protección de las características urbanísticas, pa- / norámicas y turísticas» y «Vaqueros en el departamen- / to de La Caldera». Coinciden (A:417, 06:56). El inciso b) da a San Lorenzo veinticinco metros y 625 metros cuadrados: 06:56 decía que la ley «fija allí», en las cuatro localidades, quince metros y 450 (precisión b) |
| 9468 | 5 | Decreto 3672, art. 1 | «Construcción del acueducto Campo Ale- / gre y Planta Potabilizadora - Salta». Coincide (A:422) |
| 9477 | 7 | Decreto 2550, considerandos | «Que, por razones de orden económico-finan- / ciero, la Administración … no pudo efectuar la subasta en su oportu- / nidad», y las modificaciones 1) y 2). Coinciden (A:422, C:143); el informe 1974 tenía el considerando sólo en la capa |
| 9536 | 9 | Aviso 18315 | «"Apertura de cau- / ces en el río La Caldera"» y \$1.890.000. Coincide (A:421, 09:535) |
| 9560 | 4 | Ley 4860, arts. 1 y 2 | «el quince por ciento (15%) sobre lo recaudado por el sistema tributario provincial más lo que corresponda por el régimen de coparticipación federal» y el inciso c), «en base al costo por habitante de los servicios públicos prestados por los municipios». Coinciden, sin comillas, con A:423 |
| 9571 | 8 | Decreto 4981 | «Desígnanse por un nuevo período Constitucio- / nal». Coincide (A:421, C:139, 18:470) |
| 9587 | 8 | Decreto 5770 | «"Apertura de cauce con / equipo mecánico sobre río La Caldera, provin- / cia de Salta"», fechado «9-9-70». Coincide (A:421, 09:535) |
| 9613 | 11 | Ley 4987, art. 1 | «y que continúa en dirección Sudeste / para tomar el nombre de río Los Yacones y con- / cluir como río Wierna en su confluencia con el / río La Caldera». Coincide (A:424) |
| 9629, 9630 | 1 | Tapas | Ragone hasta la 9629 (22-11); «MOSQUERA, Interventor Federal» desde la 9630 (25-11). Coincide (A:421, F:80) |

Son **36 citas entre comillas del libro cotejadas en la imagen** (24 distintas, contadas una vez por pasaje; los nombres propios entre comillas ---escuelas, fincas, el hogar, la mina--- no se cuentan), **una con diferencias** (la del decreto 1265, en tres pasajes), y datos sin comillas en 8 hojas (9346 h37, el local; 9518 h7, sanción y promulgación; 9384 h5, el art. 2; 9289 h7, el último renglón del decreto 80; 9560 h4, arts. 1 y 2 de la Ley 4860; 9456 h17, el inciso b) de la Ley 4597; 9477 h7, las modificaciones del legajo; 9629 y 9630, las tapas). Bajadas y no cotejadas: 9223 h14 (7775), 9230 h8–9 (142), 9420 h16–17 (Ley 4735), 9537 h4–5 (2938), 9555 h6 (3996). No se bajaron: las demás ediciones de las 45 fichas, que el libro cita sin comillas.

### Hallazgos (seis, todos aplicados en la fase 6) y tres precisiones

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:414, 04:4599, 18:470 | Cita del decreto 1265 con una corrección silenciosa: «mientras se desempeñe como Legislador (Diputado Provincial)» donde el original imprime «desempéñe» (9363 h9, imagen a 1.200 ppp). El AMPLÍA miró la hoja (P134: «Murúa» con tilde) y no la errata | 4 | «\textit{mientras se desempéñe como Legislador (Diputado Provincial)}» \textit{[sic]} en los tres pasajes |
| 2 | C:145 | La Ley 4834 con la fecha de promulgación, 29/05/1974, en la columna que en el resto del apéndice es la de sanción, sin decir que es la promulgación, y en «h.\ 5 y 6», cuando la sanción (23 de mayo) y la promulgación están en la h.\ 7 (9518 h7, imagen) | 3 | «Ley 4834* & 23/05/1974 & Artículo 1 del convenio, sanción y promulgación leídos sobre el facsímil. Promulgada el 29/05/1974 (Ragone); B.O.\ Nº 9518, h.\ 5 a 7, del 31/05/1974», y «destinados a la ciudad de Salta y, eventualmente, a las poblaciones del recorrido», como dice el convenio |
| 3 | 09:535 | «\textbf{En 1974 la serie suma dos obras}», y la misma oración dice que el decreto de adjudicación de la apertura de cauce «no dice si es la misma licitación»: si no lo es, son tres. Recuento que da por decidido lo que la oración declara abierto | 7 | «\textbf{En 1974 la serie suma dos obras, o tres}» |
| 4 | D:177 | El pedido de las hojas sin mirar, de las páginas faltantes y de otro ejemplar de los archivos truncados se queda en 1972 (hojas de 1961 a 1972, páginas de 1964 a 1972, la 7780), mientras F:80 declara para 1973 y 1974 344 y 181 hojas sin mirar enteras, 157 y 96 páginas faltantes y la 9333 truncada. El AMPLÍA lo dejó en P133 «para no mover el recuento», pero extender un ítem existente no lo mueve | 8 | «las de 1961 a 1974 ---…, 545, 344 y 181…», «de 1964 a 1974 ---…, 104, 157 y 96…» y «y de la 9333, del 23 de agosto de 1973, también truncada, de cuyas dieciséis páginas se rescataron doce y media»; los ítems de D siguen siendo 284 |
| 5 | F:80 | «ninguna biblioteca lo abre», de la 9333: el informe 1973 (§0) probó dos lecturas, la de `lee_auto.py` y la de PyMuPDF en la sesión. Negación universal sobre un universo no medido | 5 | «ni la lectura automática ni la de la sesión lo abren» |
| 6 | 03:1010 | «ejerció entre octubre de ese año y mayo de 1973», texto de la ronda 35 sin fuente, al que el AMPLÍA sumó el decreto 80, que le acepta la renuncia el 4 de junio (9289 h6–7), sin rehacer las fechas: los dos decretos que cita la oración dan el 18 de septiembre de 1970, «a partir de que tome posesión», y el 4 de junio de 1973 | 3 | «ejerció de 1970 a 1973: el decreto 135 del 18 de septiembre lo designa presidente de la comisión municipal a partir de que tome posesión» |

Precisiones sin aspecto propio (escala general del 5 y del 12; no bajan la nota): (a) F:80 decía «En ninguno de los dos años hay un resumen de la Tesorería» de dos años de los que, dos renglones después, «cuentan los hallazgos y no las ausencias»; F:78, del AMPLÍA 1970-1972, lo mismo de tres: los dos pasan a «En lo leído de los … años no hay ningún resumen de la Tesorería», como F:74 y F:76; (b) 06:56 decía que la Ley 4597 «fija allí», en las cuatro localidades, lotes de quince metros y 450 metros cuadrados: San Lorenzo tiene veinticinco y 625 (9456 h17, imagen): «fija en Vaqueros, como en Campo Quijano y en las Termas, … ---en San Lorenzo, veinticinco metros y 625---»; (c) C:145 decía que el acueducto se destina «a la ciudad de Salta y a las poblaciones del recorrido», cuando el convenio dice «eventual suministro»: va en el hallazgo 2.

Restan: dos casos en el aspecto 3 (−10), tres correcciones silenciosas de una cita, en tres pasajes, en el 4 (−9 sobre el techo de 90 del cotejo parcial: 81), un superlativo sin universo en el 5 (−5), un pedido del aparato que no siguió a F en el 8 (−5) y un error de consistencia en el 7: **1 en 39,7 páginas = 2,5 por cada 100** → escalón de ≤ 4 (50), y uno más abajo porque contradice la misma oración → **40**. Los seis se aplicaron: 100 en la nota final del 3, del 5 y del 7, 90 en el 4 y 95 en el 8.

**Los seis hallazgos están en material que la propia auditoría incorporó** (AMPLÍA 1973-1974, `d99ba07`; el 6, en la oración que ese AMPLÍA amplió sobre texto de la ronda 35), y **ninguno fue atrapado por un control automático**. Los controles de P74, P108 (1) y P130 (citas cotejadas en la imagen) se corrieron en el AMPLÍA sobre las citas en mayúsculas y sobre la de la Ley 4834, pero no letra por letra sobre las tildes de una cita en minúsculas; el de P86 (fechas) se corrió sobre las filas de año y no sobre la columna de fecha de C; el de P102 (privacidad) funcionó.

**Descartados (falsos positivos, 8).** «Convoca en el local municipal una asamblea extraordinaria» (A:416): el informe lo da sólo para las ordinarias, pero la imagen lo dice del aviso 15589 (9346 h37). «Las obligaciones pendientes desde el 1.º de mayo se pagan en siete cuotas» (A:415): el art. 2 del contrato habla de las obligaciones pendientes «provenientes de las certificaciones … a partir del primero de mayo de 1973» (9384 h5, imagen). «Le acepta la renuncia a ese presidente» (22-prospectiva:144): el designado en abril de 1970 es Lizondo (18-politica, 8641 a 8643), el mismo al que se le acepta en julio de 1973 (529). «Con quince metros de frente» (08:22): describe la ley de 1973, no la ficha del Código, y la oración siguiente dice que la coincidencia no prueba filiación. «El nombre del que presidió la comisión municipal de La Caldera de 1958 a 1962» (18:470): la misma línea narra el cargo con sus nombres de cada año (intendente, presidente, comisionado interventor). «Casi once hectáreas» (A:422): 3,1368 + 6,3349 + 1,4771 = 10,9489. «En junio la Administración licita» (A:421, 09:535): el aviso está fechado «Salta, junio de 1974» y se publica desde el 1.º de julio; es la fecha del acto. «Ragone hasta el 22 de noviembre y desde el 25 el interventor» (A:421): tapas de la 9629 y la 9630, imagen.

**Pendientes que cierra.** Ninguno entero. P133 queda satisfecho en dos de sus puntos (otro ejemplar de la 9333 y las 157 y 96 páginas faltantes, ahora en D:177).

**Pendientes nuevos.** P136 (lee, 1973-1974): corregir los informes con lo mirado en esta ronda: 1973 B.2.9, el VISTO del 1265 imprime «desempéñe» (9363 h9, imagen a 1.200 ppp; la capa nativa lo lee igual), errata del original para E.9; 1974 B.2.4, la Ley 4834 se sanciona el 23-5-1974 y se promulga el 29-5 (9518 h7: «Dada en la Sala de Sesiones … a los veintitrés días del mes de mayo»; «Salta, 29 de mayo de 1974 … MIGUEL RAGONE, Jesús Pérez»), con la ley en h5 a h7 y no en h5-6; 1973 B.2.5, el aviso 15589 convoca también «en el local Municipal de Vaqueros» (9346 h37). P137 (herramientas): controles para AMPLÍA (y rúbrica AMPLÍA v2), extensión de P135 con esta ronda: (1) toda cita se coteja letra por letra en la imagen, tildes incluidas, aunque esté en minúsculas y aunque la ficha la transcriba corregida (la ficha moderniza: «desempeñe» por «desempéñe»); (2) en el apéndice C la fecha de una ley es la de sanción, que está en el «Dada en la Sala de Sesiones», y la promulgación va aparte; la hoja citada es la de todo el texto, firmas incluidas; (3) un recuento («suma dos obras») no da por decidida una identidad que la misma oración declara abierta; (4) un pedido de D cuyo objeto F extiende a años nuevos se extiende en el mismo ítem, que no mueve el recuento de 22-prospectiva; (5) cuando un AMPLÍA agrega a una oración un acto con fecha, rehace las fechas que la oración ya daba.

**Pendientes revisados sin cerrar.** P54 (1973 y 1974 nombran puestos sanitarios y un médico zonal; ni hospital ni estación). P100 y P118 (1973 y 1974 en barrido con el criterio de F, como dice `amplia-1973-1974.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; ningún acto de 1973-1974 los da: por eso el aspecto 1 sigue en 82, como en las rondas 55, 56, 59 y 60). P131, P132 y P134 (láminas, H y E, correcciones de los informes: fuera del alcance de una auditoría; P134 se completa con P136). P133 (resto de los pedidos de D).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.176/25.176 líneas vigentes en `b21a592` | 25.134 vigentes, 42 caducas por el AMPLÍA 1973-1974 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*el único*, *la única*, *único*, *única*, *el primero*, *la primera*, *el primer*, *por primera vez*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos los*, *todas las*), sobre 6.553 palabras agregadas | 20 coincidencias, todas leídas | Una cae (hallazgo 5, «ninguna biblioteca»); una ausencia sin «lo leído» en un año que no la admite (precisión a, con su gemela de F:78); «el primer año» es ordinal; las demás conservan su universo («ningún acto hallado», «en lo hallado», «ningún dígito que decide un acto del departamento», que el informe 1974 da en E.8) |
| Repaso de ventana: afirmaciones que cierran en 1972 (*a 1972*, *hasta 1972*, *--1972*, *1958 a 1972*, *1961 a 1972*, *1964 a 1972*) y que abren el hueco en 1973 (*1973--2012*, *1973 a 2012*, *1973 en adelante*, *cuarenta años*, *cincuenta y ocho*, *dieciséis quedan*, *quince,*) | libro entero | Queda una que debía cambiar: D:177 (hallazgo 4). Las de *1970 a 1972* de 04:4599, 06:56, 15:185, 17:281 y D:191 son de contenido de esos años; las de *cincuenta y ocho* son otras (explotaciones, puntos de la línea de ribera, un crecimiento del 58 %) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes) | 329/329 `\ref{cap:…}` de un capítulo a uno posterior (328 en la ronda 60, más 07:249) | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1973-1974 (F:25–26 y 80, 00:43, 02:28 y 99, 01:119, 04:3659–3660, 22-infraestructura:545, A:414 y 421) contra el §0, el §1, E.2 y el §R de los informes | 2 años | Tramos: 42 + 1 + 17 = 60; fuera de las ventanas, 1948 y 1958-1974 = 18. Ediciones: 9181–9415 = 235; 9416–9654 = 239 − 1 (9503) = 238. Hojas: 640 + 6.116 = 6.756; 5.516 de edición. Hojas sin mirar: 344 y 181, dentro de «entre sesenta y nueve y setecientas sesenta y cuatro» (00:43). Páginas faltantes: 157 en 109 ediciones y 96 en 78. 9333: 1 + 11 + ½ = 12½ de 16. Resolución 1974: 5.411 de 5.517 hojas a 270–300 ppp = 98,1 %. Hueco 1975–2012: 38 años. Presidentes del 4981: 13 + 1 = 14; renuncias del 80: 31 + 1 = 32; mesas del 137: 9 + 6 = 15 |
| Aritmética de 1973-1974 | 12 cuentas | 201.592,56 / 121.981,23 = 1,653 (65 %). 7.662.606,58 × 2 = 15.325.213,16. 18.851.203,40 / 15.325.213,16 = 1,230 (23 %). 3.238.200 / 1.890.000 = 1,713. 236.399,74 − 122.960,28 = 113.439,46. 0,1284 + 0,0817 + 0,4447 = 0,6548; 0,0642 + 0,0786 + 0,8554 = 0,9982; 0,1284 / 0,0642 = 2; 0,8554 / 0,4447 = 1,92. 861 × 1,3 = 1.119,30; 399 × 1,3 = 518,70; 378 × 1,3 = 491,40; suma 2.129,40. 3,1368 + 6,3349 + 1,4771 = 10,9489 ha. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 61 | 50 de 137 oraciones con cifra en las 66 líneas, sin las que el AMPLÍA no cambió | **50/50 con fuente localizable**: 33 con la cita en la oración o en la anterior del mismo período, 13 declaraciones de cobertura cuya fuente es el apéndice F, 2 con remisión («fila de 1971», «más arriba») a un pasaje que la cita y 2 encabezados de fila o de párrafo cuya cita está en el mismo párrafo. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 66 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 66 líneas, cruzadas con contextos sensibles (P102) | 66/66 líneas | Ningún particular nombrado junto a remate, ejecución, sumario, cesantía, jubilación o embargo: el remate de Villa Urquiza, la posesión veinteañal del catastro 146, el regente cesanteado, el cabo jubilado, el personal del hogar, la encargada del Registro Civil y las auxiliares de enfermería van sin nombre, y el auxiliar de Vaqueros que es diputado, por su cargo y sin nombre. Nombrados: funcionarios (gobernadores, el interventor federal, presidentes de comisión, jueces de paz), contratistas (Sollazzo Hnos., Caminos S.A.), los titulares de las tres fracciones expropiadas por el 2938 (Horizontes S.A., Jaime Durán, Isaac Fernández), como titulares de dominio y no en contexto socioeconómico, y el presidente de El Palenque, como en 1969 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `d99ba07` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 901 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las leyes de 1973-1974 van en pasado; ninguna se da por vigente |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 2 y 6 (−10), aplicados |
| 4 | Fidelidad de transcripción | 7 | 81 | 90 | Tres correcciones silenciosas de una cita (−9); techo de 90 por cotejo parcial |
| 5 | Honestidad epistémica | 12 | 95 | 100 | Hallazgo 5 (−5); las ausencias de la Tesorería, precisión |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 40 | 100 | 1 error en 39,7 páginas (2,5/100 → 50), un escalón menos por la misma oración |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 4 (−5), aplicado; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P131 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | P102 funcionó |

**Nota inicial: 80,7 antes del tope y 80,7 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (3) cerrar con documento alguna de las tesis abiertas, por ejemplo el pedido de competencias de D:253 para 1975-2012: hasta +1,8 en el 10; (4) publicar los scripts que faltan y extender las láminas a 1974 (P131): hasta +0,2 en el 13; (5) cotejar en el facsímil el resto de las citas del libro, con la regla de P137 (1): sube el techo del 4 a 100 y vale +0,7.

**Avance del libro:** 6 de 6 hallazgos resueltos (100 %); compila sin errores ni referencias indefinidas, 901 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1973-1974 la Provincia adjudica la etapa B del embalse, conviene con Obras Sanitarias de la Nación un acueducto para la capital, fija por ley el canon de riego para la Administración y los consorcios y la coparticipación por planilla, y el municipio no interviene en ningún acto de agua), la tutela provincial sobre el fisco municipal (ayudas mensuales por decreto, la ordenanza de Vaqueros aprobada sin publicarse, índices fijados por ley sin los datos que los producen) y la designación provincial de los presidentes de comisión aun después de la convocatoria a elecciones de 1973.

**Calidad de la auditoría.** Cobertura de la ronda: 66 líneas (0,26 %; 39,7 páginas). Cobertura acumulada: 25.200 de 25.200 (100,0 %), con el registro de arriba. Falsos positivos descartados: 8. Recortes: no se cotejaron las citas sin comillas de las 45 fichas fuera de las 8 hojas nombradas, ni la Ley 4735, el 7775, el 142, el 2938 y el 3996, bajados y no mirados; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **6 de 6**, en el AMPLÍA 1973-1974 (`d99ba07`), **0 atrapados por un control automático**.

## Ronda 62 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1975. Base: commit `3b51f00` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1975, sobre `0119431`, la ronda 61), con la fase 6 en `ronda-62.patch` (commit `8afc63d` en la sesión; aplica con `git am` sobre `3b51f00`, probado en un clon limpio de GitHub: árbol `1c1a51f`). **Denominador medido: 25.205 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 61 (25.200 de 25.200, sobre `0119431`) se trasladaron por diff a `3b51f00`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1975 agrega 5 líneas netas (2 en A, 1 en C y 2 en F) y deja 40 líneas nuevas o modificadas en 22 archivos: caducan 35 líneas anteriores**, y quedan **25.165 vigentes sobre 25.205 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `3b51f00`)

Se leyeron **las 40 líneas, enteras, por la sesión**, sin subagentes (una, F:83, es un renglón en blanco): las nuevas de A, C y F completas, y las modificadas del resto en su texto entero, no sólo en el fragmento cambiado. Se cotejaron contra el informe LEE (`BO-Salta-1975_9655-9897_la-caldera_LEE-1975_2026-10-03.txt`, bajado de `corrige/lee/1975/`): §0, §1, §2, las 23 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, E.1 a E.10, §F y §R; y el `amplia-1975.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 425–426 | 2 | sesión |
| ape/C-normativa.tex | 21 | 1 | sesión |
| ape/D-pedidos.tex | 177, 191–192, 253, 406 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 82–83, 85 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/03-fincas.tex | 1010 | 1 | sesión |
| cap/04-siglo.tex | 1625, 3659–3660, 4599 | 4 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/09-defensas.tex | 535 | 1 | sesión |
| cap/10-expropiacion.tex | 332, 513 | 2 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/19-resistencias.tex | 655 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87, 182 | 2 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 04:1615–1624 (Garzón y Pinto en el partido del Potrero de Castillo, de 1908, y la finca «Cerro Nevado» de 1918, que 04:1625 une con el catastro 102), 04:749 («Potrero de Castilla» [sic]), 12-amparo:1133 y 1157 (el barrio Zavaleta, Sabaleta o Zabaleta que cita 21:182), la fila de 1973 de A (A:414: Correa designado en agosto de 1973 y Gallo en Vaqueros en junio) y 18:470 entero (Correa redesignado en julio de 1974 por el 4981). Fuera de las 40 líneas, la fase 6 toca 13 renglones vigentes de rondas anteriores (abajo), releídos enteros en ésta.

**Esta ronda: 40 líneas nuevas**, 116.896 bytes sobre 2.924.813, que en las 905 páginas de la base equivalen a **36,2 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `3b51f00` cae dentro de estos tramos.

Acumulado: 25.165 vigentes + 40 = **25.205 de 25.205 (100,0 %)**. La fase 6 toca 17 líneas: cuatro dentro de lo leído en esta ronda (A:425, A:426, 09:535 y 15:185) y trece vigentes de rondas anteriores (A:409, 04:3755–3756, 04:3932–3933, 04:4166, 04:4529, 10:446–450 y 13:248), y no cambia el largo de ningún archivo: **25.205 de 25.205 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1975 de `boletines-salta`)

Imágenes de los PDF del Release (300 ppp de origen en casi todo el año) renderizadas a 110–250 ppp con PyMuPDF, primero la hoja entera y después el recorte del renglón, ubicado con el reconocimiento `eng` de la sesión; cada recorte se miró. Se bajaron 24 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 9877 | 12 | Decreto 3519 y Ordenanza 3/75 enteros | «al régimen establecido por la ley nacional Nº 13.577 (t.o. por ley Nº 20.324)», «por el que se acuerda a los municipios provinciales la facultad de acogerse a la misma», «Que es de vital importancia para el desarrollo y el saneamiento urbano de este municipio, contar con el apoyo de un organismo especializado y de reconocida eficiencia técnica», «para su conocimiento, aprobación y posterior comunicación al organismo correspondiente», «Interventor Municipal de la Caldera». Coinciden (A:426, 01:139, 18:470, 22-infraestructura:545, C:21). La ordenanza no nombra servicio ni organismo. En la misma hoja, el 3546 del 22-11 pone a Pedrini en posesión del mando: A:425 da «las tapas», que lo traen desde la 9874 (24-11), y es exacto |
| 9667 | 5 | Decretos 2 y 15 | «Aceptase la renuncia del Sr. Eusebio Correa, al cargo de Presidente de la Comisión Municipal de la localidad de La Caldera», y el 15: «al cargo de Presidente de la Comisión Municipal de la localidad de El Bordo». 18:470 dice «la del presidente de la comisión municipal de El Bordo», y es exacto; el informe (§C) daba la renuncia «a la Comisión Municipal» (falso positivo 1) |
| 9692 | 7 | Decreto 92 | «Interventor de la Municipalidad de La Caldera». Coincide (A:425, 18:470) |
| 9784 | 6 | Decreto 1383 | «Juez Titular de Vaqueros (La Caldera)». Coincide (A:425, 18:470) |
| 9808 | 5 | Decreto 1925 | «como enfermera del Consultorio Externo de la localidad de Vaqueros». Coincide (A:425, 04:4599) |
| 9773 | 5 | Decreto 1171 | «para que se construya un "camping" destinado al uso por los señores turistas». Coincide (A:425, 21:182) |
| 9820 | 7 | Decreto 2197 | «Construc. Defensas s/ Río La Caldera - Dpto. La Caldera de A.G.A.S. por $ 654.990,00». Coincide (09:535, A:425) |
| 9826 | 17 | Aviso 22286 | «"Cerro Nevado" o "Potrero de San José" o "de las Nieves" o "Potrero de Castilla", catastro 102 de La Caldera», «Juan Pinto y Lucas Castro Olarte o a sus sucesores». Coinciden (04:1625, 19:655, D:406) |
| 9870 | 7 | Decreto 3274, nómina | «Vaqueros / Terminación Edificio Municipal $ 22.000» y «La Caldera / Construcción Nichos $ 20.000». Coinciden (03:1010, A:425, 15:185) |
| 9864 | 18 y 20 | Decreto 3222 | Vaqueros 1.685.603 − 1.348.579 = 337.024 (h18); La Caldera 1.154.137 − 1.177.249 = −23.112 (h20). Coinciden (A:425, 15:185) |
| 9810 | 5 | Decreto 2026 | «en concepto de anticipo de coparticipación de impuesto, para atender el costo del incremento salarial», La Caldera 30.290 y Vaqueros 25.242. 15:185 y A:425 lo cuentan entre los «pagos» que la Provincia «les da» sin decir que es un anticipo de su coparticipación (precisión a) |
| 9681 | 5 | Resolución 0534 | El considerando nombra «bailes públicos, bares, confiterías, kioscos, carpas, etc.» y la Capital, Cerrillos, Rosario de Lerma y La Caldera. Coincide con A:425 (falso positivo 2) |
| 9802 | 6 | Decreto 1764 | «Werfil Gallo», «José Santiago Catalán». Coinciden (A:425, 18:470) |
| 9853 | 13 | Decreto 3082 | «Centro Vecinal "Dr. Carlos Serrey" - Vaqueros (La Caldera)». Coincide (A:425, 22-infraestructura:545) |
| 9787 | 7 | Decreto 1615, art. 2 | $5.000 al Centro Vecinal «Dr. Carlos Serrey» de Vaqueros. Coincide |

Son **19 citas entre comillas del libro cotejadas en la imagen** (12 distintas, contadas una vez por pasaje; los nombres propios entre comillas ---escuelas, hogar, centro vecinal--- no se cuentan), **ninguna con diferencias**, y datos sin comillas en 6 hojas (9667 h5, 9864 h18 y h20, 9870 h7, 9810 h5, 9787 h7). Bajadas y no cotejadas: 9794, 9817, 9831, 9670, 9678, 9807, 9848, 9715 y 9744 (las demás cifras del año salen de fichas de MODO imagen).

### Control de comillas rectas sobre el libro entero (nuevo en esta ronda)

P142 dejó escrito que con `babel` en castellano una comilla recta compila mal, y el AMPLÍA 1975 corrigió sus dos casos. **Esta ronda corrió el control sobre todo el manuscrito**: un script lista cada `"` del fuente que no va precedido de `` ` `` ni de `\` y mira el carácter siguiente, saltando espacios; una prueba aislada con el preámbulo del libro (`spanish,es-noquoting,es-lcroman`) mostró que `"` seguido ---aun con espacios en medio--- de *a, e, o, A, E, O* da un ordinal volado, de *c, C* da *ç, Ç*, de *i, I, u, U* da diéresis, de *r, R* y de *-, <, >, =, ~, "* se come la comilla. Sobre las 40 comillas rectas del fuente, 18 caen en esa clase; cada una se buscó en el PDF compilado (`pdftotext`) y se miró en la página (PyMuPDF, 200 ppp). **Siete pasajes, con doce de esas comillas, salen deformados en el libro entregado** (hallazgos 2 a 8); las otras seis ---cierres seguidos de `}`--- compilan bien. Las 22 comillas rectas restantes (seguidas de *S, G, V, D, F, L, p, q*, de coma o de punto) compilan como comilla recta: no son un defecto y quedan.

### Hallazgos (ocho, todos aplicados en la fase 6) y dos precisiones

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:426 | «y el decreto-ley no se publica en 1975»: ausencia afirmada sobre un año del que, según la fila de 1975 dos renglones antes y F:82, «cuentan los hallazgos y no las ausencias» (2.308 hojas sin mirar una por una, unas 137 hojas faltantes). El informe la da en E.3 («citado, no publicado en 1975») y el AMPLÍA la llevó sin el universo | 5 | «y el decreto-ley no aparece en lo hallado de 1975» |
| 2 | 04:4166 | La resolución de minas de 1948, «denominada "CALDERA No.\ 1, 2 y 3"», compila «denominada ÇALDERA No. 1, 2 y 3"» | 4 | ``` ``CALDERA No.\ 1, 2 y 3'' ``` |
| 3 | 04:4529 | La misma mina en 1957, «denominada "Caldera 1, 2 y 3"», compila «Çaldera 1, 2 y 3"» | 4 | ``` ``Caldera 1, 2 y 3'' ``` |
| 4 | 04:3755–3756 | «la finca denominada "La Helvecia" con una superficie» compila «"La Helveciaçon una superficie» | 4 | ``` ``La Helvecia'' con ``` |
| 5 | 04:3932–3933 | «la obra "Refecciones y ampliaciones … Escuela Provincial de La Caldera"» pierde la comilla de apertura (`"R`) y queda una de cierre suelta | 4 | ``` ``Refecciones … La Caldera'' ``` |
| 6 | 10:446–450 | Las cinco coordenadas del acueducto tomadas del estudio de ruido (Secretaría de Ambiente): «65°22'32,40"O» compila «65°22'32,40.º», sin el signo de segundos ni la O de oeste, en las cinco filas | 4 | `\textquotedbl{}O` en las cinco |
| 7 | 13:248 | «la "adquisición "Finca Getsemaní" en La Caldera"» del acta de Lerma compila «"Finca Getsemaní.ᵉⁿ La Caldera»: la comilla de cierre seguida de espacio y *e* da un ordinal volado | 4 | ``` ``Finca Getsemaní'' en ``` |
| 8 | A:409 | El decreto 939 de 1971, «Etapa "A" - Departamento», compila «Etapa .ᴬ Departamento»: la *A* como ordinal y las dos comillas perdidas | 4 | ``` ``A'' ``` |

Precisiones sin aspecto propio (escala general del 10 y del 7; no bajan la nota): (a) 15:185 y A:425 decían que la Provincia «les da a los dos, como a los demás, cuatro pagos para los aumentos de sueldo de su personal»: el del decreto 2026 se liquida «en concepto de anticipo de coparticipación de impuesto» (9810 h5, imagen), es decir, adelanta a cada municipio lo que ya es suyo; pasa a «cuatro pagos …, uno de ellos como anticipo de su coparticipación», sin agregar renglones; (b) 09:535 decía «\textbf{Y en 1975 vuelve al río La Caldera}» cuando la misma serie, dos oraciones antes, ya estaba en 1974 sobre el río La Caldera (la apertura de cauces del aviso 18315 y del 5770): pasa a «\textbf{Y en 1975 suma otra sobre el río La Caldera}».

Restan: una ausencia falsa en una frase en el aspecto 5 (−5) y siete citas deformadas por la compilación en el 4 (−21 sobre el techo de 90 del cotejo parcial: 69). Ninguna toca a una sección: no hay tope por alcance. El aspecto 7 no tiene hallazgos en las 36,2 páginas auditadas (100). Los ocho se aplicaron: 100 en la nota final del 5 y 90 en la del 4.

**Errores introducidos por la propia auditoría**: el hallazgo 1 está en el AMPLÍA 1975 (`3b51f00`); el 7, en el AMPLÍA 1969 (`44c7495`), y el 8, en el AMPLÍA 1970-1972 (`d628fd6`); los otros cinco (2 a 6) están en el texto del commit inicial del repositorio (`7cd0477`, 23/09/2026), que reúne las rondas 1 a 35, y git no permite atribuirlos a una ronda. **Ninguno fue atrapado por un control automático antes de llegar al libro**: el control de P142 existía como regla para lo que agrega un AMPLÍA, no como script sobre el libro entero, y por eso los cinco casos antiguos sobrevivieron treinta rondas con el texto leído. Los controles de P86 (fechas), P102 (privacidad) y P137 (1) (citas letra por letra) funcionaron en el AMPLÍA 1975.

**Descartados (falsos positivos, 6).** «La del presidente de la comisión municipal de El Bordo» (18:470): el informe (§C) dice «a la Comisión Municipal», pero el decreto 15 dice «al cargo de Presidente» (9667 h5, imagen). «Los bailes, bares y carpas» (A:425): la resolución 0534 nombra los bares en su considerando, y el art. 1 cierra la lista con «etc.» (9681 h5). «Las tapas dan … a Ferdinando Pedrini desde el 24 de noviembre» (A:425): el 3546 lo pone en posesión el 22 (9877 h12), pero la fila atribuye la fecha a las tapas, y la primera que lo nombra es la 9874. «Le acepta la renuncia» a Correa en 22-prospectiva:144: el presidente designado en agosto de 1973 y vuelto a designar en julio de 1974 es Correa (18:470; 819 y 4981), el mismo del decreto 2. «En cada año quedaron sin mirar enteras entre sesenta y nueve y setecientas sesenta y cuatro hojas que el reconocimiento no pudo leer» (00:43): en 1975 son 204, dentro del intervalo; las 2.308 de poca tinta son otra clase, que F:82, D:177 y A:425 declaran. «Uno casi igual al del partido del cateo de 1908» (04:1625): el partido es el «Potrero de Castillo» (04:1617) y el edicto dice «Potrero de Castilla».

**Pendientes que cierra.** Ninguno entero. P142 queda cumplido en su punto (1) sobre el libro entero, pero el control sigue sin script: va en P144.

**Pendientes nuevos.** P143 (lee, 1975): corregir el informe LEE 1975 con lo mirado en esta ronda: §C, el decreto 15 acepta la renuncia de Domingo Osvaldo Juárez «al cargo de Presidente de la Comisión Municipal de la localidad de El Bordo» (9667 h5), no «a la Comisión Municipal»; E.3, «Decreto Ley 8 del 21-12-1974: citado, no publicado en 1975» pasa a «no hallado en 1975», con la reserva de E.10 (L2 y L5); A.23, transcribir el considerando del decreto «por el que se acuerda a los municipios provinciales la facultad de acogerse a la misma» (9877 h12), que el TEXTO corta con «[...]»; A.14, decir en la FICHA que el pago es «en concepto de anticipo de coparticipación de impuesto» (9810 h5). P144 (herramientas): publicar como script (`control_comillas.py` en `corrige` o junto a `control_recuentos.py`) el control de esta ronda y correrlo como último paso de todo AMPLÍA y de toda ronda MEJORA: (1) en el fuente, toda `"` no precedida de `` ` `` ni de `\` cuyo carácter siguiente, saltando espacios, sea *a, e, o, A, E, O, c, C, i, I, u, U, r, R, y* o *-, <, >, =, ~, "* es un error; (2) en el PDF compilado (`pdftotext`), toda *Ç*, *ç*, *ï*, *ü* o ordinal volado que no esté en el fuente; (3) para segundos de coordenadas, `\textquotedbl{}` y no `"`; y sumarlo a la rúbrica AMPLÍA v2 con P142.

**Pendientes revisados sin cerrar.** P54 (1975 nombra sólo el consultorio externo de Vaqueros; ni hospital ni estación). P100 y P118 (1975 en barrido con el criterio de F, como dice `amplia-1975.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; ningún acto de 1975 nombra el embalse: por eso el aspecto 1 sigue en 82). P138, P139 y P141 (láminas, H y E, correcciones del informe: fuera del alcance de una auditoría; P141 se completa con P143). P140 (resto de los pedidos de D, y la fuente de la identificación de la ley 13.577 como orgánica de Obras Sanitarias de la Nación, que se usa en A:426, 01:139, 17:281 y 22-infraestructura:545).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.200/25.200 líneas vigentes en `0119431` | 25.165 vigentes, 35 caducas por el AMPLÍA 1975 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*el único*, *la única*, *único*, *única*, *el primero*, *la primera*, *el primer*, *por primera vez*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos los*, *todas las*, *no se publica*, *no lo dice*), sobre 3.154 palabras agregadas | 26 coincidencias, todas leídas | Una cae (hallazgo 1, «no se publica en 1975»); «el apellido del primer presidente» es ordinal y está en 03:1010; «no fue siempre fiscal» lo prueba el edicto; las demás conservan su universo («en lo hallado del año», «la lectura no halló», «lo que este libro leyó no lo dice»); «no consta» de 19:655 remite al pedido de D y a 04:1625 |
| Repaso de ventana: afirmaciones que cierran en 1974 (*a 1974*, *hasta 1974*, *--1974*, *1958 a 1974*, *1961 a 1974*, *1964 a 1974*, *1969 a 1974*) y que abren el hueco en 1975 (*1975--2012*, *1975 a 2012*, *1975 en adelante*, *treinta y ocho*, *sesenta tramos*, *diecisiete,*, *dieciocho quedan*, *9.654*) | libro entero | Ninguna queda sin actualizar. Las de *1973 y 1974* de 01:139, 04:4599, 06:56, 15:185, 17:281, 21:87, 26:235 y D:191 son de contenido de esos años; «treinta y ocho de sus cincuenta y siete actos» (00:43) es de 1948 y «treinta y ocho kilómetros cuadrados» (11:223), de una cuenca |
| Comillas rectas que `babel` deforma (arriba) | 40/40 comillas rectas del fuente; 18 de riesgo, cada una buscada en el PDF y mirada en la página | 7 pasajes deformados (hallazgos 2 a 8); después de la fase 6, 0 *Ç* y 0 *ç* en el PDF, y las siete citas compilan con comillas tipográficas |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes) | 333/333 `\ref{cap:…}` de un capítulo a uno posterior (329 en la ronda 61, más 01:139, 15:185, 17:281 y 18:470) | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1975 (F:25–26 y 82, 00:43, 01:119, 02:28 y 99, 04:3659–3660, 20:880–881, 22-infraestructura:545, D:177, A:425) contra el §0, el §1, E.2, E.3, E.10 y el §R del informe | 1 año | Tramos: 42 + 1 + 18 = 61; fuera de las ventanas, 1948 y 1958-1975 = 19. Ediciones: 9655–9897 = 243 − 2 (9696 y 9698) = 241. Hojas: 4.724; a 300 ppp, 4.103. Hojas a ojos: 204 = 164 + 40. Poca tinta: 2.308. Ediciones cortas: 108; hojas faltantes, unas 137, la última en unas 76. Foliatura: 1 a 5.042, tres saltos. Hueco 1976–2012: 37 años. D:177, quince años de 1961 a 1975 y quince cifras; doce de 1964 a 1975 y doce cifras |
| Aritmética de 1975 | 6 cuentas | 1.685.603 − 1.348.579 = 337.024. 1.154.137 − 1.177.249 = −23.112. 5.000 × 4.000 m = 2.000 ha (cateo). 1.700 + 3.300 = 5.000. 13.400 + 30.290 + 12.000 + 21.692 = 77.382 (los cuatro pagos a La Caldera; el libro no da la suma). 9715 a 9724: diez apariciones del aviso 20835 = la 9715 + nueve. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 62 | 50 de 77 cláusulas con cifra en el texto agregado | **50/50 con fuente localizable**: 36 con la cita en la cláusula o en la siguiente del mismo período, 9 declaraciones de cobertura cuya fuente es el apéndice F o el informe que F cita, 3 con remisión a un capítulo que cita, 2 con la cita en la oración anterior de la misma fila o párrafo. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 40 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 40 líneas, cruzadas con contextos sensibles (P102) | 40/40 líneas | Ningún particular nombrado junto a remate, ejecución, sumario, baja, cesantía o embargo: el remate de las matrículas 116 y 117 va sin nombres, la baja policial de Vaqueros (B.2.1) no se incorporó y la enfermera del consultorio va sin nombre. Nombrados: funcionarios (interventores federales, Correa, Xamena, Gallo, Catalán, el juez Guantay), la donante del terreno del camping, como donante y no en contexto socioeconómico, y el apellido de uno de los demandados del catastro 102, que sostiene el argumento de 04 y va con la cautela de que el edicto no dice que sea el de 1918 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `3b51f00` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 905 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | La ordenanza 3/75 y el decreto-ley 8 van en pasado; ninguna norma de 1975 se da por vigente |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas de acto y de publicación separadas (337 y 404 del 31-12-1974; 2773 del 29-9); sin hallazgos |
| 4 | Fidelidad de transcripción | 7 | 69 | 90 | Siete citas deformadas por la compilación (−21); techo de 90 por cotejo parcial; las 19 citas del AMPLÍA coinciden con la imagen |
| 5 | Honestidad epistémica | 12 | 95 | 100 | Hallazgo 1 (−5), aplicado |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 36,2 páginas; la precisión b no es una contradicción |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P138 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | P102 funcionó |

**Nota inicial: 86,3 antes del tope y 86,3 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---por ejemplo, el expediente 53-7158 y el decreto-ley 8 de 1974 que D:253 pide ahora, que dirían qué tomó Obras Sanitarias del municipio---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro, con la regla de P137 (1), y dejar corriendo el control de P144: sube el techo del 4 a 100 y vale +0,7; (5) publicar los scripts que faltan y extender las láminas a 1975 (P138): hasta +0,2 en el 13.

**Avance del libro:** 8 de 8 hallazgos resueltos (100 %); compila sin errores ni referencias indefinidas, 905 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1975, con la Municipalidad intervenida, su única ordenanza hallada la adhiere al régimen nacional de Obras Sanitarias para el saneamiento urbano, y la Provincia aprueba sin el municipio el legajo de unas defensas sobre el río), la tutela provincial sobre el fisco municipal (presupuestos aprobados en noviembre, aportes por decreto y un anticipo de la coparticipación propia) y la designación provincial de las autoridades municipales (un interventor en La Caldera y un presidente en Vaqueros, ninguno electo). La pregunta del capítulo 19 sobre el catastro 102 gana un dato: en 1975 era objeto de un juicio de división de condominio entre particulares.

**Calidad de la auditoría.** Cobertura de la ronda: 40 líneas (0,16 %; 36,2 páginas). Cobertura acumulada: 25.205 de 25.205 (100,0 %), con el registro de arriba. Falsos positivos descartados: 6. Recortes: no se cotejaron las cifras de 9794, 9817 y 9831 (pagos de agosto y septiembre), ni el cateo, la caducidad y el remate, bajados y no mirados (fichas de MODO imagen); el control de comillas cubre las comillas rectas dobles y no las simples; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **8 de 8** en material que incorporaron las sesiones ---1 en el AMPLÍA 1975 (`3b51f00`), 1 en el AMPLÍA 1969 (`44c7495`), 1 en el AMPLÍA 1970-1972 (`d628fd6`) y 5 en el commit inicial (`7cd0477`, rondas 1 a 35)---, **0 atrapados por un control automático**.

## Ronda 63 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1976. Base: commit `1972d59` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1976, sobre `bc41c69`, la ronda 62), con la fase 6 en `ronda-63.patch` (commit `b81be58` en la sesión; aplica con `git am` sobre `1972d59`, probado en un clon limpio de GitHub: árbol `ca53a82`). **Denominador medido: 25.214 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 62 (25.205 de 25.205, sobre `bc41c69`) se trasladaron por diff a `1972d59`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1976 agrega 9 líneas netas (4 en A, 3 en C y 2 en F) y deja 44 líneas nuevas o modificadas en 22 archivos: caducan 35 líneas anteriores**, y quedan **25.170 vigentes sobre 25.214 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `1972d59`)

Se leyeron **las 44 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A, C y F completas, y las modificadas del resto en su texto entero, no sólo en el fragmento cambiado. Se cotejaron contra el informe LEE (`BO-Salta-1976_9898-10143_la-caldera_LEE-1976_2026-10-03.txt`, bajado de `corrige/lee/1976/`): §0, §1, §2, las 37 fichas del §A enteras (FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 a B.4, §C, §P, §D, E.1 a E.10, §F y §R; y el `amplia-1976.json` de `corrige/amplia/`. Para el cateo 8929-V se leyó además la ficha A.7 del informe LEE 1975.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 427–430 | 4 | sesión |
| ape/C-normativa.tex | 43, 149–150 | 3 | sesión |
| ape/D-pedidos.tex | 62, 177, 191–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 84–85, 87 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/07-cot.tex | 249, 251 | 2 | sesión |
| cap/09-defensas.tex | 535, 637 | 2 | sesión |
| cap/10-expropiacion.tex | 332, 513 | 2 | sesión |
| cap/14-poblacion.tex | 579 | 1 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09:636 (el encabezado del párrafo del observatorio pluviométrico que sigue en 09:637), la fila de 1974 de A (A:423, Ley 4860: los tres criterios y los índices 0,6548 y 0,9982 contra los que A:430 y 07:249 comparan) y la de 1975 (A:425, el cateo 8929-V «pedido en agosto de 1974»), C:144 (Ley 4735: sancionada el 7 y promulgada el 19 de diciembre de 1973, la fecha que le da el art. 1 de la Ley 5058) y el orden de `\input` de `main.tex` (26-presencia va antes que 09-defensas: la remisión de 26:235 a `cap:defensas` con «más adelante» es correcta).

**Esta ronda: 44 líneas nuevas**, 127.266 bytes sobre 2.946.811, que en las 909 páginas de la base equivalen a **39,3 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `1972d59` cae dentro de estos tramos.

Acumulado: 25.170 vigentes + 44 = **25.214 de 25.214 (100,0 %)**. La fase 6 toca una línea, D:253, dentro de lo leído en esta ronda, y no cambia el largo de ningún archivo: **25.214 de 25.214 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1976 de `boletines-salta`)

Imágenes de los PDF del Release (300 ppp de origen) renderizadas a 130–250 ppp con PyMuPDF, primero la hoja entera y después el recorte del renglón, ubicado con el reconocimiento `eng` de la sesión; cada recorte se miró. Se bajaron 20 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 9967 | 10 | Decreto 116 (31-3-76) | «al cargo de Interventor de la Municipalidad de La Cal- / dera», «Sub-Oficial Mayor (R) Dn. Armando Fernández». Coincide (A:427, 18:470) |
| 9982 | 6 | Decretos 513, 511 y el de las localidades de Anta | «aquellas inherentes al / Concejo Deliberante» en el 513 (Vaqueros, «Dpto. La Caldeıa» [sic]) y la misma fórmula en el 511 (Coronel Moldes) y en el de Las Lajitas, Talavera, General Pizarro, Gaona y Apolinario Saravia. Coincide (A:427, 14:579, 18:470: «la fórmula de los decretos del mismo día para otros municipios») |
| 10049 | 8 | Decreto 1586, art. 1 | «Confírmase en los cargos de titulares de los municipios que se mencionan en cada caso, al personal militar que seguidamente se detalla». Coincide (A:427, 18:470); los confirmados lo son como intendentes o como presidentes de comisión, y Fernández como «Presidente de la Comisión Municipal» |
| 9951 | 1 | Tapa | «Cnel. CARLOS A. MULHALL / Interventor Militar». Coincide (A:427, 18:470) |
| 10041 | 5 | Edicto 24860 | «MARTIN BORJA», «2,85 lts./segundo», «por medio de la acequia municipal Nº 1», «5,4212 Has.», «El Milagro, catastro Nº 6», fechado el 8 de noviembre de 1972. Coincide (A:427, 17:281) |
| 10111 | 5 | Decreto 2797, visto y considerando | «por disponer / la misma sobre una materia de competencia de / ese municipio». Coincide (A:428, 07:251) |
| 10111 | 6 | Ordenanza 7/76 transcripta | «por ser los ríos cir- / cundantes», \$1.400, \$1.300, \$140 por metro cúbico en días inhábiles, firma de Camacho. Coinciden (A:428, C:43, 01:139, 07:251). El considerando dice que el monto «resulta bajo … debido a que de la suma total recaudada debe asignarse el 50 % a la Municipalidad de La Caldera»: la ordenanza no asigna nada en su articulado (hallazgo 1). La marca sobre «debe» y «asignarse» de P150 se ve en el recorte; el libro no cita esas palabras |
| 10105 | 5 | Ley 5058, arts. 1, 2 y 6 y planilla | Deroga desde el 1.º de enero de 1976 la «Ley Nº 4735 de fecha 19 de diciembre de 1973»; \$875 a las permanentes y a las temporales permanentes y \$437 a las eventuales; art. 6, «hasta un trein- / ta (30) por ciento del valor recaudado el año an- / terior en concepto de Canon de Riego bajo la / forma de estudios técnicos, préstamos de máqui- / nas, obras de riego, jornales», destinados a los planes de obras de los consorcios; planilla, Especial 1,5 y Primera 1 con la «Intendencia de Aguas de La Caldera» primera. Coinciden (A:429, C:149, 17:281) |
| 10127 | 5 y 6 | Ley 5082, arts. 1 a 4 y planilla | 15 %, 12 %, 3 % al Fondo de Desarrollo Municipal; 30, 35 y 35 por ciento; índices 0,6894 y 0,6287. Coinciden (A:430, C:150, 07:249, 15:185). El art. 4 dice de dónde salen los datos (último censo; erogaciones reales del penúltimo ejercicio) pero no los publica: «la ley no publica los datos» es exacto |
| 9986 | 5 | Decreto 642, visto | «planteando la / situación financiera por la que atraviesan diver- / sos municipios del interior de la Provincia, la / que les imposibilita». Coincide (15:185) |
| 10134 | 19 | Decreto 3348 | «Apruébase la Ordenanza Nº 2, dicta- / da para el año 1976, por la Municipalidad de La / Caldera». Coincide (15:185, A:427) |
| 10136 | 20 | Decreto 3471, art. 1, obra 2 | «"Defensas sobre el Río La Cal- / dera - Zona Cabral (Dpto. La / Caldera)" \$ 1.725.024». Coincide (09:535, A:427) |
| 9996 | 5 | Decreto 812, art. 1 | «de \$ 20,00 a \$ 100,00 (cien pesos)», desde el 1.º de abril. Coincide (A:427, 26:235) |
| 10120 | 6 | Decreto 2982 | «Obs. pluviométrico Los Yacones», «\$ 700,- de julio a diciembre de 1976 \$ 4.200,-». Coincide (A:427, 09:637, 26:235) |
| 9910 | 7 | Decreto 3861, renglón | La Caldera 52.744 + 37.310 + 29.501 = 119.555. Coincide (A:427, 15:185) |
| 9903 | 12 | Decreto 3809, renglón | «La Caldera \$ 15.000». Coincide (A:427) |
| 10129 | 14 | Decreto 3206 | Río Las Nieves, San Francisco de los Yacones, \$1.022.190. Coincide |
| 10130 | 11 | Decreto 3211 | Juntas de los ríos San Alejo y Santa Rufina, \$1.277.738. Coincide |
| 10143 | 30 | Decreto 3713, art. 3 | «La Caldera: / Un (1) tractor de 50 a 60 HP». Coincide (A:427, 15:185) |
| 10086 | 12 | Aviso 25536 | Base \$784, «2 Has. 4.246,42 m2.», linderos remanente de La Helvecia y al oeste «Ruta Nacional», matrícula 1556. Coincide (A:427), sin nombres de las partes |

Son **19 citas entre comillas del libro cotejadas en la imagen** (10 distintas, contadas una vez por pasaje; los nombres propios entre comillas ---«El Milagro», «San Cayetano»--- no se cuentan), **ninguna con diferencias**, y datos sin comillas en 10 hojas (9910 h7, 9903 h12, 10129 h14, 10130 h11, 10143 h30, 10086 h12, 10105 h5, 10127 h5 y h6, 10120 h6, 9996 h5). Bajadas y no cotejadas: 9969 (el reconocimiento `eng` no ubicó el renglón; el anticipo de marzo sale de una ficha de MODO imagen).

### Hallazgos (uno, aplicado en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | D:253 | «la ordenanza 7/76 de Vaqueros, que asigna a la Municipalidad de La Caldera la mitad de lo que Vaqueros recauda por los áridos»: la ordenanza no asigna nada en su articulado (fija el gravamen y el monto por metro cúbico); es su considerando el que dice que el monto resulta bajo porque de lo recaudado «debe asignarse» la mitad a La Caldera (10111 h6, imagen). El libro lo dice bien en A:428 («Qué acto fija ese reparto, la ordenanza no lo dice»), en 07:251 («La ordenanza no cita el acto que fija ese reparto») y en C:43, y el mismo ítem de D pide «el acto que haya fijado ese reparto». Contradicción con pasajes a más de diez páginas | 7 | «y la ordenanza 7/76 de Vaqueros, según cuyo considerando la mitad de lo que Vaqueros recauda por los áridos de los ríos debe ir a la Municipalidad de La Caldera, cuyo expediente …», sin agregar renglones y sin citar las palabras en duda de P150 |

Resta: un error de consistencia en el aspecto 7: **1 en 39,3 páginas = 2,5 por cada 100** → escalón de ≤ 4 (**50**); no se resta el escalón adicional, porque los pasajes que lo contradicen están a más de diez páginas y el propio ítem pide el acto que fija el reparto. No toca a una sección: no hay tope por alcance. Aplicado: 100 en la nota final del 7.

**Errores introducidos por la propia auditoría**: el hallazgo 1 está en el AMPLÍA 1976 (`1972d59`). **No lo atrapó un control automático**: ningún control compara lo que el libro dice que un acto dispone con lo que su texto dispone; los controles de P86 (fechas), P102 (privacidad), P137 (1) (citas letra por letra) y P144 (comillas rectas) funcionaron en el AMPLÍA 1976.

**Descartados (falsos positivos, 5).** «Capítulo \ref{cap:defensas}, más adelante» en 26:235: 26-presencia se compila antes que 09-defensas, y la remisión es a un capítulo posterior. «Una semana después de que la tapa del Boletín empiece a nombrar a un interventor militar» (22-prospectiva:144): la tapa lo nombra desde la 9951, del 24 de marzo, y el decreto 116 es del 31. «Deroga la 4860 con los mismos tres criterios» (07:249): A:423 da para la 4860 el 30, 35 y 35 por ciento que la 5082 repite (10127 h5). «La Ley 4735 de fecha 19 de diciembre de 1973» que cita la 5058 contra el 07/12/1973 de C:144: C:144 da el 7 como sanción y el 19 como promulgación, y las dos fuentes no discrepan. «4.844 hojas, casi todas a 300 ppi» (A:427) y «4.248 de ellas a 300 ppi; … veinticuatro … a 150» (F:84): el informe (§1) suma 4.248 a 300, 552 entre 291 y 299, 20 a 362 y 24 a 150; F no da las 572 restantes, pero lo que da es exacto.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P151 (lee, 1976): corregir en el informe LEE 1976 la NOTA de A.27 con el art. 6 de la Ley 5058 en sus palabras (reintegro «hasta un treinta (30) por ciento del valor recaudado el año anterior en concepto de Canon de Riego bajo la forma de estudios técnicos, préstamos de máquinas, obras de riego, jornales», 10105 h5), con la planilla Especial 1,5 (cuatro sistemas) y con la fecha que el art. 1 da a la Ley 4735 («19 de diciembre de 1973», su promulgación); y la NOTA de A.28, que el considerando de la ordenanza 7/76 da el reparto como motivo del monto y no lo dispone (completa P148). P152 (herramientas): sumar a los controles del AMPLÍA (P149) uno de **verbos dispositivos**: toda frase nueva que diga que un acto «asigna», «fija», «otorga», «crea», «deroga» o «dispone» algo se coteja con el articulado del acto, no con su visto ni con su considerando.

**Pendientes revisados sin cerrar.** P54 (1976 nombra el médico zonal de La Caldera, el puesto sanitario de Vaqueros y la cooperadora; ni hospital ni estación). P100 y P118 (1976 en barrido, con el criterio de F, como dice `amplia-1976.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; ningún acto de 1976 nombra el embalse: el aspecto 1 sigue en 82). P138, P139, P141, P145 y P146 (láminas, H y E: fuera del alcance de una auditoría). P140 y P147 (pedidos de D que el AMPLÍA no agregó para no mover el recuento de 284). P143, P148 y P150 (correcciones de los informes LEE y la duda de 1976; la fase 6 no cita las palabras en duda). P144 y P149 (scripts de control).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.205/25.205 líneas vigentes en `bc41c69` | 25.170 vigentes, 35 caducas por el AMPLÍA 1976 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*el único*, *la única*, *único*, *única*, *el primero*, *la primera*, *el primer*, *por primera vez*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos los*, *todas las*, *no se publica*, *no lo dice*, *no publica*, *no trae*, *no interviene*, *no figura*), sobre 3.858 palabras agregadas | 20 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («ningún acto hallado del año», «lo hallado del año no trae», «en lo leído del año»); «no publica ninguno de los textos» y «ninguna de las dos leyes publica los datos» describen los actos leídos, no el corpus; «siempre las últimas» es de la cadena de folios de las 109 ediciones (E.2) |
| Repaso de ventana: afirmaciones que cierran en 1975 (*a 1975*, *hasta 1975*, *--1975*, *1958 a 1975*, *1961 a 1975*, *1964 a 1975*, *1969 a 1975*, *1970 a 1975*) y que abren el hueco en 1976 (*1976--2012*, *1976 a 2012*, *1976 en adelante*, *treinta y siete años*, *sesenta y un tramos*, *9.897*); y *treinta y seis años*, *sesenta y dos tramos*, *sesenta y una* | libro entero | Ninguna queda sin actualizar. «Pagos previstos hasta 1975» (A:409) es del decreto 1279; «queda como 1958 a 1975» (F:84) compara; «treinta y seis años» de 04:349 y de H:12 son de 1909-1945, y los de 01, 02, 04:3659 y 22-infraestructura, de 1977-2012; «sesenta y una operaciones de dominio» (03:1041) declara su universo, 1909 a 1945 |
| Comillas rectas que `babel` deforma (P144) | 25/25 comillas rectas del fuente | 0 de riesgo; en el PDF compilado, 0 *Ç*, 0 *ç* y 0 *ï* |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 336/336 `\ref{cap:…}` de un capítulo a uno posterior (333 en `bc41c69`, más 14:579, 15:185 y 26:235) | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1976 (F:25–26, 84 y 87, 00:43, 01:119 y 139, 02:28 y 99, 04:3659–3660, 20:880–881, 22-infraestructura:545, D:177, A:427) contra el §0, el §1, E.2, E.4, E.10 y el §R del informe | 1 año | Tramos: 42 + 1 + 19 = 62; fuera de las ventanas, 1948 y 1958-1976 = 20. Ediciones: 9898–10143 = 246, sin ausentes. Hojas: 4.844 presentes, 5.004 declaradas, 160 faltantes en 109 ediciones; 4.248 a 300 ppp y 24 a 150. Capa útil 530 + OCR propio 4.314 = 4.844. Hojas a ojos: 315, dentro del intervalo de 00:43 (69 a 764). Poca tinta: 1.311. Discrepancias: 434 − 234 = 200 trabajadas. Días hábiles sin edición: 16, cinco explicados por la Ley 5032. Hueco 1977–2012: 36 años. D:177, dieciséis años de 1961 a 1976 y dieciséis cifras; trece de 1964 a 1976 y trece cifras. Confirmados el 23 de julio: 11 = 2 + 9 |
| Aritmética de 1976 | 7 cuentas | 52.744 + 37.310 + 29.501 = 119.555. 12 + 3 = 15 (Ley 5082). 30 + 35 + 35 = 100. (0,9982 − 0,6287) / 0,9982 = 37,0 % («más de un tercio»). 700 × 6 = 4.200. 1.400, 1.300 y 140 (ordenanza, sin cuenta en el libro). 34.313 + 34.313 + 41.250 = 109.876 (los tres anticipos a La Caldera; el libro no da la suma). Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 63 | 50 de 98 cláusulas con cifra en el texto agregado | **50/50 con fuente localizable**: la cita en la cláusula, en la misma oración o en la misma fila, o, en las declaraciones de cobertura, el apéndice F y el informe que F cita; la de la cabeza en negrita de A:427 remite a las filas que citan. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 44 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 44 líneas, cruzadas con contextos sensibles (P102) | 44/44 líneas | Ningún particular nombrado junto a remate, cesantía, accidente o intervención: el remate de La Helvecia va sin las partes, el agente de policía accidentado, el auxiliar cesanteado, el peluquero y los médicos de la cooperadora van sin nombre. Nombrados: funcionarios (interventores federales y militar, gobernador, Xamena, Fernández, Camacho, Catalán, el juez de paz suplente Guerrero) y el titular del pedido de agua de El Milagro, Borja, en la serie que el capítulo 17 sigue con nombres, con la cautela de que el acto no dice si es el encargado de 1968 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `1972d59` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish` y sin `.aux` previos); 909 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las leyes 5058 y 5082 y la ordenanza 7/76 van en pasado; la 4735 y la 4860, derogadas, con la norma que las deroga |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Acto y publicación separados en las cuatro filas nuevas (30-9 y 16-11; 27-10 y 8-11; 1-12 y 9-12; decretos de diciembre de 1975 publicados en 1976) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 19 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Ninguna ausencia ni superlativo cae; las ausencias de 1976 llevan su universo |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 50 | 100 | 1 error en 39,3 páginas (2,5 por 100): escalón de ≤ 4; aplicado |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P138 y P145 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | P102 funcionó |

**Nota inicial: 83,8 antes del tope y 83,8 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el expediente 53-9558 de la ordenanza 7/76 y el acto que fija el reparto de los áridos que D:253 pide dirían si en 1976 hubo una competencia municipal sobre el cauce compartida entre los dos municipios---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro y dejar corriendo los controles de P144 y P152: sube el techo del 4 a 100 y vale +0,7; (5) publicar los scripts que faltan y extender las láminas a 1976 (P138, P145): hasta +0,2 en el 13.

**Avance del libro:** 1 de 1 hallazgo resuelto (100 %); compila sin errores ni referencias indefinidas, 909 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1976 el municipio no interviene en ningún acto de agua hallado; una ley del gobierno militar fija otro canon de riego sin él, y lo más parecido a una competencia sobre el río sigue siendo el cobro de los áridos, que una ordenanza de Vaqueros dice compartir con La Caldera sin acto publicado que lo funde), la tutela provincial sobre el fisco municipal (ordenanzas aprobadas por decreto y sin texto publicado, anticipos de la coparticipación propia y una ley que cambia los índices sin publicar sus datos) y la designación provincial de las autoridades municipales (dos suboficiales retirados, uno de ellos con las funciones del concejo desde mayo de 1976, cuatro años antes de la Ley 5686).

**Calidad de la auditoría.** Cobertura de la ronda: 44 líneas (0,17 %; 39,3 páginas). Cobertura acumulada: 25.214 de 25.214 (100,0 %), con el registro de arriba. Falsos positivos descartados: 5. Recortes: no se cotejaron el renglón del anticipo de marzo (9969 h5) ni los de los decretos 641, 2332, 3164, 1043, 1243, 271, 1766, 2670 y de los dos cateos (fichas de MODO imagen); el control de comillas cubre las comillas rectas dobles y no las simples; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **1 de 1**, en el AMPLÍA 1976 (`1972d59`), **0 atrapados por un control automático**.

## Ronda 64 — lecturas de Eduardo, 1977 (03/10/2026)

Tipo: **lecturas sin cambio en el libro** (CORRIGE 3.6), por la palabra clave `LECTURAS` (flujo v2 §5.6). Base: commit `deca5b6`. No hay parche: 1977 está en `puntual`, sin informe registrado, y ninguna de las formas decididas aparece en el libro. Denominador: 25.214 líneas, sin cambios. La cobertura acumulada sigue en **25.214 de 25.214 (100,0 %)**. Como el informe `BO-Salta-1977_10144-10393_la-caldera_LEE-1977_2026-10-03.txt` todavía no está registrado, las lecturas se aplicaron sobre él y se entrega de nuevo con el mismo nombre: **no queda pendiente de tipo `lee`**.

### Qué se decidió con controles, sin mostrarlo (§5.6.1)

Antes de armar la hoja se decidieron por control o por la imagen a 400 ppp: el ordinal de la Res. 539 (A.21), «1º de octubre» y no «19», por la imagen y la fecha de la resolución (3-10); el número del aviso del Centro Vecinal «Dr. Carlos Serrey» (B.2.10), 28718, por el cuerpo contra la capa nativa del sumario (28728); el expediente 29-85265/77 del Dto. 3596 (B.2.14), por la imagen. La M. I. del juez de paz titular de La Caldera (A.14) no se llevó a la hoja: es un documento que el libro no necesita (§5.6.3).

### Lecturas de Eduardo (hoja `dudas-1977-1977.html`, 2 casos con el renglón marcado)

| # | Edición y hoja | Duda | Sesión | Eduardo | Control | Clase |
|---|---|---|---|---|---|---|
| D1 | 10294 h9 | Expediente de los jueces de paz de La Caldera en el Dto. 2426 (A.14), «53-10.40?» | Imagen a 400 ppp «403»; capa «10,408» | 53-10.403 | Serie de expedientes del acto, creciente (10.300, 10.402, 10.4??, 10.413…): admite 403 y 408; sin otra aparición en el año ni en los informes LEE de 1933 a 1976 | **Decidida por Eduardo: 53-10.403**, igual que la imagen |
| D2 | 10325 h27 | Plano de la Finca Fracción A, en La Calderilla (aviso de La Calderilla S.A., A.18), «Plano 80?» | «80» y un hueco antes de «con»; capa «808» | Plano 80 | Sin control: se cita una sola vez en el año y en ningún informe anterior; hoja de otro escaneo, unos 170 ppi equivalentes | **Decidida por Eduardo: Plano 80**; se descarta «808» |

Balance: de 2 lecturas, 2 decididas por Eduardo, ninguna corregida por un control ni abierta. Las dos coinciden con la imagen mirada por la sesión y desmienten a la capa. Se suma al catálogo del §5.6: **en las hojas de escaneo de formato grande (unos 170 ppi equivalentes), la capa agrega un dígito donde la imagen deja un hueco («808» por 80); un número leído en esas hojas no se da por bueno sin la imagen.**

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Menciones en el libro de las formas decididas | 8 formas (10.403, 10.408, 10403, 53-10, Calderilla S, Plano 80, plano 80, 808) en los 38 archivos `.tex` | Ninguna del informe 1977: «808» aparece 13 veces, ajenas (edicto 808 de 1957, expedientes, montos) |
| Otras apariciones en el corpus de 1977 | Texto de las dos versiones, 249 ediciones | «53-10.40x» y «plano 808» sólo en su propia hoja |
| Cita cruzada en informes anteriores | 35 informes LEE (1933–1976) | Ni el expediente ni el plano, ni la matrícula 429, el catastro 1646 o los linderos de La Calderilla |
