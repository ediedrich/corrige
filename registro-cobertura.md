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
