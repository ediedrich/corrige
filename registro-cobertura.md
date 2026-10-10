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

## Ronda 65 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1977-1978. Base: commit `b3b2923` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1977-1978, sobre `deca5b6`, la ronda 64 sin parche), con la fase 6 en `ronda-65.patch` (commit `a43d28a` en la sesión; aplica con `git am` sobre `b3b2923`, probado en un clon limpio de GitHub: árbol `7ed57e1`). **Denominador medido: 25.235 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo**, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 64 (25.214 de 25.214, sobre `deca5b6`) se trasladaron por diff a `b3b2923`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1977-1978 agrega 21 líneas netas (8 en A, 11 en C y 2 en F) y deja 54 líneas nuevas o modificadas en 20 archivos: caducan 33 líneas anteriores**, y quedan **25.181 vigentes sobre 25.235 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `b3b2923`)

Se leyeron **las 54 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A y C completas, y las modificadas del resto en su texto entero, no sólo en el fragmento cambiado. Se cotejaron contra los informes LEE (`BO-Salta-1977_10144-10393_la-caldera_LEE-1977_2026-10-03.txt` y `BO-Salta-1978_10394-10641_la-caldera_LEE-1978_2026-10-03.txt`, bajados de `corrige/lee/`): §0, §A entero (26 fichas de 1977 y 35 de 1978: FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1 y B.2 enteros (14 y 16 entradas), E.2, E.3 y E.4 de los dos, y el §1 de 1978 en lo que hace a la resolución; y el `amplia-1977-1978.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 431–438 | 8 | sesión |
| ape/C-normativa.tex | 22–25, 48–49, 157–161 | 11 | sesión |
| ape/D-pedidos.tex | 62, 177, 191–192, 253 | 5 | sesión |
| ape/F-fuentes.tex | 25–26, 86–87, 89 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/07-cot.tex | 249, 251 | 2 | sesión |
| cap/09-defensas.tex | 535, 637 | 2 | sesión |
| cap/10-expropiacion.tex | 332, 513 | 2 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): la versión de `deca5b6` de 22-infraestructura:545, frase por frase contra la nueva, para ver dónde entró cada agregado (hallazgos 1 y 2); la serie de 1970 de 17-aguabaja:281 (la concesión a Obras Sanitarias de veinte litros por segundo junto a la desembocadura del Wierna, que usa la corrección del hallazgo 3); y el orden de `\input` de `main.tex` (09-defensas y 17-aguabaja van antes que 22-infraestructura: las dos remisiones nuevas de la fase 6 no llevan «más adelante»).

**Esta ronda: 54 líneas nuevas**, 147.898 bytes sobre 2.983.470, que en las 917 páginas de la base equivalen a **45,5 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `b3b2923` cae dentro de estos tramos.

Acumulado: 25.181 vigentes + 54 = **25.235 de 25.235 (100,0 %)**. La fase 6 toca dos líneas, A:431 y 22-infraestructura:545, dentro de lo leído en esta ronda, y no cambia el largo de ningún archivo: **25.235 de 25.235 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1977 y 1978 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 110–250 ppp con PyMuPDF, primero la hoja entera o la columna y después el recorte del renglón, ubicado con el reconocimiento `eng` de la sesión; cada recorte se miró. Se bajaron 43 ediciones (20 de 1977 y 23 de 1978).

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 10206 | 11 y 3 | Decreto 577, visto; sumario | «para el año 1976» en el cuerpo y «para el año 1977» en el sumario. Coincide (A:431, 15:185) |
| 10251 | 11 y 12 | Decreto 1542, considerandos | «reacondicionamiento total de la red existente que se encuentra obsoleta», veinte años; conexiones domiciliarias a convenir con los frentistas. Coincide (A:432, 22-infraestructura:545) |
| 10298 | 10 | Decreto 2526, considerando | «las obras paralizadas o con ritmo de trabajo disminuido», «particularmente el "Dique Campo Alegre"». Coincide (A:433, 10:513) |
| 10307 | 20 y 21 | Decreto 2584, fecha, considerando y art. 1 | 2 de agosto de 1977; «prácticamente ya concluido en su primera etapa»; «actualmente denominado "Campo Alegre", ubicado en el Departamento La Caldera». Coincide (A:433, C:157, 10:513) |
| 10311 | 5 | Ley 5165, art. 2 | «RURALES» 924; los departamentos a 351. Coincide (A:434, C:158) |
| 10376 | 31 | Decreto 3596, encabezado y considerando | **Salta, 22 de noviembre de 1977**, expediente 29-85265/77; «relacionados con el Plan de Urbanización de los diques de "Cabra Corral" y "Campo Alegre"». La cita coincide (06:56); la fecha desmiente el «en diciembre» de A:431 (hallazgo 4) |
| 10345 | 17 | Resolución 594, encabezado, visto, considerando y art. 1 | 17 de octubre de 1977, Ministerio de Economía, «Expediente Cód. 53-10082/77»; «Defensas sobre Río Wierna, Vaqueros, Dpto. La Caldera (Salta)», \$3.345.192; el considerando: «proteger las instalaciones del Matadero Municipal de Vaqueros, servicio de agua corriente de O.S.N., ruta nacional Nº 9 y zonas de cultivos». Coincide (09:535); el considerando desmiente el universo de 22-infraestructura:545 (hallazgo 3) |
| 10217 | 9 | Decreto 762, cuadro | «Construcción defensas sobre el Río La Caldera - Zona Dique Campo Alegre - Dpto. La Caldera», \$3.289.300. Coincide (09:535) |
| 10225 | 26 | Decreto 1114, considerando | «no justifica su inclusión en categoría rentada». Coincide (26:235) |
| 10314 | 16 | Decreto 2736, renglón | «Obs. Pluviométrico Los Yacones», \$9.000. Coincide (09:637) |
| 10641 | 7 | Decreto 1922, renglón | Los Yacones, \$20.000 por mes, enero a diciembre, \$240.000. Coincide (09:637) |
| 10341 | 7 | Ley 5183, art. 1 | «Acueducto Embalse Campo Alegre y Planta Potabilizadora». Coincide (22-infraestructura:545) |
| 10390 | 8 | Decreto 3711, considerando | «Consultorio Externo de La Caldera». Coincide (04:4599) |
| 10427 | 12 | Res. 66 | «en el puesto sanitario de La Caldera», médico zonal de San Lorenzo, «Alias» [sic]. Coincide (04:4599) |
| 10421 | 9 | Res. 2060, renglón | «para desempeñarse en la localidad de Vaqueros y La Caldera». Coincide (A:435) |
| 10422 | 7 | Res. 2059, visto | «anormalidades registradas en el Hogar "Dr. Luis Linares" de La Caldera». Coincide (A:435, 26:235) |
| 10472 | 8 | Decreto 553, considerandos y arts. 1 a 7 | «en ejercicio pleno del Poder de Policía»; arenas y ripios de los cauces hasta las líneas de ribera; permisos temporales; tasa de servicios no inferior al 10 % del precio del material; «podrá ser delegado a las municipalidades o policía del orden» conforme a la resolución que dicte el administrador general; reglamenta los arts. 239, 240 y 241 de la Ley 775; «muy intensiva e irracional», ríos de Vaqueros y Arenales, inundaciones de la ciudad y de Metán. Coinciden (A:436, C:160, 01:139, 07:251, D:253) |
| 10533 | 8 | Decreto 1121, visto | «Plaza General José de San Martín», ordenanza 018/78. Coincide (A:435, C:25) |
| 10588 | 17 | Decreto 1553, considerandos | «paralizada desde enero de 1976»; «asegurar un permanente abastecimiento de aguas para la Ciudad de Salta y riego en zonas aledañas». Coinciden (A:437, 10:513) |
| 10598 | 16 y 20 | Decreto 1620, considerando y anexo | «Programa Turístico de Campo Alegre - 1ra. Etapa»; «servirá principalmente para satisfacer las necesidades de recreación de la población de Salta»; 3.609, 12.537 y 206.458, «un total de 222.602». Coinciden (A:438, 06:56) |
| 10618 | 5 | Decreto 1809, inciso 20 | «En Villa San Lorenzo, con jurisdicción además en La Caldera y Vaqueros». Coincide (04:4599) |
| 10636 | 7 | Decreto 1812, art. 1 | «Establecimiento de Potabilización en el Dique "Ing. José A. Peralta" en Campo Alegre - Departamento La Caldera (Salta)». Coincide (22-infraestructura:545) |
| 10577 | 7 | Ordenanza 5/77 de Vaqueros | 900 m², 15 por 60 metros. Coincide (C:49, 15:185) |

Son **27 citas entre comillas del libro cotejadas en la imagen** (contadas una vez por pasaje; los nombres propios entre comillas como «El Palenque» no se cuentan, y sí la del considerando de la Res. 594 que la fase 6 introduce), **ninguna con diferencias**, y datos sin comillas en 5 hojas (10376 h31, 10345 h17, 10314 h16, 10641 h7, 10577 h7). Bajadas y no cotejadas: 10182 h7 (el reconocimiento ubicó el considerando y no el punto 3.º; la cita «Interior» sale de una ficha de MODO imagen), 10282, 10316, 10375, 10294, 10334, 10323, 10380, 10405, 10411, 10433, 10434, 10476, 10485, 10499, 10521, 10546, 10554, 10579 y 10635 (fichas de MODO imagen; no se buscó el renglón).

### Hallazgos (cuatro, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 22-infraestructura:545 | El AMPLÍA puso las frases de la red de agua de 1977 entre la obra por administración de 1973 y «Ese mismo año el Centro Vecinal Vaqueros … llama a ratificar o rectificar la resolución … para entregar el servicio» (aviso 15589, Nº 9346, h. 37), que es de 1973: el «mismo año» pasó a ser 1977 | 7 | «En 1973 el Centro Vecinal Vaqueros …» |
| 2 | 22-infraestructura:545 | El AMPLÍA puso la frase del retiro de la personería del Centro Vecinal Vaqueros, de 1978, delante de «\textbf{Y ese año el municipio de La Caldera se acoge al régimen de la ley nacional 13.577}», que es de 1975 (ordenanza 3/75, 3519, Nº 9877, h. 12): el «ese año» pasó a ser 1978 | 7 | «\textbf{Y en 1975 el municipio de La Caldera se acoge …}» |
| 3 | 22-infraestructura:545 | «Lo que esos dos años dejan de Obras Sanitarias es el acueducto para la capital»: afirmación de universo que el propio libro desmiente, porque 09:535 da la Res. 594 de 1977, cuyas defensas deben proteger el «servicio de agua corriente de O.S.N.» en Vaqueros (10345 h17, imagen). Además, «esos dos años» no tenía antecedente: la frase anterior hablaba de 1975 a 1978 | 5 | «Lo que 1977 y 1978 dejan de Obras Sanitarias en el departamento es una mención y una obra», con la mención de la Res. 594 y la salvedad de que el acto no dice si es el agua de la localidad ---la que el Centro Vecinal Vaqueros proponía en 1973 entregar a la Dirección de Aguas--- o la toma de veinte litros por segundo otorgada en 1970 junto a la desembocadura del Wierna para la zona norte de la capital (capítulo \ref{cap:aguabaja}); qué acto le dio a Obras Sanitarias un servicio en Vaqueros, si se lo dio, lo hallado no lo dice |
| 4 | A:431 | «y en diciembre la Provincia le da \$10.000.000 a la Dirección General de Inmuebles» (3596, Nº 10376, h. 31): el decreto es del 22 de noviembre de 1977 y se publica el 6 de diciembre; la fila usa en todo lo demás la fecha del acto (577 en marzo, 3660 en noviembre aunque se publica en diciembre) | 3 | «y ese mismo mes la Provincia le da …», después de los actos de noviembre |

Resta: dos errores de consistencia en el aspecto 7: **2 en 45,5 páginas = 4,4 por cada 100** → escalón de ≤ 8 (**40**); no se resta el escalón adicional, porque ninguno contradice una fecha que el libro dé a menos de diez páginas: la del aviso 15589 y la de la ordenanza 3/75 están en la cronología y en 01:139. Un superlativo de universo que el libro desmiente con su propio dato, en el aspecto 5: **resta 10** (90). Una fecha de publicación dada como fecha del acto, en el aspecto 3: **resta 5** (95). Ninguno sostiene una sección: no hay tope por alcance. Aplicados los cuatro: 100 en la nota final del 3, del 5 y del 7.

**Errores introducidos por la propia auditoría**: los cuatro hallazgos están en el AMPLÍA 1977-1978 (`b3b2923`). **Ninguno lo atrapó un control automático**: ningún control relee, después de insertar una frase en un párrafo, las anáforas temporales que la siguen («ese año», «ese mismo año», «esos dos años», «al año siguiente»); P159 lo propone. Los controles de P144 (comillas rectas), P152 (verbos dispositivos) y P158 (caracteres de control) funcionaron en el AMPLÍA 1977-1978.

**Descartados (falsos positivos, 6).** «En 1978 … el Centro Vecinal "Dr. Carlos Serrey" sigue convocando a sus asambleas» con un aviso de 1977 (10323) y otro de 1978 (10433): «sigue» admite las dos fechas. «El municipio no interviene en ninguno de esos actos» (01:139) aunque la Res. 594 lleva un expediente de código 53 (serie de las actuaciones municipales, P155): el municipio de la frase es La Caldera, y el acto no nombra intervención municipal; el expediente ya está pedido en P155. «La tapa da como gobernador a Ulloa todo el año» (A:435) junto a la firma de Davids como interino el 30 de marzo: lo dice E.4 del informe 1978, y la fila da las dos cosas. «Cinco días antes» (A:433): 2526 es del 28 de julio y 2584 del 2 de agosto; el «tres semanas antes» de la nota de B.2.7 del informe cuenta por la publicación. «La foliatura corre de la página 1 a la 6.024, de modo que faltan 113» (F:86) contra las 6.000 declaradas del §R: E.2 del informe da los folios 1 a 6.024 y el §R usa la tapa, como dice L6. El «en 1978 reconoce los servicios del médico zonal de ese consultorio» (04:4599) con una resolución del 13 de diciembre de 1977: el pasaje cuenta los actos hallados de cada año por su publicación, como en los años anteriores.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P159 (herramientas): control de **anáforas temporales** para AMPLÍA (extensión de P149, P152 y P158): después de insertar una o más frases en un párrafo, se listan las frases siguientes del mismo párrafo que empiezan o se apoyan en «ese año», «ese mismo año», «ese mes», «esos dos años», «al año siguiente», «un año después» o «entonces», y se comprueba que su antecedente siga siendo el mismo; en 22-infraestructura:545 el AMPLÍA 1977-1978 desplazó dos («Ese mismo año», 1973, y «Y ese año», 1975). P160 (lee, 1978): corregir la NOTA de B.2.2 del informe LEE 1978: el decreto del refuerzo de \$10.000.000 a Inmuebles es el 3596 del 22-11-1977, como imprime su encabezado en la imagen (10376 h31), y no el 3598 de la capa. P161 (libro, 1977): pedido para el apéndice D cuando se reabra el recuento de 22-prospectiva (como P155): el acto, convenio o resolución que haya puesto en Obras Sanitarias de la Nación un «servicio de agua corriente» en Vaqueros, que nombra la Res. 594 de 1977 (10345 h17), y su relación con la propuesta del Centro Vecinal Vaqueros de 1973 y con la concesión de 1970 del subálveo del río La Caldera.

**Pendientes revisados sin cerrar.** P54 (1977 y 1978 nombran el consultorio externo y el puesto sanitario de La Caldera y los consultorios externos de Vaqueros y La Caldera; ni hospital ni estación). P100 y P118 (1977 y 1978 en barrido, con el criterio de F, como dice `amplia-1977-1978.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; los actos de 1977 y 1978 que nombran el embalse no dan ninguna: el aspecto 1 sigue en 82). P138, P139, P141, P145, P146, P153 y P154 (láminas, H y E: fuera del alcance de una auditoría). P140, P147 y P155 (pedidos de D que el AMPLÍA no agregó para no mover el recuento de 284). P143, P148, P150, P151, P156 y P157 (correcciones de los informes LEE). P144, P149, P152 y P158 (scripts de control).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.214/25.214 líneas vigentes en `deca5b6` | 25.181 vigentes, 33 caducas por el AMPLÍA 1977-1978 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*el único*, *la única*, *único*, *única*, *el primero*, *la primera*, *el primer*, *por primera vez*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos los*, *todas las*, *no se publica*, *no lo dice*, *no publica*, *no trae*, *no interviene*, *no figura*, *no nombra*, *sin publicar*), sobre 6.286 palabras agregadas | 30 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («lo hallado de 1978 no trae», «la lectura no halló», «no aparece en lo hallado de los dos años», «en lo leído de los dos años»); «la más baja de cuatro ofertas» es del cuadro del decreto 3941; «la primera» son la primera etapa del programa y la primera de tres ediciones; «casi siempre las últimas» es de la foliatura (E.2). El control no atrapa la exhaustividad sin cuantificador del hallazgo 3 («Lo que esos dos años dejan … es»): se encontró leyendo |
| Repaso de ventana: afirmaciones que cierran en 1976 (*a 1976*, *hasta 1976*, *1958 a 1976*, *1958--1976*) y que abren el hueco en 1977 (*1977--2012*, *1977 a 2012*, *1977 en adelante*, *treinta y seis años*, *sesenta y dos tramos*, *sesenta y tres tramos*, *10.143*); y los *caption* de las láminas | libro entero | Ninguna queda sin actualizar. «1958 a 1976» queda sólo en F:86, que compara; los «treinta y seis años» de 04:2621, 04:3490, D:220 y H:12 son de otros universos (1909-1945 y edictos); las láminas que piden extensión siguen en P153 |
| Anáforas temporales en las líneas tocadas por el AMPLÍA (*ese año*, *ese mismo año*, *el mismo año*, *esos años*, *esos dos años*, *ese mes*, *ese mismo mes*, *ese día*, *al año siguiente*, *un año después*), por script después del hallazgo 1, con cada coincidencia leída contra la frase anterior | 54/54 líneas; 24 coincidencias en `b3b2923` | 3 desplazadas, las tres en 22-infraestructura:545 (hallazgos 1, 2 y 3); las demás siguen en su año (entre ellas el «Ese año» de 15:185, que sigue a la Ley 5082 de 1976 porque el bloque de 1977-1978 entró después). Después de la fase 6, 22 coincidencias, con el «ese mismo mes» nuevo de A:431 |
| Comillas rectas que `babel` deforma (P144) | 25/25 comillas rectas del fuente | 1 en el texto de una línea tocada (26:235, «"GUSTAVO MARTINEZ ZUVIRIA"», anterior al AMPLÍA); en el PDF compilado, 0 *Ç*, 0 *ç* y 0 *ï* |
| Caracteres de control en el diff (P158) | 54 líneas agregadas | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 337/337 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1977 y 1978 (F:25–26 y 86, 00:43, 02:28 y 99, 01:119 y 139, 04:3659–3660, 20:880–881, 22-infraestructura:545, D:177, A:431 y 435) contra §0, §1, E.2, E.3, E.4 y §R de los informes | 2 años | Tramos: 42 + 1 + 21 = 64; fuera de las ventanas, 1948 y 1958-1978 = 22. Ediciones: 10144–10393 = 250 números, 249 sin la 10347; 10394–10641 = 248, sin ausentes. Hojas 1977: 7.090 declaradas − 6.928 presentes = 162, en 105 ediciones; huecos interiores 8 + 3 + 1 = 12 en 10151, 10300 y 10318; capa 774 + OCR 6.154 = 6.928. Hojas 1978: folios 1 a 6.024 − 5.911 = 113; capa 724 + OCR 5.187 = 5.911. A ojos 320 y 221, dentro del intervalo de 00:43 (69 a 764); poca tinta 767 y 504. Discrepancias: 1977, 28 + 176 = 204 de 376; 1978, 35 sin resolver + 67 sin trabajar = 102 de 267. Actos mirados: 26 + 14 = 40 y 35 + 16 = 51, los del §R. Días hábiles sin edición: 10 y 12. Hueco 1979–2012: 34 años. D:177: dieciocho cifras de hojas sin mirar para 1961-1978, cuatro de poca tinta para 1975-1978 y quince de páginas faltantes para 1964-1978 |
| Aritmética de 1977 y 1978 | 12 cuentas | 8.237.000 − 8.018.571 = 218.429. 7.787.292 − 7.760.000 = 27.292. 44.336.362 − 41.892.977 = 2.443.385. 4.500.000 + 650.000 + 650.000 = 5.800.000. 900 × 2.000 = 1.800.000; 15 × 60 = 900. 3.609 + 12.537 + 206.458 = 222.604, contra los 222.602 impresos. 0,6894 − 0,6892 = 0,6287 − 0,6285 = 0,0002. 20.000 × 12 = 240.000. 9.000 de enero a junio y otro tanto de julio a diciembre. 21 de marzo a 17 de noviembre de 1977: ocho meses. 28 de julio a 2 de agosto: cinco días. 14.708.658 > 8.711.570 (las dos cifras de la red, que el libro no concilia). Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 65 | 50 de 189 cláusulas con cifra en el texto agregado | **50/50 con fuente localizable**: la cita en la cláusula, en la misma oración o en la misma fila, o, en las declaraciones de cobertura, el apéndice F y el informe que F cita. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 54 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 54 líneas, cruzadas con contextos sensibles (P102) | 54/54 líneas | Ningún particular nombrado junto a sumario, cesantía, retiro, suspensión, licencia o juicio: los policías, el personal y el sumario del Hogar «Dr. Luis Linares», los médicos y la odontóloga, el encargado del Registro Civil de Vaqueros, el observador pluviométrico, los socios de La Calderilla S. A., las partes de las posesiones veinteañales (salvo la firma demandada, Arancibia Hnos.), los peticionantes de agua y el minero van sin nombre; los herederos de Carlos Serrey, sin sus nombres. Nombrados: funcionarios (gobernadores, Davids, Fernández, Camacho, los jueces de paz Muñoz y los Mangogna), José Alfonso Peralta, por el nombre que el decreto da al dique, y las empresas (Luis Benjamín Chávez, de la línea 23; Jocar S. A.; M.E.I. Obras y Servicios S.R.L.; Caminos S. A.) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo |
| Compilación | libro entero, base `b3b2923` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos); 917 páginas la base y 919 con la fase 6; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, las que dicen 00:75 y F; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | La Ley 5165 deroga la 4840 y va en pasado; el Decreto 553, el 798 y la Ley 5248, en pasado |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 4 (fecha de publicación dada como fecha del acto); aplicado. Las demás filas separan acto y publicación (30-12 y enero; 13-11 y diciembre; 13-12-1977 y febrero) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 27 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgo 3: universo afirmado que el libro desmiente con su propio dato, resta 10; aplicado. Las ausencias de 1977-1978 llevan su universo |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 40 | 100 | 2 errores en 45,5 páginas (4,4 por 100): escalón de ≤ 8; aplicados |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P153 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | P102 funcionó |

**Nota inicial: 81,4 antes del tope y 81,4 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---las resoluciones de delegación del poder de policía sobre los áridos que el art. 5 del decreto 553 prevé (D:253) dirían si en 1978 el municipio recuperó por delegación algo de lo que cobraba por ordenanza---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro y dejar corriendo los controles de P144, P152, P158 y P159: sube el techo del 4 a 100 y vale +0,7; (5) publicar los scripts que faltan y extender las láminas a 1978 (P138, P145, P153): hasta +0,2 en el 13.

**Avance del libro:** 4 de 4 hallazgos resueltos (100 %); compila sin errores ni referencias indefinidas, 919 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1977 y 1978 el municipio no interviene en ningún acto de agua hallado; en 1978 la Provincia pone en la Administración General de Aguas la policía de los áridos que los dos municipios cobraban por ordenanza, con una delegación posible «a las municipalidades o policía del orden» que lo hallado no muestra ejercida), la tutela provincial sobre el fisco municipal (presupuestos aprobados por decreto sin el texto que los mismos decretos mandan publicar) y la presencia de Obras Sanitarias en el departamento (el acueducto y la potabilizadora del embalse para la capital, y un «servicio de agua corriente de O.S.N.» en Vaqueros que ningún acto hallado explica).

**Calidad de la auditoría.** Cobertura de la ronda: 54 líneas (0,21 %; 45,5 páginas). Cobertura acumulada: 25.235 de 25.235 (100,0 %), con el registro de arriba. Falsos positivos descartados: 6. Recortes: no se cotejaron el punto 3.º de la Res. Gral. 4 (10182 h7) ni los renglones de las 20 ediciones bajadas sin buscar (fichas de MODO imagen); el repaso de anáforas temporales se corrió por script en esta ronda, pero después de la lectura que encontró el hallazgo 1, y no forma parte todavía de los controles del AMPLÍA (P159); la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **4 de 4**, en el AMPLÍA 1977-1978 (`b3b2923`), **0 atrapados por un control automático**.

## Ronda 66 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1979. Base: commit `6efbc1d` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1979, sobre `7098d34`, la ronda 65), con la fase 6 en `ronda-66.patch` (commit `b59d55b` en la sesión; aplica con `git am` sobre `6efbc1d`, probado en un clon limpio de GitHub: árbol `c77027b`). **Denominador medido: 25.249 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 65 (25.235 de 25.235, sobre `a43d28a`, que en GitHub es `7098d34`, con el mismo árbol `7ed57e1`) se trasladaron por diff a `6efbc1d`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1979 agrega 14 líneas netas (6 en A, 6 en C y 2 en F, una de ellas en blanco) y deja 54 líneas nuevas o modificadas en 22 archivos: caducan 40 líneas anteriores**, y quedan **25.195 vigentes sobre 25.249 (99,8 %)**. La ubicación de cada línea se tomó del diff con `--unified=0`.

### Lectura sobre el texto (numeración de `6efbc1d`)

Se leyeron **las 54 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A, C y F completas, y las modificadas del resto en su texto entero (149.386 caracteres), además del diff palabra por palabra de cada una. Se cotejaron contra el informe LEE (`BO-Salta-1979_10642-10889_la-caldera_LEE-1979_2026-10-03.txt`, bajado de `corrige/lee/1979/`): §0, §1 en lo que hace al corpus, §A entero (33 fichas: FUENTE, FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1, B.2 entero (17 entradas), B.3, B.4, E.1, E.2 y E.3, y el `amplia-1979.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 439–444 | 6 | sesión |
| ape/C-normativa.tex | 26, 163–167 | 6 | sesión |
| ape/D-pedidos.tex | 62, 177, 192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 88–89, 91 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99, 103 | 3 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/09-defensas.tex | 535, 551, 637–638 | 4 | sesión |
| cap/10-expropiacion.tex | 332, 513 | 2 | sesión |
| cap/15-hacienda.tex | 185, 187 | 2 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 381 | 1 | sesión |
| cap/18-politica.tex | 470, 531 | 2 | sesión |
| cap/19-resistencias.tex | 814 | 1 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 508, 545, 716 | 3 | sesión |
| cap/22-prospectiva.tex | 144, 203 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09-defensas:636 (el primer renglón del título de la ficha pluviométrica, para el hallazgo 3) y 549–550 (el superlativo del hormigón de 1980 que la línea 551 acota); 15-hacienda:172 y 186–192 (el decreto 1146 de 1980 y la cautela que sigue, para la anáfora que el AMPLÍA corrigió en la 187); 18-politica:529 (la renuncia de Mogro como juez de paz titular en 1983, a la que remite el «cuándo pasó a titular» de la 531); las filas de A de 1976 y 1977 que nombran a Armando Fernández y al observador pluviométrico; y el orden de `\input` de `main.tex` (09-defensas va antes que 17-aguabaja: la remisión nueva de la fase 6 no lleva «más adelante»).

**Esta ronda: 54 líneas nuevas**, 149.438 bytes sobre 3.009.305, que en las 923 páginas de la base equivalen a **45,8 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `6efbc1d` cae dentro de estos tramos.

Acumulado: 25.195 vigentes + 54 = **25.249 de 25.249 (100,0 %)**. La fase 6 toca cinco líneas, A:439, D:62, 01:139, 09:637 y 17-aguabaja:281, dentro de lo leído en esta ronda, y no cambia el largo de ningún archivo: **25.249 de 25.249 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1979 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 200 ppp con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión y se recortó con su contexto, y cada recorte de una cita se miró. Se bajaron 40 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 10668 | 4 | Decreto 1881-D, encabezado y cláusulas primera a tercera | «M. de B. Social - M. de Economía Nº 1881-D - 29-12-78»; «Programa Reacondicionamiento de Sistemas de Abastecimiento de Aguas con Captación Superficial», «aprobado por Ley Nº 5175, con fondos transferidos por la Dirección de Saneamiento de la Nación»; once localidades, «La Caldera y Vaqueros»; la Secretaría transfiere a la A.G.A.S. «Doce millones de pesos». La cita coincide (22-infraestructura:545); la fecha desmiente el «en 1979» de 01:139 (hallazgo 1). Las cláusulas segunda y tercera se leen en la imagen: el «leídos sobre el facsímil» de C:164 es cierto |
| 10702 | 5 | Decreto 195, visto, fecha y firmas | «el reciente operativo de movilización efectuado por las Fuerzas Armadas del País»; «Salta, 28 de febrero de 1979»; «DAVIDS (Int.)». Coincide (A:440, 18:470) |
| 10718 | 9 | Decreto 359, visto y considerando | \$20.000.000 a Inmuebles; «en razón de haberse invertido en su totalidad el último desembolso del crédito otorgado con tal destino por el Consejo Federal de Inversiones». Coincide (06:56) |
| 10730 | 10 | Licitaciones 2/79 y 3/79 | «Obras de emergencia» (2/79; la 3/79 imprime «Emergencia»), río Vaqueros - río Caldera, \$41.821.150, tres meses; Salta - río Vaqueros, \$24.481.450, cuatro meses. Coincide (09:535) |
| 10742 | 7 y 8 | Res. 290, renglones | Potabilizador del dique en la h. 7, \$144.000.000; toma y canal de aducción en la h. 8, \$2.050.000.000. Coinciden las cifras y las hojas de 10:513 y 22-infraestructura:545 |
| 10777 | 4 y 5 | Ley 5434, cláusula 2 del convenio y firma | «por el término de veinte (20) años»; «una superficie de 10 hectáreas de terreno aproximadamente lindantes con el Embalse de Campo Alegre», «destinados a desarrollar la infraestructura requerida para llevar a cabo actividades náuticas»; «hasta tanto se concreten las obras definitivas», «una parcela de aproximadamente 50 x 50 metros ubicada en la margen derecha de la presa principal»; el convenio, «a los veinte días del mes de junio de mil novecientos setenta y siete». Coincide (A:441, C:165, 06:56, 17-tierrafiscal:381) |
| 10806 | 11 | Decreto 1023 | 2 ha 1151,39 m², matrícula 1782, «Escuela de Deportes Náuticos del Dique Campo Alegre». Coincide (A:441, C:166) |
| 10826 | 11 | Decreto 1184, convenio, cláusulas primera, segunda, tercera, sexta y octava | pagarés «con vencimiento a los seis (6) meses», «seis por ciento (6%) anual, con más la incidencia del impuesto al valor agregado», índice «de precios mayoristas nivel general, producido por el INDEC», pagarés «a la orden de Caminos S.A.» por los certificados de obra. Coincide (10:513, C:167). La h. 10 trae otro convenio de pagarés, con Construcnort, que no es el de Campo Alegre |
| 10829 | 10 | Decreto 1238 | «de acuerdo a las conclusiones arribadas en el sumario administrativo instruido mediante resolución ministerial Nº 2059». Coincide (26:235); el regente va sin nombre en el libro |
| 10869 | 8 | Ley 5488, artículo 1 y convenio | Convenio de la Universidad de Buenos Aires, la Secretaría de Estado de Salud Pública de la Nación y el Ministerio, «tendiente al desarrollo de un Programa de Educación Médica Continua en la citada Provincia». Coincide con «programa» de A:439 y con «convenio» de 04:4599 |
| 10873 | 8 | Ordenanza 021/78, trabajos públicos | «TRABAJOS PUBLICOS 22.766.816»; «Remodelación y Ampliac. Edificio Municipal 15.357.141». Coincide (15:185) |
| 10875 | 7 y 8 | Decretos 1675 y 1676 | «Subof. My. (R.) Dn. Armando Fernández»; «razones de índole personal»; «dándosele las gracias por los servicios prestados»; «todas aquellas facultades inherentes al Concejo Deliberante». Coincide (A:443, 18:470) |
| 10880 | 6 | Decreto 1705, visto | «perilagos de los diques de Cabra Corral y Campo Alegre y hasta tanto el Consejo Federal de Inversiones transfiera los préstamos ya otorgados». Coincide (06:56) |
| 10885 | 8 | Ley 5504, anexo | «La población de recursos menores dispone únicamente, de 3 balnearios públicos, el Balneario Municipal, el Balneario de Vaqueros y la Pileta Municipal Plaza Alvarado, los que en la actualidad son insuficientes y se hallan precariamente acondicionados». Coincide (A:439, 06:56) |
| 10885 | 14 a 17 | Ley 5505, anexo y contrato | «al tomar aguas de los ríos Angostura y La Caldera»; «en el que se halla ubicado el embalse»; 3.609, 12.537 y 206.458, «un total de 222.602»; \$91.000.000 en las hojas 15 a 17. Coincide (A:444, C:167, 06:56). La foliación de la ficha (h. 11 a 17) coincide con el PDF |

Son **16 citas entre comillas del libro cotejadas en la imagen** (contadas una vez por pasaje; los nombres propios entre comillas como «El Mollar» o «Santa Mónica» no se cuentan): todas las citas que el AMPLÍA agregó, **ninguna con diferencias**, y datos sin comillas en 7 hojas (10668 h4, 10742 h7 y h8, 10777 h4 y h5, 10826 h11, 10873 h8). Bajadas y no cotejadas: 10642, 10653, 10654, 10685, 10695, 10696, 10701, 10704, 10714, 10723, 10756, 10764, 10767, 10784, 10799, 10801, 10820, 10821, 10830, 10838, 10849, 10852, 10863, 10866, 10879 y 10881 (fichas de MODO imagen, sin cita entre comillas en el libro; no se buscó el renglón).

### Hallazgos (cuatro, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 01:139 | «y en 1979 pone a La Caldera y a Vaqueros en un programa provincial de reacondicionamiento de sus sistemas de agua»: el decreto 1881-D es del 29 de diciembre de 1978 (10668 h4, imagen) y se publica el 7 de febrero de 1979; la serie de la frase fecha cada acto por el año del acto (la red «que adjudica en diciembre» de 1977), y el propio libro lo da como de diciembre de 1978 en 22-infraestructura:545 y C:164 | 3 | «y por un decreto de fines de 1978, publicado en 1979, pone a La Caldera y a Vaqueros en un programa …, y en 1979 afecta …» |
| 2 | 17-aguabaja:281 | «lo demás que el año trae del agua es de la Provincia: la toma y el canal del embalse y un programa …»: afirmación de universo que el propio libro desmiente, porque 09:535 da las dos defensas de la ruta 9 sobre los ríos Caldera y Vaqueros que licita la Dirección Nacional de Vialidad en 1979 («dos que no son de la Provincia»), y el mismo párrafo cuenta las defensas entre lo que trae cada año del agua (1975 y 1977) | 5 | «lo demás que el año trae del agua es de la Provincia o de la Nación: la toma y el canal del embalse, un programa provincial …, y las defensas sobre los ríos Caldera y Vaqueros que licita la Dirección Nacional de Vialidad», con la remisión al capítulo \ref{cap:defensas} |
| 3 | 09:637 y D:62 | El AMPLÍA quitó el «al menos» del título de la ficha pluviométrica y del pedido: «Había una estación pluviométrica … con un observador pago por la Provincia, de 1976 a 1980» y «en funcionamiento con observador pago de 1976 a 1980». Con 1979 hallado el hueco del medio se cierra, pero los bordes no: 1958 a 1975 se leyeron con pendientes y no admiten ausencias, y 1981 a 2012 sólo tienen consultas puntuales; la frase pasa a afirmar el universo entero de la serie | 5 | «al menos de 1976 a 1980» en los dos lugares, como estaba antes del AMPLÍA |
| 4 | A:439 | «y el de los derechos y acciones de Vicente Delfín Tejerina sobre dos inmuebles del partido de La Calderilla»: un remate en un juicio ejecutivo (aviso 36683, Nº 10879, h. 21 y 22: «juicio ejecutivo seguido contra Vicente Delfín Tejerina»), en un registro de 1979, con la persona nombrada; puede estar viva por la regla de los 100 años. Es exactamente el caso del control de P102, que el AMPLÍA no corrió | 15 | «y el de los derechos y acciones de un particular sobre dos inmuebles rurales del partido de La Calderilla, en un juicio ejecutivo» |

Resta: una fecha de publicación dada como fecha del acto, en el aspecto 3: **resta 5** (95). Un universo afirmado que el libro desmiente con su propio dato (hallazgo 2), **resta 10**, y un universo afirmado sobre un período que el libro no midió entero (hallazgo 3, una sola afirmación en dos lugares), **resta 5**, en el aspecto 5 (85). Una persona que puede estar viva, nombrada en un contexto socioeconómico (hallazgo 4), en el aspecto 15: **resta 20** (70); no activa tope, que la gradación reserva a los atributos sensibles y a los menores. Ninguno de los cuatro sostiene una sección: no hay tope por alcance. **Ningún error de consistencia** en las 45,8 páginas: el aspecto 7 queda en 100 (el hallazgo 1 contradice a C:164 y a 22-infraestructura:545, a más de diez páginas, y resta en el aspecto más específico, el 3, como el hallazgo 4 de la ronda 65). Aplicados los cuatro: 100 en la nota final del 3 y del 5, y 90 en la del 15, el valor de las rondas anteriores.

**Errores introducidos por la propia auditoría**: los cuatro hallazgos están en el AMPLÍA 1979 (`6efbc1d`). **Ninguno lo atrapó un control automático**: el de P102 existe como pendiente pero no corre solo en el AMPLÍA, y no hay controles para la fecha de un acto dada por el año de su publicación ni para una salvedad de universo («al menos», «en lo hallado») que un AMPLÍA borra. P164 los propone. Los controles de P144 (comillas rectas), P158 (caracteres de control) y P159 (anáforas temporales: el AMPLÍA corrigió las dos que desplazó, 15:187 y 09:638) funcionaron en el AMPLÍA 1979.

**Descartados (falsos positivos, 7).** «Dos programas provinciales» (A:439) contra «un programa provincial … y un convenio con la Universidad de Buenos Aires» (04:4599): el convenio de la Ley 5488 es «tendiente al desarrollo de un Programa de Educación Médica Continua en la citada Provincia» (10869 h8, imagen); las dos formas valen. «Cláusulas primera y segunda leídos sobre el facsímil» (C:164), «artículo 1» (C:167) y «cláusulas de la cesión» (C:165), cuando el MODO de las fichas A.3, A.21 y B.2.7 dice que parte salió de la capa: en la imagen se leen enteras y coinciden, como dice C. «A La Caldera, en agosto, \$35.000.000» (15:185) con una resolución que ratifica lo actuado por la Secretaría: la fecha es la del acto publicado, y la cronología de la frase sigue la del acto. «Una resolución de agosto los lleva a \$6.450.000.000» (10:513), cuando la ficha B.2.9 dice que la Res. 474 «amplía» lo de mayo: la Res. 474 da el monto del renglón, y «los lleva» no dice si suma o reemplaza. Las partes de los tres juicios de posesión veinteañal nombradas en A:439 (en 1977 y 1978 iban sin nombre): una posesión alegada no es una ejecución ni una deuda, y P102 no la incluye; se deja anotado como criterio a unificar (P165). «Los dos que lo nombran» (04:4599), tras «ningún acto hallado del año nombra un establecimiento de salud»: «lo» es el departamento. «Quienes los seguían en jerarquía» (18:470): glosa del encargo del despacho al secretario de cada municipio, que el decreto da; no afirma un dato que el acto no tenga.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P164 (herramientas): dos controles más para AMPLÍA (extensión de P102, P149, P152, P158 y P159, y de la rúbrica AMPLÍA v2): (1) **fecha de acto y de publicación**: toda frase nueva que ponga un acto bajo «en <año>» se coteja con la fecha del acto en su ficha o en C, y si el acto es de otro año se escribe como en 15:185 y 22-infraestructura:545 («un decreto de fines de 1978, publicado en …»); caso, el 1881-D en 01:139 (ronda 66); (2) **salvedades borradas**: se listan las salvedades de universo que el diff del AMPLÍA quita («al menos», «en lo hallado», «en lo leído», «hasta donde», «por lo menos») y cada una se justifica o se repone; caso, 09:637 y D:62 (ronda 66). Y que el control de P102 corra como paso automático del AMPLÍA, no como pendiente. P165 (libro): unificar el criterio para las partes de los juicios de posesión veinteañal posteriores a 1945 (1977-1978 sin nombre; 1979, con nombre en A:439), con la regla que se adopte declarada en F o en el capítulo de método.

**Pendientes revisados sin cerrar.** P162 (lee, 1979: las fechas de publicación de ocho fichas; las cabeceras miradas en esta ronda —10702, 10777, 10806, 10875, 10885— coinciden con la tabla de tapas del §1, y A.17 sale en la 10806 del 30 de agosto, como dice P162). P163 (pedido de otro ejemplar de la 10808 h15: el libro no cita el número). P54 (1979 no nombra ningún establecimiento de salud del departamento). P100 y P118 (1979 en barrido, con el criterio de F, como dice `amplia-1979.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; los actos de 1979 que nombran el embalse no dan ninguna, y 10:513 es una línea que este AMPLÍA tocó: el aspecto 1 sigue en 82). P138, P139, P141, P145, P146, P153 y P154 (láminas, H y E: fuera del alcance de una auditoría). P140, P147, P155 y P161 (pedidos de D que el AMPLÍA no agregó para no mover el recuento de 284). P143, P148, P150, P151, P156, P157 y P160 (correcciones de los informes LEE). P102, P144, P149, P152, P158 y P159 (scripts de control).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.235/25.235 líneas vigentes en `7098d34` | 25.195 vigentes, 40 caducas por el AMPLÍA 1979 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*único*, *única*, *primer*, *primera*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *no lo dice*, *no trae*, *no interviene*, *no figura*, *no nombra*, *lo demás*, *ni los*, *hasta entonces*), sobre 4.205 palabras agregadas | 23 coincidencias, todas leídas | Ninguna cae por sí sola: las ausencias llevan su universo («ningún acto hallado del año», «lo hallado del año no lo dice», «en lo leído no hay»); «sólo la foliatura lo mostró» es de E.1; «hasta entonces» acota el superlativo minero de 22-prospectiva:203. El control **no atrapa** la exhaustividad del hallazgo 2 («lo demás … es de la Provincia»: la coincidencia «lo demás» salió, pero la desmiente un dato de otro capítulo) ni la salvedad borrada del hallazgo 3 (un borrado no deja palabra que buscar): se encontraron leyendo |
| Repaso de ventana: afirmaciones que cierran en 1978 (*a 1978*, *hasta 1978*, *1958 a 1978*) y que abren el hueco en 1979 (*1979--2012*, *1979 a 2012*, *treinta y cuatro años*, *sesenta y cuatro tramos*, *veintidós*, *veintiuno*, *10.641*) | libro entero | Ninguna queda sin actualizar: «1958 a 1978» queda sólo en F:88, que compara; los «treinta y cuatro» que quedan son de otros universos |
| Anáforas temporales en las líneas tocadas por el AMPLÍA (P159: *ese año*, *ese mismo año*, *el mismo año*, *esos años*, *ese mes*, *ese día*, *al año siguiente*, *un año después*, *entonces*, *otra vez*, *esta vez*) | 54/54 líneas; 39 coincidencias | Ninguna desplazada: los bloques de 1979 entraron al final de sus párrafos (06:56, 09:535, 15:185, 17-aguabaja:281, 18:470, 22-infraestructura:545, 26:235) o antes de una frase que no se apoya en el año (09:535, «Si alguna de las obras de 1969 a 1977…»); las dos que el AMPLÍA movió las corrigió él mismo (15:187, «En 1980, el año del decreto 1146»; 09:638, «esos años»); «otra vez» de 18:531 remite a la designación de 1967 |
| Comillas rectas que `babel` deforma (P144) | 25/25 comillas rectas del fuente | 0 en posición peligrosa; en el PDF compilado, 0 *Ç* y 0 *ç*, antes y después de la fase 6 |
| Caracteres de control en el diff (P158) | 54 líneas agregadas por el AMPLÍA y 5 de la fase 6 | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 339/339 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva:290 dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1979 (F:25–26, 88 y 91, 00:43, 02:28, 99 y 103, 01:119 y 139, 04:3659–3660, 20:880–881, 22-infraestructura:545, D:177, A:439) contra §0, §1, E.1, E.2, E.3 y §R del informe | 1 año | Tramos: 42 + 1 + 22 = 65; fuera de las ventanas, 1948 y 1958-1979 = 23. Ediciones: 10642–10889 = 248 números, sin ausentes. Hojas: 5.065 presentes, 16 repetidas en la 10885 (h25 a h40 = h9 a h24); folios 1 a 5.064; faltan 26 en 19 ediciones; diez ediciones de tapa impar. Capa 696 + OCR 4.369 = 5.065. Tapas: 89 en la imagen + 159 por OCR = 248. A ojos 99, dentro del intervalo de 00:43 (69 a 764); poca tinta 3.474. Discrepancias: 215, 21 sin resolver y 15 sin trabajar. Actos: 33 del §A y 17 de B.2. Días hábiles sin edición: 12. Hueco 1980–2012: 33 años. D:177: diecinueve cifras de hojas sin mirar para 1961-1979, cinco de poca tinta para 1975-1979 y la de páginas faltantes de 1979 (26) |
| Aritmética de 1979 | 10 cuentas | 108.432.287 − 106.399.442 = 2.032.845. 15.357.141 + 1.324.041 + 995.010 + 325.704 + 2.899.229 + 1.865.691 = 22.766.816. 31-7-1978 a 16-11-1979: quince meses y medio; 31-12-1978 a 16-11-1979: diez meses y medio. 3,15 / 6 = 0,525 y 0,26 / 0,5 = 0,52. 30.000 × 12 = 360.000. 3.609 + 12.537 + 206.458 = 222.604, contra los 222.602 impresos. 101 + 101 = 202 millones. 16-7 a 14-8: un mes. 6 ediciones de la 10830 a la 10835 (el aviso y cinco más); 6 de la 10879 a la 10884 (el aviso y cinco más); nueve ediciones de la 10881 a la 10889 (el aviso y ocho más). Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 66 | 50 de 96 cláusulas con cifra en el texto agregado | **50/50 con fuente localizable**: la cita en la cláusula, en la misma oración o en la misma fila, la fila de A a la que remite la fila de resumen, o, en las declaraciones de cobertura, el apéndice F y el informe que F cita (dos de las 50 son fragmentos de la lista palabra por palabra del diff, cifras de cobertura de D:177 y 00:43, con la misma fuente). 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 54 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 54 líneas, cruzadas con contextos sensibles (P102: *remate*, *ejecución*, *juicio ejecutivo*, *contra*, *deudor*, *embargo*, *cesante*, *sumario*) | 54/54 líneas | **1 caída**: Tejerina, junto a «remate» en A:439 (hallazgo 4). Sin nombre: el agente cesanteado, el oficial que renuncia, el regente cesanteado, los condenados de A.23 y B.2.13 (que el libro no trae), las partes del juicio laboral de «Lesser Lote E». Nombrados sin contexto sensible: funcionarios (Davids, Ulloa, Fernández, Camacho, Montero, los jueces de paz), los concesionarios y peticionantes de agua y de minas, las partes de las posesiones veinteañales (P165) y las empresas |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `6efbc1d` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos); 923 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin normas nuevas citadas en presente |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 1 (fecha de publicación dada como fecha del acto); aplicado. Las demás separan acto y publicación (Res. 784, «de fines de 1978 publicada en enero»; 1881-D en 22-infraestructura) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 16 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 85 | 100 | Hallazgo 2 (universo que el libro desmiente, −10) y hallazgo 3 (universo no medido entero, −5); aplicados |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 45,8 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P153 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 70 | 90 | Hallazgo 4 (persona que puede estar viva, nombrada junto a un remate en juicio ejecutivo, −20); aplicado |

**Nota inicial: 85,2 antes del tope y 85,2 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---las resoluciones de delegación del poder de policía sobre los áridos que prevé el decreto 553 de 1978, y ahora el texto del convenio de Salud Pública de 1978 sobre lo que el programa de reacondicionamiento hizo en La Caldera y en Vaqueros, dirían si el municipio intervino en algo de su agua---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro y dejar corriendo los controles de P102, P144, P152, P158, P159 y P164: sube el techo del 4 a 100 y vale +0,7; (5) publicar los scripts que faltan y extender las láminas a 1979 (P138, P145, P153): hasta +0,2 en el 13.

**Avance del libro:** 4 de 4 hallazgos resueltos (100 %); compila sin errores ni referencias indefinidas, 923 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1979 la Provincia pone a los dos municipios en un programa de reacondicionamiento de sus sistemas de agua, cede tierra del embalse a la Armada y a Deportes, y el municipio no interviene en ningún acto de agua o de suelo hallado; las defensas del año las licita la Nación), la tutela provincial sobre el fisco municipal (el presupuesto de 1978 de La Caldera se aprueba diez meses y medio después de cerrado el ejercicio, esta vez publicado entero) y la intervención continua de la Provincia en el gobierno municipal (licencias por la movilización militar, renuncia del presidente designado en 1976 y designación de su sucesor con las facultades del Concejo Deliberante).

**Calidad de la auditoría.** Cobertura de la ronda: 54 líneas (0,21 %; 45,8 páginas). Cobertura acumulada: 25.249 de 25.249 (100,0 %), con el registro de arriba. Falsos positivos descartados: 7. Recortes: no se cotejaron los renglones de las 26 ediciones bajadas sin cita entre comillas en el libro (fichas de MODO imagen); el control de privacidad de P102 y los dos de P164 se corrieron a mano en esta ronda, y el de superlativos no atrapa ni una exhaustividad que desmiente otro capítulo ni una salvedad borrada; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **4 de 4**, en el AMPLÍA 1979 (`6efbc1d`), **0 atrapados por un control automático**.

## Ronda 67 — auditoría con fase 6 (03/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1980. Base: commit `b0feac9` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1980, sobre `795e3db`, la ronda 66), con la fase 6 en `ronda-67.patch` (commit `05dc82a` en la sesión; aplica con `git am` sobre `b0feac9`, probado en un clon limpio de GitHub: árbol `99feb7b`). **Denominador medido: 25.264 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 66 (25.249 de 25.249, sobre `b59d55b`, que en GitHub es `795e3db`, con el mismo árbol `c77027b`) se trasladaron por diff a `b0feac9`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1980 agrega 15 líneas netas (5 en A, 8 en C y 2 en F, una de ellas en blanco) y deja 60 líneas nuevas o modificadas en 22 archivos: caducan 45 líneas anteriores**, y quedan **25.204 vigentes sobre 25.264 (99,8 %)**. La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `b0feac9`)

Se leyeron **las 60 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A y C completas y la de F (F:90), y las modificadas del resto en su texto entero (155.706 bytes), además de la lista de cada cambio palabra por palabra con su contexto (105 segmentos). Se cotejaron contra el informe LEE (`BO-Salta-1980_10890-11138_la-caldera_LEE-1980_2026-10-03.txt`, bajado de `corrige/lee/1980/`): §0, §1 entero (tabla de 249 tapas), §2, §A entero (30 fichas: FUENTE, FICHA, MODO DE LECTURA, TEXTO y NOTA), B.1, B.2 entero (10 entradas), B.3, B.4, §C, §P, E.1 a E.10, §F y §R, y el `amplia-1980.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 445–454 | 10 | sesión |
| ape/C-normativa.tex | 27–29, 54–55, 173–175, 273 | 9 | sesión |
| ape/D-pedidos.tex | 177, 192, 253, 260 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 90–91, 93 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 4599 | 3 | sesión |
| cap/05-tierra.tex | 285 | 1 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/09-defensas.tex | 535, 578, 594, 602, 611 | 5 | sesión |
| cap/10-expropiacion.tex | 332, 362, 513 | 3 | sesión |
| cap/14-poblacion.tex | 579 | 1 | sesión |
| cap/15-hacienda.tex | 175, 185 | 2 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 345 | 1 | sesión |
| cap/18-politica.tex | 470, 531 | 2 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09-defensas:536–566 (la ficha de la licitación 9/80 y sus tres observaciones, para la precisión a) y 549–551 (el superlativo del hormigón de 1980); 09-defensas:575–600 (el título «Tres cuencas en tres semanas» y el cuadro de los encauzamientos); 10-expropiacion:355–361 y el índice de secciones del capítulo (para los hallazgos 3 y 4: la adjudicación de 1974 a Caminos S. A. sólo está en la 513, y la 61 nombra la etapa B por la expropiación, no por la adjudicación); 26-presencia:225–234 y 236–249 (las dos estaciones sanitarias de 1935 y 1947 y el epígrafe de `fig:votado`, «Lo que se votó y lo que llegó, 1929–1949», para el hallazgo 5); 14-poblacion:579 entera y la fila de C de la Ley 5686 (20/11/1980, para el «casi cinco meses»); 18-politica:470 desde «Y dos nombres de estos años» hasta el fin (El Palenque, para el «escrito René»); 06-pdua:50–56 (los «tampoco» del plan de 1975 a 1979); 15-hacienda:185 en lo que da el camión de Vaqueros de 1979 (\$42.387.890); y el orden de `\input` de `main.tex`.

**Esta ronda: 60 líneas nuevas**, 155.706 bytes sobre 3.033.105, que en las 929 páginas de la base equivalen a **47,7 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `b0feac9` cae dentro de estos tramos.

Acumulado: 25.204 vigentes + 60 = **25.264 de 25.264 (100,0 %)**. La fase 6 toca seis líneas: A:445 y A:452, 10:362 y 10:513, 17-aguabaja:281 y 22-infraestructura:508, dentro de lo leído en esta ronda, y 26-presencia:236, que estaba vigente y se releyó como contexto; no cambia el largo de ningún archivo: **25.264 de 25.264 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Release 1980 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 200 ppp con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión y se recortó con su contexto, y cada recorte de una cita se miró. Se bajaron 34 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 10895 | 9 | Res. 1682-D, encabezado y texto | «Resolución Nº 1682-D - 27-12-79»; «Construcción de Defensas sobre el Río Vaqueros - Departamento La Caldera - Salta»; \$1.037.880, «por vía administrativa». La cita coincide (09:535); la fecha, con «una resolución de fines de 1979, publicada en enero» (A:451, 09:611). La siguiente es la 1683-D, del río El Naranjo |
| 10998 | 5 | Res. 323, considerando y planilla | «obras denominadas "Complejos Deportivos"»; «La Caldera \$ 100.000.000». Coincide (A:445, 15:185) |
| 11047 | 7 | Ley 5636, anexo | «durante el presente año mil novecientos setenta y nueve»; «Continuación de construcción de Estación turística - Dique de Campo Alegre (Dpto. La Caldera) (\$ 36.000.000)»; cabecera «Salta, 19 de agosto». Coincide (C:175, 06:56, F:90) |
| 11058 | 10 | Res. 554 | «cese de funcionamiento de la Oficina Seccional del Registro del Estado Civil y de la Capacidad de las Personas Nº 2081 de Vaqueros», «en mérito a las razones precedentemente enunciadas». Coincide (26:235, A:445) |
| 11133 | 5 | Decreto 1769, acta transcripta | «Consejo Asesor Municipal-Acta de Elección del Escudo» en el encabezado y «los miembros del Consejo Asesor Comunal Sres. Don Arturo Renée Fernández, Don Esteban Mogro, Don José Félix Robles, Don Esteban Muñóz» en el cuerpo; «convocados por el Sr. Presidentte de la Comisión Municipal … Don Diego Jorge Montero, en el despacho del mismo». Coincide (14:579, 18:470: «que Montero convoca en su despacho») |
| 11126 | 27 y 7 | Decretos 1712 y 1713 | «Acéptase la renuncia presentada por el Sub Oficial Mayor (R) Dn. Telmo Camacho», del 1-12-80, sin fecha de la renuncia; Michaux «a partir de la fecha en que tome posesión», con «todas aquellas facultades inherentes al Concejo Deliberante». Coincide con A:453 y 18:470; desmiente el «Camacho renuncia en diciembre» de A:445 (hallazgo 1) |
| 11111 | 12 y 13 | Res. 1181-D | «Aprobar, los contratos de locación de obra, celebrados entre el señor Secretario de Estado de Hacienda y Economía … y las personas que seguidamente se identifican», del 7-11-80, sin fecha de los contratos; el renglón de La Caldera en la h. 13. Desmiente el «la Provincia contrata en noviembre» de A:445 (hallazgo 2) |
| 11059 | 7 | Ordenanza 028/79, firmas | «Diego Jorge Montero, Presidente Comisión Municipal - La Caldera»; «Rodolfo Marcelo Cointte, Subof. My. (R), Secretario Administrativo». Coincide (A:450, C:27, 15:175, 18:470) |
| 10955 | 8 y 9 | Res. 163, planillas | Agua corriente, sub-parcial 2, «Proyecto Establecimiento Potabilizador Dique Ing. José Alfonso Peralta - La Caldera», «300.000.009» en la columna R. G.; el parcial, 300 + 14 + 57 + 9 + 100 = 480 millones, decide 300.000.000. Obras hidráulicas en la h. 9 (pág. 1227), sub-parcial 1, «Toma y Canal de Aducción - Embalse Ing. José Alfonso Peralta - La Caldera», 4.060.000.000, en la columna R. G. Coincide (A:447, C:174, 10:362, 22-infraestructura:545) |
| 10966 | 6 | Licitación 9/80 | «obras en la Ruta 9. Tramo: Río Caldera - Alto de la Sierra (construcción defensas de hormigón)»; \$62.264.460; cuatro meses; apertura el 9 de mayo. Coincide con A:448 y 09:539–558; el acto no dice que las defensas sean «sobre el río Caldera» (precisión a) |
| 10918 | 14 | Decreto 133, artículo 1 | La Caldera y Chicoana «a partir del 1 de diciembre de 1979 hasta el 31 de diciembre de 1980», y desde el 14 de enero Capital, Rosario de Lerma, Cerrillos, Guachipas y La Viña; «las hectáreas afectadas superan las 2.000». Coincide (A:446, C:173, 05:285, D:260) |
| 10904 | 5 | Decreto 12, artículos 1 y 2 | «desde el 1º de Diciembre de 1979, por el término de seis (6) meses, a las localidades de La Caldera y Chicoana». Coincide (A:446, C:173) |
| 11114 | 13 | Decreto 1591 | 1½ ha del catastro 1575, «sobre el perilago del Dique Ing. Alfonso Peralta», «Plano Nº 148 inserto a fs. 5», «con carácter revocable y por el término máximo de cinco (5) años». Coincide con C:273 y 17-tierrafiscal:345; A:452 decía «por cinco años» (precisión b) |
| 11125 | 10 | Ordenanza 032/80 | «Almirante Guillermo Brown», de la avenida General Martín Miguel de Güemes, frente a los catastros 533 y 546, a la margen derecha del río «Caldera», frente a los 544 y 545, «en uso de facultades conferidas por Decreto Nº 1676/79». Coincide (C:28, A:454) |
| 10891 | 5 y 9 | Decreto 1788, saldos y deuda | Saldos 5.104.235 + 16.151 + 3.000.000 + 170.000 = 8.290.386 y «TOTAL \$ 8.290.879»; «Municipalidad de La Caldera 119.530». Coincide (C:54, 15:185, A:450) |
| 11073 | 8 | Res. 943-D | «Resolución Nº 943-D - 18-9-80»; «Encauzamiento sobre Río Vaqueros - Dpto. La Caldera», \$85.219.679. Coincide (A:451, 09:578, 594 y 602) |
| 11062 | 15 | Res. 914 | «3-9-80»; «Encauzamiento y defensa sobre Río La Caldera - Zona Campo Alegre», \$107.291.751. Coincide |
| 11126 | 28 | Res. 1282-D | «Dar por autorizado y cumplido el desempeño en la función de Regente del Instituto "Dr. Luis Linares"», del 3-12-80. Coincide (26:235, sin nombre) |
| 10953 | 7 | Decreto 434, artículo 1 | Fiori y Ferro Podestá, jueces de paz titular y suplente de Vaqueros, por dos años. Coincide (A:445, 18:470) |
| 10998 | 17 | Edicto 38439 | «Mojotoro» partido del mismo nombre, «Catastro Nº 132», hasta \$6.890.099,20; «En efecto [sic] de tal pago». Coincide (A:445, sin nombres) |
| 11107 | 19 | Remate 40211 | «otro ubicado en La Caldera con Base de \$ 508.666, catastro 668, sección "B", manzana 31 de La Caldera». Coincide (A:445, sin nombres) |
| 10937 | 34 | Aviso 37373 | «compra de un terreno de 4 ó 5 hectáreas en la localidad de Vaqueros», sin destino. Coincide (A:445) |

Son **9 citas entre comillas del libro cotejadas en la imagen** (contadas una vez por pasaje: «Construcción de Defensas sobre el Río Vaqueros» en 09:535; «Complejos Deportivos» en A:445 y 15:185; «presente año mil novecientos setenta y nueve» en C:175, 06:56 y F:90; «Consejo Asesor Comunal» en 14:579 y 18:470; «en mérito a las razones precedentemente enunciadas» en 26:235; los nombres propios entre comillas como «Mojotoro» o «Dr. Luis Linares» no se cuentan): todas las citas que el AMPLÍA agregó, **ninguna con diferencias**, y datos sin comillas en 17 hojas más (las de la tabla). Bajadas y no cotejadas renglón por renglón: 10890, 10893, 10899, 10919, 10945, 10954, 10968, 10984, 10988, 11000, 11019, 11057, 11091 y 11100 (el renglón se ubicó y se recortó, sin cita entre comillas en el libro; se miraron los de 10890, 10919, 11019, 11057, 11058 h11, 11091 y 11100, y coinciden con sus fichas).

### Hallazgos (cinco, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:445 | «\textbf{Municipio}: Camacho renuncia en diciembre a la presidencia de la comisión municipal de Vaqueros»: el decreto 1712 del 1 de diciembre «acepta la renuncia presentada», cuya fecha no da (11126 h27, imagen). Es la falla de la ronda 57 (hallazgo 3, P116) y de la 59 (hallazgo 3): la fecha del acto que acepta dada como la del acto aceptado. A:453 y 18:470 lo dicen bien | 3 | «en diciembre la Provincia le acepta a Camacho la renuncia a la presidencia …» |
| 2 | A:445 | «\textbf{Otros}: la Provincia contrata en noviembre a veintinueve personas»: la Res. 1181-D del 7 de noviembre aprueba contratos de locación de obra «celebrados» en una fecha que no da (11111 h12, imagen). La misma falla | 3 | «en noviembre la Provincia aprueba los contratos de locación de obra de veintinueve personas …, sin decir cuándo se celebraron ni para qué» |
| 3 | 10:513 | «En 1980 el plan de marzo le da \$4.060.000.000 (más abajo)»: el plan de 1980 está en 10:360–362, en la sección «Ocho años después, el dique tiene nombre», ciento cincuenta líneas más arriba. Remisión con la dirección invertida, agregada por este AMPLÍA | 12 | «(más arriba)» |
| 4 | 10:362 | «la etapa B que la Provincia había adjudicado en 1974 a Caminos S. A. (…; más arriba)»: la adjudicación de 1974 sólo está en 10:513, más abajo (la 61 nombra la etapa B por la expropiación). La remisión es del AMPLÍA 1973-1974 (`d99ba07`), y la ronda 61 no la vio; este AMPLÍA tocó la línea | 12 | «más abajo» |
| 5 | 26:236 | «La lámina \ref{fig:votado} pone las dos en la misma escala que el resto de lo que se votó»: «las dos» son las estaciones sanitarias de 1935 y de 1947 (26:234, «La de 1935 no dejó rastro; la de 1947 llegó»), y entre ellas y la lámina las incorporaciones posteriores a la ronda 38 (`ae1f0b7`, donde todavía estaban juntas) pusieron el párrafo de 1952 a 1980; con el AMPLÍA 1980 lo que queda inmediatamente antes son «las razones precedentemente enunciadas» del Registro Civil. Anáfora desplazada, como las de la ronda 65 | 7 | «pone las dos estaciones sanitarias, la de 1935 y la de 1947, en la misma escala …» |

**Precisiones aplicadas sin restar.** (a) La licitación 9/80 de Vialidad es «en la Ruta 9. Tramo: Río Caldera - Alto de la Sierra (construcción defensas de hormigón)» (10966 h6, imagen); el capítulo de defensas dice que lo que se defiende es la traza vial (09:556–558). A:445, 17-aguabaja:281 y 22-infraestructura:508 la daban «sobre el río Caldera»: pasan a «del tramo de la ruta 9 que empieza en el río Caldera» o equivalente. Las dos de 1979 (2/79 y 3/79), que el libro da «sobre» los ríos por los tramos que terminan en ellos, se dejan como están y se anotan en P170. (b) A:452 decía que el permiso precario del Club de Regatas era «por cinco años»; el decreto dice «por el término máximo de cinco (5) años» (11114 h13), como C:273 y 17-tierrafiscal:345: «por cinco años como máximo».

Resta: dos fechas del acto que acepta o aprueba dadas como las del acto aceptado o aprobado, en el aspecto 3: **resta 10** (90). Dos remisiones internas con la dirección invertida, en el aspecto 12, por analogía con la remisión a un capítulo posterior sin marcar: **resta 10** (90). Una anáfora desplazada, en el aspecto 7: **1 error en 47,7 páginas = 2,1 por cada 100** → escalón de ≤ 4 (**50**); no se resta el escalón adicional, porque no contradice material del libro sino que deja sin antecedente una palabra. Ninguno sostiene una sección: no hay tope por alcance. Aplicados los cinco: 100 en la nota final del 3, del 7 y del 12.

**Errores introducidos por la propia auditoría**: los cinco. Tres están en el AMPLÍA 1980 (`b0feac9`: hallazgos 1, 2 y 3); uno en el AMPLÍA 1973-1974 (`d99ba07`, hallazgo 4), en una línea que este AMPLÍA tocó; y uno se fue armando con las incorporaciones de las rondas 39 a 66 (hallazgo 5). **Ninguno lo atrapó un control automático**: el de anáforas de P159 busca anáforas temporales y no las pronominales («las dos»), que P169 propone; ninguno mira la dirección de «más arriba» y «más abajo»; y el de fecha de acto y publicación de P164 no mira la fecha del acto aceptado o aprobado. P170 los propone. Los controles de P144 (comillas rectas), P158 (caracteres de control), P164 (salvedades borradas: ninguna) y P102 (privacidad) funcionaron en el AMPLÍA 1980.

**Descartados (falsos positivos, 6).** «Lo demás que el año trae del agua es de la Provincia o de la Nación: …» (17-aguabaja:281), que no nombra el proyecto de la potabilizadora de la Res. 163 ni la defensa del Vaqueros de la 1682-D, publicada en enero: la afirmación es sobre quién actúa, y los dos son de la Provincia; la de 1979 tampoco nombra la potabilizadora de la Res. 290, y la ronda 66 la dejó así. «Un Consejo Asesor Comunal de cuatro vecinos» (14:579): el acta nombra cuatro miembros, y la ley que el mismo párrafo cita los crea «de vecinos». «Casi cinco meses antes de la Ley 5686»: del 30 de junio al 20 de noviembre (C:317), cuatro meses y veinte días. «Nominalmente, el doble del presupuesto municipal sancionado en 1979» (A:451): \$527.621.981 contra \$258.178.081, 2,04. «La asignación más alta de los cuarenta y cuatro municipios de esa prioridad» (A:445, 15:185): la siguiente es Cachi, \$68.000.000 (LEE A.11), y el universo está declarado. El catastro 132 del embargo de «Mojotoro» y el 668 del remate (A:445): el libro da los catastros y no los nombres, como en los remates de 1953, 1965, 1970 y 1979; llegar a las personas exige la fuente citada, y la gradación no identifica a nadie por figurar en una fuente pública citada.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P170 (herramientas): tres controles más para AMPLÍA (extensión de P164, P169 y de la rúbrica AMPLÍA v2) y uno de `registrar`. (1) **Dirección de las remisiones internas**: toda «más arriba» o «más abajo» de una línea que el AMPLÍA agrega o toca se resuelve a la línea del referente, y el script compara la posición (casos: 10:513 y 10:362, ronda 67). (2) **Fecha del acto aceptado o aprobado**: en las filas de resumen y en el texto nuevo, «renuncia», «contrata», «celebra», «firma» o «sanciona» bajo una fecha se cotejan con la ficha, y si el acto sólo da la fecha de la aceptación o de la aprobación se escribe así (casos: A:445, Camacho y la Res. 1181-D, ronda 67; antes, P116). (3) **Tramos de ruta**: una licitación vial por tramo se describe por su tramo, no por el río que lo limita; revisar con eso las dos de 1979 en 09:535, 01:139, 17-aguabaja:281, 22-infraestructura:508 y A:439. (4) **Pendientes duplicados en `estado.json`**: diecisiete identificadores figuran dos veces con el mismo contenido (P58, P59, P80, P87, P123, P124 y P159 a P169); `registrar` tendría que agregar un pendiente sólo si su id no está.

**Pendientes revisados sin cerrar.** P166 (láminas de 1979 y 1980: sin cambio en esta ronda; la licitación 9/80, si entra en `fig:votado`, va como defensa del tramo de la ruta 9). P167 (apéndices H y E de 1980). P168 (pedidos de 1980 que el AMPLÍA no agregó a D para no mover el recuento de 284: siguen fuera, y 22-prospectiva:290 cierra con 284 ítems). P169 (anáforas pronominales: el hallazgo 5 es un caso más). P54 (1980 no nombra ningún establecimiento de salud del departamento; 04:4599 y 21:87 lo dicen con su universo). P100 y P118 (1980 en barrido, con el criterio de F, como dice `amplia-1980.json`). P115 (10:513 sigue sin fuente para capacidad, espejo, profundidad y cota; los actos de 1980 que nombran el embalse no dan ninguna, y 10:513 es una línea que este AMPLÍA tocó: el aspecto 1 sigue en 82). P40 (la muestra de trazabilidad no se rehízo). P102, P144, P158, P159, P164 y P165 (controles: corrieron; 1980 no trae posesiones veinteañales).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.249/25.249 líneas vigentes en `795e3db` | 25.204 vigentes, 45 caducas por el AMPLÍA 1980 |
| Superlativos, cierres y ausencias en el texto agregado por el AMPLÍA (*único*, *única*, *primer*, *primera*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *no lo dice*, *no trae*, *no interviene*, *no figura*, *no nombra*, *lo demás*, *ni los*, *hasta entonces*, *más alta*, *mayor*, *doble*, *otra vez*, *vuelve*, *no se publica*, *no publica*, *no transcribe*, *no explica*, *por qué*), sobre 4.129 palabras agregadas | 30 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («ningún acto hallado del año», «en lo hallado de 1980», «en lo leído no hay»); «la única cifra que la imagen deja en duda» es de E.8 y §F7; «la asignación más alta» declara su universo; «mayor» es el grado de suboficial; «el doble» cierra (2,04) |
| Salvedades de universo que el diff del AMPLÍA quita (P164: *al menos*, *en lo hallado*, *en lo leído*, *hasta donde*, *por lo menos*, *con pendientes*, *salvo*, *unos*, *unas*), sobre 185 palabras quitadas | 0 coincidencias | Ninguna salvedad borrada |
| Fecha del acto y de su publicación en el texto nuevo (P164) | 10 filas de A, 9 de C y las frases nuevas de 01, 05, 06, 09, 10, 14, 15, 18, 22 y 26 | Los actos de fines de 1979 publicados en 1980 van como tales (1788, 1682-D, 1699-D: «de fines de 1979, publicado en enero»); 1146 y 1147 van por su fecha (15-8), con la publicación del 4-9 en C. Caen dos casos de otra clase, la fecha del acto que acepta o aprueba (hallazgos 1 y 2) |
| Anáforas en las líneas tocadas por el AMPLÍA (P159 y P169: *ese año*, *ese mismo año*, *el mismo año*, *esos años*, *estos años*, *ese mes*, *ese día*, *al año siguiente*, *un año después*, *entonces*, *otra vez*, *esta vez*, *las dos*, *los dos*, *ambos*, *ambas*, *el anterior*, *la anterior*, *el siguiente*, *la siguiente*, *más arriba*, *más abajo*, *enseguida*), con la línea siguiente | 60/60 líneas y sus siguientes; 104 coincidencias | 3 caídas: 26:236 «las dos» (hallazgo 5), 10:513 «más abajo» y 10:362 «más arriba» (hallazgos 3 y 4). Las dos que el AMPLÍA movió las corrigió él mismo (14:579 y 09:611, según `amplia-1980.json`); «enseguida» de 18:470 remite a El Palenque, que sigue en el mismo párrafo; «Y dos nombres de estos años» de 18:470 sigue apoyándose en los años del párrafo; el resto, en su frase |
| Comillas rectas que `babel` deforma (P144) | 2 comillas rectas en las líneas agregadas por el AMPLÍA, 0 en la fase 6 | Las 2 son la cita «\textit{"GUSTAVO MARTINEZ ZUVIRIA", …}» de 21:87, que ya estaba; en el PDF compilado, 0 *Ç* y 0 *ç*, antes y después de la fase 6 |
| Caracteres de control en el diff (P158) | 60 líneas agregadas por el AMPLÍA y 7 de la fase 6 | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 342/342 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva:290 dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Recuentos de 1980 (F:25–26, 90 y 93, 00:43, 02:28 y 99, 01:119 y 139, 04:3659–3660, 20:880–881, 22-infraestructura:545, D:177 y 192, A:445) contra §0, §1, §2, E.1, E.2, E.3, E.4, E.8 y §R del informe | 1 año | Tramos: 42 + 1 + 23 = 66; fuera de las ventanas, 1948 y 1958-1980 = 24. Años sin leer de corrido: 1981 a 2012 = 32. Ediciones: 10890–11138 = 249 números, sin ausentes. Hojas: 5.022; capa 581 + OCR 4.441 = 5.022; folios 1 a 5.132; faltan 11 en 3 ediciones (8 en la 10997, 2 en la 10937, 1 en la 11057); 82 ediciones de tapa impar y 13 con salto de dos. Días hábiles sin edición: 12, 10 explicados por el calendario escolar. Tapas: 249 en la imagen, 24 fechas arrastradas por el OCR. A ojos 90; poca tinta 3.725. Discrepancias: 147, 35 sin resolver. Fichas: 30 del §A y 10 del §B. D:177: veinte cifras de hojas sin mirar para 1961 a 1980, seis de poca tinta para 1975 a 1980 y diecisiete de páginas faltantes para 1964 a 1980 |
| Repaso de ventana: afirmaciones que cierran en 1979 (*1958 a 1979*, *1958--1979*, *hasta 1979*, *a 1979*) y que abren el hueco en 1980 (*1980--2012*, *1980 a 2012*, *1980 y 2012*, *treinta y tres años*, *sesenta y cinco tramos*, *veintidós tramos*, *veintitrés tramos*, *10.889*, *posterior a 1979*, *desde 1980*, *1980 en adelante*) | libro entero | Ninguna queda sin actualizar: «1958 a 1979» queda sólo en F:90, que compara; «10.889» y «10889», en 00:43, A:439 y F:88, como límite de 1979; «desde 1980, hormigón» (G:467) es del material |
| Aritmética de 1980 | 11 cuentas | 335.110.551 + 107.291.751 + 85.219.679 = 527.621.981. 527.621.981 / 258.178.081 = 2,04. 27-8 a 18-9: 22 días. 5.104.235 + 16.151 + 3.000.000 + 170.000 = 8.290.386, contra 8.290.879 impreso. 300 + 14 + 57 + 9 + 100 = 480 millones. 4.060 + 1.493 + 630 + 756 + 525 + 1.000 = 8.464 millones. 27-7-1979 a 28-11-1979: cuatro meses. 30-6 a 20-11-1980: cuatro meses y veinte días. 31-12-1978 a 18-12-1979: once meses y medio, «casi un año después de cerrado el ejercicio». 42 + 1 + 23 = 66. 581 + 4.441 = 5.022. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 67 | 50 de 519 cláusulas con cifra en las 60 líneas | **50/50 con fuente localizable**: la cita en la cláusula, en la misma oración o en la misma fila, o, en las declaraciones de cobertura, el apéndice F y el informe que F cita. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115, 10:513, en una línea que este AMPLÍA tocó) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 60 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 60 líneas, cruzadas con contextos sensibles (P102: *remate*, *ejecución*, *juicio ejecutivo*, *contra*, *deudor*, *embargo*, *cesante*, *cesantía*, *sumario*, *renuncia*) | 60/60 líneas | 0 caídas. Sin nombre: los herederos del embargo de «Mojotoro», el demandado del remate del catastro 668, los cuatro policías (retiro, renuncia y dos cesantías), la regente y la subregente del hogar, el contratado de La Caldera. Nombrados sin contexto sensible: funcionarios (Ulloa, Davids, Müller, Folloni, Montero, Camaño, Camacho, Michaux, los jueces de paz Fiori y Ferro Podestá), los cuatro del Consejo Asesor Comunal y el peticionante de agua de 1979. La renuncia de Camacho es a un cargo público |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `b0feac9` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos); 929 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin normas nuevas citadas en presente; la Ley 5686 va en pasado |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 1 y 2 (fecha del acto que acepta o aprueba dada como la del acto aceptado o aprobado, −5 cada uno); aplicados. Los actos de fines de 1979 publicados en 1980 separan acto y publicación |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 9 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Las ausencias de 1980 llevan su universo, ninguna salvedad borrada, el superlativo del F.D.M. declara el suyo; la precisión a no resta |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 50 | 100 | 1 error en 47,7 páginas (2,1 por 100): escalón de ≤ 4; aplicado |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 90 | 100 | Hallazgos 3 y 4 (remisiones internas con la dirección invertida, −5 cada una); aplicados. 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P153 y P166 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 60 líneas; 90 como en la ronda 66 |

**Nota inicial: 83,0 antes del tope y 83,0 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---las resoluciones de delegación del poder de policía sobre los áridos que prevé el decreto 553 de 1978, o, desde 1980, la Resolución Municipal 021/80 del certamen del escudo y el expediente 53-15091/79 del presupuesto que firma Montero, que dirían qué hacía el municipio por sí mismo bajo las facultades del decreto 1676/79---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:513 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro y dejar corriendo los controles de P164, P169 y P170 como paso automático del AMPLÍA: hasta +0,7 en el 4 y, sobre todo, que los hallazgos de cada ronda pasen a «atrapados»; (5) llevar a las láminas la extensión de P153 y P166: +0,2 en el 13.

**Avance del libro:** 5 de 5 hallazgos resueltos (100 %) y dos precisiones aplicadas; compila sin errores ni referencias indefinidas, 929 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (entre fines de 1979 y septiembre de 1980 la Provincia aprueba por vía administrativa una defensa y tres encauzamientos sobre los ríos del departamento y da un permiso sobre el perilago, y el municipio no interviene en ninguno), la tutela provincial sobre el fisco municipal (los tres presupuestos atrasados del departamento se publican enteros, y el de La Caldera de 1979 lo firma un presidente designado cuatro meses después de su fecha) y la intervención como régimen municipal (Vaqueros pasa de un suboficial retirado a otro con las facultades del Concejo, y el Consejo Asesor Comunal de La Caldera se reúne antes de la ley que lo generaliza).

**Calidad de la auditoría.** Cobertura de la ronda: 60 líneas (0,24 %; 47,7 páginas). Cobertura acumulada: 25.264 de 25.264 (100,0 %), con el registro de arriba. Falsos positivos descartados: 6. Recortes: no se cotejaron renglón por renglón las 14 ediciones bajadas sin cita entre comillas en el libro (fichas de MODO imagen; siete se miraron en el recorte); los controles de P164, P169 y P170 se corrieron a mano en esta ronda; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **5 de 5**, tres en el AMPLÍA 1980 (`b0feac9`), uno en el AMPLÍA 1973-1974 (`d99ba07`) y uno acumulado por las incorporaciones de las rondas 39 a 66, **0 atrapados por un control automático**.

## Ronda 68 — auditoría con fase 6 (04/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1981-1983. Base: commit `58b897f` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1981-1983, sobre `f5125e8`, la ronda 67), con la fase 6 en `ronda-68.patch` (commit `810d4a5` en la sesión; aplica con `git am` sobre `58b897f`, probado en un clon limpio de GitHub: árbol `ec3867c`). **Denominador medido: 25.306 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 67 (25.264 de 25.264, sobre `05dc82a`, que en GitHub es `f5125e8`, con el mismo árbol `99feb7b`) se trasladaron por diff a `58b897f`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1981-1983 agrega 42 líneas netas (10 en A, 14 en C, 2 en F, 11 en 09, 2 en 10 y 3 en 18) y deja 95 líneas nuevas o modificadas en 24 archivos: caducan 53 líneas anteriores**, y quedan **25.211 vigentes sobre 25.306 (99,6 %)**. La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `58b897f`)

Se leyeron **las 95 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A, C, F, 09, 10 y 18 completas, y las modificadas del resto en su texto entero (193.089 bytes), además de la lista de cada cambio palabra por palabra con su contexto (180 segmentos, 8.040 palabras agregadas). Se cotejaron contra los tres informes LEE (`BO-Salta-1981_11139-11385_la-caldera_LEE-1981_2026-10-03.txt`, `BO-Salta-1982_11386-11632_la-caldera_LEE-1982_2026-10-04.txt` y `BO-Salta-1983_11633-11880_la-caldera_LEE-1983_2026-10-04.txt`, de `corrige/lee/`): la lista entera de fichas (130: §A y §B.2 de los tres años, FUENTE y FICHA), el TEXTO y la NOTA de las fichas que sostienen afirmaciones con cifra o fecha (1981 A.1 a A.3, A.7 a A.9, A.17 a A.20, A.27, A.30, B.2.2; 1982 A.8, A.20, A.21, A.25, B.2.4, B.2.9; 1983 A.1, A.16, A.34, A.38, B.2.3), E.4 de 1983 y §0 y §R de los tres, el informe LEE de 1980 (A.11, Res. 323) y `amplia-1981-1983.json` de `corrige/amplia/`.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 455–468 | 14 | sesión |
| ape/C-normativa.tex | 28, 31–32, 34–36, 62, 281–287 | 14 | sesión |
| ape/D-pedidos.tex | 62, 156, 160, 177, 192, 243, 253 | 7 | sesión |
| ape/E-personas.tex | 99 | 1 | sesión |
| ape/F-fuentes.tex | 25–26, 92–93, 95 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 2075, 3659–3660, 4599 | 4 | sesión |
| cap/05-tierra.tex | 285 | 1 | sesión |
| cap/06-pdua.tex | 56 | 1 | sesión |
| cap/09-defensas.tex | 535, 619–629, 648 | 13 | sesión |
| cap/10-expropiacion.tex | 67–68, 92, 117, 334, 515 | 6 | sesión |
| cap/14-poblacion.tex | 159, 517 | 2 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/17-tierrafiscal.tex | 381 | 1 | sesión |
| cap/18-politica.tex | 470, 474, 481, 487–488, 501, 533, 667–668, 724 | 10 | sesión |
| cap/19-resistencias.tex | 869 | 1 | sesión |
| cap/20-opacidad.tex | 880–881, 1038 | 3 | sesión |
| cap/21-ausencias.tex | 87 | 1 | sesión |
| cap/22-infraestructura.tex | 508, 545 | 2 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 10-expropiacion:40–66 (los cinco incisos de la Ley 4486, el mecanismo de pago y la asimetría, para la precisión a y para «el catastro 1576 y las otras cuatro propiedades de la ley»); 09-defensas:600–618 (las del camino y las de los ríos, antes de «Y en 1981 Vialidad Nacional vuelve a licitar»); 15-hacienda:185 en lo que da la Res. 323 de 1980 (hallazgo 1); 18-politica:470 desde 1980 («Arturo Renée Fernández … escrito René»), 478–487 (la ficha de la Ley 6131 y «Eso confirma»), 718–724 (Galli y las designaciones de 1983 a 1987) y la tabla de intendencias (661–669); 14-poblacion:150–159; 19-resistencias:869 entera; 20-opacidad:1030–1038; E:150–157; 17-tierrafiscal:376–381; y el orden de `\input` de `main.tex`.

**Esta ronda: 95 líneas nuevas**, 193.089 bytes sobre 3.079.879, que en las 943 páginas de la base equivalen a **59,1 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `58b897f` cae dentro de estos tramos.

Acumulado: 25.211 vigentes + 95 = **25.306 de 25.306 (100,0 %)**. La fase 6 toca siete líneas: C:31, 10:67, 15:185, 17-tierrafiscal:381, 18:470 y 26:235, dentro de lo leído en esta ronda, y 10:64, que estaba vigente y se releyó como contexto; no cambia el largo de ningún archivo: **25.306 de 25.306 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1980 a 1983 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 200 ppp (250 en la planilla de la Res. 323) con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión, se recortó con su contexto y cada recorte se miró. Se bajaron 15 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 11484 | 6 | Decreto 432, considerando | «por no haber finalizado los juicios de expropiación respectivos». Coincide (A:461, 10:67) |
| 11612 | 11 | Res. 1071-D | «M. de Bienestar Social - Resolución Nº 1071-D - 22-11-82»; «Con vigencia al 1º de octubre y hasta el 31 de diciembre del año en curso, designar en carácter de personal temporario, a los empleados … quienes vienen desempeñándose en el perilago del Dique Campo Alegre, dependiente de la Dirección General de Deportes y Recreación». La cita coincide (17-tierrafiscal:381); desmiente «en noviembre esa Dirección toma» (hallazgo 2) |
| 11683 | 13 | Decreto 1486, art. 2 | «las Oficinas Seccionales que se detallan a continuación no integran el presente Cuadro de Cargos pero continuarán funcionando bajo la modalidad que se menciona: Oficina Seccional Vaqueros, a cargo de la autoridad municipal». La cita coincide (26:235); «como hasta entonces» no está en el acto (precisión c) |
| 11849 | 8 | Decreto 1700, art. 7 | «jefe Servicio Zonal "La Caldera, Vaqueros y Lesser"». Coincide (A:466, 04:4599) |
| 11870 | anexo, 50 | Decreto 2050 | «Aceptase la renuncia del Sr. Arturo Rene Fernández … designado mediante Decreto N. 877 de fecha 1.9.82, a partir del día 11 de diciembre de 1983 dándosele las gracias por los importantes y patrióticos servicios prestados». Coincide (A:468, 18:470) |
| 11811 | 5 | Ley 6163, art. 1 | «dos (2) miembros de Comisiones Municipales titulares y dos (2) suplentes, y no como se consignara en el inciso c) del citado artículo». Coincide (18:488) |
| 11582 | 6 | Ley 5982, planilla V | «La Caldera: Embalse J. A. Peralta 3.000,0». Coincide (10:515) |
| 11555 | 6 | Decreto 877, art. 1 | «Desígnase al señor Arturo Renée Fernández … en el cargo de Presidente de la Comisión Municipal de La Caldera, a partir de la fecha en que tome posesión … todas aquellas facultades inherentes al Concejo Deliberante». Coincide (A:463, C:285, 18:470); la matrícula y la clase que trae el acto no están en el libro |
| 11166 | 6 | Res. 5 | «la partida de \$ 35.000.000 que la Resolución Ministerial Nº 323 del 2-VI-80 le acuerda originariamente para la ejecución de obras del Complejo Deportivo». Coincide con 15:185 en la cifra; discrepa de la planilla de la 323 (hallazgo 1) |
| 10998 | 6 | Res. 323, planilla de la prioridad 1 | «Vaqueros \$ 40.000.000». Coincide con 15:185 (1980) y con el LEE 1980, A.11; la Res. 5 de 1981 dice 35.000.000 (hallazgo 1) |

Bajadas y no cotejadas renglón por renglón: 11614, 11474, 11263, 11212 y 11780 (convenios de 1982, decretos de Vaqueros de 1981 y Ley 6131; los datos de 10:67, 18:470 y 18:481 se cotejaron contra el TEXTO de las fichas).

Son **7 citas entre comillas del libro cotejadas en la imagen** (contadas una vez por pasaje: «por no haber finalizado …» en A:461 y 10:67; «vienen desempeñándose en el perilago» en 17-tierrafiscal:381; «Oficina Seccional Vaqueros, a cargo de la autoridad municipal» en 26:235; «Servicio Zonal "La Caldera, Vaqueros y Lesser"» en A:466 y 04:4599; «dándosele las gracias …» en A:468; «y no como se consignara en el inciso c)» en 18:488; «La Caldera: Embalse J. A. Peralta» en 10:515; los nombres propios entre comillas como «Santa Mónica» o «Fátima» no se cuentan): todas las citas que el AMPLÍA agregó, **ninguna con diferencias**, y datos sin comillas en 3 hojas más (11555, 11166 y 10998).

### Hallazgos (dos, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 15:185 | El párrafo de 1980 da a Vaqueros «\$40.000.000» de la Res. 323 (10998 h6, imagen; LEE 1980 A.11) y, dos oraciones después, el texto agregado por el AMPLÍA dice que en 1981 se autoriza a Vaqueros «a pagar con los \$35.000.000 de su complejo» la expropiación de los cuatro lotes, que es lo que la Res. 5 dice que la 323 le había acordado (11166 h6, imagen; LEE 1981 B.2.2). Las dos fuentes discrepan y el libro no lo dice | 6 | «a pagar con la partida de su complejo la expropiación … ---\$35.000.000, dice la resolución, aunque la planilla de la 323 le daba \$40.000.000---» |
| 2 | 17-tierrafiscal:381 | «en noviembre esa Dirección toma como personal temporario a dos agentes de servicio»: la Res. 1071-D es del Ministerio de Bienestar Social, del 22 de noviembre, y los designa con vigencia desde el 1 de octubre (11612 h11, imagen). La falla de P116 y de la ronda 67 (hallazgos 1 y 2): la fecha del acto dada como la del hecho, y el acto atribuido a la dependencia y no a quien lo dicta | 3 | «y en noviembre el Ministerio de Bienestar Social designa como personal temporario de esa Dirección, desde el 1 de octubre, a dos agentes de servicio …» |

**Precisiones aplicadas sin restar.** (a) 10:64, «La tierra se pagó a valuación fiscal más treinta por ciento en 1972»: el párrafo que el AMPLÍA puso a continuación (10:67) muestra que para los catastros 1575, 1577 y 1578 el pago terminó por convenio en 1982, con actualización e interés. Leídas juntas, las dos frases no se contradicen ---el depósito de 1972 es un pago---, y el AMPLÍA lo hizo a propósito (P174); pero la frase de resumen sostiene la asimetría del capítulo, y se precisa: «La tierra se tomó depositando la valuación fiscal más treinta por ciento, por una ley de 1972». (b) 10:67, «con un interés del siete por ciento y no del seis»: el seis por ciento de los convenios de mayo no estaba dicho; pasa a «y no del seis de los convenios de mayo» (LEE 1982 A.21 y B.2.4). (c) 26:235, «cinco oficinas que seguirán funcionando como hasta entonces»: el decreto dice «bajo la modalidad que se menciona» (11683 h13); pasa a «bajo la modalidad que el decreto indica para cada una». (d) 18:470: el decreto 877 escribe «Arturo Renée Fernández» (11555 h6) y los de 1983 «René» (360) o «Rene» (2050), y la tabla de intendencias (18:667) dice René; se agrega «---René en los decretos de 1983---», como el párrafo de 1980 anota «escrito René». (e) C:31, «los menores de diez años, sin cargo»: la ordenanza 035/80 dice «Los menores hasta diez (10) años» (LEE 1981 A.17): «hasta diez años».

Resta: una discrepancia entre fuentes no señalada, en el aspecto 6: **resta 5** (85, desde el 90 de las rondas anteriores). Una fecha del acto dada como la del hecho, en el aspecto 3: **resta 5** (95). Ninguno sostiene una sección: no hay tope por alcance. Ningún error de consistencia en las 59,1 páginas: el aspecto 7 queda en 100. Aplicados los dos: 90 en la nota final del 6 y 100 en la del 3.

**Errores introducidos por la propia auditoría**: los dos, en el AMPLÍA 1981-1983 (`58b897f`). **Ninguno lo atrapó un control automático**: el de fecha de acto de P164 y P170 (2) mira «renuncia», «contrata», «celebra», «firma» y «sanciona», y no «toma» ni la vigencia retroactiva de una designación; y ningún control compara una cifra que un acto posterior atribuye a uno anterior con la que el libro ya da de ese acto. P175 los propone. Los controles de P144 (comillas rectas: 0 nuevas), P158 (caracteres de control: 0), P164 (salvedades borradas: ninguna), P102 (privacidad), P169 y P174 (anáforas: ninguna caída) funcionaron en el AMPLÍA 1981-1983.

**Descartados (falsos positivos, 7).** «Del catastro 1576 y de las otras cuatro propiedades de la ley» (10:67): la ley tiene cinco incisos, uno de ellos el bloque de los catastros 1575 a 1578 (10:40), y quedan sin convenio el 1576 y los otros cuatro incisos; cierra con las «cinco propiedades» de 19:869. «Cuatro presidentes en doce meses, contando a Camacho» (18:470): Camacho hasta el 1 de diciembre de 1980, Michaux, Oller y Clement desde el 29 de junio de 1981. «Armando Fernández ---el nombre del presidente de la comisión municipal hasta 1979» (18:488): las filas de 1976 a 1978 de A y el capítulo 18 lo dan como interventor y presidente desde 1976, y Montero lo sucede en 1979. «La contratista de la etapa A» para Sollazzo (10:515): 10:515 y A:415 y 422. «Las quince mesas» (18:488): 9 masculinas y 6 femeninas en el decreto 1478. «Ocho decretos de anticipos …, siete de ellos para mejoras o diferencias salariales» (15:185): A.17, A.18, A.21, A.26, A.28, A.30, A.33 y A.35 de 1983, y el A.28 no declara destino. «Entre 1983 y 1987» en 20:1036 y E:156, que el AMPLÍA no llevó a 1984 como D:160 y 18:724: las designaciones de los reemplazantes de diciembre de 1983 siguen pedidas (D:156), de modo que el tramo sigue empezando en 1983.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P175 (herramientas): dos controles más para AMPLÍA (extensión de P164, P170 y P174). (1) **Cifra de un acto citada por otro**: cuando un acto nuevo dice cuánto dio, fijó o acordó un acto anterior que el libro ya cita con su cifra, el script compara las dos y, si difieren, la frase lo dice (caso: Res. 5 de 1981 y Res. 323 de 1980, 15:185, ronda 68). (2) **Autor y vigencia de una designación**: «toma», «designa», «nombra» o «contrata» bajo un mes se cotejan con la ficha: quién dicta el acto y desde cuándo rige, y si la vigencia es anterior a la fecha del acto se escribe así (caso: Res. 1071-D, 17-tierrafiscal:381, ronda 68; antes P116 y P170).

**Pendientes revisados sin cerrar.** P171 (láminas de 1981-1983: sin cambio; la Res. 5 de 1981 y la 323 de 1980, si entran en `fig:votado`, con las dos cifras). P172 (H y E de 1981-1983). P173 (pedidos de 1981-1983 fuera de D para no mover el recuento: siguen fuera, y 22-prospectiva cierra con 284 ítems; el expediente 53-18772/80, que P173 ya pide por las dos superficies, también daría la cifra de la partida). P174 (la frase de 10:64 se precisó en esta ronda; el control propuesto sigue abierto). P168 (26:235 sigue sin decir si la oficina de Vaqueros de 1982 es la 2081). P170 (los controles (1) a (3) corrieron a mano en esta ronda; (4), los pendientes duplicados, sigue). P115 (10:515 sigue sin fuente para capacidad, espejo, profundidad y cota; es una línea que este AMPLÍA tocó: el aspecto 1 sigue en 82). P40 (la muestra de trazabilidad no se rehízo). P100 (1981-1983 en barrido, con el criterio de F, como dice `amplia-1981-1983.json`). P102, P144, P158, P159, P164, P165 y P169 (controles: corrieron).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.264/25.264 líneas vigentes en `f5125e8` | 25.211 vigentes, 53 caducas por el AMPLÍA 1981-1983 |
| Citas de edición y hoja del texto agregado contra los bloques FUENTE de los tres informes | 134 pares (acto, edición, hoja) de los años 1981-1983 | 134 localizados: el acto en la ficha de esa edición y la hoja dentro de su tramo (8 que el script no resolvió, por tramos escritos «h4 (col. 1) a h41», se resolvieron a mano) |
| Cifras del texto agregado contra los tres informes | 82 cifras con separador de miles o decimales | 82 halladas, 77 tal cual y 5 en otra forma (3.000.000.000 como «3.000 millones»; 3.474, 3.725, 9.698 y 10.347 son de años anteriores) |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *única*, *primer*, *primera*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *no lo dice*, *no trae*, *no figura*, *no nombra*, *lo demás*, *hasta entonces*, *más alta*, *mayor*, *doble*, *otra vez*, *vuelve*, *vuelven*, *no se publica*, *no publica*, *no muestra*), sobre 8.040 palabras agregadas | 34 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («lo hallado de 1981 a 1983, leído con la reserva del apéndice», «en lo hallado de 1983», «en lo leído no hay»); «la primera aparición de un aviso» es la de un aviso; «una única propiedad» y «no mayor que el mínimo» son de la ordenanza 047; «vuelven a nombrar los consultorios» se resuelve en la enumeración que sigue; «como hasta entonces» de 26:235 pasa a precisión c |
| Repaso de ventana: afirmaciones que cierran en 1980 (*1958 a 1980*, *1958--1980*, *hasta 1980*, *a 1980*) y que abren el hueco en 1981 (*1981--2012*, *1981 a 2012*, *treinta y dos años*, *sesenta y seis*, *veintitrés*, *veinticuatro*, *11.138*, *desde 1981*, *posterior a 1980*) | libro entero | Ninguna queda sin actualizar: «hasta 1980» de 00:43 compara con 1981-1983; «11.138» y «11138», en 00:43, A:445 y F:90, como límite de 1980; «de 1961 a 1980» de D:177 es la serie de hojas a ojos sin mirar, que en 1981-1983 se miraron en miniatura. Recuentos: 42 + 1 + 26 = 69 tramos; 69 − 42 = 27 fuera de las ventanas; 1984 a 2012 = 29 años |
| Anáforas en las líneas tocadas por el AMPLÍA (P159, P169 y P174: *ese año*, *esos años*, *ese día*, *entonces*, *otra vez*, *las dos*, *los dos*, *ambos*, *el siguiente*, *más arriba*, *más abajo*, *enseguida*, *mismo*, *misma*, *ese*, *esa*, *esos*, *esas*), con la línea siguiente | 95/95 líneas y sus siguientes; 53 coincidencias (con *también*, *aquel* y *aquella*) | 0 caídas: «(véase más arriba)» de 18:724 remite al 877 de 18:470, más arriba; «ese año» de 06:56 es 1981 y el de 18:488, 1983; «los dos» de 18:470 son Fernández y Clement; los dos párrafos que el AMPLÍA movió (10:67 después de «Ese diseño explica» y 18:488 después de «Eso confirma») quedan con su antecedente |
| Comillas rectas que `babel` deforma (P144) | 1 comilla recta en las líneas del AMPLÍA, 0 en la fase 6 | La de 21:87 («GUSTAVO MARTINEZ ZUVIRIA»), que ya estaba; en el PDF compilado, 0 *Ç* y 0 *ç*, antes y después de la fase 6 |
| Caracteres de control (P158) | 38 archivos | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 346/346 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6. Ningún pedido de D queda satisfecho por lo incorporado: el texto del 877/82 y las renuncias de 1983 salieron de D:156 y D:160 en el AMPLÍA; D:156 sigue pidiendo las designaciones de diciembre de 1983 |
| Aritmética de 1981-1983 | 12 cuentas | 203.472.500 / 139.860.000 = 1,455 (45 %). 1.326.543.863 / 825.668.000 = 1,607 (61 %). 23,48 / 44,7393 = 0,525; 3,15 / 6 = 0,525; 31,50 / 60 = 0,525. 3 a 14 de mayo de 1982: once días. 1972 a 1982: diez años. 30-6 a 5-12-1983: cinco meses. 9-4 a 29-6-1981: menos de tres meses. 581 + 4.201 = 4.782. 42 + 1 + 26 = 69. 9 + 6 = 15 mesas. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 68 | 50 de 491 oraciones con cifra en las 95 líneas | **50/50 con fuente localizable**: la cita en la oración o en la misma fila (45 por script; las otras 5 son una ausencia con su universo, dos oraciones de síntesis seguidas de su cita, una fila de C con la cita en la columna anterior y la del censo de 1947, con tomo y página). 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 95 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 95 líneas, cruzadas con contextos sensibles (P102: *remate*, *ejecución*, *juicio ejecutivo*, *concurso civil*, *contra*, *deudor*, *embargo*, *cesante*, *cesantía*, *desalojo*) | 95/95 líneas | 0 caídas. Sin nombre: el demandado del remate de las fincas Severino, el concursado de La Calderilla y Los Perales, el vecino del arado, el agente cesante, la encargada de despensa y el maestro de granja, los dos agentes del perilago. Las matrículas y clases que traen los decretos 877, 1258, 1872 y 2013 y la Res. 1071-D no están en el libro. Nombrados sin contexto sensible: funcionarios, autoridades partidarias, peticionantes de agua, donantes y expropiados por la Ley 4486 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `58b897f` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos); 943 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin normas nuevas citadas en presente; las de 1981-1983 van en pasado |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 2 (fecha y autor de la Res. 1071-D, −5); aplicado. Los actos de fines de un año publicados en el siguiente van como tales (1700/81, 1654/81, 1486/82, 1525/82) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 7 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Las ausencias de 1981-1983 llevan su universo; ninguna salvedad borrada; el repaso de ventana no deja ninguna sin actualizar |
| 6 | Tipo y jerarquía de fuente | 5 | 85 | 90 | Hallazgo 1 (discrepancia entre la Res. 323 y la Res. 5 no señalada, −5); aplicado |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 59,1 páginas (la precisión a no es una contradicción: ver arriba) |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar; las internas, con la dirección correcta |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P171 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 95 líneas; 90 como en la ronda 67 |

**Nota inicial: 87,8 antes del tope y 87,8 después** (tope de 90 por la cobertura acumulada inicial del 99,6 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el expediente 47.742/73 y la resolución judicial de 1979 que citan los convenios de 1982 dirían cuánto se depositó y cuánto se pagó al final por la tierra del embalse, que es la asimetría del capítulo 10---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:515 (P115): +0,9 (el 1, de 82 a 90); (4) cotejar en el facsímil el resto de las citas del libro y dejar corriendo los controles de P164, P170, P174 y P175 como paso automático del AMPLÍA: hasta +0,7 en el 4 y, sobre todo, que los hallazgos de cada ronda pasen a «atrapados»; (5) llevar a las láminas la extensión de P171: +0,2 en el 13.

**Avance del libro:** 2 de 2 hallazgos resueltos (100 %) y cinco precisiones aplicadas; compila sin errores ni referencias indefinidas, 943 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (de 1981 a 1983 la Provincia ofrece el perilago a inversores, cierra los convenios de la tierra del embalse, da su posesión a Deportes sin ser dueña del suelo y licita los pozos de alivio, y el municipio sólo acepta, en 1980, una donación de 400 m² del catastro 1578 que le ofrece una de las expropiadas de 1972, Juana Mercado de Sánchez, la misma que en 1982 cierra por convenio la expropiación de 3 ha de ese catastro: un cruce que el libro todavía no hace), la tutela provincial sobre el fisco municipal (presupuestos aprobados por decreto, anticipos para sueldos y fondos de destino fijo que cambian de destino por resolución, con una cifra que la propia Provincia da de dos maneras) y la intervención como régimen municipal (tres cambios de presidente por decreto en tres años, y el presidente de La Caldera de 1983 designado en 1982).

**Calidad de la auditoría.** Cobertura de la ronda: 95 líneas (0,38 %; 59,1 páginas). Cobertura acumulada: 25.306 de 25.306 (100,0 %), con el registro de arriba. Falsos positivos descartados: 7. Recortes: se leyeron enteras las fichas que sostienen cifras o fechas del texto nuevo y la lista entera de las 130, no el TEXTO de todas; no se cotejaron renglón por renglón las 5 ediciones bajadas sin cita entre comillas en el libro; los controles de P164, P170, P174 y P175 se corrieron a mano; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **2 de 2**, los dos en el AMPLÍA 1981-1983 (`58b897f`), **0 atrapados por un control automático**.

## Ronda 69 — auditoría con fase 6 (04/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1983-1985. Base: commit `4807954` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1983-1985, sobre `7b95d27`, la ronda 68), con la fase 6 en `ronda-69.patch` (commit `3feef81` en la sesión; aplica con `git am` sobre `4807954`, probado en un clon limpio de GitHub: árbol `cf0d7dc`). **Denominador medido: 25.337 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 68 (25.306 de 25.306, sobre `810d4a5`, que en GitHub es `7b95d27`, con el mismo árbol `ec3867c`) se trasladaron por diff a `4807954`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1983-1985 agrega 31 líneas netas (7 en A, 8 en C, 2 en F y 14 en 09) y deja 64 líneas nuevas o modificadas en 18 archivos: caducan 33 líneas anteriores**, y quedan **25.273 vigentes sobre 25.337 (99,7 %)**. La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `4807954`)

Se leyeron **las 64 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A, C, F y 09 completas, y las modificadas del resto en su texto entero (167.933 bytes), además de la lista de cada cambio palabra por palabra con su contexto (5.177 palabras agregadas). Se cotejaron contra los dos informes LEE (`BO-Salta-1984_11881-12127_la-caldera_LEE-1984_2026-10-04.txt` y `BO-Salta-1985_12128-12373_la-caldera_LEE-1985_2026-10-04.txt`, de `corrige/lee/`): la lista entera de fichas (90: §A y §B.2 de los dos años, FUENTE, FICHA y NOTA), el §E de 1984 (interinatos) y el §R de los dos años, y el TEXTO de las fichas que sostienen afirmaciones con cifras, fechas o citas.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 469–476 | 8 | sesión |
| ape/C-normativa.tex | 288–295, 340 | 9 | sesión |
| ape/D-pedidos.tex | 160, 177, 192, 253 | 4 | sesión |
| ape/F-fuentes.tex | 25–26, 94–95, 97 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659–3660, 3818, 4599 | 4 | sesión |
| cap/05-tierra.tex | 285 | 1 | sesión |
| cap/09-defensas.tex | 535, 628–642 | 16 | sesión |
| cap/10-expropiacion.tex | 112, 334, 515 | 3 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470, 724 | 2 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 04-siglo:3700–3875 (el agua de La Helvecia del decreto 9041-E de 1948, 12,6 l/s para 24 ha, y Dantón Cermesoni candidato por Chicoana, que 17-aguabaja:281 y 18:470 citan del capítulo); 04-siglo:4590–4598 (el hospital, para «tampoco nombra el hospital»); 10-expropiacion:82 y 100–110 (la ficha de la Ley 6354, con su expediente 336-C/84, para la precisión a); A:259 y 464 (filas de 1948 y 1983: el 9041-E y el remate en el concurso civil de La Calderilla y Los Perales); 18:470 desde 1981 (las renuncias del 11 de diciembre de 1983 y Esteban Mogro, para «los dos nombres de siempre»); 18:718–724; 21-conclusion:118–120 (hallazgo 2); D:258–260 (emergencias agropecuarias, precisión b).

**Esta ronda: 64 líneas nuevas**, 167.933 bytes sobre 3.110.195, que en las 947 páginas de la base equivalen a **51,1 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `4807954` cae dentro de estos tramos.

Acumulado: 25.273 vigentes + 64 = **25.337 de 25.337 (100,0 %)**. La fase 6 toca cuatro líneas: A:469, dentro de lo leído en esta ronda, y 10:112, también leída en esta ronda; 21-conclusion:120 y D:260, que estaban vigentes y se releyeron como contexto; no cambia el largo de ningún archivo: **25.337 de 25.337 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1984 y 1985 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 200 ppp con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión, se recortó con su contexto y cada recorte se miró. Se bajaron 12 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 12134 | 5 | Decreto 2862, considerando | «Que es propósito del Poder Ejecutivo disponer la designación por un nuevo período de funciones de los señores Presidentes de Comisiones Municipales». Coincide (A:470) |
| 12134 | 5 | Decreto 2862, art. 1 | «Designar por el período que fija el artículo 182º de la Constitución Provincial y artículo 35 de la Ley nº 1349». Coincide (18:470) |
| 12040 | 7 | Res. 1097-D, art. 1 | «Con vigencia al 21 de mayo del año en curso, adscribir … de la Estación Sanitaria de La Viña … con la misma … función en el Centro de Salud de La Caldera». Coincide (04:4599, A:469) |
| 12113 | 9 | Decreto 2519, art. 5 | «Puesto Sanitario de La Caldera (personal temporario)». Coincide (04:4599, A:469) |
| 12119 | 9 | Decreto 2623, art. 2 | «(\$a 41.398.000) de la obra "Toma y canal de aducción, Campo Alegre, Etapa "B", que se imputará al Fondo de Desarrollo Regional». Coincide (10:515) |
| 12328 | 12 | Decreto 2050 | «María Cristina Orellana de Cruz … jefa del Instituto "Dr. Luis Linares", mayo/85 44,25 %». Coincide (26:235) |
| 12294 | 10 | Res. 417-D | «Pintura General Edificio Hogar de Niños "Dr. Luis Linares" - La Caldera - Departamento La Caldera». Coincide (26:235, A:472) |
| 11954 | 6 | Firma del decreto 761, del 3 de abril de 1984 | «DE LOS RIOS (Int.) - Isa - Cantarero - Saravia - Montoya», y la del decreto anterior de la misma columna. Desmiente «en febrero» de A:469 (hallazgo 1) |
| 12004 | 5 y 6 | Firmas de decretos del 21 y 22 de junio de 1984 | «DE LOS RIOS (I)» y «DE LOS RIOS (Int.)» en tres decretos; la edición es del 29 de junio, la última del tramo que el LEE 1984 da en su §E (11917 a 12004). Hallazgo 1 |
| 12184 | 5 | Decreto 476, temas 20 y 21 | «Catastro Nº 1229 en Vaqueros … Expediente Nº 335-C/84» y «inmueble de propiedad de la señora Elena S. de González Bonorino y otros, para la construcción de Viviendas Familiares, ubicado en La Caldera, Expediente Nº 336-C/84». Coincide con 10:112 en lo que dice; el expediente es el de la ficha de la Ley 6354 (10:101): precisión a |

Bajadas y no cotejadas renglón por renglón: 12178, 12144 y 12268 (decretos 437 y 1465 y el escrutinio interno de 1985; sus datos se cotejaron contra el TEXTO de las fichas).

Son **7 citas entre comillas del libro cotejadas en la imagen** (contadas una vez por pasaje: «por un nuevo período de funciones» en A:470; «por el período que fija el artículo 182º …» en 18:470; «en el Centro de Salud de La Caldera» en 04:4599 y A:469; «Puesto Sanitario de La Caldera» en 04:4599 y A:469; «Toma y canal de aducción, Campo Alegre, Etapa ``B''» en 10:515; «jefa del Instituto» en 26:235; «Hogar de Niños ``Dr. Luis Linares''» en 26:235 y A:472; los nombres propios entre comillas como «Unidad», «El Palenque» o «Juana Moro de López» no se cuentan): **ninguna con diferencias**, y datos sin comillas en 4 hojas más (11954 h6, 12004 h5 y h6, 12184 h5). Las dos citas del 2862 que el AMPLÍA tomó, una del considerando y otra del artículo 1º, están las dos en el acto: no se contradicen.

### Hallazgos (dos, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:469 | La fila de 1984 dice que firman como gobernador interino «Figueroa y, en febrero, De los Ríos, vicepresidente del Senado en ejercicio del Poder Ejecutivo». De los Ríos firma el decreto 761 del 3 de abril (Nº 11954, h. 6, imagen) y decretos del 21 y 22 de junio (Nº 12004, h. 5 y 6, imagen); el LEE 1984 da sus firmas en diez ediciones de la 11917 a la 12004 (§E, «Interinatos»), y el AMPLÍA tomó la primera, la de la ficha A.7, como si fuera el tramo. Es un intervalo importado de un informe y no rehecho sobre el documento | 3 | «Figueroa y, de febrero a junio, De los Ríos, vicepresidente del Senado …» |
| 2 | 21-conclusion:120 | «Lo que falta, y no se consigue buscando» sigue dando por faltantes «las intendencias anteriores a 1999 --- que para 1983--1987 no se buscan como proclamaciones sino como decretos de designación». Desde el AMPLÍA 1981-1983 el libro tiene el decreto 877 de 1982, y desde el 1983-1985 los 145 y 2862 de 1984 (18:470 y 724; D:160 ya pide sólo 1986 y 1987). El repaso de ventana del AMPLÍA no lo alcanzó porque la fórmula es «1983--1987» y no una de las ventanas buscadas | 5 (texto desactualizado) | «que para 1986 y 1987 no se buscan como proclamaciones sino como decretos de designación, porque entonces los intendentes no se elegían, como no lo eran los presidentes de 1982 a 1985, que la lectura halló en los decretos 877 de 1982 y 145 y 2862 de 1984 (capítulo \ref{cap:politica})» |

**Precisiones aplicadas sin restar.** (a) 10:112: el inmueble de La Caldera de Elena S. de González Bonorino que el decreto 476 pone en el temario de las extraordinarias de 1985 «por el nombre y el destino parece ser el de la Ley 6354»: el decreto le da el expediente 336-C/84 (Nº 12184, h. 5, imagen), y es el mismo que la ficha de la Ley 6354 trae diez líneas más arriba (10:101). El libro tenía el dato que cierra la identidad y no lo usaba: pasa a «que es el de la Ley 6354, porque lleva su mismo expediente, el 336-C/84; el de la fracción de Vaqueros es el 335-C/84». (b) D:260, el pedido de la serie de declaraciones de emergencia agropecuaria de 1980 a 2018 nombraba sólo lo que halló la lectura de 1980; suma el decreto 1156 de 1984, «que no nombra localidades», y su expediente, el C/19-03716/84 (LEE 1984, A.22), en el mismo ítem: el recuento de D no cambia.

Resta: un intervalo importado y no recalculado, en el aspecto 3: **resta 5** (95). Un texto desactualizado ---algo obtenido que se sigue dando por faltante---, en el aspecto 5: **resta 3** (97). Ninguno sostiene una sección: no hay tope por alcance. Ningún error de consistencia en las 51,1 páginas: el aspecto 7 queda en 100. Aplicados los dos: 100 en la nota final del 3 y del 5.

**Errores introducidos por la propia auditoría**: los dos. El 1, en el AMPLÍA 1983-1985 (`4807954`); el 2, en el AMPLÍA 1981-1983 (`58b897f`), que incorporó el 877 sin actualizar la conclusión, y lo agravó el 1983-1985, que actualizó D:160 y 18:724 y no 21-conclusion:120. **Ninguno lo atrapó un control automático**: ningún control rehace sobre las fechas de las ediciones un tramo que el informe da por números de edición, y el repaso de ventana busca las fórmulas de cobertura y no los pedidos con rango de años fuera de D. P181 los propone. Los controles de P144 (comillas rectas: 0 nuevas), P158 (caracteres de control: 0), P164 (salvedades borradas: ninguna), P102 (privacidad), P169 y P174 (anáforas: ninguna caída) y P175 (autor y vigencia: Res. 1097-D, «desde mayo» y «de agosto») funcionaron en el AMPLÍA 1983-1985.

**Descartados (falsos positivos, 6).** La remisión de 17-aguabaja:281 al capítulo \ref{cap:siglo} por el decreto 9041 de 1948 y los 12,6 l/s de La Helvecia: el capítulo lo trae (04:3710–3760, sin el número del decreto en la misma línea, por eso no lo halló la primera búsqueda). «Dantón Cermesoni, el nombre de un candidato a constituyente por Chicoana en 1948 (capítulo \ref{cap:siglo})»: está en 04:3821, con el nombre partido entre dos renglones. Las dos citas del 2862 (A:470, considerando; 18:470, artículo 1º): son dos pasajes distintos del acto, los dos en la imagen. «Tres de esas planillas no suman el total que imprimen, y ningún dígito dudoso lo explica» (15:185): en el 351 los dígitos cortados de cinco renglones mueven la suma en unidades, y la diferencia es de 145 a 155; cierra sólo con Tartagal en la cifra de su escala, que es una corrección del impreso (LEE 1984, A.6). «Tres de los cuatro designados en 1984 se van antes de terminar su período» (18:470): Quipildor en mayo de 1984, Perales de Mangoña en julio de 1985 y García en septiembre de 1985, con períodos de dos años desde marzo de 1984; González sigue. «Los dos cargos cuyas renuncias se habían aceptado desde el 11 de diciembre de 1983» (A:470): la serie de decretos del 9-12-83 incluye la de Vaqueros (LEE 1983, A.38, nota).

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P181 (herramientas): dos controles más para AMPLÍA (extensión de P170 y P175). (1) **Tramo dado por ediciones**: cuando un informe LEE da un hecho repetido por un rango de ediciones (firmas de un interino, apariciones de un aviso, «de la 11917 a la 12004»), el script convierte las dos ediciones extremas a sus fechas con el §1 del informe y compara con el mes o el tramo que escribe el libro (caso: De los Ríos «en febrero», A:469, ronda 69). (2) **Rangos de años fuera de D**: el repaso de ventana busca además, en todo el libro, los rangos «19xx--19yy» y «19xx a 19yy» que contienen un año recién incorporado y que están en una oración de falta o de pedido («falta», «faltan», «se buscan», «hay que buscar», «se pide»), y no sólo las fórmulas de cobertura (caso: 21-conclusion:120, «para 1983--1987», ronda 69).

**Pendientes revisados sin cerrar.** P176 (láminas de 1984-1985: sin cambio). P177 (H y E de 1984-1985: la precisión a no los toca; el expediente 336-C/84 se agrega a lo que P177 lleva de la Ley 6354). P178 (pedidos de 1984-1985 fuera de D: siguen fuera; la precisión b agrega un expediente dentro de un ítem existente y no mueve el recuento: 22-prospectiva cierra con 284). P179 (complemento LEE: 10:515 sigue diciendo que «que sea la etapa B de este embalse lo dice sólo el nombre», que es lo que el LEE permite mientras P179 no se haga). P180 (registrar). P115 (10:515 sigue sin fuente para las cifras físicas del embalse). P89 (el 437/85 cambia el destino de una parcela del fraccionamiento de Getsemaní: queda en P177 y en D:40). P100, P102, P144, P158, P159, P164, P169, P170, P171, P172, P173, P174, P175: sin cambio.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.306/25.306 líneas vigentes en `7b95d27` | 25.273 vigentes, 33 caducas por el AMPLÍA 1983-1985 |
| Citas de edición y hoja del texto agregado contra los bloques FUENTE de los dos informes | 67 pares (edición, hoja) de los años 1984-1985 | 67 localizados (66 por script; la 12033 h. 9, por la FUENTE escrita «h3 a h13; el renglón del departamento en h9», a mano) |
| Cifras del texto agregado contra los dos informes | 34 cifras con separador de miles o decimales | 30 halladas; las otras 4 son de años anteriores (10.347 y 11.651, ediciones que faltan; 12,6 l/s de 1948; 2.996 hojas de 1983) |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *nunca*, *jamás*, *ningún*, *ninguna*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *no lo dice*, *no se publica*, *no nombra*, *no dice*, *sin que*, *mayor*, *doble*, *otra vez*, *vuelve*, *siguen*, *de siempre*, *corriente*), sobre 5.177 palabras agregadas | 49 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («en lo hallado del año», «lo hallado de 1985 no lo dice», «en lo hallado de esos años», «lo hallado de 1975 a 1985»); «casi el doble» es 12.787.200 / 6.990.500 = 1,83; «los dos nombres de siempre» son Arturo Fernández y Esteban Mogro, que 18:470 sigue desde 1961 y 1969 |
| Repaso de ventana: afirmaciones que cierran en 1983 (*1958 a 1983*, *hasta 1983*, *a 1983*, *y 1983*) y que abren el hueco en 1984 (*1984--2012*, *1984 a 2012*, *veintinueve años*, *sesenta y nueve*, *11.880*, *desde 1984*, *de 1984 en adelante*, *veintiséis*, *veintisiete tramos*) | libro entero | Una sin actualizar: 21-conclusion:120, «para 1983--1987» (hallazgo 2). Las demás: «veintinueve años» de 15:46 es otra cuenta; «sesenta y nueve» de 00:43 son hojas; «hasta 1985» de 04:3818 compara con el capítulo 18; «11.880», en 00:43, A:464 y F:92, como límite de 1983. Recuentos: 42 + 1 + 28 = 71 tramos; 71 − 42 = 29 fuera de las ventanas; 1986 a 2012 = 27 años; 1964 a 1985 = 22 cifras de páginas faltantes en D:177, y 1975 a 1985 = 11 de poca tinta |
| Anáforas en las líneas tocadas por el AMPLÍA (P159, P169 y P174: *ese año*, *esos años*, *entonces*, *otra vez*, *las dos*, *los dos*, *ambos*, *más arriba*, *más abajo*, *mismo*, *misma*), con la línea siguiente | 64/64 líneas y sus siguientes | 0 caídas: «La lámina \ref{fig:votado} pone las dos estaciones sanitarias, la de 1935 y la de 1947» (26:235) quedó después del texto nuevo, pero nombra las dos (ronda 67); «El dique tiene» (10:515) reemplaza al «Tiene» que el texto nuevo habría dejado sin sujeto; «(véase más arriba)» de 18:724 remite a 18:470 |
| Comillas rectas que `babel` deforma (P144) | 0 en lo agregado por el AMPLÍA y por la fase 6 | en el PDF compilado, 0 *Ç* y 0 *ç*, antes y después de la fase 6 |
| Caracteres de control (P158) | 38 archivos | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`; sin los apéndices) | 346/346 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 (la de la fase 6 en 21-conclusion remite al 18, anterior) |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6. Ningún pedido de D queda satisfecho por lo incorporado: D:160 se redujo a 1986-1987 en el AMPLÍA; D:260 sigue pidiendo la serie de emergencias y suma el expediente de 1984 |
| Aritmética de 1984-1985 | 9 cuentas | 12.787.200 / 6.990.500 = 1,83. 4,78 / 9,1156 = 0,524; 12,6 / 24 = 0,525. 3,5 − 2 = 1,5 meses de plazo. 14.178.286 $a = A 14.178,29. 23 + 2 = 25 comisiones del 2862. 9 + 6 = 15 mesas. 1 + 4 + 7 + 12 = 24 páginas faltantes de 1984. 42 + 1 + 28 = 71. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 69 | 50 de 369 oraciones con cifra en las 64 líneas | **50/50 con fuente localizable**: la cita en la oración o en la misma fila (35 por script; las otras 15 son ausencias con su universo, oraciones de síntesis seguidas de su cita, una fila de C con la cita en la columna anterior, una cuenta sobre cifras citadas y declaraciones del apéndice F, que es la fuente de sí mismo). 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 64 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 64 líneas, cruzadas con contextos sensibles (P102: *remate*, *quiebra*, *concurso*, *ejecución*, *juicio*, *contra*, *deudor*, *embargo*, *renuncia*, *jubila*) | 64/64 líneas | 0 caídas. Sin nombre: el fallido de La Calderilla y Los Perales, la celadora que se jubila, la psicóloga y su sucesora, la médica de La Viña, el profesional del Puesto Sanitario, los dos ingenieros adjudicatarios, el donante de Rosario. Los D.N.I., las clases y las matrículas que traen los decretos 145, 146, 545, 576, 947, 1360, 1709 y 1966 no están en el libro. Nombrados sin contexto sensible: autoridades comunales, jueces de paz y candidatos (cargos públicos), dirigentes partidarios, peticionantes de agua y propietarios de inmuebles expropiados por ley |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `4807954` y fase 6, cada una en un clon limpio | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos); 947 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin normas nuevas citadas en presente; las de 1984-1985 van en pasado |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 1 (tramo de De los Ríos importado del informe y no rehecho, −5); aplicado. Los actos de fines de 1984 publicados en 1985 van como tales (2861, 2862, 2823) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 7 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 97 | 100 | Hallazgo 2 (texto desactualizado, −3); aplicado. Las ausencias de 1984-1985 llevan su universo; ninguna salvedad borrada |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin discrepancias nuevas sin señalar: la adjudicación de la línea casi al doble y las planillas que no cierran se dicen; 90 como en la nota final de la ronda 68 |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 51,1 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin faltas nuevas; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P176 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 64 líneas; 90 como en la ronda 68 |

**Nota inicial: 87,7 antes del tope y 87,7 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el expediente 47.742/73 y la resolución judicial de 1979 de la tierra del embalse (capítulo 10), o los decretos de designación de 1986 y 1987 que D:160 pide y que dirían si el ejecutivo municipal se siguió nombrando hasta la Constitución de 1986---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:515 (P115): +0,9 (el 1, de 82 a 90); (4) dejar corriendo los controles de P164, P170, P174, P175 y P181 como paso automático del AMPLÍA, que habrían atrapado los dos hallazgos de esta ronda y los dos de la 68: protege +0,6 por ronda en los aspectos 3, 5 y 6; (5) el 8 (de 95 a 100) y el 15 (de 90 a 100): +0,9.

**Avance del libro:** 2 de 2 hallazgos resueltos (100 %) y dos precisiones aplicadas; compila sin errores ni referencias indefinidas, 947 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 1984 y 1985 el ejecutivo de las dos comisiones sigue designado por decreto, renovado por un año, mientras el departamento vuelve a votar sólo los miembros de las comisiones; el municipio aparece ante los ríos como parte de dos convenios de defensas que no se publican, y ante el agua de riego no aparece: el único trámite de particulares de los dos años no lo consulta) y la tutela provincial sobre el fisco municipal (catorce anticipos de coparticipación en 1984 para pagar sueldos y dietas, tres planillas que no suman lo que imprimen, y en noviembre de 1985 dos decretos del mismo total que dan a La Caldera mil australes en uno y nada en el otro). Ninguna tesis cambió de estado en esta ronda.

**Calidad de la auditoría.** Cobertura de la ronda: 64 líneas (0,25 %; 51,1 páginas). Cobertura acumulada: 25.337 de 25.337 (100,0 %), con el registro de arriba. Falsos positivos descartados: 6. Recortes: se leyeron enteras las fichas de los dos años en su FUENTE, FICHA y NOTA, y el TEXTO de las que sostienen cifras, fechas o citas, no el TEXTO de todas; no se cotejaron renglón por renglón las 3 ediciones bajadas sin cita entre comillas en el libro; los controles de P164, P170, P174, P175 y P181 se corrieron a mano; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **2 de 2**, uno en el AMPLÍA 1983-1985 (`4807954`) y otro en el 1981-1983 (`58b897f`), **0 atrapados por un control automático**.

## Ronda 70 — auditoría con fase 6 (04/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1986-1988. Base: commit `1bd1c1d` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1986-1988, sobre `83a0b59`, la ronda 69), con la fase 6 en `ronda-70.patch` (commit `8ef9319` en la sesión; aplica con `git am` sobre `1bd1c1d`, probado en un clon limpio de GitHub: árbol `9b3c0f2`). **Denominador medido: 25.366 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 69 (25.337 de 25.337, sobre `3feef81`, que en GitHub es `83a0b59`, con el mismo árbol `cf0d7dc`) se trasladaron por diff a `1bd1c1d`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1986-1988 agrega 29 líneas netas (8 en A, 16 en C, 2 en F, 1 en 10 y 2 en 18) y deja 80 líneas nuevas o modificadas en 21 archivos: caducan 51 líneas anteriores**, y quedan **25.286 vigentes sobre 25.366 (99,7 %)**. La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `1bd1c1d`)

Se leyeron **las 80 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A y C completas, y las modificadas del resto en su texto entero (201.177 bytes), además de la lista de cada cambio palabra por palabra con su contexto (8.347 palabras agregadas). Se cotejaron contra los tres informes LEE (`BO-Salta-1986_12374-12618_la-caldera_LEE-1986_2026-10-04.txt`, `BO-Salta-1987_12619-12855_la-caldera_LEE-1987_2026-10-04.txt` y `BO-Salta-1988_12856-13101_la-caldera_LEE-1988_2026-10-04.txt`, de `corrige/lee/`): la lista entera de fichas (150: §A y §B.2 de los tres años, FUENTE y FICHA), el §0 de los tres, el §E.9 de 1986 (contradicciones) y el TEXTO y la NOTA de las fichas que sostienen afirmaciones con cifras, fechas, nombres o citas (685, 766, 2786, 1527, 2410, 2444 y 3041 de 1986; Ley 6434 de 1987; 271 de 1988), y el informe LEE 1985 para la superficie de la Ley 6334.

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 477–486 | 10 | sesión |
| ape/C-normativa.tex | 296–311 | 16 | sesión |
| ape/D-pedidos.tex | 39, 160, 192, 239, 253, 260 | 6 | sesión |
| ape/F-fuentes.tex | 25–26, 96–97, 99 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/03-fincas.tex | 865, 1029–1031 | 4 | sesión |
| cap/04-siglo.tex | 3659–3660, 3818, 4599 | 4 | sesión |
| cap/05-tierra.tex | 285 | 1 | sesión |
| cap/09-defensas.tex | 535, 642 | 2 | sesión |
| cap/10-expropiacion.tex | 101, 108, 113, 115, 133, 137, 139, 146, 335, 516 | 10 | sesión |
| cap/15-hacienda.tex | 185 | 1 | sesión |
| cap/16-redes.tex | 789 | 1 | sesión |
| cap/17-aguabaja.tex | 281 | 1 | sesión |
| cap/18-politica.tex | 470, 668–670, 726 | 5 | sesión |
| cap/20-opacidad.tex | 880–881, 1036, 1038 | 4 | sesión |
| cap/21-conclusion.tex | 28, 120 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/22-prospectiva.tex | 144 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): A:476 (Ley 6334, 1.736,80 m²); C:122 (Ley 6354); E:82 (Carlos Serrey, con la Ley 6354, la 6334 y la 6464); 10:100–110 (la ficha de la Ley 6354); 03:862–866; 04:3812–3819; 18:660–672 (la ficha de intendencias), 18:497 y 531–533 (Esteban Mogro, para el «más abajo» de 18:470); 22-prospectiva:140–150; D:177 (pedido de hojas sin mirar y páginas faltantes), y 26:235 hasta la Ley 1402.

**Esta ronda: 80 líneas nuevas**, 201.177 bytes sobre 3.157.101, que en las 961 páginas de la base equivalen a **61,2 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `1bd1c1d` cae dentro de estos tramos.

Acumulado: 25.286 vigentes + 80 = **25.366 de 25.366 (100,0 %)**. La fase 6 toca diez líneas: A:477 y 478, 03:1031, 10:113 y 137 y 15:185, dentro de lo leído en esta ronda, y C:122, D:177 y E:82, que estaban vigentes y se releyeron como contexto; no cambia el largo de ningún archivo: **25.366 de 25.366 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 1985 a 1988 de `boletines-salta`)

Imágenes de los PDF del Release renderizadas a 200 ppp con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión, se recortó a 300 ppp con su contexto y cada recorte se miró. Se bajaron 12 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 12682 | 85 | Ley 6434, plan del I.P.D.U.V., renglón 75 | «30 VIV. LA CALDERA». Coincide (10:146, D:39, C:304) |
| 12589 | 7 | Decreto 3041, art. 1 | «"Provincia de Salta vs. Manuel F. Serrey y otros"». Coincide (10:113) |
| 12589 | 8 | Decreto 3042 | «con destino a Obras Públicas». Coincide (15:185) |
| 12594 | 14 | Licitación 11/86 | «Ampliación y Remodelación Hogar de Niños Luis Linares - La Caldera». Coincide (26:235, A:477) |
| 12595 | 26 | Ley 6416, Hidráulica, obra 5 (hoja girada) | «Toma y Canal Campo Alegre - Etapa 3», 300.000 + 249.537,38 + 69.000 = 618.537,38. Coincide (10:516, C:301) |
| 12551 | 6 | Decreto 2444, arts. 1 y 2 | Los cinco propietarios y «(-A- 515,48)» a Fiscalía de Gobierno. Coincide (10:108) |
| 12416 | 7 | Decreto 685, art. 1 | «2 Has. 1.735,80 m2». Hallazgo 3 |
| 12311 | 5 | Ley 6334, art. 1 (LEE 1985) | «2 Has. 1.736,80». Hallazgo 3 |

Bajadas y no cotejadas renglón por renglón: 12544, 12710, 12721, 12790 y 12920 (decretos 2410, 907 y 908, 1080, 1928 y 271; sus datos se cotejaron contra el TEXTO de las fichas).

Son **5 citas entre comillas del libro cotejadas en la imagen** («30 VIV. LA CALDERA», «Manuel F. Serrey y otros», «con destino a Obras Públicas», «Hogar de Niños», «Toma y Canal Campo Alegre - Etapa 3»; los nombres propios entre comillas, como «Dr. Luis Linares» o «La Reconquista», no se cuentan): **ninguna con diferencias**, sobre 5 citas nuevas del AMPLÍA (5/5), y datos sin comillas en 3 hojas más (12551 h6, 12416 h7, 12311 h5).

### Hallazgos (cuatro, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:478, C:122, E:82, 03:1031 | El CONTRADICE del AMPLÍA ---el decreto 2444/86 no nombra a Elena Serrey de González Bonorino entre los cinco propietarios de la matrícula 1303--- se aplicó en 03:865 y 1029–1031 y en el capítulo 10, pero no en el resto: la fila del 4 de marzo de 1986 dice que la Ley 6354 «expropia 8.158,71 m² de Elena Serrey de González Bonorino» y, en la misma fila, que no está entre los propietarios; C:122 («Expropia … de Elena Serrey»), E:82 («en 1986 se expropió a Elena Serrey de González Bonorino un inmueble») y el cierre de 03:1031 («el mismo apellido cede tierra al Estado por expropiación») siguen diciendo lo que el AMPLÍA corrigió. La ley dice «Elena Serrey de González Bonorino y otros» y declara la utilidad pública | 7 (contradicción en la misma fila) | A:478 y C:122: «declara de utilidad pública y sujetos a expropiación 8.158,71 m² de Elena Serrey de González Bonorino y otros»; C:122 suma que el 2444 no la nombra; E:82: «la Ley 6354 declaró expropiable un inmueble de La Caldera de Elena Serrey de González Bonorino y otros … y el decreto que manda promover el juicio no la nombra entre sus cinco propietarios»; 03:1031: «el mismo apellido está en una expropiación para vivienda social cuyo juicio la Provincia manda promover en 1986» |
| 2 | 10:137, 03:1031 | «En 1985 y 1986 dos fracciones de la misma Finca Vaqueros pasaron al Estado por expropiación», y en 03:1031 el linaje «cede … por dos expropiaciones de 1985 y 1986, tierra». Veinticuatro líneas más arriba (10:113 y 115) el texto del AMPLÍA da para las dos sólo el decreto que faculta a promover el juicio y, para una, la posesión al Instituto «hasta que se resuelva el juicio» (3041, Nº 12589, h. 7, imagen); y la frase siguiente de 10:137, en el mismo estado procesal, dice de La Caldera «fueron declarados expropiables … y la Provincia promovió el juicio» | 7 (contradicción a menos de diez páginas) | 10:137: «fueron declaradas expropiables, y la Provincia promovió sus juicios y le dio al Instituto de vivienda la posesión de una de ellas»; 03:1031: «tiene además dos fracciones declaradas expropiables en 1985 y 1986» |
| 3 | 10:113 | El texto agregado cita el decreto 685/86, que faculta a promover el juicio de la Ley 6334 por «2 Has. 1.735,80 m2» (Nº 12416, h. 7, imagen), en la misma oración que da la superficie de la ley, 2 ha 1.736,80 m² (Nº 12311, h. 5, imagen), sin señalar que difieren en un metro cuadrado | 6 (discrepancia entre fuentes no señalada) | «faculta a Fiscalía de Gobierno a promover el juicio ---por un inmueble de 2 ha 1.735,80 m², un metro cuadrado menos que el de la ley, sin decir por qué--- y le paga A~90,51» |
| 4 | D:177 | El pedido de lectura sobre la imagen de las hojas sin mirar y de las páginas faltantes llega a 1985 («153 de poca tinta de 1975 a 1985», «escaneos de 1964 a 1985»), y no suma los límites que el propio AMPLÍA declara en 00:43 y F:96: las 290 hojas de poca tinta de 1986 sin mirar una por una, las dos páginas faltantes de la 12567 (una, la recaudación que cita su sumario) y las diecisiete que declaran las tapas de la 12567, la 12575 y la 12596. El AMPLÍA 1983-1985 sí había sumado las suyas en ese ítem | 8 (límite declarado sin su pedido) | «y 153 de poca tinta de 1975 a 1985 y las 290 de 1986»; «escaneos de 1964 a 1986 --- … 24, 19 y 2», con la 12567; y las diecisiete páginas declaradas por las tres tapas. El ítem no cambia el recuento: 284 |

**Precisiones aplicadas sin restar.** (a) 15:185: «las otras dos no cierran por A~182 y por A~914, sin dígito dudoso que lo explique»: el LEE 1986 (A.24, E.9) explica exactamente los 182 ---Payogasta se imprime 424 donde el decreto 1196, del mismo concepto y del mes anterior, imprime 242---; pasa a decirlo. (b) A:477 y C:296: los convenios de La Caldera de 1985-1986 iban todos «para defensas en la margen derecha del río»; el 766 dice «Zona Cabral y frente al Pueblo», sin margen: A:477, «dos de ellos en su margen derecha»; C:296, «unas en la Zona Cabral y frente al pueblo y otras en su margen derecha». (c) 15:185: la cita de los «otros quince decretos de anticipos» que no publican planilla daba sólo los diez del 12954; suma 1668 a 1670 (Nº 13040), 1772 (Nº 13044) y 2112 (Nº 13071), del LEE 1988 B.2.5.

Resta: dos errores de consistencia en 61,2 páginas (3,3 por cada cien: escalón de ≤ 4, 50), uno de ellos con material a menos de diez páginas y otro dentro de la misma fila: un escalón más, **40** en el aspecto 7. Una discrepancia entre fuentes no señalada, en el aspecto 6: **resta 5** (85, desde el 90 de la ronda 69). Un límite sin pedido, en el aspecto 8: **resta 5** (90). Ninguno sostiene una sección: no hay tope por alcance. Aplicados los cuatro: 100 en el 7, 90 en el 6 y 95 en el 8 en la nota final.

**Errores introducidos por la propia auditoría**: los cuatro, en el AMPLÍA 1986-1988 (`1bd1c1d`): el 1 y el 2 aplicaron el CONTRADICE sólo donde el índice del AMPLÍA buscaba la matrícula 1303 y el nombre en capítulos, no en A, C y E ni en la frase vecina sobre Vaqueros; el 3 incorporó una cifra del decreto sin cruzarla con la de la ley, que el libro ya tenía; el 4 actualizó 00:43 y F:96 y no el ítem de D que pide lo mismo. **Ninguno lo atrapó un control automático.** P186 los propone. Los controles de P144 (comillas rectas: 0 nuevas), P158 (caracteres de control: 0), P164 (fecha de acto y de publicación: el 2876 de octubre publicado en noviembre, el 3041 de octubre publicado en noviembre, bien dichos), P170 (remisiones), P174 (anáforas) y P102 (privacidad) se corrieron a mano y no dieron caídas.

**Descartados (falsos positivos, 7).** «Fiscalía de Gobierno» (2444 y 685) y «Fiscalía de Estado» (3367) en la misma página: son los organismos que nombra cada decreto (fichas A.10, A.39 y A.59). «El decreto se había publicado en noviembre de 1986» (10:115) contra «en octubre el 3041» (10:113): el 2876 es del 14 de octubre y sale en la 12579 del 3 de noviembre; el 3041 es del 29 de octubre. «Se prorroga dos veces en el año» (A:481) contra «cinco veces» (10:516): dos en 1987 y tres en 1988 (B.2.8 de 1987 y B.2.4 de 1988). «La más baja de cinco, rebajada un nueve por ciento» (A:479): 599.314,24 es la menor de las cinco y 545.375,96 / 599.314,24 = 0,910. «Más de cuatro veces y media su presupuesto» (A:485): 3.003.122,13 / 654.123 = 4,59. Las dos listas del anexo del artículo 29 (A:481: hospital, colegio, gas; 22:545: energía, gas, alumbrado): son ocho obras y cada pasaje nombra las que sirven a su tema. «Mogro … (más abajo)» en 18:470: Esteban Mogro está en 18:497 y 531–533.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P186 (herramientas): dos controles más para AMPLÍA (extensión de P175 y P181). (1) **Propagación de un CONTRADICE**: cuando el AMPLÍA clasifica una ficha como CONTRADICE, el script busca en todo el libro, apéndices incluidos, el nombre, la matrícula, el catastro y el número de la norma de la ficha, y lista cada línea que conserva el verbo o la afirmación desmentida («expropia», «se expropió», «cede tierra»), para corregirla o justificarla (caso: A:478, C:122, E:82 y 03:1031, ronda 70). (2) **Límites declarados y su pedido**: cada cifra de hojas sin mirar o de páginas faltantes que el AMPLÍA agrega a 00 o a F se busca en D:177; si no está, el ítem se actualiza (caso: las 290 de 1986, ronda 70). Y una regla de lectura: al citar un acto que da una superficie o un importe que el libro ya trae de otro acto, se comparan (caso: 1.735,80 contra 1.736,80, ronda 70).

**Pendientes revisados sin cerrar.** P182 (láminas de 1986-1988: sin cambio). P183 (H y E de 1986-1988: la corrección de E:82 toca la entrada de Carlos Serrey, no las personas que P183 agrega; sigue abierto). P184 (pedidos de 1986-1988 fuera de D: siguen fuera; la fase 6 actualiza un ítem existente y no mueve el recuento: 22-prospectiva cierra con 284). P185 (dudas 1986-1988: ninguna toca la fase 6). P115 (10:516 sigue sin fuente para las cifras físicas del embalse). P40 (trazabilidad).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.337/25.337 líneas vigentes en `83a0b59` | 25.286 vigentes, 51 caducas por el AMPLÍA 1986-1988 |
| Citas de edición y hoja del texto agregado contra los bloques FUENTE de los tres informes | 146 pares (edición, hoja) de 1986-1988 | 146 localizados |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *nunca*, *jamás*, *ningún*, *ninguna*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *no lo dice*, *no se publica*, *no publica*, *no nombra*, *no dice*, *sin que*, *mayor*, *doble*, *otra vez*, *vuelve*, *de siempre*), sobre 8.347 palabras agregadas | 40 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («lo hallado de 1987 ni el de 1988», «en lo hallado del año», «la lectura halló seis trámites … y en ninguno»); «la más baja de cinco» y «sólo uno se publica» cierran contra las fichas |
| Repaso de ventana: afirmaciones que cierran en 1985 (*1958 a 1985*, *hasta 1985*, *a 1985*, *1958--1985*, *12.373*, *lo hallado de 1985*) y que abren el hueco en 1986 (*1986--2012*, *1986 a 2012*, *veintisiete años*, *setenta y un*, *veintiocho*, *veintinueve*, *desde 1986*, *de 1986 en adelante*) | libro entero | Una sin actualizar: D:177, «de 1975 a 1985» y «de 1964 a 1985» (hallazgo 4). Las demás: «1964 a 1985» y «1975 a 1985» de 22:545 son universos cerrados de una afirmación que el párrafo nuevo extiende; F:96 «quedan como 1958 a 1985» compara; «no se afora el río desde 1986» (23:13) es otra serie; «veintisiete años» de 03 y E, «veintiocho» de 10:44 y 22-prospectiva:144 son otras cuentas. Recuentos: 42 + 1 + 31 = 74 tramos; 74 − 42 = 32 fuera de las ventanas; 1989 a 2012 = 24 años |
| Propagación del CONTRADICE de la Ley 6354 (*Elena Serrey*, *1.303*, *6354*, *expropi*) | libro entero, 10 líneas con el nombre y 03:1031, que lo sigue | 4 sin corregir: A:478, C:122, E:82 y 03:1031 (hallazgo 1) |
| Anáforas en las líneas tocadas por el AMPLÍA (P159, P169 y P174) y texto que sigue a cada inserción | 80/80 líneas y las 27 inserciones de más de 300 caracteres | 0 caídas: «El dique tiene» sigue a la inserción de 10:516, con sujeto; «La lámina» de 22-prospectiva y 26 remite a la lámina, no al texto nuevo |
| Comillas rectas que `babel` deforma (P144) | 0 en lo agregado por el AMPLÍA y por la fase 6 | en el PDF compilado, 0 *Ç* y 0 *ç* |
| Caracteres de control (P158) | 38 archivos | 0 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`) | 351/351 `\ref{cap:…}` de un capítulo a uno posterior | 0 sin marcar, antes y después de la fase 6 |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Aritmética de 1986-1988 | 10 cuentas | 545.375,96 / 445.158,23 = 1,2251; 545.375,96 / 599.314,24 = 0,910; 3.003.122,13 / 654.123 = 4,59; 1.244.891,44 + 731.423,86 + 1.019.069,38 = 2.995.384,68; 300.000 + 249.537,38 + 69.000 = 618.537,38; 259.725,75 + 86.575,25 + 43.287,62 = 389.588,62 (la ley imprime 389.588); 15 planillas de 1986 (fichas A.1 a A.57); 4 de 1987; 6 de 1988; 10 + 5 = 15 decretos sin planilla. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 70 | 50 de 462 oraciones con cifra en las 80 líneas | **50/50 con fuente localizable**: 42 con la cita en la oración o en la fila (por script); las otras 8 son declaraciones de cobertura de 00, 02 y F, que remiten al apéndice F, y oraciones de síntesis seguidas de su cita o con remisión de capítulo. 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 80 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 80 líneas, cruzadas con contextos sensibles (P102: *remate*, *ejecución*, *juicio*, *deudor*, *embargo*, *cesante*, *renuncia*, *jubila*, *D.N.I.*, *clase*) | 80/80 líneas | 0 caídas. Sin nombre: la médica cesante, el ejecutado de la esquina de Güemes y Los Sauces, los deudores de las ejecuciones fiscales de Vaqueros, el titular de los derechos rematados en la avenida Güemes, los deudores del Banco Provincial, la becaria, el odontólogo. La clase de Mogro y el D.N.I. del juez de paz no están en el libro. Nombrados: autoridades comunales, candidatos y propietarios de expropiaciones por ley (actos públicos de utilidad pública, sin imputación) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `1bd1c1d` y fase 6, cada una en una copia limpia | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos, tres pasadas de `pdflatex`); 961 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin normas nuevas citadas en presente; las de 1986-1988 van en pasado |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas de acto y de publicación bien distinguidas (2876, 3041, 2786/85, 3653 y 3659/86) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 5 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Las ausencias de 1986-1988 llevan su universo; ninguna salvedad borrada |
| 6 | Tipo y jerarquía de fuente | 5 | 85 | 90 | Hallazgo 3 (−5); aplicado |
| 7 | Consistencia interna | 9 | 40 | 100 | Hallazgos 1 y 2: 2 errores en 61,2 páginas (50), con material a menos de diez páginas (un escalón más); aplicados |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 4 (−5); aplicado. 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P182 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 80 líneas; 90 como en la ronda 69 |

**Nota inicial: 82,3 antes del tope y 82,3 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el escrutinio del 6 de septiembre de 1987 en La Caldera y Vaqueros, que D:160 pide y que diría quién fue el primer intendente votado desde 1983, o la resolución judicial de la tierra del embalse---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9 (el 1, de 82 a 90); (4) dejar corriendo los controles de P164, P170, P174, P175, P181 y P186 como paso automático del AMPLÍA, que habrían atrapado los cuatro hallazgos de esta ronda: protege el 7, el 6 y el 8 en la nota inicial de la ronda siguiente (aquí, 6 puntos de la inicial); (5) hacer las láminas de P182 y las entradas de P183: hasta +0,2 en el 13 y el 15.

**Avance del libro:** 4 de 4 hallazgos resueltos (100 %) y tres precisiones aplicadas; compila sin errores ni referencias indefinidas, 961 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (de 1986 a 1988 la Provincia sigue designando por decreto a los presidentes de las dos comisiones hasta mayo de 1987, y el municipio aparece ante el agua como parte de convenios de defensas y, en Vaqueros, desplazado por un centro de usuarios; la convocatoria de 1987 le devuelve un ejecutivo votado, no una competencia) y la de la expropiación como mecanismo opuesto al mercado sucesorio, que con la fase 6 queda dicha en su estado documentado: tres declaraciones de utilidad pública, tres juicios promovidos y una posesión, sin sentencia hallada.

**Calidad de la auditoría.** Cobertura de la ronda: 80 líneas (0,32 %; 61,2 páginas). Cobertura acumulada: 25.366 de 25.366 (100,0 %), con el registro de arriba. Falsos positivos descartados: 7. Recortes: se leyeron enteras las fichas de los tres años en su FUENTE y FICHA, y el TEXTO y la NOTA de las que sostienen cifras, fechas, nombres o citas, no el TEXTO de todas; no se cotejaron renglón por renglón 5 de las 12 ediciones bajadas; los controles de P164, P170, P174, P175, P181 y P186 se corrieron a mano; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **4 de 4**, todos en el AMPLÍA 1986-1988 (`1bd1c1d`); **0 atrapados por un control automático**.

## Ronda 71 — auditoría con fase 6 (04/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2002, 2005. Base: commit `dbec62a` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2002, 2005, sobre `e8aae23`, la ronda 70), con la fase 6 en `ronda-71.patch` (commit `be14ccc` en la sesión; aplica con `git am` sobre `dbec62a`, probado en un clon limpio de GitHub: árbol `6d9ea02`). **Denominador medido: 25.394 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 70 (25.366 de 25.366, sobre `8ef9319`, que en GitHub es `e8aae23`, con el mismo árbol `9b3c0f2`) se trasladaron por diff a `dbec62a`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2002, 2005 agrega 28 líneas netas (6 en A, 9 en C, 1 en F, 1 en 05, 2 en 15, 3 en 16, 4 en 17 y 2 en 19) y deja 70 líneas nuevas o modificadas en 21 archivos: caducan 42 líneas anteriores**, y quedan **25.324 vigentes sobre 25.394 (99,7 %)**. La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `dbec62a`)

Se leyeron **las 70 líneas, enteras, por la sesión**, sin subagentes: las nuevas de A, C y F completas, y las modificadas del resto en su texto entero (177.558 bytes), además de la lista de cada cambio palabra por palabra con su contexto (5.885 palabras agregadas). Se cotejaron contra los dos informes LEE (`BO-Salta-2002_16302-16548_la-caldera_LEE-2002_2026-10-04.txt` y `BO-Salta-2005_17039-17166_la-caldera_LEE-2005_2026-10-04.txt`, de `corrige/lee/`), **leídos enteros**: §0, §1, §2, las 72 fichas del §A (43 de 2002 y 29 de 2005) y las 9 del §B.2 con su TEXTO y su NOTA, §B.3, §B.4, §C, §P, §D, §E y §F; y contra `amplia-2002-2005.json` (índice de 139 coincidencias y clasificación de fichas).

| Archivo | Líneas | Nuevas | Quién |
|---|---|---|---|
| ape/A-cronologia.tex | 4, 490–494, 496–498 | 9 | sesión |
| ape/C-normativa.tex | 312–320 | 9 | sesión |
| ape/D-pedidos.tex | 177, 253, 256, 324 | 4 | sesión |
| ape/E-personas.tex | 101 | 1 | sesión |
| ape/F-fuentes.tex | 25–26, 57, 97, 100 | 5 | sesión |
| cap/00-advertencia.tex | 43 | 1 | sesión |
| cap/01-planteo.tex | 119, 139 | 2 | sesión |
| cap/02-metodo.tex | 28, 99 | 2 | sesión |
| cap/04-siglo.tex | 3659 | 1 | sesión |
| cap/05-tierra.tex | 58, 372 | 2 | sesión |
| cap/09-defensas.tex | 690 | 1 | sesión |
| cap/13-loteo.tex | 325 | 1 | sesión |
| cap/14-poblacion.tex | 843, 847 | 2 | sesión |
| cap/15-hacienda.tex | 185, 473–474 | 3 | sesión |
| cap/16-redes.tex | 655–657, 664, 668–669 | 6 | sesión |
| cap/17-tierrafiscal.tex | 376–377, 379, 383, 401–402, 404, 434 | 8 | sesión |
| cap/18-politica.tex | 656, 672 | 2 | sesión |
| cap/19-resistencias.tex | 185–187, 201, 203, 206, 871 | 7 | sesión |
| cap/20-opacidad.tex | 880–881 | 2 | sesión |
| cap/22-infraestructura.tex | 545 | 1 | sesión |
| cap/26-presencia.tex | 235 | 1 | sesión |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09:535–642 (la serie de defensas de 1956 a 1988) y 09:684–692; 10:533–541 (la concesión de Skru S.A. en el catastro 1782) y 11:1080–1100 (el cuadro de catastros); 16:650–684; 17:355–436 (la comparación 1980-2015, la ficha del Decreto 2949 y sus dos cautelas); 19:105–177 (los cuadros de informes de impacto de 2021, 2020 y 2018) y 19:854–858 (la liga de fútbol); 21:70–80 y 136–150; 14:841–848; 15:468–476; 18:652–658; A:441 y 486–490; C:177; D:391.

**Esta ronda: 70 líneas nuevas**, 177.558 bytes sobre 3.191.804, que en las 967 páginas de la base equivalen a **53,8 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `dbec62a` cae dentro de estos tramos.

Acumulado: 25.324 vigentes + 70 = **25.394 de 25.394 (100,0 %)**. La fase 6 toca once líneas: A:491 y 496, D:177, 253 y 256, F:97, 17:376 y 26:235, dentro de lo leído en esta ronda, y 09:687, 10:539 y 19:858, que estaban vigentes y se releyeron como contexto; no cambia el largo de ningún archivo: **25.394 de 25.394 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 2002 y 2005 de `boletines-salta`)

Esta vez el Release se alcanzó desde la sesión (los informes LEE lo bajaron por la máquina del autor). Imágenes de los PDF renderizadas a 200 ppp con PyMuPDF; el renglón se ubicó con el reconocimiento `eng` de la sesión o con la capa del PDF (2005), se recortó a 230–300 ppp con su contexto y cada recorte se miró. Se bajaron 21 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 16423 | 5 | Ley 7192, art. 1 | «con cargo a la promoción de actividades sociales, culturales y deportivas», 3 hectáreas 5.092,76 m², matrícula 1.782, plano 475. Coincide (A:493, 17:376, 19:871) |
| 16488 | 11 | Decreto 1686, arts. 2 y 3 | «la prohibición de operar los servicios en cuestión» desde el 25 de septiembre; nueve municipios. Coincide (16:669, C:315) |
| 16434 | 7 | Decreto 1106, art. 3 | «Intendente de La Caldera, Dr. Héctor Miguel Calabró» e «Inauguración de obras en el Hospital Corina Bustamante». Coincide (18:656, E:101, 26:235) |
| 16322 | 5 | Licitación 01/02, objeto y lugar de venta | «comprende la prestación del servicio público entre las localidades ubicadas en los departamentos Capital, La Caldera y Cerrillos»; pliego de \$6.000 vendido en el Centro Cívico Grand Bourg y en la Casa de Salta. Coincide (16:655–658: el dato del pliego que P193 daba sin cotejo queda cotejado) |
| 16450 | 19 | La Caldera S.A., objeto | «loteos y urbanizaciones». Coincide (14:843) |
| 16421 | 10 | Aviso 085 | «50 Viviendas en La Caldera», préstamo BIRF 4273. Coincide (22:545) |
| 16308 | 37 y 38 | Ley 7170, renglones 5.7.6.1.28–29 y 5.7.6.2.28–29 | 420,036, 383,042, 58,703 y 55,789. Coincide (15:185, C:312) |
| 16363 | 16 | La Ferroviaria | «departamento Capital», expediente 17.394. Coincide (19:185) |
| 16544 | 39 | Rentas, aviso 698 | «PROVINCIA DE SALTA», catastro 102, \$108,126.07. Coincide (05:58) |
| 17078 | 32 | Remate en quiebra | «el monte ha borrado» varios de los trazados de las calles. Coincide (A:496) |
| 17045 | 9 | Res. SOP 1087 | «Refacción de Techos, Baños y Pintura» Escuela Nº 4534, \$48.210,61. Coincide (15:474) |
| 17123 | 10 | Decreto 768 | «Rehabilitación de la Toma Dique Campo Alegre», UTE Campo Alegre, \$33.741,26 al mes de agosto de 2003. Coincide (22:545) |
| 17087 | 11 | Puente Ferroviario | «lugar Río Mojotoro», expediente 16.386. Coincide (19:187) |
| 17044 | 12 | La Mesa Redonda, 2005 | «Abasto, José; Díaz, José y Otros», expediente 14.971. Coincide (19:201) |
| 17097 | 7 | Decreto 534, art. 1 | «Proyecto I S.A.», \$108.000, condición resolutoria. Coincide (17:401) |
| 17062 | 15 | Decreto 138, art. 1 | «Proyecto 1 S.A.», 3 lts./seg. del espejo del dique. Coincide (17:401, A:497) |

Bajadas y no cotejadas renglón por renglón: 16455, 16480, 17104 y 17158 (Ana María, Decreto 1594, Centauro y Decreto 1195; sus datos se cotejaron contra el TEXTO de las fichas).

Son **16 citas entre comillas del libro cotejadas en la imagen** («con cargo a la promoción…», «la prohibición de operar…», «Intendente de La Caldera, Dr. Héctor Miguel Calabró», «Inauguración de obras…», «comprende la prestación…», «loteos y urbanizaciones», «50 Viviendas en La Caldera», «departamento Capital», «PROVINCIA DE SALTA», «el monte ha borrado», «Refacción de Techos, Baños y Pintura», «Rehabilitación de la Toma Dique Campo Alegre», «lugar Río Mojotoro», «y Otros», «Proyecto I S.A.» y «Proyecto 1 S.A.»; los nombres propios entre comillas, como «Ana María» o «El Palenque», no se cuentan): **ninguna con diferencias**, sobre 18 citas nuevas del AMPLÍA (16/18; quedan sin cotejar «la prohibición…» de C, que repite la de 16, y «de propiedad fiscal» de 19:187, cotejada en dos de sus tres edictos), y datos sin comillas en 3 hojas más (16308 h37 y h38, 16322 h5).

### Hallazgos (dos, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 09:687 | «Después de 1980, el siguiente eslabón documentado de esta serie es de noviembre de 2001». El mismo capítulo, cuarenta y cinco líneas antes (09:640–642), da los convenios de defensas de 1985 a 1987 de la Provincia con las dos municipalidades (2786, 766, 1358, 603, 2447, 3206, 2436, 2437 y 2494) y las licitaciones de Vialidad Nacional de 1986 y 1987 en la ruta 9. La primacía se volvió falsa con el AMPLÍA 1983-1985 y sobrevivió a las rondas 69 y 70; el AMPLÍA 2002, 2005 tocó la ficha de dos renglones más abajo (09:690) y dejó la frase anotada como P191 | 5 (primacía sobre un universo que el libro desmiente con su propio dato) | «Después de los convenios y las licitaciones de 1985 a 1987, el siguiente eslabón documentado de esta serie ---en lo que este libro leyó de corrido, que de 1988 pasa a 2002--- es de noviembre de 2001» |
| 2 | D:177 | El pedido de las páginas que faltan en los escaneos suma de 2005 las cinco ediciones ausentes y las 22 páginas de la 17166, pero no las otras **454 páginas** que las tapas de cuarenta y siete ediciones de 2005 declaran y el archivo no trae ---sesenta y cuatro en la 17076: «EDICION DE 92 PAGINAS» con 28 hojas---, que F:97 declara («476 páginas más de las que hay», con las 22 de la 17166) y que el informe LEE 2005 da como límite 11. Para 1986 el mismo ítem sí pide «las diecisiete páginas que las tapas … declaran y el archivo no trae». Además fechaba «de marzo de 2005» las ediciones 17098 a 17101, que caen del 29 de marzo al 1 de abril | 8 (límite declarado sin su pedido) | «las otras cuatrocientas cincuenta y cuatro páginas que las tapas de cuarenta y siete ediciones de 2005 declaran y el archivo no trae ---sesenta y cuatro de ellas en la 17076, del 23 de febrero---»; «del 21 de marzo y del 29 de marzo al 1 de abril de 2005». El ítem no cambia el recuento: 284 |

**Precisiones aplicadas sin restar.** (a) A:491 y F:97: «se miraron sobre la imagen las tapas de 51 ediciones»; el informe LEE 2002 dice en su §1 «Las tapas no se leyeron en la imagen» y que lo cotejado en las 51 ediciones con ficha es la fecha (su E.10 lo deja ambiguo): «se cotejaron sobre la imagen las fechas de 51 ediciones» y, en F, «las tapas no se miraron». (b) A:496 y 26:235: la Res. 407-D/04 no deja sin efecto «la función de gerente general» sino «la asignación interina de función y el adicional por función jerárquica como Gerente General» de un médico (A.3/2005): «la asignación interina de la gerencia general». (c) A:496: después del Decreto 3073 la fila seguía con «; declara en emergencia…», de modo que el sujeto era el decreto de Las Mesadas; la emergencia es del 212: «otro, de febrero, declara…». (d) D:253: los convenios que coordina el Consejo Profesional de Ciencias Económicas son de colaboración de la Provincia con los municipios, y el del Consejo con la Provincia es de 2004 (Decreto 2079/04), prorrogado en 2005 (677, A.21/2005); el pedido decía «los convenios de 2005 con el Consejo». (e) D:256: «si la La Caldera S.A.» → «si La Caldera S.A.». (f) 17:376: el Decreto 996 veta también parte del artículo 2 de la Ley 7192 («…que el comodatario inicie…», el plazo de cinco años para construir), no sólo el plano y el artículo 5. (g) 19:858: «la liga de fútbol lo resolvió sola en 2015» (repaso de ventana): el libro tiene su estatuto aprobado en 1985 (A:472) y su sede en Vaqueros en 2002 (A:491): «con estatuto aprobado en 1985 y sede en Vaqueros al menos desde 2002». (h) 10:539: la cautela de la concesión de Skru S.A. en el catastro 1782 dice que el edicto no da la relación del catastro con el inmueble expropiado, y el libro no cruzaba que con ese número hay una matrícula fiscal ---la de la escuela náutica del dique en 1979 (A:441, C:177) y la del comodato al Club de Regatas Güemes en 2002 (17:376)--- y que Rentas lista en 2002 el catastro 1782 a nombre de la Provincia (A.41/2002, que el informe da como inferencia por la igualdad de número): se agrega, con remisión y sin afirmar que sea parte de lo expropiado.

Resta: una primacía desmentida por el propio libro, en el aspecto 5: **resta 10** (90), por su alcance de frase y el agravante de la rúbrica. Un límite sin pedido, en el aspecto 8: **resta 5** (90). Ninguno sostiene una sección: no hay tope por alcance. Sin errores de consistencia en las 53,8 páginas: **100** en el aspecto 7. Aplicados los dos: 100 en el 5 y 95 en el 8 en la nota final.

**Errores introducidos por la propia auditoría**: los dos. El 1, en material del AMPLÍA 1983-1985 (`4807954`) y 1986-1988 (`1bd1c1d`), que agregaron a 09:640–642 los convenios que desmienten la frase sin repasarla; el AMPLÍA 2002, 2005 la vio y la dejó como pendiente (P191) en lugar de corregirla. El 2, en el AMPLÍA 2002, 2005 (`dbec62a`), que agregó la cifra a F:97 y no al ítem de D que pide lo mismo: es el control (2) de P186, que no corre solo. **Ninguno lo atrapó un control automático.** Los controles de P144 (comillas rectas: 0 nuevas), P158 (caracteres de control: 0), P164 (fecha de acto y de publicación: Res. SOP 516 de 2001 publicada en enero de 2002, Res. SOP 1087 y 407-D y Decreto 3073 de fines de 2004 publicados en enero de 2005, el 534 de marzo publicado el 28: bien dichos), P170 (remisiones), P174 (anáforas) y P102 (privacidad) se corrieron a mano y no dieron caídas.

**Descartados (falsos positivos, 10).** «Tierra fiscal junto al dique» (A:491, 01:139) contra «Que la fracción esté sobre el perilago no lo dice la ley» (17:376): lo primero describe la matrícula 1.782, la de la escuela náutica del dique de 1979; lo segundo, la fracción dentro de ella. «Casi cinco veces el plazo de 2015, sobre una doceava parte de su superficie» (17:376): 99 / 20 = 4,95 y 3,509 / 41,83 = 0,084. «El agua se concedió dos meses antes» (17:401): del 17 de enero al 9 de marzo, cincuenta y un días; redondeo admisible y el texto no da la cifra exacta como tal. «Tres cosas conviene retener» (16:662): la base tenía dos y el AMPLÍA agrega la tercera. «Tomasito, del mismo titular que en el cuadro» (19:187): Héctor Enrique Medina en el edicto y en el cuadro. «Unas setenta y dos hectáreas» (19:203): 42,0658 + 4,4395 + 22,7773 + 2,9412 = 72,22. «Once años antes» (19:201): de 2005 a 2016. «Proyecto I S.A.» y «Proyecto 1 S.A.»: las dos grafías están en la imagen. «El archivo de cuatro, entre ellas Felisa» (A:491): Oscar, Gimena, María Belén y Felisa (A.8, A.13, A.22 y A.31 de 2002). «La deuda más alta del departamento en ese listado» (05:58): la siguiente del aviso 698 es de \$33.393,47.

**Pendientes que cierra.** P191 (09:687, hallazgo 1).

**Pendientes nuevos.** P195 (herramientas): dos controles más para AMPLÍA (extensión de P186). (1) **Páginas declaradas por las tapas**: toda cifra de páginas que las tapas declaran y el archivo no trae, que el AMPLÍA agregue a 00 o a F, se busca en D:177, igual que las hojas sin mirar (caso: las 454 de 2005, ronda 71). (2) **Primacías relativas en el capítulo que recibe material**: además de las oraciones con un rango que incluya los años nuevos, el repaso de ventana busca en los capítulos que el AMPLÍA toca las fórmulas «el siguiente», «después de», «recién en», «hasta» seguidas de un año, y las juzga contra lo que el mismo capítulo ya trae (caso: 09:687, ronda 71). Y una regla de lectura: un pendiente que el AMPLÍA abre sobre una frase que ya sabe falsa se corrige en el mismo AMPLÍA; dejarlo como pendiente no lo saca del libro.

**Pendientes revisados sin cerrar.** P186 (sus controles siguen corriendo a mano). P187 (láminas de 2002 y 2005: sin cambio). P188 (H y E de 2002 y 2005: la precisión de 10:539 cruza la matrícula 1782 en el texto, no en H). P189 (pedidos de 2002 y 2005 fuera de D: siguen fuera; la fase 6 amplía un ítem existente y no mueve el recuento: 22-prospectiva cierra con 284). P190 (separata del Decreto 1.989/02: no se miró el 16515). P192 (dudas 2002-2005: ninguna toca la fase 6). P193 (su punto 2, el pliego del corredor que «se vende en dos lugares», queda cotejado en la imagen: 16322 h5; los puntos 1 y 3 siguen). P194 (sin cambio). P115 y P40.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.366/25.366 líneas vigentes en `e8aae23` | 25.324 vigentes, 42 caducas por el AMPLÍA 2002, 2005 |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *tampoco*, *sólo*, *siempre*, *todos*, *todas*, *mayor*, *menor*, *más alta*, *ya*), sobre 5.305 palabras agregadas | 37 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («en lo hallado», «leídos también con pendientes», «en ese listado», «en lo leído de los dos años»); «el primer año posterior a 1988 que este libro lee de corrido» y «los primeros posteriores a 1988» cierran contra la serie; «mayor que La Mesa Redonda» cierra (42,07 contra 32,52 ha) |
| Repaso de ventana: afirmaciones con un año de 1989 a 2012 precedido de *no*, *ningún*, *único*, *primer*, *sólo*, *recién*, *hasta*, *desde*, *todavía*, *tampoco*, *falta*, fuera de las líneas del AMPLÍA | libro entero (base `dbec62a`), 78 coincidencias en 75 líneas, todas leídas | Ninguna cae por lo de 2002 y 2005: «la serie de trámites … al menos, en 2004» (11:1609), «los más antiguos que la serie registra son de 2004 y 2005» (D:57), «se usa desde 2005» (17-aguabaja:393) y «el único acto … como una unidad de planificación es el convenio … de 2009» (19:484) no tienen dato contrario en los dos informes. Por la lectura del capítulo de contexto, no por el script: 09:687 (hallazgo 1, P191) y 19:858 (precisión g) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, con el renglón siguiente, y 60 antes; orden de `\input` de `main.tex`) | 356/356 `\ref{cap:…}` de un capítulo a uno posterior antes de la fase 6; 357/357 después | 0 sin marcar, antes y después |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Aritmética de 2002 y 2005 | 9 cuentas | 420.036 / 73.485.667 = 0,57 %; 42.848,85 / 33.741,26 = 1,270; 99 / 20 = 4,95; 3,509 / 41,83 = 0,084; suma de las cuatro canteras = 72,22 ha; 62.129,05 − 62.121,05 = 8; 476 − 22 = 454 páginas; 92 − 28 = 64 en la 17076; 108.126,07 de 220.352,36. Cierran |
| Citas de edición y hoja del texto agregado contra el texto de los dos informes (FUENTE, §B, §C y §D) | 58 pares (edición, primera hoja) de 2002 y 2005 | 58 localizados |
| Muestra de 50 afirmaciones (aspecto 1), semilla 71 | 50 de 350 oraciones con cifra en las 70 líneas | **50/50 con fuente localizable**: 32 con la cita en la oración o en la fila (por script); las otras 18 son declaraciones de cobertura de F (13, la mayoría de la línea F:57, que el AMPLÍA tocó por una palabra) y de 02, que remiten al apéndice F y a los informes, y oraciones de síntesis seguidas de su cita o de su ficha (17:434, 19:187, 15:185). 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 70 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 70 líneas, cruzadas con contextos sensibles (P102: *remate*, *quiebra*, *prescripción*, *deudor*, *concurso*, *cesante*, *renuncia*, *D.N.I.*) | 70/70 líneas | 0 caídas. Sin nombre: los titulares de los catastros de las dos prescripciones, los treinta y siete deudores del listado de Rentas salvo la Provincia y Vialidad, el fallido del remate, los propietarios de los tres loteos de Vaqueros, el médico de la gerencia, la odontóloga, la jefa del Registro Civil, los dos contadores de La Caldera S.A. Nombrados: autoridades (Calabró), presidentes de asociaciones con asamblea publicada (Teodoro B.\ Mogro), sociedades y concesionarios mineros que el libro ya nombraba en el cuadro de 2021 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `dbec62a` y fase 6, cada una en una copia limpia | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos, tres pasadas de `pdflatex`); 967 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2002 y 2005 van en pasado; la Ley 7192 se cita como lo que dispuso |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas de acto y de publicación distinguidas (Res. SOP 516, 1087, 407-D, Decreto 3073, Ley 7192 y Decreto 996) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 16 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgo 1 (−10); aplicado. Las ausencias de 2002 y 2005 llevan su universo |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales (expediente /00 y /02, planos 475 y 457, Proyecto 1 e I, 768 y 1195, letras y cifras del camping) están señaladas |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores de consistencia en 53,8 páginas |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 2 (−5); aplicado. 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P187 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 70 líneas; 90 como en la ronda 70 |

**Nota inicial: 86,7 antes del tope y 86,7 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el escrutinio de 1987, la resolución judicial de la tierra del embalse o, ahora, si el catastro 1782 de la turbina de 2019 es parte de lo expropiado en 1972---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9 (el 1, de 82 a 90); (4) dejar corriendo los controles de P186 y P195 como paso automático del AMPLÍA, que habrían atrapado los dos hallazgos de esta ronda: protege el 5 y el 8 en la nota inicial de la ronda siguiente (aquí, 1,6 puntos de la inicial); (5) hacer las láminas de P187 y las entradas de P188: hasta +0,2 en el 13 y el 15.

**Avance del libro:** 2 de 2 hallazgos resueltos (100 %) y ocho precisiones aplicadas; compila sin errores ni referencias indefinidas, 967 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (en 2002 y 2005 el municipio aparece ante el suelo como el que dio factibilidad al hotel por la Ordenanza 339/01, citada por la Provincia en la venta de la tierra, y como contratista por convenio de una escuela; la Provincia da en comodato, vende y concede agua del embalse) y la de la intensidad regulatoria inversa, que suma la venta de 2005 de la matrícula 3337, con la escritura exenta de todo tributo, al comodato de 2015 de la misma firma.

**Calidad de la auditoría.** Cobertura de la ronda: 70 líneas (0,28 %; 53,8 páginas). Cobertura acumulada: 25.394 de 25.394 (100,0 %), con el registro de arriba. Falsos positivos descartados: 10. Recortes: no se cotejaron renglón por renglón 4 de las 21 ediciones bajadas ni 2 de las 18 citas nuevas; los controles de P164, P170, P174, P186 y P195 se corrieron a mano; la muestra de trazabilidad no se rehízo; no se miró el 16515 (P190). Errores introducidos por la propia auditoría: **2 de 2**, uno en los AMPLÍA 1983-1985 y 1986-1988 (`4807954`, `1bd1c1d`) y otro en el AMPLÍA 2002, 2005 (`dbec62a`); **0 atrapados por un control automático**.

## Ronda 72 — incorporación (05/10/2026)

Tipo: **incorporación** (CORRIGE 3.6): integra al libro la cuarta tesis, «la desidia es selectiva», a pedido del autor. No es una auditoría: se informa sólo la nota final, sin tope de cobertura, y el aspecto 7 no se calcula. Base: commit `e1e33ce` de `ediedrich/dispositivo-caldereno` (la ronda 71). La incorporación está en `ronda-72.patch` (commit `9b362d4` en un clon limpio de GitHub, árbol `c5e21e3`). **Denominador: 25.394 líneas antes y 25.419 después** (38 archivos `.tex` con `main.tex`, `wc -l`).

### Qué entra

- **Capítulo 1** (pasa a llamarse «Las cuatro tesis»): sección nueva, «Cuarta tesis: la desidia es selectiva», con su evidencia, su formulación, su diferencia con la primera tesis y su límite («que el Boletín Oficial no publique el cierre de una obra no prueba que la obra no se haya hecho»). En «Cómo se relacionan», la cuarta como tesis de resultado; en «Qué refutaría cada tesis», su refutador.
- **Advertencia**: la cuarta tesis en un párrafo, y «Ninguna de las cuatro».
- **Conclusión**: «Las cuatro tesis, al cabo», con un párrafo de balance; «Las cuatro tesis tienen sus propios refutadores».
- **Capítulo de infraestructura** y **`main.tex`**: de tres a cuatro tesis.
- **Apéndice D**: un pedido nuevo, en «Obra pública, prestadoras y programas de financiamiento», de los certificados finales y las actas de recepción de las obras de defensa y de cauce de 1967 a 1977. **22-prospectiva**: «doscientos ochenta y cinco pedidos».

Toda frase nueva remite a material que el libro ya tenía, con su capítulo: 09:535 (serie de defensas, con las citas de edición y hoja que el pedido nuevo repite), 01:155 y capítulo 10 (expropiación del embalse), 17:376 y 17:401 (comodato de 2002 y venta de 2005), la ficha del Decreto 2949 (comodato de 2015), 16:669 (línea 23) y capítulo 10 (expropiaciones de 1985 y 1986 sin sentencia). Las diez citas de decreto, edición y hoja del pedido nuevo se cotejaron contra 09:535: coinciden.

### Cobertura

Esta ronda no audita. **Caducan 13 líneas** anteriores y quedan **38 líneas nuevas o modificadas** sin auditar: D:331; 00:15–17; 01:1, 123–140, 143, 151, 159–161; 21:22, 29–30, 91; 22-infraestructura:20, 23, 25–26; 22-prospectiva:290; main:310. Las audita la ronda MEJORA siguiente. Acumulado: **25.381 de 25.419 (99,9 %)**.

### Controles por script

| Control | Denominador | Resultado |
|---|---|---|
| Menciones de «tres tesis» y sus variantes («las tres se», «tres condiciones», «las tres son», «pero las tres», «ninguna de las tres» referidas a las tesis) | libro entero | 11 actualizadas, en 00, 01, 21, 22-infraestructura y `main.tex`; las demás coincidencias son de otras cosas |
| Remisiones a capítulos posteriores sin «más adelante» | 367/367 `\ref{cap:…}` | 0 sin marcar |
| `\pendiente{}`, ítems de D | 52; 285 | 22-prospectiva dice «doscientos ochenta y cinco pedidos»: cierra |
| Superlativos y ausencias en el texto agregado | «ninguna sentencia hallada», «lo hallado hasta 1988», «sin cierre conocido» | llevan su universo |
| Compilación | libro entero, en un clon limpio con el parche aplicado | compila con tres pasadas de `pdflatex`; 969 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas de la ronda 71 |

### Nota final

La misma de la ronda 71 en catorce aspectos. **Aspecto 10 (argumentación): 70.** La cuarta tesis tiene evidencia primaria y declara qué la refutaría, pero no pasó todavía por la verificación (dos sí: 70), y el promedio entre tesis no cambia. **Nota final: 88,3** (incorporación: sin tope).

**Avance de la investigación.** Se suma una tesis abierta: la cuarta, «la desidia es selectiva», con 0 (abierta). La serie que la mediría ---obras y trámites del departamento clasificados por a quién sirven, con la proporción y el tiempo de sus actos de cierre publicados--- queda como pendiente P196.

**Pendientes nuevos.** P196 (libro): serie de la cuarta tesis, a construir con las fichas LEE de todos los años leídos.

**Calidad de la ronda.** Errores introducidos: no se sabe todavía; los mide la auditoría siguiente sobre las 38 líneas.

## Ronda 73 — auditoría con fase 6 (06/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2007-2009 y sobre las 38 líneas que la ronda 72 dejó sin auditar. Base: commit `82b47fb` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2007-2009, sobre `573f289`, la ronda 72), con la fase 6 en `ronda-73.patch` (un commit; aplica con `git am` sobre `82b47fb`, probado en un clon limpio de GitHub: árbol `2971e38`). **Denominador medido: 25.440 líneas** (38 archivos `.tex` con `main.tex`, `wc -l`) antes y después de la fase 6: **ningún archivo cambia de largo** con la fase 6, y la numeración de abajo vale para las dos versiones. Sesión del ciclo automático (tarea programada), con el turno tomado en `auto/sesion.json`.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 72 (25.381 de 25.419, sobre `9b362d4`, que en GitHub es `573f289`, con el mismo árbol `c5e21e3`) se trasladaron por diff a `82b47fb`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2007-2009 agrega 21 líneas netas (9 en A, 9 en C, 1 en F y 2 en 09) y deja 68 líneas nuevas o modificadas en 24 archivos: reemplaza o borra 47 líneas anteriores**, dos de las cuales (01:127 y 01:129 de `573f289`) estaban entre las 38 sin auditar de la ronda 72: **caducan 45 líneas vigentes**, y quedan **25.336 vigentes sobre 25.440 (99,6 %)**. Las otras 36 líneas de la ronda 72 siguen en su lugar o se corren sin cambiar (00:15–17; 01:1, 123–126, 128, 130–140, 143, 151, 159–161; 21-conclusion:22, 29–30, 91; 22-infraestructura:20, 23, 25–26; 22-prospectiva:290; D:331; main:310). La ubicación de cada línea se tomó del diff con `difflib` sobre las dos versiones de cada archivo.

### Lectura sobre el texto (numeración de `82b47fb`)

Se leyeron **las 104 líneas, enteras, por la sesión**, sin subagentes: las 68 del AMPLÍA (las nuevas de A y C completas y las modificadas del resto en su texto entero) y las 36 de la ronda 72 (161.624 bytes). Se cotejaron contra los tres informes LEE (`BO-Salta-2007_17532-17776_la-caldera_LEE-2007_2026-10-06.txt`, `BO-Salta-2008_17777-18019_la-caldera_LEE-2008_2026-10-06.txt` y `BO-Salta-2009_18020-18258_la-caldera_LEE-2009_2026-10-06.txt`, de `corrige/lee/`): §0, §1 y §2 de los tres, **las 149 fichas del §A enteras** (50 de 2007, 45 de 2008 y 54 de 2009) con su TEXTO y su NOTA, el B.2 de 2007 y los renglones del B.2 de 2008 y 2009 que el libro cita, y §E y §R de 2007 y E.2 y E.4 de 2008 y 2009; y contra `amplia-2007-2009.json` (índice de 213 coincidencias, clasificación de fichas, controles y citas que pedía cotejar).

| Archivo | Líneas | Nuevas | De dónde |
|---|---|---|---|
| ape/A-cronologia.tex | 4, 478, 499–501, 503–504, 506–509 | 11 | AMPLÍA |
| ape/C-normativa.tex | 4, 122, 321–329 | 11 | AMPLÍA |
| ape/D-pedidos.tex | 39, 177, 239, 253, 256, 331 | 6 | AMPLÍA 5, ronda 72 1 |
| ape/F-fuentes.tex | 25–26, 98, 101 | 4 | AMPLÍA |
| cap/00-advertencia.tex | 15–17, 45 | 4 | AMPLÍA 1, ronda 72 3 |
| cap/01-planteo.tex | 1, 119, 123–140, 143, 151, 157, 159–161 | 26 | AMPLÍA 4, ronda 72 22 |
| cap/02-metodo.tex | 28, 99 | 2 | AMPLÍA |
| cap/03-fincas.tex | 1031 | 1 | AMPLÍA |
| cap/04-siglo.tex | 3659 | 1 | AMPLÍA |
| cap/05-tierra.tex | 372 | 1 | AMPLÍA |
| cap/09-defensas.tex | 723–724, 824 | 3 | AMPLÍA |
| cap/10-expropiacion.tex | 139, 146 | 2 | AMPLÍA |
| cap/11-ribera.tex | 1619 | 1 | AMPLÍA |
| cap/13-loteo.tex | 264 | 1 | AMPLÍA |
| cap/14-poblacion.tex | 847 | 1 | AMPLÍA |
| cap/15-hacienda.tex | 185, 474 | 2 | AMPLÍA |
| cap/16-redes.tex | 580 | 1 | AMPLÍA |
| cap/17-aguabaja.tex | 319, 325 | 2 | AMPLÍA |
| cap/17-tierrafiscal.tex | 142, 401, 434 | 3 | AMPLÍA |
| cap/19-resistencias.tex | 187, 201, 203, 484, 918, 926 | 6 | AMPLÍA |
| cap/20-opacidad.tex | 880–881 | 2 | AMPLÍA |
| cap/21-ausencias.tex | 76 | 1 | AMPLÍA |
| cap/21-conclusion.tex | 22, 29–30, 91 | 4 | ronda 72 |
| cap/22-infraestructura.tex | 20, 23, 25–26, 545 | 5 | AMPLÍA 1, ronda 72 4 |
| cap/22-prospectiva.tex | 290 | 1 | ronda 72 |
| cap/26-presencia.tex | 235 | 1 | AMPLÍA |
| main.tex | 310 | 1 | ronda 72 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09:535 (la serie de defensas de 1956 a 1988, con las adjudicaciones de 1967, 1970 y 1974); 16:650–672 (el corredor de 2002 y el Decreto 1686); 19:100–160 (los cuadros de informes de impacto de 2021 y 2020) y 19:895–926 (Macarena, El Vaquero y Los Yacones); D:255–260 (los pedidos del hotel y de las emergencias agropecuarias); 21-ausencias:182 (la Ley 4708); las entradas de C que nombran las normas de C:4.

**Esta ronda: 104 líneas nuevas**, 161.624 bytes sobre 3.242.292, que en las 983 páginas de la base equivalen a **49,0 páginas**: ése es el denominador del aspecto 7. El diff entero del AMPLÍA `82b47fb` y las 36 líneas restantes de la ronda 72 caen dentro de estos tramos.

Acumulado: 25.336 vigentes + 104 = **25.440 de 25.440 (100,0 %)**. La fase 6 toca ocho líneas: 01:129, 01:139, 14:847, 19:187, A:499, C:4 y D:331, dentro de lo leído en esta ronda, y D:260, que estaba vigente y se releyó como contexto; no cambia el largo de ningún archivo: **25.440 de 25.440 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 2007 a 2009 de `boletines-salta`)

Esta vez las descargas directas del Release llegaron desde la sesión. Imágenes de los PDF renderizadas a 220–250 ppp en gris con PyMuPDF; el renglón se ubicó con la capa del PDF y cada recorte se miró. Se bajaron 18 ediciones.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 17771 | 21 | La Generosa, solicitante | «Ing.\ Medina, ha solicitado la renovación», Expte. 16.893. Coincide (16:580, 19:187, A:499) |
| 17612 | 7 | Decreto 1231, considerando | «pendientes de resolución, numerosos pedidos de adjudicación en venta», sección «B», Barrio El Jardín. Coincide (17-tierrafiscal:142) |
| 17710 | 18 | Res. 753, art. 2 | «\$ 64.000,00 ... como crédito legal y suscribir el Convenio». Coincide (15:474, A:499) |
| 17630 | 16 | Res. Conj. 128-125, art. 1 | «Optimización Sistema de Agua Potable a La Caldera - Nueva Captación Río La Caldera ...». Coincide (A:501, 22:545, C:322) |
| 17568 | 6 | Decreto 391, considerando | «único y universal heredero de Manuel Serrey, titular registral de 6/10 partes». Coincide (A:500, 10:146, C:321, D:239) |
| 17810 | 14 | Res. SOP 16, art. 1 | «Encauzamiento en el Arroyo Urquiza - Chaile y Río Vaqueros», \$50.398,00. Coincide (09:723, A:503) |
| 17909 | 16 | Decreto 2838, art. 1 | «Hospital "Enfermera Adela Corina Bustamante"». Coincide (26:235) |
| 18189 | 12 | Decreto 3979, art. 1 | «Hospital "Enfermera Adela Corina Bustamante"». Coincide (26:235) |
| 17898 | 18 | La Serena, superficie | «s/fs.\ 9:05 has.\ 1.599 m2». Coincide (19:187) |
| 17916 | 6 | Decreto 2959, considerando | «el pertinente proceso se encuentra en trámite», Juzgado Civil y Comercial de 12ª Nominación; la carátula empieza por «Serrey de González Bonorino, Elena». Coincide (A:504, 10:146, C:324, D:39) |
| 17802 | 12 | La Vaquera, lugar | «Lugar: Río Vaquero», Expte. 18.770. Coincide (19:187) |
| 18033 | 7 | Decreto 5859, art. 1 | «a edificarse en un inmueble de 6 Has.\ de extensión, ubicado en el Dique Campo Alegre», Matrícula 3.337. Coincide (17-tierrafiscal:401, A:506) |
| 18135 | 29 | La Mesa Redonda, 2009 | «Juan Domingo Lozano por Cooperativa La Mesa Redonda, ha solicitado publicación de la renovación», Expte. 14.971. Coincide (19:201) |
| 18236 | 39 | Remate de las matrículas 1120 y 1121 | «Sur: Prop.\ de Francisco Urquiza». Coincide (09:723, A:507) |
| 17646 | 10 | Firma del Decreto 847 | «Sr.\ Mashur Lapad, Vice-Presidente 1º Cámara de Senadores a Cargo Poder Ejecutivo»; el número y la fecha (7 de marzo de 2007), por la capa. Hallazgo 3 |
| 17756 | 8 | Firma del Decreto 3044 | La misma firma; número y fecha (7 de noviembre de 2007), por la capa. Hallazgo 3 |

Bajadas y no cotejadas renglón por renglón: 17626 (Res. SOP 220, cotejada contra el TEXTO de la ficha A.15/2007).

Son **12 citas entre comillas del libro cotejadas en la imagen** («Ing.\ Medina», «pendientes de resolución, numerosos pedidos de adjudicación en venta», «como crédito legal», «Optimización Sistema de Agua Potable a La Caldera», «Arroyo Urquiza - Chaile», «Enfermera Adela Corina Bustamante», en sus dos actos, «9:05 has.», «se encuentra en trámite», «Río Vaquero», «en un inmueble de 6 Has.\ de extensión», «por Cooperativa La Mesa Redonda» y «Prop.\ de Francisco Urquiza»): **ninguna con diferencias**. Son las once que `amplia-2007-2009.json` pedía cotejar, más la del nombre de la obra de agua; las demás citas nuevas (75 en total, según el AMPLÍA, literales en el TEXTO de los informes) quedan cotejadas sólo contra el informe: 12/75 en la imagen, y datos sin comillas en 3 hojas más (17568 h6, 17646 h10, 17756 h8).

### Hallazgos (cuatro, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 01:139 | La medida de la cuarta tesis contaba entre los actos de cierre la **adjudicación** («su acto de cierre ---adjudicación, certificado final, recepción, sentencia---»). Con esa medida la evidencia de la tesis se da vuelta: las obras de defensa y de cauce de 1967 (D-16), 1970 (D-3/69) y 1974 (Caminos S.\ A.) tienen la adjudicación publicada (09:535; D:331, de la misma ronda 72, dice «la D-3/69, adjudicada en 1970»), y la obra de agua potable del pueblo de 2007 llega a la adjudicación dos meses después de su llamado (A:501, 22:545), de modo que lo que «queda abierto» (01:129) tendría cierre y lo que sirve al pueblo cerraría rápido. El refutador de la misma sección (01:159) mide con certificados finales y actas de recepción, no con adjudicaciones. Y la oración siguiente decía que la serie «queda pendiente para los años que falta leer», como si estuviera armada para los leídos (P196 la da por armar entera) | 7 (contradicción entre la medida de una tesis y su evidencia, a menos de diez líneas) | «acto de cierre ---certificado final, recepción, sentencia, escritura---. La adjudicación no es un cierre: la tienen publicada las obras de defensa y de cauce de 1967, 1970 y 1974 (capítulo defensas, más adelante), y la tiene, dos meses después de su llamado, la obra de agua potable del pueblo de 2007, de la que lo leído no dice si se terminó (capítulo infraestructura, más adelante); es el dato del libro que más se acerca a contradecir la tesis, y se deja a la vista. La serie queda por armar, con lo ya leído y con los años que falta leer»; en el título, «todavía no la midió» |
| 2 | 19:187 | «Los de 2007 a 2009 ... dan el origen de otras tres filas, **renuevan dos que ya lo tenían** y traen tres canteras que el cuadro no trae»: renuevan tres. Además de «Tomasito» y «Ana María», cuyo origen dan los edictos de 2002, en 2009 se pide la renovación de «La Mesa Redonda» (Nº 18135, h.\ 29; LEE 2009, A.24), cuyo origen da el edicto de 2005, y el propio capítulo lo cuenta catorce líneas más abajo (19:201) | 7 (recuento del contenido que no cierra con material a menos de diez páginas) | «renuevan tres que ya lo tenían ---la tercera, «La Mesa Redonda», más abajo---» |
| 3 | A:499 | La fila de 2007 daba como firmantes a cargo del Ejecutivo «el vicegobernador y, **en febrero**, el vicepresidente primero del Senado». El informe LEE 2007 (E.4) da a Mashur Lapad en el decreto 391 del 5 de febrero y en decretos de las ediciones 17646, 17653, 17661 y 17756; en la imagen, su firma cierra el Decreto 847 del 7 de marzo (Nº 17646, h.\ 10) y el 3044 del 7 de noviembre (Nº 17756, h.\ 8). Es la falla de la ronda 69 (De los Ríos «en febrero»), que el control (1) de P181 debía atrapar | 3 (tramo de una firma dado por el primer acto, de segunda mano y sin recalcular) | «y, en decretos sueltos de febrero a noviembre, el vicepresidente primero del Senado» |
| 4 | C:4 | «Trece de sus entradas ---... las Leyes 3292/58, **4708**, 4829/74, ...--- no se citan en ningún capítulo»: la Ley 4708 la cita el capítulo de ausencias (21-ausencias:182, «Ley 4708, Nº 9421, h.\ 8»), desde el AMPLÍA 1973-1974 (`d99ba07`). El AMPLÍA 2007-2009 rehízo esta frase (de catorce a trece, por la Ley 7460) sin buscar las demás. Las otras doce, buscadas en los 26 archivos de `cap/`: ninguna aparece | 8 (recuento del aparato que no coincide con la estructura que lo produce) | «Doce de sus entradas ---los Decretos 1.045/96, 1498, 3774/09 y 4.913/98 y las Leyes 3292/58, 4829/74, 5061, 5114, 5814, 6133, 6895 y 27.424--- ... Once se consignan ...; la duodécima, el Decreto 1.045/96» |

**Precisiones aplicadas sin restar.** (a) 01:129: el reclamo del intendente por la línea 23, puesto entre «lo que queda abierto», sólo «tiene respuesta en septiembre de 2002», que se lee como un cierre; el capítulo de redes (16:669) dice que la respuesta es quitarle las líneas a la empresa y que lo hallado no dice quién las tomó: se agrega «cuando la Provincia le quita las líneas a esa empresa, sin que lo hallado diga quién las tomó». (b) D:331: el pedido de los certificados de las defensas de 1967 a 1977 enumeraba «los legajos de 1974 a 1977» sin el de las defensas del río Las Nieves de 1974 (6489, Nº 9618, h.\ 11) ni el del Wierna de 1977 (Res.\ 594, Nº 10345, h.\ 17), que el capítulo de defensas da en la misma serie, y el primero de la lista (5770) es una adjudicación: «la adjudicación y los legajos de 1974 a 1977», con los dos agregados. (c) D:260: el pedido de la serie de declaraciones de emergencia agropecuaria de 1980 a 2018 enumera lo hallado de 1980, 1984 y 1987 y no el Decreto 212 de 2005 ni los 2247 de 2008 y 1197 de 2009, que el capítulo de tierra ya da (05:372; LEE 2008 A.13 y LEE 2009 A.7): se agregan, con los expedientes de los dos últimos (090-0017.418/07 y 31.566/09), dentro del mismo ítem. (d) 14:847: «y para construir el hotel en el que la firma ya había obtenido ... otro contrato» → «y en el que, para construir el hotel, la firma ya había obtenido ... otro contrato».

Resta: dos errores de consistencia en 49,0 páginas, 4,08 por cada 100: **40** por el escalón; el primero sostiene una tesis y limita el aspecto a 50, y los dos contradicen material a menos de diez páginas: un escalón más, **30** en el aspecto 7. Un tramo de segunda mano sin recalcular, en el aspecto 3: **resta 5** (95). Un recuento del aparato, en el aspecto 8: **resta 5** (90). Ninguno es una ausencia falsa ni un error de vigencia: no hay tope por alcance. Aplicados los cuatro: 100 en el 3 y en el 7 y 95 en el 8 en la nota final.

**Errores introducidos por la propia auditoría**: los cuatro. El 1, en la incorporación de la ronda 72 (`9b362d4`, `573f289` en GitHub), que definió la medida. El 2 y el 3, en el AMPLÍA 2007-2009 (`82b47fb`). El 4, en el AMPLÍA 1973-1974 (`d99ba07`), que citó la Ley 4708 en un capítulo, y el AMPLÍA 2007-2009 lo arrastró al rehacer la frase. **Ninguno lo atrapó un control automático**: el 3 es el control (1) de P181, que no corre solo; el 2 y el 4 son controles que no existían (P202). Los controles de P102 (privacidad: 0 caídas), P144 (comillas rectas: 0), P158 (caracteres de control: 0), P164 (fecha de acto y de publicación: el 5859 de diciembre de 2008 publicado en enero de 2009, la Res.\ Conj.\ 128-125 de febrero publicada en mayo, el 391 de febrero, la Ley 7581 del 1 de septiembre tenida por ley el 23: bien dichos), P170 (remisiones) y P195 (primacías relativas: «el siguiente», «después de», «recién», «hasta» en las 104 líneas, sin caídas) se corrieron en la sesión, a mano o por script, y no dieron otras caídas.

**Descartados (falsos positivos, 10).** «El único acto ... como una unidad de planificación propia es el convenio del Corredor Intermunicipal de 2009» (19:484) contra la macro-cuenca del Decreto 2785 y la Región Metropolitana de la Ley 7322: la primera es de planificación ambiental y la segunda, de transporte, y las dos agrupan a otros municipios; «propia» las deja afuera. «El acto de mayor monto entre los del departamento hallados en 2007» (22:545): universo de las 50 fichas del informe; la cisterna de Vaqueros, del B.2, es de \$1.547.149,05. «Una mayor que las dos» (19:203): 49,36 ha contra 42,06 y 32,5. «La Provincia las vendió a \$18.000 la hectárea» (17-tierrafiscal:401): 108.000 / 6, condicionado («si esas seis hectáreas son las que se vendieron»). «Menos de un tercio de eso» (17-aguabaja:325): 0,165 < 0,175. «En 2014 y 2015 es su cuarta aparición» (19:926): la ventana va dicha, y 2007 y 2008 se dan después. «Tres caen sobre los tramos de aquellos convenios» (09:723): Cabral en 2007 y en 2008 y Urquiza--Chaile en 2008. «Juntos no llegan al uno por ciento» (15:185): 0,37 + 0,41 = 0,78. «El llamado ... se publica en mayo, después de dictados la adjudicación y el contrato» (A:501): la adjudicación se publica el 28 de mayo, cinco días después del llamado, pero se dictó en febrero; «dictados» es exacto. La remisión de 01:157 que el script marca (siete capítulos posteriores en una sola enumeración, con «más adelante» al final, a más de 140 caracteres del primero): está marcada.

**Pendientes que cierra.** Ninguno.

**Pendientes nuevos.** P202 (herramientas): tres controles para AMPLÍA (extensión de P181 y P195). (1) **La lista de C:4 se rehace entera en cada AMPLÍA**: cada norma de «no se citan en ningún capítulo» se busca por script en `cap/*.tex`, y la lista y sus cifras se corrigen aunque el AMPLÍA no la haya tocado (caso: Ley 4708, citada en 21-ausencias:182 desde el AMPLÍA 1973-1974, ronda 73). (2) **Recuentos de clases en las frases de síntesis** («dan el origen de N filas», «renuevan N», «traen N»): el script cuenta las fichas del informe que caen en cada clase, incluidas las que el capítulo trata en otro párrafo (caso: 19:187 y La Mesa Redonda de 2009, ronda 73). (3) **El control (1) de P181 sigue sin correr**: las firmas de interinos que una fila da por mes se cotejan con la lista de ediciones del E.4 del informe (caso: A:499, «en febrero», ronda 73; el mismo de la ronda 69). Y una regla de lectura para P196: la serie de la cuarta tesis no cuenta la adjudicación como acto de cierre (01:139, ronda 73), y anota a la vista los casos que van contra la tesis, como la obra de agua de 2007.

**Pendientes revisados sin cerrar.** P196 (la medida cambia con el hallazgo 1; la serie sigue sin armar). P197 (láminas de 2007 a 2009: sin cambio). P198 y P199 (H, E y opacidad de 2007 a 2009: sin cambio). P200 (Res.\ 25.810 o 25.819: la imagen de la 18255 no se miró en esta ronda). P201 (nivel de 2008: sin cambio). P181 (su control 1 falló otra vez: hallazgo 3). P186 y P195 (sus controles se corrieron a mano: la propagación del CONTRADICE de la matrícula 3.337 está completa en 14:847, 17-tierrafiscal:401 y 434 y D:256). P193 (las citas que el AMPLÍA pidió cotejar quedan cotejadas en la imagen). P102 y P164 (sin caídas). P115, P40 y P12.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.381/25.419 líneas vigentes en `573f289` y las 38 sin auditar de la ronda 72 | 25.336 vigentes; 45 caducas por el AMPLÍA 2007-2009 y 2 de las 38 reemplazadas por él |
| Superlativos, cierres y ausencias en las 104 líneas (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *mayor*, *más alta*, *recién*, *el siguiente*), sin *primera mitad*, *primer semestre* ni *mayor parte* | 92 coincidencias, todas leídas | Ninguna cae: las ausencias llevan su universo («en lo leído de los tres años», «en lo hallado», «leídos con pendientes»); los superlativos de 19:203, 19:484 y 22:545, en los descartados |
| Repaso de ventana: oraciones fuera de las líneas del AMPLÍA con un rango de años que cubre 2007-2009 y *no*, *ningún*, *único*, *primer*, *sólo*, *recién*, *hasta*, *desde*, *todavía*, *tampoco*, *falta*, *se pide* | libro entero (base `82b47fb`), 10 coincidencias, todas leídas | Ninguna cae por lo de 2007 a 2009: D:160 (actas de proclamación hasta 2007), D:260 (emergencias de 1980 a 2018: precisión c), 01:159, 05:164, 174 y 384, 11:620, 18-trabajo:42, 19:885 y 21-conclusion:106 |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, y 60 antes; orden de `\input` de `main.tex`; sólo de `cap/` a `cap/`) | 377/377 `\ref{cap:…}` antes de la fase 6; 379/379 después | 1 marcada por la ventana del script, la misma antes y después (01:157, enumeración de siete capítulos con «más adelante» al final): 0 sin marcar |
| Normas de C:4 citadas en algún capítulo | 13 normas antes de la fase 6; 12 después; 26 archivos de `cap/` | Antes: 1 (Ley 4708, 21-ausencias:182: hallazgo 4). Después: 0 |
| `\pendiente{}`, ítems de D | 52; 285 | 22-prospectiva dice «doscientos ochenta y cinco pedidos»: cierra, antes y después de la fase 6 (las precisiones b y c amplían ítems existentes) |
| Aritmética de 2007 a 2009 | 10 cuentas | 108.000 / 6 = 18.000; 7,875 / 15 = 0,525; 0,525 / 3 = 0,175 > 0,165; 3.453.835,37 / 3.800.000 = 90,9 %; 1.547.149,05 / 1.300.000 = 1,190; 0,37 + 0,41 = 0,78; 47,66 / 86,51 > la mitad; 79 − 42 = 37 tramos fuera de las ventanas (00:45, F:26) y 1 + 31 + 2 + 3 = 37; de 2001 a 2015, catorce años; 25.336 + 104 = 25.440. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 73 | 50 de 346 oraciones con cifra en las 104 líneas | **50/50 con fuente localizable**: 33 con la cita en la oración (por script); las otras 17 son declaraciones de cobertura de 00, 02, 20 y F, que remiten al apéndice F y a los informes, y oraciones de síntesis seguidas de su cita o de su ficha (19:187, 19:201, 19:203, 22:545, 15:474, 17-tierrafiscal:434). 100 % → 90 por el criterio; el aspecto queda en 82 por la escala general (P115) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 104 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 104 líneas, cruzadas con contextos sensibles (P102: *remate*, *quiebra*, *concurso*, *deudor*, *sentencia*, *cesante*, *renuncia*, *D.N.I.*) | 104/104 líneas | 0 caídas. Sin nombre: el heredero de Manuel Serrey, los adjudicatarios y desadjudicados de El Jardín, los ejecutados de los remates de 2008 y 2009, los condenados, el concursado, los agentes del hospital. Nombrados: autoridades (Calabró, Lapad por su cargo), concesionarios de canteras que el cuadro de 2021 ya nombra o que firman un pedido público (Héctor Enrique Medina, César Domingo Dal Borgo, Alejandrina Morales, Juan Domingo Lozano por la cooperativa), Elena Serrey de González Bonorino como demandada de 1987 |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `82b47fb` y fase 6 aplicada con `git am` en un clon limpio de GitHub | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló, y sin `.aux` previos, tres pasadas de `pdflatex`); 983 páginas las dos; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2007 a 2009 van en pasado; la Ley 7322 se cita como lo que establece la región |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 3 (−5); aplicado. Fechas de acto y de publicación distinguidas (P164) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 12 citas cotejadas, ninguna con diferencias; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Las ausencias de 2007 a 2009 llevan su universo y ninguna se afirma sobre años en barrido; superlativos con universo declarado |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales (La Generosa, La Mesa Redonda, «9:05», «Adela Corina», «Clarisa» y «María del Carmen», Da Souza) están señaladas |
| 7 | Consistencia interna | 9 | 30 | 100 | Hallazgos 1 y 2: 4,08 por cada 100 de las 49,0 páginas (40), uno sostiene una tesis (tope 50) y los dos contradicen material cercano (un escalón más); aplicados |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 4 (−5); aplicado. 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (abajo); la cuarta tesis tiene ahora una medida coherente con su evidencia y declara el dato que más se le opone |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; las láminas que piden extensión, en P197 |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 104 líneas; 90 como en la ronda 71 |

**Nota inicial: 81,3 antes del tope y 81,3 después** (tope de 90 por la cobertura acumulada inicial del 99,6 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas ---el escrutinio de 1987, la resolución judicial de la tierra del embalse, la sentencia del juicio de la matrícula 1.303 o, para la cuarta, los certificados finales de las defensas de 1967 a 1977---: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9 (el 1, de 82 a 90); (4) dejar corriendo los controles de P181, P195 y P202 como paso automático del AMPLÍA, que habrían atrapado tres de los cuatro hallazgos de esta ronda: protege el 3, el 7 y el 8 en la nota inicial de la ronda siguiente (aquí, 7,0 puntos de la inicial); (5) hacer las láminas de P197 y las entradas de P198: hasta +0,2 en el 13 y el 15.

**Avance del libro:** 4 de 4 hallazgos resueltos (100 %) y cuatro precisiones aplicadas; compila sin errores ni referencias indefinidas, 983 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la cuarta tesis (en 2007 y 2008 las expropiaciones para vivienda de 1985 y 1986 siguen sin cierre: la de La Caldera en juicio, la de Vaqueros sin escritura; los encauzamientos de 2007 y 2008 vuelven a los tramos de 1985 a 1987; y en contra, a la vista, la obra de agua del pueblo de 2007, adjudicada en dos meses y sin cierre conocido) y la tercera (2007 a 2009 tampoco traen un acto que devuelva al municipio competencia sobre el agua o el suelo).

**Calidad de la auditoría.** Cobertura de la ronda: 104 líneas (0,41 %; 49,0 páginas). Cobertura acumulada: 25.440 de 25.440 (100,0 %), con el registro de arriba. Falsos positivos descartados: 10. Recortes: 63 de las 75 citas nuevas quedan cotejadas sólo contra el TEXTO de los informes; una de las 18 ediciones bajadas no se cotejó renglón por renglón; del B.2 de 2008 y 2009 se leyeron los renglones que el libro cita, no el apartado entero; los controles de P164, P170, P186 y P195 se corrieron en la sesión, no como paso automático; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: **4 de 4**, uno en la incorporación de la ronda 72 (`573f289`), dos en el AMPLÍA 2007-2009 (`82b47fb`) y uno en el AMPLÍA 1973-1974 (`d99ba07`), arrastrado por el de 2007-2009; **0 atrapados por un control automático**.

## Ronda 74 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2010-2012. Base: commit `a8e72e9` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2010-2012, sobre `e2c9ae2`, la ronda 73), con la fase 6 en `ronda-74.patch` (un commit, `0dbe681`, árbol `40bf20d`; aplica con `git apply --check` sobre `a8e72e9` en un clon limpio de GitHub). La sesión que hace esta ronda es la misma que escribió el AMPLÍA: se audita trabajo propio, y por eso cada cita nueva se volvió a mirar en la imagen y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 73 (25.440 de 25.440, sobre `e2c9ae2`) se trasladaron por diff a `a8e72e9`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2010-2012 caduca 36 líneas y deja 48 nuevas o modificadas** (12 netas: 6 en A, 3 en C, 2 en F y 2 en 11, menos 1 en D), en 19 archivos. Vigentes después del traslado: 25.404 de 25.452.

### Lectura sobre el texto (numeración de `a8e72e9`)

Se leyeron **las 48 líneas, enteras, por la sesión**, sin subagentes (88.621 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-2010_18259-18499_la-caldera_LEE-2010_2026-10-07.txt`, `BO-Salta-2011_18500-18740_la-caldera_LEE-2011_2026-10-07.txt` y `BO-Salta-2012_18741-18978_la-caldera_LEE-2012_2026-10-07.txt`) y, en las citas, contra la imagen.

| Archivo | Líneas | Nuevas |
|---|---|---|
| ape/A-cronologia.tex | 4, 511, 515, 517–520, 522, 672 | 9 |
| ape/C-normativa.tex | 330–332, 352–353 | 5 |
| ape/D-pedidos.tex | 55, 176, 252 | 3 |
| ape/F-fuentes.tex | 25–26, 100–101, 103 | 5 |
| cap/00-advertencia.tex | 45 | 1 |
| cap/01-planteo.tex | 119, 157 | 2 |
| cap/02-metodo.tex | 28, 99 | 2 |
| cap/04-siglo.tex | 3659–3660 | 2 |
| cap/10-expropiacion.tex | 146 | 1 |
| cap/11-ribera.tex | 491–492, 1032, 1048, 1375, 1383, 1676 | 7 |
| cap/12-amparo.tex | 1175 | 1 |
| cap/13-loteo.tex | 694, 709 | 2 |
| cap/17-aguabaja.tex | 330 | 1 |
| cap/17-tierrafiscal.tex | 401 | 1 |
| cap/19-resistencias.tex | 187 | 1 |
| cap/20-opacidad.tex | 880–881 | 2 |
| cap/21-ausencias.tex | 76 | 1 |
| cap/22-infraestructura.tex | 545 | 1 |
| cap/22-prospectiva.tex | 290 | 1 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 11:476–503 (la sección de 2012 y 2013), 11:1026–1047 (la tabla del río Vaqueros y su cautela), 11:1365–1420 (el aviso de inicio de 2012 y su cautela), 11:1664–1677, 13:690–713, 17-aguabaja:300–345, 11:560–566 (composición de las comisiones), D:392 y 11:1112.

**Esta ronda: 48 líneas nuevas**, 88.621 bytes sobre 3.267.948, que en las 987 páginas de la base equivalen a **26,8 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.404 vigentes + 48 = **25.452 de 25.452 (100,0 %)**. La fase 6 toca once líneas: A:511, A:517, A:518, C:331, 01:157, 11:1383, 17-tierrafiscal:401 y 22:545, dentro de lo leído en esta ronda, y D:392, 11:1112 y 11:1384, que estaban vigentes y se releyeron como contexto; no cambia el largo de ningún archivo: **25.452 de 25.452 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 2010 a 2012 de `boletines-salta`)

Las ediciones de 2011 y 2012 estaban en la sesión desde sus lecturas LEE; de 2010 se bajaron siete (18327, 18339, 18370, 18433, 18437, 18458, 18488). Recortes a 200 ppp en gris con PyMuPDF; el renglón se ubicó con la capa y cada recorte se miró.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 18728 | 18 | Ley 7699, art. 1 | «con el cargo de ser destinado exclusivamente al desarrollo integral de la zona». Coincide (A:520, 12:1175, 01:157) |
| 18837 | 25 | Cateo, titulares | «1576, 1846 y 1891 de Prov. de Salta» y «Matrícula 2065 de Amigos Club de la Montaña». Coincide (A:518, A:520, A:522) |
| 18574 | 14 y 15 | Decreto 1684 | «Matrícula N° 05-2565»; «Finca Campo Arrieta – Loma Bola y Cañada Ancha», con raya. Precisión (A:518, C:331, 17-tierrafiscal:401) |
| 18370 | 15 | Decreto 2410 | «Dentritas de Manganeso – La Caldera», con raya. Precisión (A:511) |
| 18370 | 19 | Res. SOP 354 | \$586.353,44. Coincide (A:511) |
| 18763 | 19 | Res. 066 | «Proyecto de Urbanización en Lesser», matrícula 1869, Vaqueros. Coincide (13:694) |
| 18827 | 16 | Res. 290, art. 4 | «sobre el Ante Proyecto del Camino que deberá ser presentado y controlado por la Municipalidad de Vaqueros». Coincide (13:694); hallazgo 1 |
| 18846 | 34 | Res. SRH 9/12 | «la Ing. Civil Mariela Adriana Nieva y el Dr. en Geología Omar Viera», «matrículas N° 87.337 del Dpto. Capital». Coincide (11:1032, 11:1676, D:55, C:353) |
| 18970 | 25 | Res. SRH 322/12 | «M.P. N° 155 y el Topógrafo N° Félix Márquez, DNI ...». Confirma la corrección M.F. → M.P. del AMPLÍA (P205); hallazgo 3 |
| 18974 | 14 | La Vaquera | «ubicada en las márgenes del Río Vaqueros», sin departamento. Coincide (19:187) |
| 18559 | 23 | Concesión, catastro 3989 | «Club de Campo Las Vertientes – Ecopueblo», con raya. Precisión (A:517) |
| 18948 | 23 | Noroeste Construcciones | 19 Has. 1.593 m2, «colinda con Cantera "Los Yacones", Expte. N° 20.604/2010». Coincide (19:187) |
| 18433 | 8 | Decreto 3639, art. 2 | \$15.353,91, «Valor Fiscal incrementado en un 30%». Coincide (A:515, C:330, 10:146) |
| 18327 | 19 | Res. SOP 213 | \$677.680,71. Coincide (A:511, 22:545) |
| 18660 | 8 | Ley 7674 y Decreto 3766 | calle Antonio Magnonia al sur, Andrés Anderson al oeste, calles sin nombre al norte y al este; Decreto N° 3766. Coincide (A:519, C:332) |
| 18677 | 11 | Decreto 4137 | 4,1412 hectáreas, 2,174 lts/seg, Río Wierna, margen izquierda, permanente. Coincide (17-aguabaja:330) |
| 18458 | 14 | Decreto 4393 | «La Caldera: Un (1) diputado titular y uno (1) suplente». Coincide (A:511) |
| 18884 | 21 | Tierra Gaucha | «Superficie registrada total 22 Has. 9.330 m2», fiscal. Coincide (19:187, F:100) |
| 18507 | 11 | Res. SOP 890 | \$597.346,30. Coincide (A:517) |
| 18339 | 14 | Decreto 1614 | «Ing. Miguel Angel Aleman», Vaqueros, sin tilde. Coincide (A:511, F:100, D:176) |

Son **10 de las 21 cadenas entre comillas del texto nuevo cotejadas en la imagen**; las otras once son nombres de canteras, minas, obras y asociaciones (diez) y «Campo Arrieta», cotejados contra el TEXTO de las fichas. Tres llevan raya en el original y guion en el libro: se corrigen como precisión tipográfica, sin restar.

### Hallazgos (tres, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 01:157 | El refutador de la tercera tesis dice que de 2010 a 2012 «tampoco» aparece un acto que devuelva al municipio competencia efectiva sobre el agua o el suelo, y enumera sólo actos de la Provincia. El mismo AMPLÍA trae en el capítulo de loteos (13:694) la Res. 290/12, cuyo art. 4 deja «presentado y controlado por la Municipalidad de Vaqueros» el anteproyecto del camino de la urbanización de Lesser (Nº 18827, h. 16, imagen). El párrafo de 2007 a 2009 da siempre «lo más parecido a una competencia suya»; el de 2010 a 2012 lo omitía, y era justo el dato que más se acerca a refutar | 7 | Se agrega «lo más parecido a una competencia suya sobre el suelo es que el certificado de aptitud ambiental de una urbanización de Lesser deja a cargo de la Municipalidad de Vaqueros el control del anteproyecto de su camino», con la remisión al capítulo de loteos |
| 2 | D:392 | El pedido de las resoluciones de otorgamiento o rechazo de las concesiones de agua de 2004 a 2025 seguía incluyendo la de la matrícula 388 (expediente 34-2.253/56), que el AMPLÍA incorpora otorgada por el Decreto 4137 de 2011 (17-aguabaja:330) y cuyo pedido propio retiró de D | 8 | Se agrega que esa ya no se pide |
| 3 | 11:1383–1384 | La ficha de la Res. 322/12 transcribe «M.P.\ Nº 155, y el Topógrafo N.\ Félix Márquez. Estableciéndose»: la imagen dice «M.P. N° 155 y el Topógrafo N° Félix Márquez, DNI ... Estableciéndose». Dos correcciones silenciosas (la coma y «N.») y una omisión sin marca | 4 | «M.P.\ Nº 155 y el Topógrafo Nº Félix Márquez [\ldots]. Estableciéndose» |

**Precisiones aplicadas sin restar.** (a) A:511, A:517, A:518, C:331 y 17-tierrafiscal:401: raya del original en «Dentritas de Manganeso -- La Caldera», «Club de Campo Las Vertientes -- Ecopueblo» y «Finca Campo Arrieta -- Loma Bola y Cañada Ancha». (b) 11:1112: «cuyo propietario fue advertido» pasa a «cuyos propietarios fueron advertidos»: las resoluciones 91/12 y 92/12, que el AMPLÍA incorpora, advierten a otros tres propietarios de la misma matrícula 4027. (c) 17-tierrafiscal:401: «Otra fracción junto al dique había salido antes por ley» decía más que el acto, que recuerda una autorización de venta y no la venta: «Antes aún, una ley había autorizado a vender otra fracción junto al dique». (d) 22:545: las obras de agua de Vaqueros de 2011 y 2012 «las contrata la Provincia» decía más que la Res. SOP 523, que aprueba un legajo: «son de la Provincia, que aprueba el legajo del primero y adjudica los segundos».

Resta: un error de consistencia en 26,8 páginas, 3,7 por cada 100: **50** por el escalón; no contradice material a menos de diez páginas (el capítulo de loteos está a más de seiscientas). Un pedido satisfecho en parte que seguía en la lista, en el aspecto 8: **resta 5** (90). Dos correcciones silenciosas en una cita, en el aspecto 4: **resta 6**, que el techo de 90 por cotejo parcial absorbe.

**Errores introducidos por la propia auditoría**: los tres. El 1 y el 2, en el AMPLÍA 2010-2012 (`a8e72e9`), escrito por esta misma sesión. El 3, en la incorporación de la ficha de la Res. 322/12, anterior a la ventana del clon (presente en `8182f9d`, AMPLÍA 1953); el AMPLÍA 2010-2012 corrigió en el mismo renglón la matrícula del geólogo y no cotejó el resto. **Ninguno lo atrapó un control automático**.

**Descartados (falsos positivos, 6).** «Entre todas las comisiones que este capítulo leyó después, de 2011 a 2019, sólo una ---la del río Vaqueros de 2016--- incluye un ingeniero hidráulico» (11:565): las comisiones de 2011 y 2012 de los informes LEE no traen ninguno (búsqueda de «hidráulic» en los dos informes: 0). «En ninguna de las ocho comisiones cuya integración consta aparece un agrimensor» (11:564): la 322/12 trae un topógrafo, no un agrimensor. «La primera es la que más pesa. En mayo de 2012 la Secretaría ... advirtió por escrito al propietario» (11:504): sigue cierta con las 91/12 y 92/12, que advierten del mismo modo. «El de La Caldera es el más bajo» (A:522): universo declarado, los ocho municipios de la Res. 67/12. «La 94/12 no fue la única de ese día» (11:491): universo, el día y la matrícula. «En lo leído de los tres años no hay ningún plano publicado» (F:100): ausencia con su universo, sobre años en barrido, en la fórmula de 2007 a 2009.

**Pendientes que cierra.** P205: la matrícula del geólogo Olañeta es «M.P. N° 155» en la imagen (18970 h25); la corrección del AMPLÍA queda confirmada.

**Pendientes nuevos.** P206 (libro): el Decreto 1684/11 declara reserva la Fracción A-2 «Finca Campo Arrieta -- Loma Bola y Cañada Ancha», y la tabla de expropiaciones del dique (10:26–28) tiene «Fracciones de Loma Bola, Campo de Arrieta y Cañada Ancha» de los Mercado; establecer si la tierra que la Ley 6627 autorizó a vender al club sale de esas fracciones expropiadas, con la ley y el plano de desmembramiento.

**Pendientes revisados sin cerrar.** P203 (Res. 9/12: el edicto de 2012 da la matrícula 87.337 de la Capital, mirado en la imagen; la relación con la 216 sigue abierta). P204 (hojas «a ojos» de 2010 a 2012: sin cambio). P196 (la serie de la cuarta tesis: los años 2010 a 2012 suman una obra de agua del pueblo adjudicada al municipio sobre su propio legajo, sin cierre conocido). P202 (su control 1, la lista de C:4, se corrió y no hubo cambio).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.440/25.440 líneas vigentes en `e2c9ae2` | 25.404 vigentes; 36 caducas por el AMPLÍA 2010-2012 |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *mayor*, *más bajo*, *recién*, *el siguiente*, *tampoco*, *sólo*, *todavía*) | 25.494 bytes de palabras agregadas, 6 coincidencias, todas leídas, más las cuatro que el script no ve por salto de renglón (11:491, 01:157, 13:694, 13:709) | Ninguna cae; la de 01:157 es el hallazgo 1 por lo que omite, no por lo que afirma |
| Repaso de ventana: oraciones fuera de las 48 líneas con 2010, 2011 o 2012, o con un rango que los cubre, y *no*, *ningún*, *único*, *primer*, *sólo*, *recién*, *todavía*, *tampoco*, *falta*, *nunca*, *el más* | libro entero (base `a8e72e9`), 76 coincidencias, todas leídas | Ninguna cae por lo de 2010 a 2012; una precisión (11:1112) y un pedido (D:392, hallazgo 2) |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, 60 antes; orden de `\input` de `main.tex`; de `cap/` a `cap/`) | 936/936 `\ref{cap:…}` después de la fase 6 | 1 marcada por la ventana del script, la misma de la ronda 73 (01:157, enumeración con «más adelante» al final): 0 sin marcar |
| Normas de C:4 citadas en algún capítulo (P202, control 1) | 12 normas; 26 archivos de `cap/`; y las 3 normas nuevas de C | Las 12: 0 citas (dos coincidencias de «1045» son «10456», número de boletín). Las 3 nuevas (Decretos 3639/10 y 1684/11, Ley 7674) se citan en 10 y 17-tierrafiscal: la lista no cambia |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Aritmética de 2010 a 2012 | 6 cuentas | 15.353,91 / 1,30 = 11.810,70; 240.800 / 4.749.780 = 5,07 %; Tierra Gaucha, polígono de seis vértices por la fórmula del área: 18,7353 ha contra 22,9330; 82 − 42 = 40 = 1 + 31 + 2 + 6 tramos fuera de las ventanas; 39 = 31 + 1 + 1 + 6; 25.404 + 48 = 25.452. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 74 | 50 de 256 oraciones con cifra en las 48 líneas | **50/50 con fuente localizable**: 39 con la cita en la oración (por script); las otras 11 son declaraciones de cobertura de 00, 01, 02 y F, que remiten al apéndice F y a los informes, la fila de 2026 de la cronología (asterisco, capítulo del amparo), la oración de 12:1175 (fuente en el pasaje) y la fila de la tabla de 11:1032 (fuente en la misma fila) |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 48 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 48 líneas, cruzadas con contextos sensibles (P102: *remate*, *quiebra*, *concurso*, *deudor*, *sentencia*, *cesante*, *renuncia*, *D.N.I.*) | 48/48 líneas | 0 caídas. Sin nombre: las agentes del hospital que renuncian, las técnicas contratadas por Minería, las mediadoras, el contador afectado al municipio, los socios de las sociedades; el DNI del topógrafo, omitido con marca. Nombrados: funcionarios por su función, los concesionarios de la matrícula 388 y los peticionantes de canteras, por sus actos públicos |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `a8e72e9` y fase 6, cada una en un clon limpio, sin `.aux` previos | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló); 987 páginas la base y 985 la fase 6 (reacomodo de flotantes a partir del capítulo 1: la sección «Las hipótesis heredadas y su saldo» pasa de la página 10 a la 12 y el capítulo 27, de la 615 a la 613); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2010 a 2012 van en pasado o como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas de acto, de sanción, de promulgación y de publicación distinguidas (Ley 7699 y Decreto 5079; Ley 7674 y Decreto 3766); las cifras tomadas de los informes se recalcularon |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgo 3 (−6, absorbido por el techo); 10 citas nuevas cotejadas, tres con raya; techo de 90 por cotejo parcial |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Ninguna ausencia afirmada sobre 2010 a 2012, que quedan en barrido; superlativos con universo |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales (la matrícula de la Res. 9/12, Viera y Nieva, la matrícula 05-2565 contra la 2065, la 1.846 «de Prov. de Salta», la superficie de Tierra Gaucha) están señaladas |
| 7 | Consistencia interna | 9 | 50 | 100 | Hallazgo 1: 3,7 por cada 100 de las 26,8 páginas (50); aplicado |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 2 (−5); aplicado. 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado; la tercera tesis tiene a la vista, de 2010 a 2012, el dato que más se le acerca a oponerse |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas nuevas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 48 líneas; 90 como en la ronda 73 |

**Nota inicial: 83,4 antes del tope y 83,4 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) dejar corriendo como paso automático de cada AMPLÍA los controles de P181, P195 y P202, más uno nuevo: que todo refutador de tesis que el AMPLÍA extienda nombre «lo más parecido» que el mismo AMPLÍA incorpore (caso: hallazgo 1): evita los −4,5 del aspecto 7 de esta ronda en la nota inicial de la siguiente; (5) mirar las hojas «a ojos» de 2010 a 2012 (P204) para subirlos a nivel imagen: no mueve la nota, sí lo que el libro puede afirmar.

**Avance del libro:** 3 de 3 hallazgos resueltos (100 %) y cuatro precisiones aplicadas; compila sin errores ni referencias indefinidas, 985 páginas. **Avance de la investigación:** sin cambios de estado. Ganan evidencia sin cambiarlo la tercera tesis (de 2010 a 2012 el municipio aparece como ejecutor de obras de la Provincia por convenio y la competencia más cercana a una suya sobre el suelo es el control de un camino de una urbanización privada, impuesto por un certificado ambiental provincial) y la cuarta (la expropiación de vivienda de Vaqueros de 2009 avanza en 2010 al juicio y en 2011 se achica por ley, sin cierre conocido; la red de agua de Santa Mónica y el tendido eléctrico del paraje, adjudicados al municipio, no tienen cierre publicado en lo leído).

**Calidad de la auditoría.** Cobertura de la ronda: 48 líneas (0,19 %; 26,8 páginas). Cobertura acumulada: 25.452 de 25.452 (100,0 %), con el registro de arriba. Falsos positivos descartados: 6. Recortes: de las citas nuevas, once quedan cotejadas sólo contra el TEXTO de las fichas; de los actos que las filas de 2010 a 2012 citan sin comillas, se miraron en la imagen once (las cifras y los nombres de la tabla de cotejo) y los demás quedan contra el TEXTO de los informes; la muestra de trazabilidad no se rehízo; los controles de P181, P195 y P202 se corrieron en la sesión, no como paso automático. Errores introducidos por la propia auditoría: 3, dos de ellos en el AMPLÍA que la misma sesión escribió; atrapados por un control automático: 0.

## Ronda 75 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2013-2015. Base: commit `23a7ab4` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2013-2015, sobre `429f17a`, la ronda 74; registrado por `3-registrar` a las 03:04 del 07/10, con el mismo árbol, `51ed4d2`, que el parche entregado), con la fase 6 en `ronda-75.patch` (un commit, `dca23b8`, árbol `2c36c2b`; aplica con `git am` sobre `23a7ab4` en un clon limpio de GitHub y deja el mismo árbol). La sesión que hace esta ronda es la misma que escribió el AMPLÍA: se audita trabajo propio, y por eso cada cita nueva se volvió a mirar en la imagen y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 74 (25.452 de 25.452, sobre `429f17a`) se trasladaron por diff a `23a7ab4`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2013-2015 caduca 69 líneas y deja 89 nuevas o modificadas** (20 netas: 9 en A, 3 en C, 2 en F y 6 en 11), en 18 archivos. Vigentes después del traslado: 25.383 de 25.472.

### Lectura sobre el texto (numeración de `23a7ab4`)

Se leyeron **las 89 líneas, enteras, por la sesión**, sin subagentes (82.901 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-2013_18979-19216_la-caldera_LEE-2013_2026-10-07.txt`, `BO-Salta-2014_19217-19453_la-caldera_LEE-2014_2026-10-07.txt` y `BO-Salta-2015_19454-19690_la-caldera_LEE-2015_2026-10-07.txt`), contra el bloque de la ronda 74 de este registro y, en las citas, contra la imagen.

| Archivo | Líneas | Nuevas |
|---|---|---|
| ape/A-cronologia.tex | 4, 526, 530–532, 535, 538, 553, 558, 560 | 10 |
| ape/C-normativa.tex | 351, 353–354, 363 | 4 |
| ape/D-pedidos.tex | 71, 73, 176 | 3 |
| ape/F-fuentes.tex | 25–26, 102–103, 105 | 5 |
| ape/G-propuestas.tex | 278 | 1 |
| cap/00-advertencia.tex | 45 | 1 |
| cap/01-planteo.tex | 85 | 1 |
| cap/02-metodo.tex | 28, 99 | 2 |
| cap/04-siglo.tex | 1764 | 1 |
| cap/10-expropiacion.tex | 313–314 | 2 |
| cap/11-ribera.tex | 312, 348, 386–387, 511, 513, 515–517, 529, 532–533, 550, 556, 571, 573, 584, 594–595, 614, 618, 620, 624, 628, 630, 634, 669, 681, 719, 793, 1028, 1233, 1507, 1519, 1619, 1722 | 36 |
| cap/15-hacienda.tex | 470, 486 | 2 |
| cap/17-aguabaja.tex | 8 | 1 |
| cap/19-resistencias.tex | 87, 203, 422, 455, 924 | 5 |
| cap/20-opacidad.tex | 116, 806, 989, 995, 1016 | 5 |
| cap/21-ausencias.tex | 76 | 1 |
| cap/22-infraestructura.tex | 46–47, 426, 545 | 4 |
| cap/23-plan.tex | 43, 110–111, 216, 261 | 5 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 11:370–400 (la cautela del procedimiento: hallazgo 1), 11:476–510 (la sección de 2012 y 2013), 11:520–640 (la serie y sus dos tablas), 11:700–725, 11:1440–1530 (la secuencia del Guaranguay en la matrícula 4082), 19:180–212 y 19:905–930 (canteras), 20:985–996, 15:460–490 y 21:70–80.

**Esta ronda: 89 líneas nuevas**, 82.901 bytes sobre 3.287.179, que en las 995 páginas de la base equivalen a **25,1 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.383 vigentes + 89 = **25.472 de 25.472 (100,0 %)**. La fase 6 toca cinco líneas: A:560, F:105, 00:45 y 11:382–383; las cuatro primeras están dentro de lo leído en esta ronda, y 11:382–383 estaba vigente y se releyó como contexto; no cambia el largo de ningún archivo: **25.472 de 25.472 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (Releases 2013 a 2015 de `boletines-salta`)

Se bajaron de los Releases quince ediciones (18980, 19027, 19041, 19085, 19101, 19129, 19173, 19198, 19232, 19360, 19457, 19532, 19573, 19574, 19596), y antes, durante el AMPLÍA, otras seis (19299, 19394, 19607, 19613, 19644, 19651). Recortes a 170–220 ppp con pdfplumber; el renglón se ubicó con la capa y cada recorte se miró.

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 19173 | 20 | Res. SOP 878 | «Red de Agua para Loteos en la Caldera - Dpto. La Caldera». Coincide (A:530, C:351, 22:545) |
| 18980 | 23 | Decreto municipal de Vaqueros | «notable crecimiento poblacional». Coincide (A:526) |
| 19101 | 18 | Decreto 1990 | «Mil200 1era Edición de Carrera Pedestre La Caldera Trail». Coincide (A:526) |
| 19027 | 22 | Res. SRH 51/13 | «Catastro N° S/N°, Sección B, de la localidad de Vaqueros». Coincide (11:511) |
| 19041 | 23 | Res. SRH 60 | «por Resolución N° 60 del día 15/03/12». Coincide (11:511) |
| 19574 | 21 | Res. SRH 199/15 | «Ing. Civil Marcelo R. Toigo y Lic. en Geologia Enrique Salvador Chalabe», «Catastro N° 2020, Finca Wiera, Localidad de La Caldera», «matemático y fotográfico». Coincide (11:550) |
| 19198 | 24 | Res. SRH 336/13 | «(Dcto. N° 1898/...». Coincide (11:533) |
| 19232 | 26 | Res. SRH 395/13 | «Catastro N° 1366, Finca La Caldera o Getsemaní». Coincide (F:105) |
| 19457 | 16 | Res. 771D | «Escuela N° 4274 "Monseñor Pedro Reginaldo Lira" de la localidad La Calderilla». Coincide (21:76) |
| 19360 | 20 | LP 23/14 | «Jardín Maternal N° 2525 - Dr. Luis Linares», Localidad La Caldera. Coincide (21:76, A:535) |
| 19129 | 26 | Archivo de expedientes mineros | «21.189 Doña Rufina Plomo - plata.- La Caldera». Coincide (A:526) |
| 19085 | 29 | Mina | «Chañy I». Coincide (A:526) |
| 19532 | 17 | Aguas del Norte, LP 29/2015 | «Planta Depuradora Cloacal - Vaqueros». Coincide (A:560; hallazgo 3) |
| 19596 | 6 | Ley 7881 | «Matrícula N° 899, de la localidad La Caldera», «destinado exclusivamente a la radicación de un». Coincide (A:560) |
| 19573 | 11 | Decreto 2226 | «se trasladará, simbólicamente y por ese único día, la Capital de la Provincia de Salta». Coincide (A:560) |

Son **15 de las 26 cadenas entre comillas del texto nuevo cotejadas en la imagen**; las otras once son nombres de canteras, sociedades, loteos y fincas, cotejados contra el TEXTO de las fichas. Además, durante el AMPLÍA se miraron en la imagen la superficie y la condición fiscal de Terranostra, Los Yacones y Don Roque I (19607 h22, 19644 h27 y h28), el nombre de la geóloga de la Res. 96/14 («Marcia», 19299 h23, como el libro y no «Maida», como el informe) y el capital de Jardín Celestial (19394 h37: el aumento es de \$365.000 y el capital queda en \$545.000, como el libro).

### Hallazgos (tres, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 11:382–383 | La cautela del procedimiento dice que el libro no puede afirmar que «las tres resoluciones que remitieron sus coordenadas a la sede» incumplieran el decreto; dos renglones después (11:386–387) el mismo AMPLÍA lleva a cinco las determinaciones de la serie que no publicaron sus coordenadas (347/13, 336/13, 142/14, 383/14 y 467/15). El AMPLÍA corrigió el recuento y no la frase que lo anuncia | 7 | «las cinco determinaciones de la serie que no publicaron sus coordenadas», sin cambiar el largo |
| 2 | F:105 | Entre las contradicciones del original de 2013 a 2015, el apéndice F dice que el expediente 20.604 de la cantera Los Yacones «es de INCOVI en 2015 y de Noroeste Construcciones en 2012». Es la lectura del informe LEE de 2015 (A.55, E.9), importada sin comprobar: el edicto de 2012 (18948 h23, mirado en la ronda 74) dice que la cantera de Noroeste «colinda con Cantera "Los Yacones", Expte. N° 20.604/2010», y el capítulo de canteras (19:187) ya la daba como «lindera de otra llamada «Los Yacones»». No hay contradicción en el original | 3 | Se reemplaza por una contradicción que sí está en el original y en la tabla del capítulo 11: el expediente de la comisión del río Vaqueros de la Res. 198/15 termina en «/15» en su aviso y en «/14» en el de su determinación |
| 3 | A:560 | La fila de 2015 de la cronología dice que Aguas del Norte «licita las cloacas de Vaqueros» y no cita la edición de la licitación (Nº 19532, h. 17): las dos que cita son las de las máquinas sobre el río | 1 | Se agrega «Nº 19532, h.\ 17» |

**Precisión aplicada sin restar.** 00:45: la frase nueva de 2013 a 2015 terminaba en «leídas por la capa» y no decía la consecuencia que las frases de los tramos anteriores dicen; se agrega «también de ellos cuentan los hallazgos y no las ausencias».

Resta: un error de consistencia en 25,1 páginas, 4,0 por cada 100: **50** por el escalón, y **40** porque contradice material a menos de diez páginas (dos renglones). Un dato importado de un informe sin comprobar, en el aspecto 3: **resta 5** (95). Una fuente sin edición, en el aspecto 1: no mueve la nota, que está en 82 por P115.

**Errores introducidos por la propia auditoría**: los tres, en el AMPLÍA 2013-2015 (`23a7ab4`), escrito por esta misma sesión. El 2 lo vio la misma sesión al releer el bloque de la ronda 74 de este registro, después de entregar el AMPLÍA y antes de que se registrara; no se tocó la entrega para no cruzarse con `3-registrar` y se corrige aquí. **Ninguno lo atrapó un control automático**.

**Descartados (falsos positivos, 5).** «por primera vez desde 2006» (F:105): universo declarado, y el informe de 2015 lo da contra 2007 a 2014. «La 383/14 no fue la única de la serie sin coordenadas publicadas» (11:618): sigue cierta y ahora dice cuáles. «Entre todas las comisiones ... sólo una ---la del río Vaqueros de 2016--- incluye un ingeniero hidráulico» (11:571): la de 2013 trae un ingeniero en recursos hídricos, y la frase ya lo dice. «La más grande de las siete es la que tiene el informe de impacto expresamente no aprobado» (19:203): La Mesa Redonda, 32,5 ha, contra 21,6 de Los Yacones, la mayor de las seis restantes. «Ninguna publica las coordenadas» (A:531): las dos resoluciones de la fila, por sus avisos (19196 h19, 19198 h24).

**Pendientes que cierra.** P209: su supuesto es el hallazgo 2; la cantera de Noroeste de 2012 colinda con la de INCOVI y no comparten expediente (18948 h23, ronda 74).

**Pendientes revisados sin cerrar.** P207 (lámina de ribera: la 46/13 y la 105/13 siguen sin dibujar; el libro lo declara en 11:719). P208 (matrículas 3841 y 1499: la capa catastral del capítulo 11 da la 1499 como rural, finca San Jorge, en 2026, lo que no dice si estaba en loteo en 2013). P210 (los dos errores del informe LEE 2014, confirmados en la imagen; el libro no los tenía). P39: su ítem «11:1497 (rectificación de marzo de 2013)» queda resuelto por el AMPLÍA (Res. SRH 46/13, Nº 19026, h. 20, y Nº 19027, h. 29, en 11:1507); los demás ítems siguen abiertos. P196 (la serie de la cuarta tesis: los años 2013 a 2015 suman una red de agua «para Loteos» hecha por la Provincia y adjudicada a una empresa, y la protección de la captación del acueducto que abastece a la capital, adjudicada en cuatro meses).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.452/25.452 líneas vigentes en `429f17a` | 25.383 vigentes; 69 caducas por el AMPLÍA 2013-2015 |
| Filas de las dos tablas de la serie (11) | 30 filas de la primera; 14 de la segunda | 13 comisiones y 17 determinaciones con la 023/14; 13 determinaciones y una rectificación, 9 con «Publicadas»: cierran con 11:515, 11:584 y 11:594 |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *no consta*, *mayor*, *recién*, *tampoco*, *sólo*, *todavía*) | 20.669 bytes de palabras agregadas, 16 coincidencias, todas leídas, más las cinco que el script no ve porque la palabra ya estaba en el renglón (11:571, 11:573, 11:618, 15:486 y 19:203) | Ninguna cae: las cinco descartadas de arriba, «ningún plano publicado ... ningún balance municipal» de F:105 con su universo, como en 2010 a 2012, y las demás sin universo en juego («su primera edición», «por ese único día», «la primera ... la segunda») |
| Repaso de ventana: frases con 2013, 2014 o 2015, o con un rango que los cubre, y una forma de ausencia o superlativo, fuera del capítulo 11 | libro entero (base `429f17a`), 25 frases, todas leídas | Las que caían las corrigió el AMPLÍA; ninguna nueva |
| Remisiones a capítulos posteriores sin «más adelante» (140 caracteres después del `\ref`, 60 antes; orden de `\input` de `main.tex`; de `cap/` a `cap/`) | 937/937 `\ref{cap:…}` después de la fase 6 | 1 marcada por la ventana del script, la misma de las rondas 73 y 74 (01:157): 0 sin marcar |
| Normas de C:4 citadas en algún capítulo (P202, control 1) | 12 normas; 26 archivos de `cap/`; y las 3 filas nuevas de C | Las 12: 0 citas. Las 3 nuevas se citan en 11 y 22: la lista no cambia |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra, antes y después de la fase 6 |
| Aritmética de 2013 a 2015 | 7 cuentas | 1.946.089,99 / 2.240.271,97 = 0,8687 (13,13 %); 10 + 9,0347 + 21,6375 + 10,8772 + 6,1060 + 10,6630 + 32,5 = 100,8 ha; 104,2382 + 18,1116 + 2,4217 + 18,0351 = 142,8066 ha (Las Vertientes); 14 + 13 + 10 = 37 actos publicados de 2013 a 2015 con el departamento, sin la 023/14 = 9 anteriores a la serie + 26 de la serie + 2 rectificaciones; 42 + 1 + 42 = 85 tramos; 25.383 + 89 = 25.472; 562 hojas de la 19321 a la 19335. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 75 | 50 de 267 oraciones con cifra en las 89 líneas | **50/50 con fuente localizable**: 35 con la cita en la oración o en la fila (por script); las otras 15 son recuentos de la serie con la fuente en las tablas del mismo capítulo, declaraciones de cobertura que remiten a F y a los informes, y oraciones anteriores al AMPLÍA dentro de renglones modificados, con la fuente en el pasaje. El hallazgo 3, fuera de la muestra, salió de la lectura |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 89 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 89 líneas, cruzadas con contextos sensibles (P102: *remate*, *quiebra*, *concurso*, *deudor*, *sentencia*, *cesante*, *renuncia*, *D.N.I.*) | 89/89 líneas | 0 caídas. Sin nombre: el copropietario de la matrícula 3721, los jubilados de las escuelas y del hospital, las partes de los remates, los socios de las sociedades. Nombrados: funcionarios y técnicos por su función en actos públicos, el intendente, y los peticionantes de canteras por sus actos públicos |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `23a7ab4` y fase 6, cada una en un árbol limpio, sin `.aux` previos | Compilan las dos (con `texlive-lang-spanish`, que la sesión instaló); 995 páginas cada una (985 antes del AMPLÍA); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115; hallazgo 3 aplicado |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2013 a 2015 van en pasado o como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 2 (−5), aplicado; las demás cifras de los informes se recalcularon |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 15 citas nuevas cotejadas, sin diferencias; techo de 90 por cotejo parcial |
| 5 | Honestidad epistémica | 12 | 100 | 100 | Ninguna ausencia afirmada sobre 2013 a 2015, que quedan en barrido; los superlativos que la ventana desmentía los corrigió el AMPLÍA |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales (1366 y 4366, los vértices de 6/14 y 7/14, el balance de Las Vertientes) están señaladas |
| 7 | Consistencia interna | 9 | 40 | 100 | Hallazgo 1: 4,0 por cada 100 de las 25,1 páginas (50), y un escalón más por estar a dos renglones (40); aplicado |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin pedidos satisfechos en la lista; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado; la segunda tesis pierde parte de su indicio (ver avance) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series y cruces reproducibles |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; el libro declara las dos resoluciones con coordenadas que la lámina no dibuja (P207) |
| 14 | Utilidad pública | 4 | 100 | 100 | La propuesta de 23:43 se actualizó con la serie |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 89 líneas; 90 como en la ronda 74 |

**Nota inicial: 82,6 antes del tope y 82,6 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11, que no pasan de 90 mientras el cotejo y las muestras sean parciales) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6 (del 30 al 90 en el 9); (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; P208 decide si la segunda conserva el indicio que el AMPLÍA le recortó; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) un control de recuentos encadenados como paso automático de cada AMPLÍA: cuando cambia el número de una serie («veinticinco actos», «trece determinaciones», «seis concesiones»), buscar todas sus menciones y las frases que anuncian el número ---el hallazgo 1 es eso---: evita los −5,4 del aspecto 7 en la nota inicial; (5) dibujar en la lámina de ribera las coordenadas de las Res. 46/13 y 105/13 (P207): no mueve la nota, completa la serie que el libro reconstruye.

**Avance del libro:** 3 de 3 hallazgos resueltos (100 %) y una precisión aplicada; compila sin errores ni referencias indefinidas, 995 páginas. **Avance de la investigación:** sin cambios de estado. La **segunda tesis** (la opacidad de criterio) pierde parte de un indicio y gana amplitud: las determinaciones sin coordenadas publicadas de noviembre de 2013 a diciembre de 2014 son cuatro de trece y no dos de once, y sólo dos recaen sobre suelo que el libro sabe en loteo, de modo que la coincidencia entre omisión y loteo se debilita (P208); a la vez, la omisión aparece un año antes de El Durazno, con la misma fórmula. La **cuarta tesis** (la desidia es selectiva) gana evidencia sin cambiar de estado: en 2013 la Provincia aprueba y adjudica en dos meses una red de agua «para Loteos en la Caldera» y la protección de la captación del acueducto que lleva el agua del río a la capital, mientras las determinaciones sobre el suelo de quienes viven en el departamento siguen sin coordenadas publicadas. La **tercera** (la pérdida de competencia municipal) gana un recuento: treinta y siete actos de línea de ribera publicados de 2013 a 2015, ninguno con intervención municipal salvo la 023/14.

**Calidad de la auditoría.** Cobertura de la ronda: 89 líneas (0,35 %; 25,1 páginas). Cobertura acumulada: 25.472 de 25.472 (100,0 %), con el registro de arriba. Falsos positivos descartados: 5. Recortes: de las citas nuevas, once quedan cotejadas sólo contra el TEXTO de las fichas; de los actos que las filas de 2013 a 2015 citan sin comillas, se miraron en la imagen los de la tabla de cotejo y los seis del AMPLÍA, y los demás quedan contra el TEXTO de los informes; la muestra de trazabilidad no se rehízo; los controles de P181, P195 y P202 se corrieron en la sesión, no como paso automático. Errores introducidos por la propia auditoría: 3, los tres en el AMPLÍA que la misma sesión escribió; atrapados por un control automático: 0.

## Ronda 76 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2016-2018. Base: commit `bab001f` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2016-2018, sobre `4cc3e36`, la ronda 75; registrado por `3-registrar` a las 05:04 del 07/10, con el mismo árbol, `6f94cb8`, que el parche entregado), con la fase 6 en `ronda-76.patch` (un commit, `2d06895`, árbol `2d17ce7`; aplica con `git am` sobre `bab001f` en un clon limpio de GitHub y deja el mismo árbol). La sesión que hace esta ronda es la misma que escribió el AMPLÍA: se audita trabajo propio, y por eso cada cita nueva se volvió a buscar en el PDF de la edición y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 75 (25.472 de 25.472, sobre `4cc3e36`) se trasladaron por diff a `bab001f`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2016-2018 caduca 27 líneas y deja 44 nuevas o modificadas** (17 netas: 2 en A, 2 en F, 3 en 11 y 10 en 15), en 13 archivos. Vigentes después del traslado: 25.445 de 25.489.

### Lectura sobre el texto (numeración de `bab001f`)

Se leyeron **las 44 líneas, enteras, por la sesión**, sin subagentes (56.453 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-2016_19691-19931_la-caldera_LEE-2016_2026-10-07.txt`, `BO-Salta-2017_19932-20173_la-caldera_LEE-2017_2026-10-07.txt` y `BO-Salta-2018_20174-20413_la-caldera_LEE-2018_2026-10-07.txt`), contra la capa de las ediciones (`Vd.json` de las sesiones LEE) y, en las citas y cifras, contra el PDF de la edición.

| Archivo | Líneas | Nuevas |
|---|---|---|
| ape/A-cronologia.tex | 568, 571, 573, 575, 581–584, 587–588, 590, 593 | 12 |
| ape/C-normativa.tex | 352 | 1 |
| ape/D-pedidos.tex | 78, 341 | 2 |
| ape/E-personas.tex | 123 | 1 |
| ape/F-fuentes.tex | 25–26, 104–105 | 4 |
| cap/00-advertencia.tex | 45 | 1 |
| cap/02-metodo.tex | 28, 99 | 2 |
| cap/11-ribera.tex | 571, 903, 921, 932–933, 961 | 6 |
| cap/12-amparo.tex | 604 | 1 |
| cap/15-hacienda.tex | 490, 498, 500, 503, 505–507, 511, 531 | 9 |
| cap/19-resistencias.tex | 203 | 1 |
| cap/20-opacidad.tex | 995, 1016, 1018 | 3 |
| cap/22-infraestructura.tex | 545 | 1 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 11:900–962 (la tabla de 2016 y 2017 y sus cautelas: hallazgo 2), 11:565–575, 15:486–535 (Vialidad: hallazgos 3 y 5), 19:185–205 (canteras), 20:985–1020, 22:540–546 y A:553–600.

**Esta ronda: 44 líneas nuevas**, 56.453 bytes sobre 3.301.162, que en las 1.001 páginas de la base equivalen a **17,1 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.445 vigentes + 44 = **25.489 de 25.489 (100,0 %)**. La fase 6 toca diez líneas: A:581, A:588, F:104, 11:903, 11:940, 15:494, 15:499–500, 15:512 y 22:545; A:581, A:588, F:104, 11:903 y 22:545 están dentro de lo leído en esta ronda, y las otras cinco estaban vigentes y se releyeron como contexto; no cambia el largo de ningún archivo: **25.489 de 25.489 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (`pdftotext` sobre los PDF de los Releases 2016 a 2018 de `boletines-salta`)

Desde 2016 el Boletín es un PDF nacido digital: el texto es vectorial y la imagen se compone de él, de modo que el cotejo se hizo sobre el texto del PDF de la edición (no sobre la capa de `lee_auto`), en la hoja que cita el libro, y tres renglones se miraron además rasterizados a 200 ppp (20121 h60, 19907 h36, 19763 h31).

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 20170 | 14–15 | Decreto 1.817 | «Colectora Máxima y Colectores Principales Cloacales para la localidad de Vaqueros»; «Localidad de la Caldera, Departamento Vaqueros». Coinciden (A:584) |
| 19763 | 31 | Res. SRH 62/16 | «La Caderilla»; «Ing. Hidráulico Víctor Sacarías Pérez» (mirado). Coinciden (11:921, 11:903: precisión) |
| 19984 | 30 | Audiencia pública | «La Misión Urbanización Abierta Etapa II». Coincide (A:583) |
| 20277 | 8–9 | Decreto 625 | «Nueva Planta Potabilizadora Campo Alegre». Coincide (A:590) |
| 20382 | 15–17 | Decreto 1266 | «Optimización del Sistema de Agua de la Localidad de San Lorenzo». Coincide (A:593) |
| 20067 | 9 | Decreto 965 | «Provisión de agua en el barrio Santiago Apóstol». Coincide (A:583) |
| 19828 | 33 | La Serena | nombre y «Los terrenos afectados son de propiedad Fiscal». Coinciden (19:203) |
| 19907 | 36 | Tereza | nombre y la misma fórmula (mirado). Coinciden (19:203) |
| 19776 | 21 | Tierra Gaucha | nombre, 10 ha y ningún renglón sobre la propiedad del terreno: la fórmula fiscal que sigue en 19810 h47 es del aviso de la cantera «Norma», de Los Andes. Coincide con 19:203 |
| 20121 | 59–60 | Vialidad | \$606.078,00 y \$606.025,00 (mirado), «Centro de Convenciones», «acceso Salta y camión para tareas varias», cuatro meses los dos. Hallazgo 3 |
| 19934 | 27 | Res. SRH 427/16 | «Río La Caldera», con mayúscula. Hallazgo 4 |

Son **las 11 cadenas entre comillas del texto nuevo, todas cotejadas en el PDF**, y siete cifras o renglones más (18 cotejos).

### Hallazgos (cinco, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:581 | La fila de 2017 da entre lo hallado ese año «cuatro determinaciones sobre el arroyo Chaile en una sola manzana de Vaqueros»; las determinaciones (205, 210, 211 y 212/17) llevan número de 2017 pero se publicaron en abril y mayo de 2018 (20249 h36–37; 20253 h27). En el Boletín de 2017 salen las cuatro comisiones (19934 h25–27) | 3 | La fila de 2017 dice lo que se publicó ese año (las comisiones y la 279/17, 20106 h33), y la de 2018 agrega las determinaciones, «con número de 2017» |
| 2 | 11:940 | «Todas las comisiones de 2016 invocan el método «geológico-geomorfológico»»: la Res. 62/16, que el mismo AMPLÍA agregó a la tabla de arriba, no nombra método (19763 h31). Repaso de ventana no hecho sobre la frase | 5 | «Todas las comisiones de 2016 que nombran un método...», con la 62/16 dicha |
| 3 | 15:499–500 | La ficha de las contrataciones de octubre de 2017 decía «mantenimiento vial en cinco rutas provinciales, caminos vecinales de la zona y el acceso al Centro de Convenciones», mezcla de los dos avisos que el AMPLÍA conservó de la consulta puntual sin cotejarla (P169): el de rutas nombra las cinco rutas, el Centro de Convenciones y los caminos vecinales; el otro, el acceso Salta; los dos, camión | 3 | Se separan los dos avisos, sin cambiar el largo |
| 4 | F:104 | «río La Caldera» por «Río La Caldera» en una cita del aviso de la Res. 427/16 | 4 | Se repone la mayúscula |
| 5 | 15:494 | La apertura de la sección dice «Hay un tercer punto en la serie» (2017), y diez renglones después el AMPLÍA cierra «La serie queda así: 1933 y, sin un año vacío en lo leído, de 2014 a 2018» | 7 | «Y la serie no se corta ahí.» |

**Precisiones aplicadas sin restar.** 11:903: «con los mismos tres nombres» pasa a «con los mismos tres técnicos», porque el aviso de la 62/16 escribe «Sacarías» y el de la 147/16, según el libro, «Zacarías». 15:512: «tres años después» quedaba a continuación de dos años (2017 y 2018); pasa a «en 2020». 22:545: «también:» pasa a «lo hallado sigue siendo provincial:».

Resta: un error de consistencia en 17,1 páginas, 5,8 por cada 100: **40** por el escalón, y **30** porque contradice material a diez renglones. Dos datos de fecha u origen en el aspecto 3: **−10** (90). Un superlativo que el propio libro desmiente, en el aspecto 5: **−10** (90). Una corrección silenciosa en el aspecto 4: −3, que no mueve el 90 del techo por cotejo parcial.

**Errores introducidos por la propia auditoría**: los cinco, en el AMPLÍA 2016-2018 (`bab001f`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 2 y el 5 son el caso de P159 y P174 (anáforas y frases de anuncio de una serie que crece), que la sesión no corrió como script.

**Descartados (falsos positivos, 4).** «sólo dos ---la del río La Caldera de marzo de 2016 (Res. 62/16) y la del río Vaqueros de mayo...--- incluyen un ingeniero hidráulico» (11:571): sobre las comisiones leídas de 2011 a 2019, y la de 2013 trae un ingeniero en recursos hídricos, como la frase dice. «La más grande de las nueve» (19:203): La Mesa Redonda, 32,5 ha, contra 21,6 de Los Yacones. «Y no fueron las únicas» (15:505): presencia, no unicidad. «En lo leído de los tres años no hay ningún plano publicado ... ningún balance municipal» (F:104): con su universo, como en los tramos anteriores.

**Pendientes revisados sin cerrar.** P211: la ficha del cap. 15 queda corregida (hallazgo 3); sigue abierta la cotización de la contratación de mayo de 2017 (20042 h41, renglón cortado). P212 (Release 2017 y 2018), P213 (Res. 338/16), P214 (Tierra Gaucha: el cotejo confirma que su edicto de 2016 no da el régimen del terreno) y P215 (fichas NUEVO sin incorporar): sin cambios. P13: el informe de 2016 no halló ediciones de otro año en la carpeta 2016; la de 2017 trae 19858.pdf, copia de la 19958 (P212).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.472/25.472 líneas vigentes en `4cc3e36` | 25.445 vigentes; 27 caducas por el AMPLÍA 2016-2018 |
| Citas entre comillas nuevas contra la capa de los tres años y contra el PDF | 11 cadenas | 11/11 literales en la capa; 10/11 en el PDF, con la mayúscula del hallazgo 4 |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *no aparece*, *mayor*, *todas*) | 56.453 bytes agregados; 9 coincidencias nuevas, todas leídas | Una cae (hallazgo 2, que el script no veía porque «Todas» estaba en un renglón no tocado); las demás, descartadas arriba |
| Repaso de ventana: líneas del índice del AMPLÍA con un año 2016 a 2018 o una edición del rango | 368 de 445 líneas del índice (1.037 coincidencias) | Las que caían las corrigió el AMPLÍA (C:352, E:123, 11:571, 20:995, 20:1016); el hallazgo 2 se le escapó |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` de `cap/` a `cap/` agregados por el AMPLÍA y la fase 6 | 0 nuevas entre capítulos (las nuevas van de capítulos a apéndices o de apéndices a capítulos) |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra |
| Aritmética de 2016 a 2018 | 8 cuentas | 100,8 + 3,8967 + 8,6732 = 113,4 ha; 606.078 + 606.025 = 1.212.103; 650.424 + 650.756 + 606.025 + 606.078 + 606.078 + 606.025 = 3.725.386; 606.078 + 606.025 + 709.034 + 708.969 + 901.484 + 901.396 = 4.432.986; 3.267,26 + 216,36 = 3.483,62 m²; 4.083,34 + 665,23 + 169,75 = 4.918,32 m²; 42 + 1 + 45 = 88 tramos; 242 + 240 = 482 números. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 76 | 50 de 149 fragmentos con cifra en las 44 líneas (95 de los 149 llevan la cita en el fragmento) | **50/50 con fuente localizable**: 35 con la cita en el fragmento (por script); las otras 15 son declaraciones de cobertura que remiten a F, filas cuya edición está en la misma fila, una remisión a otra fila de la cronología y oraciones anteriores al AMPLÍA dentro de renglones modificados, con la fuente en el pasaje |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 44 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 44 líneas | 44/44 líneas | 0 caídas. Sin nombre: los donantes de las matrículas 5.832 y de la 4.063 (Barrio La Misión 3), el propietario de Valle Alegre, los titulares de Cerros de Buena Vista, los jubilados. Nombrados: funcionarios y técnicos por su función en actos públicos, la peticionante de La Serena (ya nombrada en 19:187) y sociedades |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `bab001f` y fase 6 | Compilan las dos; 1.001 páginas cada una (995 antes del AMPLÍA); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, como dice la Advertencia; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2016 a 2018 van en pasado o como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 1 y 3 (−5 cada uno), aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgo 4 (−3, bajo el techo de 90 por cotejo parcial del libro); 11 citas nuevas cotejadas |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgo 2: superlativo que el propio libro desmiente (−10), aplicado; ninguna ausencia afirmada sobre 2016 a 2018, que quedan en barrido |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales (fecha de la 414/16, río y arroyo en la 2344, Valle Alegre, Cerros de Buena Vista) están señaladas en F |
| 7 | Consistencia interna | 9 | 30 | 100 | Hallazgo 5: 5,8 por cada 100 de las 17,1 páginas (40), y un escalón más por estar a diez renglones (30); aplicado |
| 8 | Integridad del aparato | 8 | 95 | 95 | Los pedidos de D que el AMPLÍA satisfizo se actualizaron (D:78, D:341); 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (ver avance) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series reproducibles: la de Vialidad de 2014 a 2018, la de ribera |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas tocadas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 44 líneas |

**Nota inicial: 80,2 antes del tope y 80,2 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) correr como script, al final de cada AMPLÍA, el control de frases que anuncian o resumen una serie cuando la serie crece (P159, P174) y el de fecha de acto contra fecha de publicación en las filas de año de la cronología (P164): evitan los −7,2 de los hallazgos 1 y 5 en la nota inicial; (5) LEE complemento de las catorce ediciones de 2017 y 2018 que el Release no trae o trae truncas (P212): no mueve la nota, completa el tramo.

**Avance del libro:** 5 de 5 hallazgos resueltos (100 %) y tres precisiones aplicadas; compila sin errores ni referencias indefinidas, 1.001 páginas. **Avance de la investigación:** sin cambios de estado. La **tercera tesis** (la pérdida de competencia municipal) gana evidencia sin cambiar de estado: de 2016 a 2018 la Municipalidad de La Caldera aparece en el Boletín como contratista de Vialidad seis veces por año, con la cotización igual al presupuesto oficial en los avisos que la dejan leer, y como destinataria de fondos que una ley y una comisión departamental reasignan; las determinaciones de ribera del departamento siguen sin intervención municipal. La **cuarta tesis** (la desidia es selectiva) gana un dato: en 2018 la Provincia recibe en donación, en La Caldera, el terreno de la nueva planta potabilizadora que abastecerá a la capital, y constituye en el departamento la servidumbre de la cisterna del acueducto de San Lorenzo, mientras los fondos destinados al agua del barrio Santiago Apóstol pasan a una retroexcavadora.

**Calidad de la auditoría.** Cobertura de la ronda: 44 líneas (0,17 %; 17,1 páginas). Cobertura acumulada: 25.489 de 25.489 (100,0 %), con el registro de arriba. Falsos positivos descartados: 4. Recortes: los actos que las filas de 2016 a 2018 citan sin comillas se cotejaron contra el TEXTO de los informes y la capa, y sólo los de la tabla contra el PDF; la muestra de trazabilidad no se rehízo; los controles de P159, P164 y P174 se corrieron a mano y no como paso automático, y por eso no atraparon los hallazgos 1, 2 y 5. Errores introducidos por la propia auditoría: 5, los cinco en el AMPLÍA que la misma sesión escribió; atrapados por un control automático: 0.

## Ronda 77 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2019-2021. Base: commit `4627cfa` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2019-2021, sobre `bcd2b73`, la ronda 76 registrada; aplicado por `3-registrar` a las 06:34 del 07/10, con el mismo árbol, `c0d3109`, que el parche entregado), con la fase 6 en `ronda-77.patch` (un commit, `38acbf0`, árbol `3ee5a58`; aplica con `git am` sobre `4627cfa` en un clon limpio de GitHub y deja el mismo árbol). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los tres informes LEE que lo alimentan: se audita trabajo propio, y por eso cada cita nueva se volvió a buscar en el PDF de la edición y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 76 (25.489 de 25.489, sobre `2d06895`, el mismo árbol, `2d17ce7`, que `bcd2b73`) se trasladaron por diff a `4627cfa`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2019-2021 caduca 30 líneas y deja 46 nuevas o modificadas** (16 netas: 11 en A, 2 en F, 1 en 11 y 2 en 15), en 16 archivos. Vigentes después del traslado: 25.459 de 25.505.

### Lectura sobre el texto (numeración de `4627cfa`)

Se leyeron **las 46 líneas, enteras, por la sesión**, sin subagentes (69.208 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-2019_20414-20654_la-caldera_LEE-2019_2026-10-07.txt`, `BO-Salta-2020_20655-20896_la-caldera_LEE-2020_2026-10-07.txt` y `BO-Salta-2021_20973-21141_la-caldera_LEE-2021_2026-10-07.txt`), contra la capa de las ediciones (`Vd.json` de las sesiones LEE) y, en las citas y cifras, contra el PDF de la edición.

| Archivo | Líneas | Nuevas |
|---|---|---|
| ape/A-cronologia.tex | 595, 601, 603, 606–607, 610, 613, 616, 621, 623, 625–626 | 12 |
| ape/D-pedidos.tex | 78, 341, 391 | 3 |
| ape/F-fuentes.tex | 25–26, 106–107 | 4 |
| cap/00-advertencia.tex | 45 | 1 |
| cap/02-metodo.tex | 28, 99 | 2 |
| cap/08-vaqueros.tex | 207 | 1 |
| cap/10-expropiacion.tex | 539 | 1 |
| cap/11-ribera.tex | 951, 978, 995, 1029, 1046, 1060, 1095, 1124 | 8 |
| cap/12-amparo.tex | 604 | 1 |
| cap/13-loteo.tex | 264 | 1 |
| cap/15-hacienda.tex | 507–509, 513, 531, 533 | 6 |
| cap/16-redes.tex | 148 | 1 |
| cap/17-aguabaja.tex | 66 | 1 |
| cap/19-resistencias.tex | 187 | 1 |
| cap/20-opacidad.tex | 1016, 1018 | 2 |
| cap/22-infraestructura.tex | 545 | 1 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 11:925–1110 (las tablas del Chaile, del Wierna y del Vaqueros, sus cautelas y la tabla catastral: hallazgo 1 y la cita del hallazgo 6), 11:1560–1650 (los avisos de 2009 a 2011 del Lesser), 10:530–545 (Skru), 15:486–535 (Vialidad), 19:100–215 (canteras), 13:258–268, 08:183–215, 22:540–546, 17:60–68, 20:1010–1020 y A:585–630.

**Esta ronda: 46 líneas nuevas**, 69.208 bytes sobre 3.320.610, que en las 1.007 páginas de la base equivalen a **21,0 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.459 vigentes + 46 = **25.505 de 25.505 (100,0 %)**. La fase 6 toca nueve líneas: A:603, A:606, A:616, F:106, 10:539, 11:980, 11:1060, 15:507 y 22:545; todas salvo 11:980 están dentro de lo leído en esta ronda, y la 11:980, vigente, se releyó como contexto; no cambia el largo de ningún archivo: **25.505 de 25.505 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (`pdftotext` sobre los PDF de los Releases 2019 a 2021 de `boletines-salta`)

Como en 2016 a 2018, el Boletín de estos años es un PDF nacido digital: el cotejo se hizo sobre el texto del PDF de la edición, en la hoja que cita el libro, y los renglones decisivos se habían mirado ya rasterizados en las sesiones LEE (130 ppp).

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 20690 | 39 | Audiencia de Almería | «Almería - Urbanización Abierta». Coincide (A:606–607, 11:995) |
| 21067 | 50 | Res. 43/21 de Minería | «sin tener concesión de la cantera». Coincide (A:621, 19:187) |
| 21111 | 15 | Decreto 977 | «Rotonda Av. Bolivia - Puente Río Wierna» (el libro compone el guion como raya corta, como en la ficha de 2023). Coincide (A:623, 08:207) |
| 21010 | 12 | Decreto 469 | «Matricula Nº 316», sin tilde. Coincide (F:106, 13:264) |
| 20495 | 47 | Res. 83/19 | «arroyo Seco». Coincide (11:1046, 11:1060, 11:1124) |
| 20608 | 34 | Res. 306/19 | «en la zona». Coincide (11:951) |
| 20776 | 45 | Res. 75/2020 | «Arroyos Vaqueros y Chaile», con mayúscula; el libro escribe «arroyos» en 11:980 (vigente, de consulta puntual) y lo repite en 11:1060. Hallazgo 6 |
| 20829 | 21 | Vialidad, Res. 767/2020 | «parcialmente» y «sujeto a disponibilidad presupuestaria y financiera de la Provincia». Coinciden (15:507) |
| 20479 | 38 | Mojotoro Norte | «paraje Finca Mojotoro», «de propiedad privada». Coinciden (19:187) |
| 20616 | 65 | La Ferroviaria | «lugar río Mojotoro». Coincide (19:187) |
| 20692 | 46–48 | Res. IPV 0073 | «MEJOR VIVIR», en mayúsculas: el libro lo da como nombre del programa, sin cita literal. Coincide (A:606) |
| 20994 | 7 | Res. COE 13 | «Alto Riesgo», con mayúsculas; el libro escribe «alto riesgo» (A:616). Hallazgo 5 |
| 21122 | 16 | Res. MI 118 | «OPTIMIZACIÓN DEL SERVICIO DE LA CALDERILLA - NUEVA RED DISTRIBUIDORA», que el libro da en minúsculas, como ya lo hacía en 07 y 16. Coincide (A:625, 16:148) |
| 20514 | 8 | Decreto 716 | Considerando: «la razón social SKRU S.A. (hoy KALKSTEN S.A.)»; artículo 1º: «a favor de la razón social KALKSTEN S.A. (controlada por SKRU S.A.)». Hallazgo 3 |
| 20560 | 21–24 | Rescisiones de Vialidad | Res. 1112, 1122 a 1127/2019, sin fecha de dictado en el aviso. Hallazgo 4 |

Son **las 15 cadenas entre comillas del texto nuevo que citan un acto, todas cotejadas en el PDF**, y seis cifras o renglones más (21 cotejos).

### Hallazgos (seis, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | 11:1060 | El AMPLÍA insertó la oración sobre la Res. 83/19 entre «veintisiete meses entre la resolución y su publicación» y «Durante ese lapso rigió la prohibición...»: «ese lapso» pasaba a ser los tres meses entre el edicto de la comisión y su determinación | 7 | La oración nueva va después de la de «ese lapso» |
| 2 | 22:545 | «La Provincia ... contrata con Aguas del Norte el reparto de agua en camión cisterna»: el aviso es la Licitación Pública 04/2020 de la propia Aguas del Norte, que contrata el reparto con terceros (20673 h20). Lectura apresurada de la nota de la ficha | 3 | «Aguas del Norte licita el reparto ...», con la L.P. citada |
| 3 | 10:539, A:603 | El Decreto 716/19 llama a la peticionante «SKRU S.A. (hoy KALKSTEN S.A.)» en el considerando y otorga la concesión a «KALKSTEN S.A. (controlada por SKRU S.A.)» en el artículo 1º; el libro daba sólo la segunda forma, sin señalar la discrepancia (la nota del informe LEE 2019, A.27, tampoco: P220) | 6 | Las dos formas, entre comillas, en el capítulo, y la discrepancia dicha en la cronología |
| 4 | 15:507 | «que Vialidad rescinde de común acuerdo en agosto, el mismo día que los de otros municipios»: los avisos no dan la fecha de dictado de las resoluciones (20560 h21–24) | 3 | «en la misma serie de resoluciones que los de otros municipios» |
| 5 | A:616 | «alto riesgo» por «Alto Riesgo» en una cita de la Res. COE 13 | 4 | Se reponen las mayúsculas |
| 6 | 11:1060 y 11:980 | «arroyos Vaqueros y Chaile» por «Arroyos Vaqueros y Chaile» en la cita de la Res. 75/2020: la 980 venía de la consulta puntual y el AMPLÍA la copió | 4 | Se repone la mayúscula en las dos |

**Precisiones aplicadas sin restar.** 10:539: el Decreto 209 es del 7 de febrero y la concesión del 29 de mayo: «tres meses antes» pasa a «casi cuatro meses antes». A:606: «La Provincia expropia tierra» pasa a «declara sujeta a expropiación» (la Ley 8.202 declara la utilidad pública; A:610 ya lo decía bien). A:616: la obra de la Ruta 9 se conviene con Vialidad Nacional y el convenio la llama «Proyecto y Ejecución», no «pavimentación». F:106: «una frase ... no se sostuvo» pasa a «una duda ... quedó resuelta», porque la frase del capítulo 15 era de ignorancia declarada. 22:545: «El municipio de La Caldera no aparece en esas obras» se acota a «En ninguno de esos actos interviene la Municipalidad de La Caldera», para que no se lea como ausencia sobre años que quedan en barrido.

Resta: un error de consistencia en 21,0 páginas, 4,8 por cada 100: **40** por el escalón, y **30** porque contradice material a un renglón. Dos datos de segunda mano o mal atribuidos en el aspecto 3: **−10** (90); con la precisión del intervalo, que se informa y no resta, la nota inicial del aspecto queda en **90**. Una discrepancia entre fuentes no señalada en el aspecto 6: −5 sobre 100, que no baja del 90 de la escala general. Dos correcciones silenciosas en el aspecto 4: −6, que no mueven el 90 del techo por cotejo parcial. Una afirmación que va más allá del acto (A:606, «expropia») en el aspecto 5: **90** por la escala general.

**Errores introducidos por la propia auditoría**: los cinco nuevos, en el AMPLÍA 2019-2021 (`4627cfa`), escrito por esta misma sesión; el sexto, en la parte que venía de 11:980, es anterior. **Ninguno lo atrapó un control automático**: el 1 es el caso de P159 y P174 (una anáfora que se rompe cuando se intercala texto), y el 3 lo encontró el cotejo en el PDF, no la ficha.

**Descartados (falsos positivos, 4).** «una fórmula que ninguna otra de las leídas usa» (11:1029): las comisiones de 2020 y 2021 leídas no traen esa fórmula, y la de 2019 del Lesser la usa y quedó sumada. «la demora más larga de toda la serie» (11:1060): veintisiete meses contra veintidós de la 251/16 y los de las comisiones de 2019, de semanas. «En lo leído de los tres años no hay ningún plano publicado ... ningún balance municipal» (F:106): con su universo, como en los tramos anteriores. «todas con los puntos en la sede» (A:595): las cuatro determinaciones de 2019 remiten los puntos de vinculación a la sede; la 306/19 publica además las coordenadas de los extremos del tramo, que son las de la comisión de 2017.

**Pendientes revisados sin cerrar.** P216 (Release 2021 sin enero a abril): el AMPLÍA lo declara en 00, 02, F, D y en la fila de 2021; sigue abierto. P217 (lámina del catastro): sin cambios. P218 (fichas NUEVO sin llevar al cuerpo): sin cambios. P219 (tramo cubierto en el estado): sin cambios. P214 (Tierra Gaucha): el capítulo 19 suma la multa de 2021 a Supercemento; el expediente y la superficie siguen sin aclarar. P211 y P212: sin cambios.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.489/25.489 líneas vigentes en `bcd2b73` | 25.459 vigentes; 30 caducas por el AMPLÍA 2019-2021 |
| Citas entre comillas nuevas contra el PDF | 15 cadenas que citan un acto | 13/15 literales; 2 con mayúsculas cambiadas (hallazgos 5 y 6) |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *mayor*, *todas*, *todos*, *sólo*) | 20.019 bytes de palabras agregadas; 14 coincidencias, todas leídas | Una se acota (22:545, precisión); las demás son descriptivas («todos con archivo», «el primer tramo», «sólo desde el 26 de abril») o se descartan arriba |
| Repaso de ventana: líneas del índice del AMPLÍA con un año 2019 a 2021 o una edición del rango | 394 de 394 líneas del índice (529 coincidencias) | Las que caían las corrigió el AMPLÍA (11:951, 11:1029, 15:531, 10:539, 20:1016, D:391); el hallazgo 6 estaba en una línea del índice que el AMPLÍA leyó y no cotejó |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` de `cap/` a `cap/` agregados por el AMPLÍA y la fase 6 | 0 (la única nueva dentro de un capítulo, 11:1029, dice «más adelante») |
| `\pendiente{}`, ítems de D | 52; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra; D:391 se actualizó con el Decreto 716/19 ya leído |
| Aritmética de 2019 a 2021 | 9 cuentas | 42 + 1 + 48 = 91 tramos; 1 + 31 + 1 + 1 + 15 = 49 fuera de las ventanas; 241 + 242 + 169 ediciones con 76 ausentes; 2.127.369 / 3 = 709.123 y 2.340.069 / 3 = 780.023; 1.950.948 + 1.951.346 + 1.170.682,50 + 1.170.602,50 + 2.341.365 + 2.341.205 = 10.926.149 («casi once millones»); 4.841.127,29 + 18.365.610,42 + 614.370,68 + 2.879.638,07 + 14.874.995,11 = 41.575.741,57 («más de cuarenta y un millones y medio»); 114.372.450,98 / 95.899.772,97 = 1,193 («un 19 por ciento»); 3,7702 y 3,8781 ha («unas tres hectáreas y tres cuartos»); 1933 a 2021 = 88 años. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 77 | 50 de 235 fragmentos con cifra en las 46 líneas | **50/50 con fuente localizable**: 32 con la cita en el fragmento (por script); las otras 18 son declaraciones de cobertura que remiten a F o son F, filas que remiten a otra fila, sumas de contratos citados en el mismo párrafo y oraciones anteriores al AMPLÍA dentro de renglones modificados, con la fuente en el pasaje |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 46 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 46 líneas | 46/46 líneas | 0 caídas. Sin nombre: el titular de la concesión de riego de 2021, el particular de El Durazno, la fallida de 2021, los socios de las sociedades. Nombrados: los intendentes Escalera y Moreno por su función, los técnicos de las comisiones de ribera, sociedades y fideicomisos |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `4627cfa` y fase 6 | Compilan las dos; 1.007 páginas cada una (1.001 antes del AMPLÍA); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, como dice la Advertencia; 2 cajas desbordadas, las mismas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 50/50 en la muestra (90 por el criterio); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2019 a 2021 van en pasado o como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 2 y 4 (−5 cada uno), aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgos 5 y 6 (−3 cada uno, bajo el techo de 90 por cotejo parcial del libro); 15 citas nuevas cotejadas |
| 5 | Honestidad epistémica | 12 | 90 | 100 | «Expropia» por una declaración de utilidad pública (escala general, 90), corregido; ninguna ausencia afirmada sobre 2019 a 2021, que quedan en barrido, y la de 22:545 se acotó a los actos citados |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Hallazgo 3 (−5 sobre 100; la escala lo deja en 90); las discrepancias de los originales de 2019 a 2021 (Matrícula 316, arroyo Seco, la paginación de la 21096, el Decreto 716) quedan señaladas |
| 7 | Consistencia interna | 9 | 30 | 100 | Hallazgo 1: 4,8 por cada 100 de las 21,0 páginas (40), y un escalón más por estar a un renglón (30); aplicado |
| 8 | Integridad del aparato | 8 | 95 | 95 | El pedido de D satisfecho por el AMPLÍA se actualizó (D:391) y los de cobertura (D:78, D:341); 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (ver avance) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series reproducibles: Vialidad de 2014 a 2021, ribera por curso |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas (P217 pide sumar dos actos a la lámina del catastro) |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas tocadas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 46 líneas |

**Nota inicial: 80,2 antes del tope y 80,2 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) correr como script, al final de cada AMPLÍA, el control de anáforas de frase siguiente («ese lapso», «esa cifra», «la segunda») sobre cada párrafo donde se intercala texto (P159, P174), y el cotejo de las citas nuevas contra el PDF antes de entregar: evitan los −6,3 del hallazgo 1 en la nota inicial y los hallazgos 5 y 6, que no restan bajo el techo de 90; (5) LEE complemento de las 76 ediciones de enero a abril de 2021 (P216): no mueve la nota, completa el tramo y puede traer las determinaciones de ribera que el capítulo 11 tiene de consulta puntual.

**Avance del libro:** 6 de 6 hallazgos resueltos (100 %) y cinco precisiones aplicadas; compila sin errores ni referencias indefinidas, 1.007 páginas. **Avance de la investigación:** sin cambios de estado. La **tercera tesis** (la pérdida de competencia municipal) gana evidencia sin cambiar de estado: de 2019 a 2021 la Municipalidad de La Caldera aparece en el Boletín como contratista de Vialidad, con contratos aprobados mes a mes «sujeto a disponibilidad presupuestaria» en 2020, y no interviene en ninguno de los actos de agua del período, ni en la nueva red de La Calderilla; la de Vaqueros, en cambio, recibe por convenio cinco obras en 2021. La **cuarta tesis** (la desidia es selectiva) gana dos datos: en 2019 la Provincia concede a una sociedad privada el agua del dique para generar energía al pie de la presa y da en comodato a dos asociaciones profesionales tierra fiscal de la misma matrícula, y en 2021 adjudica por más de ciento catorce millones la red de La Calderilla, derivada del acueducto que lleva el agua del departamento a la capital.

**Calidad de la auditoría.** Cobertura de la ronda: 46 líneas (0,18 %; 21,0 páginas). Cobertura acumulada: 25.505 de 25.505 (100,0 %), con el registro de arriba. Falsos positivos descartados: 4. Recortes: los actos que las filas de 2019 a 2021 citan sin comillas se cotejaron contra el TEXTO de los informes y la capa, y sólo los de la tabla contra el PDF; la muestra de trazabilidad no se rehízo; los controles de P159 y P174 se corrieron a mano y no como paso automático, y por eso no atraparon el hallazgo 1. Errores introducidos por la propia auditoría: 5, en el AMPLÍA que la misma sesión escribió, y uno heredado de la consulta puntual; atrapados por un control automático: 0.

## Ronda 78 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 2022-2024. Base: commit `30aa34a` de `ediedrich/dispositivo-caldereno` (AMPLÍA 2022-2024, sobre `3480f2c`, la ronda 77 registrada; aplicado por `3-registrar` a las 08:34 del 07/10), con la fase 6 en `ronda-78.patch` (un commit sobre `30aa34a`; aplica con `git am` en un clon limpio de GitHub). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los tres informes LEE que lo alimentan: se audita trabajo propio, y por eso cada cita nueva se volvió a buscar en la capa de la edición (`Vd.json` de las sesiones LEE, texto del PDF) y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 77 (25.505 de 25.505, sobre `3480f2c`) se trasladaron por diff a `30aa34a`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 2022-2024 caduca 26 líneas y deja 40 nuevas o modificadas** (14 netas: 5 en A, 2 en F, 2 en 08, 1 en 09, 2 en 11 y 2 en 15), en 18 archivos. Vigentes después del traslado: 25.479 de 25.519.

### Lectura sobre el texto (numeración de `30aa34a`)

Se leyeron **las 40 líneas, enteras, por la sesión**, sin subagentes (69.061 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-2022_21145-21380_la-caldera_LEE-2022_2026-10-07.txt`, `BO-Salta-2023_21381-21621_la-caldera_LEE-2023_2026-10-07.txt` y `BO-Salta-2024_21622-21864_la-caldera_LEE-2024_2026-10-07.txt`) y, en las citas y cifras, contra la capa de la edición.

| Archivo | Líneas | Nuevas |
|---|---|---|
| ape/A-cronologia.tex | 629, 643, 647, 662, 669, 682 | 6 |
| ape/B-matriz.tex | 39 | 1 |
| ape/D-pedidos.tex | 78, 147, 341 | 3 |
| ape/F-fuentes.tex | 25–26, 108–109 | 4 |
| cap/00-advertencia.tex | 45 | 1 |
| cap/02-metodo.tex | 28, 99 | 2 |
| cap/07-cot.tex | 365 | 1 |
| cap/08-vaqueros.tex | 191, 204–205 | 3 |
| cap/09-defensas.tex | 808, 811–812 | 3 |
| cap/10-expropiacion.tex | 539 | 1 |
| cap/11-ribera.tex | 1063–1064 | 2 |
| cap/12-amparo.tex | 604 | 1 |
| cap/15-hacienda.tex | 509–511 | 3 |
| cap/16-redes.tex | 148 | 1 |
| cap/20-opacidad.tex | 1016, 1018 | 2 |
| cap/21-ausencias.tex | 141, 145, 148, 154 | 4 |
| cap/22-infraestructura.tex | 378 | 1 |
| cap/26-presencia.tex | 235 | 1 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09:790–830 (la serie de las defensas), 08:183–215 (la audiencia de la Ruta 9), 11:964–1062 (las tablas del Chaile, del Wierna y del Vaqueros y sus cautelas), 15:500–520 (Vialidad), 16:140–150, 07:350–368, 22:370–382, 21:136–175, 26:235, D:390–396 y A:595–690.

**Esta ronda: 40 líneas nuevas**, 69.061 bytes sobre 3.336.168, que en las 1.011 páginas de la base equivalen a **20,9 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.479 vigentes + 40 = **25.519 de 25.519 (100,0 %)**. La fase 6 toca once líneas: A:629, A:662, D:394, 08:204, 09:811, 16:148, 21:141, 21:145, 21:148, 21:154 y 26:235; todas salvo D:394 están dentro de lo leído en esta ronda, y la D:394, vigente, se releyó entera al modificarla; no cambia el largo de ningún archivo: **25.519 de 25.519 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (capa de los PDF de los Releases 2022 a 2024 de `boletines-salta`)

El Boletín de estos años es un PDF nacido digital: el cotejo se hizo sobre el texto del PDF de la edición, y los renglones decisivos se habían mirado ya rasterizados en las sesiones LEE (130 ppp).

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 21171 | 16 | Res. SOP 80/22, financiamiento | «Argentina hace», con minúscula; el libro escribía «Argentina Hace» y citaba h. 14 y 15 (A:629). Hallazgo 4 |
| 21455 | 42 | Audiencia de la sección I de la Ruta 9 | «Rotonda Avda. Bolivia - Puente Río Vaqueros»; 5 de mayo, Escuela de Bellas Artes, El Huaico; «Responsable del Proyecto: Empresa ING. MEDINA S.A.». La cita coincide; «consultora» no lo dice el aviso (08:204). Hallazgo 3 |
| 21591 | 40 | Audiencia de noviembre | «Sección: Rotonda Avda. Bolivia - Puente Río Caldera. Sección II: Puente Río Vaqueros - Puente Rio Caldera». Coincide con la ficha corregida (08:191) |
| 21794 | 29 | Res. SOP 864/24 | «ciento setenta y siete millones» en letras. Coincide (F:108) |
| 21833 | 20 | Res. SOP 1044/24 | «COLEGIO Nº 5.046». Coincide, en la caja baja con que el libro da los títulos de obra (F:108) |
| 21801 | 44 | El Triunfo III | «en el departamento La Caldera, lugar río La Caldera». Coincide (A:662) |
| 21822 | 44 | Aguas del Norte, exp. 26024/24 | «Convenio Economía - Finalización de obra: nueva red distribuidora La Calderilla», con mayúscula; el libro escribía «finalización» (16:148). Hallazgo 5 |
| 21420 | 25 | Decreto 150/23 | «Madre Tierra». Coincide (A:643) |
| 21433 | 38 | Res. SRH 27/2023 | «Río Castellano»; los puntos «en la sede». Coinciden (11:1063) |
| 21444, 21493, 21861 | 51; 28; 43 | Res. SRH 21/2023, 97/2023, 233/2024 | Los puntos de vinculación «a disposición de los interesados en la sede». Coinciden (11:1063) |
| 21159 | 49, 52 | Vialidad, Res. 86 y 87/22 | «Y UN CAMIÓN PARA TRABAJOS VARIOS Y/O EMERGENCIAS», que el libro da en caja baja. Coincide (15:509) |
| 21717 | 28 | Res. AMT 205/24 | tarifa única de «pesos seiscientos noventa ($ 690)» desde el 27 de mayo. Coincide (A:669) |
| 21314 | 29 | Res. SOP 628/22 | «en forma previa y por cuestiones de emergencia el encauce en el Arroyo Guaranguay, terraplén en el Río La Caldera y la descolmatación del puente de ingreso». Coincide con la paráfrasis (09:811) |

Son **las 11 cadenas entre comillas del texto nuevo, todas cotejadas en la capa**: 6 literales, 3 que el libro pasa a caja baja desde un título en mayúsculas, como hace con todos los títulos de obra, y 2 con una mayúscula cambiada; y diez cifras o renglones más (21 cotejos).

### Hallazgos (siete, aplicados en la fase 6)

| # | Dónde | Hallazgo | Aspecto | Corrección |
|---|---|---|---|---|
| 1 | A:629 | «publica siete convenios con la de Vaqueros ---... y un adicional de la toma del Quintín---»: el adicional (Res. 782/22) no es un convenio; son seis y un adicional | 3 | «seis convenios ... y un adicional de la toma del Quintín» |
| 2 | A:662, 26:235 | «el hospital cambia sus tres gerencias» / «le cambia sus tres gerencias»: la D.A. 286 sólo deja sin efecto la de atención de las personas y no designa reemplazo (21743 h8) | 5 | «releva a los titulares de las tres gerencias ... y designa nuevos en dos» |
| 3 | 08:204 | «otra audiencia sobre el mismo estudio ... y la misma consultora, Ing. Medina S.A.»: los expedientes de las dos audiencias son distintos (-65 y -181), y el aviso llama a la empresa «Responsable del Proyecto» | 5 | «sobre el estudio de impacto de la misma obra ... y la misma responsable del proyecto» |
| 4 | A:629 | «Argentina Hace» por «Argentina hace», y la hoja (16, no 14 y 15) | 4 | Se repone la minúscula y la hoja |
| 5 | 16:148 | «finalización de obra: ...» por «Finalización de obra: ...» en una cita | 4 | Se repone la mayúscula |
| 6 | 11:1064 | El AMPLÍA abrió un `\pendiente{}` (ubicación y titulares de seis inmuebles) sin pedido en el apéndice D | 8 | El pedido se suma al ítem de la serie del Chaile (D:394), sin cambiar el número de pedidos |
| 7 | 21:145 | «Biblioteca Popular El Molino y Asociación Civil Ciencia al Alcance de Todos, de Vaqueros (2022 a 2024)»: la segunda tiene asambleas en 2023 y 2024 | 3 | Se separan los intervalos |

**Precisiones aplicadas sin restar.** 21:141, 145, 148 y 154: las nueve asambleas que el AMPLÍA sumó a la ficha de entidades llevan su edición y su hoja (la muestra del aspecto 1 tomó una sin ellas; el aspecto ya estaba en 82 por la escala general). 09:811: la Resolución 158/22 se lista como antecedente, «con otro legajo», porque no dice que la defensa de 2022 sea la de Santiago Apóstol y El Nogalar~4, que es la obra cuya historia el pasaje cuenta.

Resta: dos datos mal caracterizados en el aspecto 3 (hallazgos 1 y 7): **−10** (90). Dos afirmaciones que van más allá del acto en el aspecto 5 (2 y 3) y la precisión de 09:811: **90** por la escala general. Dos correcciones silenciosas en el aspecto 4: −6, que no mueven el 90 del techo por cotejo parcial. Una falta del aparato en el aspecto 8: −5 (90). Ningún error de consistencia en las 20,9 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los siete, en el AMPLÍA 2022-2024 (`30aa34a`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: los 4 y 5 los encontró el cotejo de las cadenas entre comillas contra la capa, que esta ronda corrió por script sobre todas las cadenas nuevas; el 6, el recuento de `\pendiente{}` contra los ítems de D.

**Descartados (falsos positivos, 3).** «traen tres más que el buscador no devolvía» (22:378): se sigue de lo que el propio capítulo dice que devolvía el buscador (Lares de la Inmaculada como única audiencia sobre un loteo, y la de noviembre de 2023 de la Ruta 9). «Los Boletines de 2023 y 2024 ... no traen ninguno» (15:509): con el criterio del apéndice F dicho en la misma oración. «En lo leído de los tres años no hay ningún plano publicado ... ningún balance municipal» (F:108): con su universo, como en los tramos anteriores.

**Pendientes revisados sin cerrar.** P221 (21142-21144): el AMPLÍA lo declara en 00, 02, F, D y en la fila de 2022; sigue abierto. P222 (la 21864 en 2024 y 2025) y P13: sin cambios. P223 (fichas NUEVO sin llevar al cuerpo) y P224 (lámina del catastro): sin cambios. P216 a P219: sin cambios.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.505/25.505 líneas vigentes en `3480f2c` | 25.479 vigentes; 26 caducas por el AMPLÍA 2022-2024 |
| Citas entre comillas nuevas contra la capa | 11 cadenas | 6/11 literales; 3 en caja baja desde un título en mayúsculas, como el libro hace con los títulos; 2 con una mayúscula cambiada (hallazgos 4 y 5) |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *mayor*, *todas*, *todos*, *sólo*) | 15.634 bytes de palabras agregadas; 18 coincidencias, todas leídas | Descriptivas («las tres primeras del año», «sin ninguna ausente», «primera etapa», «única oferente», «tarifa única») o descartadas arriba |
| Repaso de ventana: líneas del índice del AMPLÍA con un año 2022 a 2024 o una edición del rango | 564 de 564 líneas del índice (712 coincidencias) | Las que caían las corrigió el AMPLÍA (07:365, 22:378, 16:148, 15:509, D:147, D:341, 08:191) |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` de `cap/` a `cap/` agregados por el AMPLÍA y la fase 6 | 0 |
| `\pendiente{}`, ítems de D | 53; 284 | 22-prospectiva dice «doscientos ochenta y cuatro pedidos»: cierra; el `\pendiente{}` nuevo de 11:1064 tiene su pedido en D:394 después de la fase 6 |
| Aritmética de 2022 a 2024 | 8 cuentas | 42 + 1 + 51 = 94 tramos; 1 + 31 + 1 + 1 + 18 = 52 fuera de las ventanas; 236 + 241 + 242 + 1 ediciones; 3.462.902,95 + 4.841.285,54 + 35.915.887,17 + 39.900.254,77 = 84.120.330,43; 167.218.508,21 + 216.819.417,19 = 384.037.925,40; 60 + 120 = 180 m; 1933 a 2022 = 89 años; 23/10 a 30/10/2024 = una semana. Cierran |
| Muestra de 50 afirmaciones (aspecto 1), semilla 78 | 50 de 188 fragmentos con cifra en las 40 líneas | **49/50 con fuente localizable en la base** (98 %: 82 por interpolación): 30 con la cita en el fragmento (por script); 19 son declaraciones de cobertura que remiten a F o son F, filas o pasajes que remiten a otro con la cita, y oraciones anteriores al AMPLÍA dentro de renglones modificados; la que falta es la lista de entidades agregada a la ficha de 21:136–155, sin número de edición. La fase 6 agrega las ediciones y hojas de las nueve asambleas sumadas: **50/50** después |
| Muestra de 20 datos web o de prensa (aspecto 9) | 0 datos web o de prensa nuevos en las 40 líneas | no se rehízo; vale la de la ronda 42 (5/12) |
| Privacidad: personas nombradas en las 40 líneas | 40/40 líneas | 0 caídas. Sin nombre: los titulares de concesiones de riego, los fallidos, los agentes del hospital y el particular de El Durazno. Nombrados: el intendente Sumbay por su función, los gerentes del hospital por su designación (en los informes LEE; el libro no los nombra), la empresa unipersonal adjudicataria del complejo y las sociedades |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `30aa34a` y fase 6 | Compilan las dos; 1.011 páginas la base y 1.013 con la fase 6 (1.007 antes del AMPLÍA); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, como dice la Advertencia |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | 49/50 en la muestra de la base (82 por interpolación) y 50/50 después de la fase 6 (90); la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2022 a 2024 van en pasado o como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 1 y 7 (−5 cada uno), aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgos 4 y 5 (−3 cada uno, bajo el techo de 90 por cotejo parcial del libro); 9 citas nuevas cotejadas |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgos 2 y 3 (escala general, 90), corregidos; ninguna ausencia afirmada sobre 2022 a 2024, que quedan en barrido: las dos frases que lo rozan (15:509, D:341) declaran el criterio |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias de los originales de 2022 a 2024 (monto en letras, «Colegio Nº 5.046», D.A. 379/21 y 379/23, sorteo de 2023) quedan señaladas en F |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores de consistencia en 20,9 páginas |
| 8 | Integridad del aparato | 8 | 90 | 95 | Hallazgo 6 (−5), aplicado; 95 como en las rondas anteriores |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (ver avance) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series reproducibles: Vialidad de 2014 a 2022, ribera por curso, defensas de 2022 a 2026 |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones a capítulos posteriores sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas (P224 pide sumar cuatro determinaciones y dos donaciones a la lámina del catastro) |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas tocadas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 40 líneas |

**Nota inicial: 86,1 antes del tope y 86,1 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) correr como paso automático del AMPLÍA el cotejo de las cadenas entre comillas contra la capa y el recuento de `\pendiente{}` contra D, que esta ronda corrió después: habrían atrapado los hallazgos 4, 5 y 6 antes de entregar (+0,4 en la nota inicial); (5) LEE complemento de las ediciones 21142 a 21144 (P221) y de las 76 de enero a abril de 2021 (P216): no mueven la nota, completan los tramos.

**Avance del libro:** 7 de 7 hallazgos resueltos (100 %) y dos precisiones aplicadas; compila sin errores ni referencias indefinidas, 1.013 páginas. **Avance de la investigación:** sin cambios de estado. La **tercera tesis** (la pérdida de competencia municipal) gana evidencia sin cambiar de estado: de 2022 a 2024 la Municipalidad de La Caldera sólo publica en el Boletín un acto propio, la licitación de un camión que firma su intendente; todo lo demás llega como convenio que la Provincia le adjudica y rescinde ---dos de 2023 rescindidos en 2024 por el desfase de precios, y la defensa del río rehecha a valores nuevos---, mientras la red de La Calderilla, rescindida a su contratista, sigue por contratación de emergencia de Aguas del Norte sin montos publicados. La **cuarta tesis** (la desidia es selectiva) gana un contraste: en el mismo diciembre de 2024 la Provincia licita por novecientos cincuenta y cinco millones el centro de salud de Vaqueros y conviene con la Municipalidad de La Caldera, por ciento sesenta y siete, la primera etapa de la refacción de su hospital.

**Calidad de la auditoría.** Cobertura de la ronda: 40 líneas (0,16 %; 20,9 páginas). Cobertura acumulada: 25.519 de 25.519 (100,0 %), con el registro de arriba. Falsos positivos descartados: 3. Recortes: los actos que las filas de 2022 a 2024 citan sin comillas se cotejaron contra el TEXTO de los informes y la capa, y sólo los de la tabla contra el renglón del PDF; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: 7, en el AMPLÍA que la misma sesión escribió; atrapados por un control automático antes de llegar al libro: 0 (los controles que los encontraron corrieron en esta ronda, después de la entrega del AMPLÍA).

## Ronda 79 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1937,2025-2026. Base: commit `2f3f54c` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1937,2025-2026, sobre `29739eb`, la ronda 78 registrada; aplicado por `3-registrar` a las 10:04 del 07/10), con la fase 6 en `ronda-79.patch` (un commit sobre `2f3f54c`; aplica con `git am` en un clon limpio de GitHub). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los tres informes LEE que lo alimentan (1937, 2025 y 2026): se audita trabajo propio, y por eso cada cita y cada cifra nueva se volvió a buscar en la capa de la edición (`Vd.json` de las sesiones LEE, texto del PDF) y no en las fichas.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 78 (25.519 de 25.519, sobre `29739eb`) se trasladaron por diff a `2f3f54c`, con el criterio de siempre: en un commit de incorporación una línea modificada o nueva caduca. **El AMPLÍA 1937,2025-2026 caduca 19 líneas y deja 23 nuevas o modificadas** (4 netas: 2 en A y 2 en F), en 13 archivos. Vigentes después del traslado: 25.500 de 25.523.

### Lectura sobre el texto (numeración de `2f3f54c`)

Se leyeron **las 23 líneas, enteras, por la sesión**, sin subagentes (38.296 bytes), y se cotejaron contra los tres informes LEE (`BO-Salta-1937_1669-1721_la-caldera_LEE-1937_2026-10-07.txt`, `BO-Salta-2025_21864-22100_la-caldera_LEE-2025_2026-10-07.txt` y `BO-Salta-2026_22101-22271_la-caldera_LEE-2026_2026-10-07.txt`) y, en las citas y cifras, contra la capa de la edición.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 2 (filas de 2025 y de 2026) |
| ape/C-normativa.tex | 2 |
| ape/D-pedidos.tex | 2 |
| ape/F-fuentes.tex | 4 |
| cap/00-advertencia.tex | 1 |
| cap/02-metodo.tex | 2 |
| cap/04-siglo.tex | 1 |
| cap/09-defensas.tex | 1 |
| cap/11-ribera.tex | 2 |
| cap/16-redes.tex | 1 |
| cap/18-trabajo.tex | 2 |
| cap/20-opacidad.tex | 2 |
| cap/22-infraestructura.tex | 1 |

Contexto releído entero (no suma cobertura, porque ya estaba vigente): 09:775–830 (la serie de las defensas y la ficha de la Res. 479), 11:986–997 y 11:1240–1300 (la serie de ribera y los edictos de 2025 y 2026), 16:121, 18-trabajo:215–300 (las tres sociedades y su cautela), 22:370–382, 12:1197, 04:3009–3260 (1937 y 1938), 26-presencia:159–200, D:60–80 y D:140–150, A:185–196 y A:670–723.

**Esta ronda: 23 líneas nuevas**, 38.296 bytes sobre 3.345.697, que en las 1.015 páginas de la base equivalen a **11,6 páginas**: ése es el denominador del aspecto 7.

Acumulado: 25.500 vigentes + 23 = **25.523 de 25.523 (100,0 %)**. La fase 6 toca dos líneas, A (fila de 2025 y fila de 2026, una sola línea física cada una) y 11:1275, todas dentro de lo leído en esta ronda; no cambia el largo de ningún archivo: **25.523 de 25.523 (100,0 %)** después de ella.

### Cotejo sobre el facsímil (capa de los PDF de los Releases 1937, 2025 y 2026 de `boletines-salta`)

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 1670 | 24 | Licencia del comisario Ramón Juárez (04:3257) | «Salta, Febrero 10 de 1936», mirado a 170 ppp: el decreto es de 1936 y se publica el 08/01/1937. Coincide con la corrección del AMPLÍA |
| 1707 | 8 | Decreto sobre Potrero de Castilla (A:189, 22:721, 26:39) | «1421—Salta, Setiembre 10 de 1937», mirado a 250 ppp; el 1420 en la h. 7 y el 1422 a continuación. El libro dice 1421: coincide. El informe LEE 1937 decía 1419 (P225) |
| 1707 | 26 | Sentencia de la Corte, río Wierna (D:63) | «Salta, Abril 28 de 1936», mirado: la Corte rechazó en 1936, como dice D. Coincide |
| 21994 | 61 | Sede de Campo Alegre Constructora (18-trabajo) | «RN 9 - km 1931». Literal |
| 22148 | 78 | Sede de Cantera El Rescoldo (18-trabajo) | «Ruta Provincial 9, Km 1627». Literal (la misma fórmula en los domicilios especiales de la h. 80) |
| 22000 | 31 | Res. SOP 367/25 (16:121) | «obra que impidió el inicio de los trabajos». Coincide con la paráfrasis |
| 22037 | 25 | Res. SOP 482/25 (16:121) | «oportunamente rescindida de común acuerdo por un cambio de proyecto por parte de la empresa Aguas del Norte». Coincide con la paráfrasis |
| 22205 | 21–22 | Res. SOP 300/26 (09:815) | «tramos de mayor riesgo», \$42.725.963,14 a valores de «Enero de 2.026», «20 (veinte) días corridos», adjudicada a la Municipalidad de La Caldera. Coincide |
| 21865 | 1 | Fecha de la primera edición de 2025 sin repetir (A, F, 00) | «Salta, viernes 3 de enero de 2025». Coincide |
| 21998 | 19–20 | Res. SOP 351/25 | La refacción del Colegio Nº 5045 está adjudicada a una firma (Res. 1045/24), no por convenio con la Municipalidad. Hallazgo 1 |
| 21869 | 12 | Res. 69 SSPC | Del 26/12/2024, publicada el 09/01/2025. Hallazgo 2 |

Son **las 2 cadenas entre comillas del texto nuevo, las dos literales en la capa**; las demás comillas de las líneas tocadas ya estaban en la base.

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | A (filas de 2025 y 2026) | Ponía la redeterminación (Res. 351/25) y el adicional (Res. 357/26) de la refacción del Colegio Nº 5045 entre lo que la Secretaría «conviene con la Municipalidad de La Caldera»: la obra está adjudicada a una empresa desde 2024 | 3 | Se separan: «La refacción del Colegio Nº 5045, adjudicada a una empresa, tiene su primera redeterminación» y «aprueba además el adicional Nº 1 de la refacción del Colegio Nº 5045, adjudicada a una empresa en 2024» |
| 2 | A (fila de 2025) | «Se aprueban los pliegos del Centro de Salud de Vaqueros»: la Res. 69 es del 26/12/2024; en 2025 sólo se publica (control de fechas de P86 y P164) | 3 | «En enero se publican los pliegos ..., aprobados el 26 de diciembre de 2024» |

**Precisión aplicada sin restar.** 11:1275: «la encuentra en todas sus determinaciones» enumera también dos rectificaciones (108/2025 y 130/2025): pasa a «determinaciones y rectificaciones».

Resta: dos datos mal caracterizados en el aspecto 3: **−10** (90). Ningún error de consistencia en las 11,6 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los dos, en el AMPLÍA 1937,2025-2026 (`2f3f54c`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró la relectura de la ficha LEE contra la fila; el 2, el control de fechas de P86 y P164, corrido a mano en esta ronda.

**Descartados (falsos positivos, 2).** «los dos que consignan el kilometraje lo dan con un error» (18-trabajo): la cantera da la kilometría correcta de la ruta, pero la llama provincial; la frase dice «con la jurisdicción de la ruta cambiada». «traen cuatro más que el buscador no devolvía» (22:378): la de la finca Antilla es de 2025 y en La Caldera, de modo que la consulta que el capítulo cita (2023-2026, La Caldera) no la devolvió.

**Pendientes revisados.** P222 lo cerró el AMPLÍA (el informe LEE 2025 declara la 21864 ya leída). Quedan abiertos los tres que el AMPLÍA abrió: P225 (el informe LEE 1937 dice 1419 donde la imagen y la serie dan 1421; el libro dice 1421), P226 (fichas NUEVO sin llevar al cuerpo) y P227 (complemento de 2026 desde la 22272).

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.519/25.519 líneas vigentes en `29739eb` | 25.500 vigentes; 19 caducas por el AMPLÍA |
| Citas entre comillas nuevas contra la capa | 2 cadenas | 2/2 literales |
| Superlativos, cierres y ausencias en el texto agregado (*único*, *primer*, *el más*, *la más*, *nunca*, *jamás*, *ningún*, *ninguna*, *ninguno*, *no aparece*, *mayor*, *todas*, *todos*, *sólo*) | 9.157 bytes de palabras agregadas; 7 coincidencias, todas leídas | Con su universo («En lo leído no hay ningún plano...», «todas con los puntos en la sede», «sólo hasta el 21 de septiembre») o citas («tramos de mayor riesgo») |
| Repaso de ventana: líneas del índice del AMPLÍA con 1937, 2025 o 2026 | 231 de 614 líneas del índice (842 coincidencias), las que citan Boletín, resolución o decreto | Las que caían las corrigió el AMPLÍA (04:3257, 18-trabajo, 20:1016–1018, 22:378, D:78, D:147); las 383 restantes del cap. 12 y de prensa no las toca ningún informe LEE |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` de `cap/` a `cap/` agregados por el AMPLÍA y la fase 6 | 0 |
| `\pendiente{}` | Agregados por el AMPLÍA: 0 | Sin cambios en D |
| Aritmética | 7 cuentas | 42 + 1 + 53 = 96 tramos; 1 + 31 + 1 + 1 + 20 = 54 fuera de las ventanas; 31 + 1 + 1 + 20 = 53 (02); 236 + 171 ediciones; 16 + 11 = 27 sociedades, 13 + 7 = 20 en Vaqueros y 3 + 4 = 7 en La Caldera; 182.540.096,21 + 57.669.522,87 = 240.209.619,08; 14/2025, 56, 57, 108, 130 y 142 = seis. Cierran |
| Privacidad: personas nombradas en las 23 líneas | 23/23 líneas | 0 caídas. Sin nombre: los socios de las sociedades, los titulares de la finca Antilla, el donante de las motocicletas y la empresa del Colegio Nº 5045. Nombrados: Ramón Juárez, como comisario (ya en la base) |
| Largo de los archivos antes y después de la fase 6 | 38/38 archivos | ninguno cambia de largo con la fase 6 |
| Compilación | libro entero, base `2f3f54c` y fase 6 | Compilan las dos; 1.015 páginas cada una (1.013 antes del AMPLÍA); 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas, como dice la Advertencia |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Todas las frases nuevas con edición y hoja o con remisión a la fila o al capítulo que las tiene; la escala general lo deja en 82 por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Las normas de 2025 y 2026 van como lo que dispusieron |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 1 y 2 (−5 cada uno), aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 2 citas nuevas, literales; techo de 90 por cotejo parcial del libro |
| 5 | Honestidad epistémica | 12 | 100 | 100 | 2025 y 2026 quedan en barrido y el texto lo dice; 2026, sólo hasta el 21 de septiembre |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias del original (kilometrajes, causas de la rescisión de la red de Vaqueros) quedan señaladas |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores de consistencia en 11,6 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin `\pendiente{}` nuevos |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado (ver avance) |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Series reproducibles: defensas, ribera y redes hasta septiembre de 2026 |
| 12 | Estructura y prosa | 2 | 100 | 100 | 0 remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin propuestas tocadas |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas en las 23 líneas |

**Nota inicial: 87,7 antes del tope y 87,7 después** (tope de 90 por la cobertura acumulada inicial del 99,9 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %: sin tope). De la distancia a 100 de la nota final, **3,8 puntos son estructurales** (los aspectos 1, 4, 9, 10 y 11) y **7,9 son corregibles** (P115 en el 1, P40 en el 9, las tesis abiertas en el 10, el 6, el 8, el 13 y el 15).

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna de las tesis abiertas: hasta +1,8 en el 10; (3) dar fuente o pedido a las cifras físicas del embalse de 10:516 (P115): +0,9; (4) correr en el AMPLÍA, antes de entregar, el control de fechas de P86 y P164 y el cotejo de cada «conviene con la Municipalidad» contra el adjudicatario de la ficha: habrían atrapado los dos hallazgos (+0,6 en la nota inicial); (5) llevar al cuerpo las fichas NUEVO de P226: no mueven la nota, completan los capítulos.

**Avance del libro:** 2 de 2 hallazgos resueltos (100 %) y una precisión aplicada; compila sin errores ni referencias indefinidas, 1.015 páginas. **Avance de la investigación:** sin cambios de estado. La **tercera tesis** (la pérdida de competencia municipal) gana evidencia sin cambiar de estado: en 2025 y 2026 la Provincia sigue conviniendo con las dos municipalidades obra por obra ---el hospital, el azud de Campo Alegre y el encauzamiento con La Caldera; la red de la zona alta, calles y una plaza con Vaqueros---, rescinde tres convenios con Vaqueros y uno con La Caldera, y los dos actos sobre la red de Vaqueros no dan la misma causa de la rescisión. La **cuarta tesis** (la desidia es selectiva) suma un contraste: el nexo de agua de Villa Sara, en Vaqueros, se licita a empresas por seiscientos setenta y siete millones, y el encauzamiento del río en La Caldera se conviene con su Municipalidad por cuarenta y dos millones y veinte días.

**Calidad de la auditoría.** Cobertura de la ronda: 23 líneas (0,09 %; 11,6 páginas). Cobertura acumulada: 25.523 de 25.523 (100,0 %), con el registro de arriba. Falsos positivos descartados: 2. Recortes: las cifras de las filas de 2025 y 2026 que no van entre comillas se cotejaron contra el TEXTO de los informes y la capa, y sólo las de la tabla contra el renglón del PDF; la muestra de trazabilidad no se rehízo. Errores introducidos por la propia auditoría: 2, en el AMPLÍA que la misma sesión escribió; atrapados por un control automático antes de llegar al libro: 0.

## Ronda 80 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1938-1940. Base: commit `3c57fb1` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1938-1940, sobre `144f844`, la ronda 79 registrada; aplicado por `3-registrar` a las 11:19 del 07/10), con la fase 6 en `ronda-80.patch` (un commit sobre `3c57fb1`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los informes LEE 1938, 1939 y 1940: se audita trabajo propio, y cada cita y cifra nueva se volvió a buscar en la capa de la edición y, en las citas, en la imagen.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 79 (25.523 de 25.523, sobre `144f844`) se trasladaron por diff a `3c57fb1`. **El AMPLÍA 1938-1940 caduca 47 líneas y deja 48 nuevas o modificadas** (1 neta, en A), en 10 archivos. Vigentes después del traslado: 25.476 de 25.524.

### Lectura sobre el texto (numeración de `3c57fb1`)

Se leyeron **las 48 líneas, enteras, por la sesión** (11.477 bytes), contra los informes `BO-Salta-1938_1722-1773_la-caldera_LEE-1938_2026-10-07.txt`, `BO-Salta-1939_1774-1825_la-caldera_LEE-1939_2026-10-07.txt` y `BO-Salta-1940_1826-1877_la-caldera_LEE-1940_2026-10-07.txt` y, en las citas, contra la imagen.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 5 |
| ape/F-fuentes.tex | 1 |
| ape/H-dominio.tex | 1 |
| cap/04-siglo.tex | 25 |
| cap/15-hacienda.tex | 6 |
| cap/16-redes.tex | 1 |
| cap/17-tierrafiscal.tex | 1 |
| cap/20-opacidad.tex | 2 |
| cap/22-infraestructura.tex | 2 |
| cap/26-presencia.tex | 4 |

Contexto releído entero (no suma cobertura): 04:3009–3330 (1937 a 1940), 04:3590–3606, 04:460–470 y 04:715–720 (el decreto 1.660 de 1918), 15:15–60, 15:198–246, 20:720–730, 26:25–50, 22:555–562, A:185–210.

**Esta ronda: 48 líneas nuevas**, 11.477 bytes sobre 3.349.684, que en las 1.017 páginas de la base equivalen a **3,5 páginas**.

Acumulado: 25.476 vigentes + 48 = **25.524 de 25.524 (100,0 %)**. La fase 6 toca cinco líneas de 04 (3020, 3021, 3099, 3186, 3187) y una de 15 (244); las de 04:3020, 3021 y 3187 estaban vigentes y se releyeron al modificarlas; no cambia el largo de ningún archivo: **25.524 de 25.524 (100,0 %)** después de ella.

### Cotejo sobre el facsímil

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 1724 | 19 | Decreto 1502, defensa de La Calderilla | «márgen izquierda del Rio Caldera», «las aguas del Río Caldera amenazan las propiedades con eminente peligro», mirado a 150 ppp. El libro escribía «margen», «río» y, en la base, «inminente»: el AMPLÍA corrigió «eminente» y la fase 6 las otras tres grafías. Hallazgo 2 |
| 1750 | 12 | Decreto 2155, balance de 1937 | 510,42; 2.835,10; 2.957,14; 372,38. Coinciden |
| 1763 | 6 | Decreto 3161 | 283,51. Coincide |
| 1875 | 21 | Acta de Vialidad, transferencia de caminos | «De La Calderilla a Río Saladillo por Gallinato y Campo Santo»; «por El Jardín». El libro escribía «de la Calderilla a río» y «por el Jardín». Hallazgo 2 |
| 1808 | 8 | Decreto 3918 | «por así reclamarlo los intereses de su población». Literal |
| 1780 | 8 / 1850 | 2 | Decretos 3456 y 90 | San Alejo (08/02/1939) y «GALLINATO» (17/05/1940). Coinciden con la corrección del AMPLÍA |
| 1828 | 21 | Decreto 3351 | Confirma el 2805. Coincide |
| 1810 | 19 | Boletas incineradas | Once cifras y el total 11.108,80. Coinciden |

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | 04:3099 | Los decretos de 1938 sobre el balance de 1937 eran «los primeros que dejan ver su número»: el decreto 1.660 de 1918 ya calcula la renta real del municipio (04:468, 15:40) | 5 | «los primeros desde 1922 que dejan ver su número» |
| 2 | 04:3020-3021, 04:3186-3187 | Cuatro grafías del original normalizadas dentro de citas: «margen», «río», «de la Calderilla a río», «por el Jardín» | 4 | «márgen», «Rio», «Río», «De La Calderilla a Río», «por El Jardín» |

**Precisión aplicada sin restar.** 15:244: «sólo dos con cifras» contaba decretos dentro de una serie que cuenta actos; pasa a «sólo uno con cifras: la rendición de 1937, que el Decreto 2155/1938 devuelve ... y el 3161/1938 aprueba».

Resta: un superlativo sin universo en el aspecto 5 (hallazgo 1): escala general, **90**. Cuatro grafías en el aspecto 4: −3 cada una, bajo el techo de 90 por cotejo parcial. Ningún error de consistencia en las 3,5 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los dos, en el AMPLÍA 1938-1940 (`3c57fb1`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró la búsqueda de superlativos sobre el texto agregado; el 2, el cotejo de las citas contra la imagen.

**Descartados (falsos positivos, 2).** «la única mina del departamento» (F): con su universo, el padrón minero de 1939 y 1940. «Y resolvió a su favor» (04:3172): el Decreto 2805 funda la denegatoria en la ordenanza de 1914.

**Pendientes revisados.** P228 y P229, abiertos por el AMPLÍA, siguen abiertos. P225 sin cambios.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.523/25.523 vigentes en `144f844` | 25.476 vigentes; 47 caducas |
| Citas entre comillas en las líneas nuevas contra la imagen | 6 cadenas | 2/6 literales; 4 con grafía normalizada (hallazgo 2) |
| Superlativos, cierres y ausencias en el texto agregado | 48 líneas; 6 coincidencias, todas leídas | Una sin universo (hallazgo 1); «única mina» y «único balance con sus renglones» con su universo |
| Repaso de ventana: líneas del índice del AMPLÍA con 1938, 1939 o 1940 | 217 de 217 | Las que caían las corrigió el AMPLÍA |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos | 0 |
| Aritmética | 4 cuentas | 510,42 + 2.835,10 − 2.957,14 = 388,38 (el decreto da 372,38); 10 % de 2.835,10 = 283,51; boletas: 11.078,80 contra 11.108,80; 11/07 a 10/10 = tres meses. Cierran |
| Privacidad: personas nombradas en las 48 líneas | 48/48 | 0 caídas. Nombrados: candidatos, funcionarios y el presidente de un partido que nombra un acto; sin nombre: encargadas del Registro Civil |
| Largo de los archivos antes y después de la fase 6 | 38/38 | ninguno cambia |
| Compilación | base `3c57fb1` y fase 6 | Compilan; 1.017 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con edición y hoja; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas y números de decreto cotejados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgo 2 (−3 cada grafía, bajo el techo de 90), aplicado |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgo 1, aplicado |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Las discrepancias del original (saldo de 1937, boletas) quedan señaladas |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 3,5 páginas; el AMPLÍA corrigió una inconsistencia previa (Mamani, A:204 contra 04:3242) |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin `\pendiente{}` nuevos |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado |
| 11 | Aporte y originalidad | 5 | 90 | 90 | La serie de saldos de Tesorería 1937-1940 sin corte queda en F |
| 12 | Estructura y prosa | 2 | 100 | 100 | Sin remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin cambios |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas |

**Nota inicial: 87,1 antes del tope y 87,1 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 79.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) correr en el AMPLÍA, antes de entregar, el cotejo letra por letra de las citas contra la imagen, también en las líneas vecinas de una cita que se toca, y la búsqueda de superlativos contra las series del propio capítulo: habrían atrapado los dos hallazgos (+1,2 en la nota inicial); (5) llevar al cuerpo las fichas de P228.

**Avance del libro:** 2 de 2 hallazgos resueltos y una precisión; compila sin errores, 1.017 páginas. **Avance de la investigación:** la **tercera tesis** gana un dato: el único resumen de caja del municipio publicado entre 1922 y 1945 (Decreto 2155/1938) da ingresos propios de \$2.835,10 contra \$2.957,14 de egresos, y el saldo de traspaso que el mismo acto declara no cierra con sus cifras. La **opacidad** (cap. 20) se matiza sin caer: la práctica de no publicar cifras tuvo una excepción en 1938.

**Calidad de la auditoría.** Cobertura de la ronda: 48 líneas (0,19 %; 3,5 páginas). Cobertura acumulada: 25.524 de 25.524 (100,0 %). Falsos positivos descartados: 2. Errores introducidos por la propia auditoría: 2, en el AMPLÍA de la misma sesión; atrapados por un control automático: 0.

## Ronda 81 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1941-1943. Base: commit `942f865` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1941-1943, sobre `306a6eb`, la ronda 80 registrada; aplicado por `3-registrar` a las 12:49 del 07/10), con la fase 6 en `ronda-81.patch` (un commit sobre `942f865`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los informes LEE 1941, 1942 y 1943: se audita trabajo propio, y cada cita y cifra nueva se volvió a buscar en la capa de la edición y, en las citas, en la imagen.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 80 (25.524 de 25.524, sobre `306a6eb`) se trasladaron por diff a `942f865`. **El AMPLÍA 1941-1943 caduca 32 líneas y deja 38 nuevas o modificadas** (6 netas: 1 en A, −1 en F, 6 en 04), en 6 archivos. Vigentes después del traslado: 25.492 de 25.530.

### Lectura sobre el texto (numeración de `942f865`)

Se leyeron **las 38 líneas, enteras, por la sesión** (23.918 bytes), contra los informes `BO-Salta-1941_1878-1929_la-caldera_LEE-1941_2026-10-07.txt`, `BO-Salta-1942_1930-1982_la-caldera_LEE-1942_2026-10-07.txt` y `BO-Salta-1943_1983-2035_la-caldera_LEE-1943_2026-10-07.txt` y, en las citas, contra la imagen.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 5 |
| ape/D-pedidos.tex | 2 |
| ape/F-fuentes.tex | 5 |
| cap/00-advertencia.tex | 1 |
| cap/02-metodo.tex | 1 |
| cap/04-siglo.tex | 24 |

Contexto releído entero (no suma cobertura): 04:3278–3420 (1941 a 1943), 04:3536–3556 (las escuelas de 1945), 04:1716–1760 (la mina), 04:4436–4446, A:205–235, F:36–60, D:200–210, 00:45.

**Esta ronda: 38 líneas nuevas**, 23.918 bytes sobre 3.354.900, que en las 1.021 páginas de la base equivalen a **7,3 páginas**.

Acumulado: 25.492 vigentes + 38 = **25.530 de 25.530 (100,0 %)**. La fase 6 toca una línea de 04 (3553) y una de A (214), las dos nuevas de esta ronda; no cambia el largo de ningún archivo: **25.530 de 25.530 (100,0 %)** después de ella.

### Cotejo sobre el facsímil

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 1880 | 8 | Decreto 4368 | «donación o venta de los terrenos necesarios para la ejecución de las mejoras del camino Calderilla a Río de las Pavas, tramo Desmonte-Campo Santo»; 634,64 m²; «imprescindible». Literal |
| 1889 | 18 | Acta 391, prórroga | «aún en trámite». Literal |
| 1964 | 22 | Decreto 6262-H | «a partir del año 1749 hasta la fecha se ha hecho en forma continua y sin interrupción». Literal |
| 1974 | 7 | Decreto 4673-G | «ha sufrido una sensible despoblación». Literal; el decreto concede aquiescencia al Consejo Nacional para trasladar la escuela. Hallazgo 1 |
| 1958 | 20 | Decreto 4091-G | «destacado en comisión para atender la vigilancia de «La Calderilla»». El libro citaba sin las comillas interiores. Hallazgo 2 |
| 2020 / 2021 / 2034 | 6-7 / 13-14 / 11 | Decretos 526-G, 581-G y 1469-G | Fechas, números y orden: renuncia aceptada el 10/09, sucesor el 21/09, reconocimiento de nueve días el 13/12. Coinciden con la corrección del AMPLÍA |
| 1940 / 2026 | 27 / 36 | Precios de La Caldera | Carne común \$0,55 (1942) y \$0,60 (1943). Coinciden |
| 1932 | 1 | Aviso del Release | «ESTE NÚMERO DE BOLETÍN NO FUE PUBLICADO». Coincide |
| 2030 | todas | Edición 2.030 | 31 hojas, leída en el informe de 1943; no trae el acto de la intervención. Coincide |

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | 04:3553, A:214 | El decreto 4673-G de 1942 «la trasladó» de San Alejo a Wierna / la escuela «pasa» de San Alejo a Wierna: el decreto concede la aquiescencia al Consejo Nacional de Educación para el traslado, que no se publica (la llegada a Wierna la prueba el acto de 1945) | 5 | «dio la aquiescencia para llevarla de San Alejo a Wierna»; «la Provincia da la aquiescencia para que la escuela nacional Nº 250 pase de San Alejo a Wierna» |
| 2 | A:214 | La cita de la vigilancia de 1942 omitía las comillas del original alrededor de «La Calderilla» | 4 | «destacado en comisión para atender la vigilancia de “La Calderilla”» |

Resta: un hecho afirmado más allá del acto en el aspecto 5 (hallazgo 1): escala general, **90**. Una grafía en el aspecto 4: −3, bajo el techo de 90 por cotejo parcial. Ningún error de consistencia en las 7,3 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los dos, en el AMPLÍA 1941-1943 (`942f865`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró la relectura del verbo de cada acto contra el informe; el 2, el cotejo de las citas contra la imagen.

**Descartados (falsos positivos, 3).** «Y por primera vez el Estado expropia tierra en el departamento para hacer un camino» (04:3317) y sus ecos en A y D: el universo está dado en la frase siguiente («Hasta 1940 los caminos del departamento aparecen como jornales, ripio y certificados de obra»), con los años 1908-1940 leídos por imagen. «tres años después» (04:3553): 1942 a 1945. «1.492 leídos, de 1.502 ediciones publicadas» (F): 1.503 números del 962 al 2.464, uno no publicado, diez sin leer.

**Pendientes revisados.** P19, cerrado por el AMPLÍA (la 2.030 se leyó). P230, P231 y P232, abiertos por el AMPLÍA, siguen abiertos; P230 (la identidad del presidente municipal y el comisario de 1942-1943, que el capítulo 4 afirma y los actos no dicen) queda para una ronda que lo resuelva con documento o lo baje a homónimo declarado.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.524/25.524 vigentes en `306a6eb` | 25.492 vigentes; 32 caducas |
| Citas entre comillas en las líneas nuevas contra la imagen | 9 cadenas | 8/9 literales; 1 sin las comillas interiores (hallazgo 2) |
| Superlativos, cierres y ausencias en el texto agregado | 38 líneas; 5 coincidencias, todas leídas | Las tres «primera vez» del camino de 1941 con su universo; ninguna sin universo |
| Repaso de ventana: líneas del índice del AMPLÍA con 1941, 1942 o 1943 | 162 de 162 | Las que caían las corrigió el AMPLÍA; P230 queda abierto |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos | 0 |
| Aritmética | 4 cuentas | 1.503 − 1 − 10 = 1.492; 1942 a 1945, tres años; 10/09 a 21/09; cuatro cambios de titular en Vaqueros (marzo de 1942 a diciembre de 1943). Cierran |
| Privacidad: personas nombradas en las 38 líneas | 38/38 | 0 caídas. Nombrados: funcionarios (comisarios, jueces de paz, presidente municipal); sin nombre: el propietario expropiado, las encargadas del Registro Civil, la receptora y la expendedora, la causante del sucesorio |
| Largo de los archivos antes y después de la fase 6 | 38/38 | ninguno cambia |
| Compilación | base `942f865` y fase 6 | Compilan; 1.021 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con edición y hoja; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | Fechas y números de decreto cotejados; el AMPLÍA corrigió la fecha del decreto 520-H y el orden de la renuncia de 1943 |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgo 2 (−3, bajo el techo de 90), aplicado |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgo 1, aplicado |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | La compra de 1941 pasa a expropiación según el acto |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 7,3 páginas; el AMPLÍA alineó la cobertura (2.030 y 1.932) en la advertencia, el método y los apéndices D y F |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin `\pendiente{}` nuevos |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | Sin cambios de estado; P230 abierto |
| 11 | Aporte y originalidad | 5 | 90 | 90 | La escuela Nº 250 entre San Alejo y Wierna, de 1942 a 1945 |
| 12 | Estructura y prosa | 2 | 100 | 100 | Sin remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas; el epígrafe del método describe la cruz de la 2.030 como estado de la lámina |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin cambios |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas |

**Nota inicial: 87,1 antes del tope y 87,1 después** (tope de 90 por la cobertura acumulada inicial del 99,9 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 80.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) en el AMPLÍA, releer el verbo de cada acto contra el informe (aquiescencia, autorización, pedido) antes de escribir que algo se hizo: habría atrapado el hallazgo 1 (+1,2 en la nota inicial); (5) resolver P230.

**Avance del libro:** 2 de 2 hallazgos resueltos; compila sin errores, 1.021 páginas. **Avance de la investigación:** el departamento gana un dato de población: la escuela Nº 250 se lleva de San Alejo a Wierna en 1942 por la despoblación de San Alejo, y de Wierna a Yacones en 1945 por la de Wierna, cuando San Alejo ya tiene cincuenta y un chicos en edad escolar. Y la relación entre camino y dominio se precisa: la tierra del camino de 1941 no se compró sino que se expropió, después de fracasar la donación o venta.

**Calidad de la auditoría.** Cobertura de la ronda: 38 líneas (0,15 %; 7,3 páginas). Cobertura acumulada: 25.530 de 25.530 (100,0 %). Falsos positivos descartados: 3. Errores introducidos por la propia auditoría: 2, en el AMPLÍA de la misma sesión; atrapados por un control automático: 0.

## Ronda 82 — auditoría con fase 6 (07/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1944-1945. Base: commit `046c890` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1944-1945, sobre `cac3842`, la ronda 81 registrada; aplicado por `3-registrar` a las 14:34 del 07/10), con la fase 6 en `ronda-82.patch` (un commit sobre `046c890`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los informes LEE 1944 y 1945: se audita trabajo propio, y cada cita y cifra nueva se volvió a buscar en la capa de la edición y, en las citas y las cifras del revalúo, en la imagen.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 81 (25.530 de 25.530, sobre `cac3842`) se trasladaron por diff a `046c890`. **El AMPLÍA 1944-1945 caduca 59 líneas y deja 74 nuevas o modificadas** (15 netas: 1 en A, 5 en 03, 6 en 04, 1 en 09, 1 en 20, 1 en 26), en 13 archivos. Vigentes después del traslado: 25.471 de 25.545.

### Lectura sobre el texto (numeración de `046c890`)

Se leyeron **las 74 líneas, enteras, por la sesión** (67.028 bytes; varias son párrafos de una sola línea en los apéndices A, D, E, F y H), contra los informes `BO-Salta-1944_2036-2183_la-caldera_LEE-1944_2026-10-07.txt` y `BO-Salta-1945_2184-2464_la-caldera_LEE-1945_2026-10-07.txt` y, en las citas y las cifras, contra la imagen.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 7 |
| ape/D-pedidos.tex | 3 |
| ape/E-personas.tex | 2 |
| ape/F-fuentes.tex | 4 |
| ape/H-dominio.tex | 1 |
| cap/03-fincas.tex | 21 |
| cap/04-siglo.tex | 22 |
| cap/09-defensas.tex | 2 |
| cap/10-expropiacion.tex | 1 |
| cap/14-poblacion.tex | 2 |
| cap/20-opacidad.tex | 3 |
| cap/22-prospectiva.tex | 1 |
| cap/26-presencia.tex | 5 |

Contexto releído entero (no suma cobertura): 03:870–1000 (el padrón de 1944), 03:645–760 (Chalchanio y Las Lagunas), 04:3380–3400, 04:3430–3560 y 04:3596–3620, 09:359–460, 20:745–766, 26:40–80, A:236–254, D:200–205.

**Esta ronda: 74 líneas nuevas**, 67.028 bytes sobre 3.360.475, que en las 1.021 páginas de la base equivalen a **20,4 páginas**.

Acumulado: 25.471 vigentes + 74 = **25.545 de 25.545 (100,0 %)**. La fase 6 toca seis líneas nuevas de esta ronda (03:928–929, 04:3516, A:244, A:252, F:56) y no cambia el largo de ningún archivo: **25.545 de 25.545 (100,0 %)** después de ella.

### Cotejo sobre el facsímil

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 2166 | 6–7 | Sección «Departamento de LA CALDERA» del revalúo | 72 partidas, de la 1 a la 184; tres sin valuación (36, 44, 45). Suma de la columna izquierda de la h6, a 170 ppp: \$322.600; la de las otras 47, \$353.100, la misma que el libro daba: total \$675.700. Control aritmético cerrado |
| 2166 | 34 | «Caldera, Dominga M. de» | En la sección que abre «Departamento de CERRILLOS» en la h27; no en la del departamento |
| 2313 | 13 | Remate de «Chalchanio» | «el día 27 de Julio de 1945 a horas 16». Literal |
| 2202 | 6 | Límites de «Las Lagunas» | «serranías de La Caldera hasta dar con el Río de Los Yacones, enfrentando con el arroyo de "Las Carretas"». Literal |
| 2402 | 5 | Decreto 9053 G | Art. 2°: renuncia de Augusto Regis al cargo de Interventor de la Comuna de La Caldera; designa a Francisco Mercado. Literal |
| 2043 | 37 | Decreto 2097-G | «ocho (8) días del mes de setiembre de 1943». Literal |
| 2411 | 4 | Decretos 9155 y 9156 G | 42 niños en San Francisco (Yacones), 51 en San Alejo; aquiescencia a pedido del Inspector Técnico Seccional. Literal |
| 2418 | 3 | Decreto 9264-H | Encabezado y «a la misma no se ha presentado ningún proponente». Literal; la frase «para ejecutar por vía administrativa las obras de defensa en el río de La Caldera» es del 9401-H (2429 h5). Hallazgo 1 |
| 2237 | 8 | Decreto 6428-H | \$557,38: el 10 % de \$5.573,80 (5.018,02 + 555,78). Control aritmético cerrado |
| 2101 | 4 | Decreto 4576 G | «EDUARDO JOSE PORCEL»; los actos de 1945 dicen «JOSE EDUARDO». Hallazgo 5 |

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | 04:3516 | Al agregarle la edición del 9264-H (Nº 2418, h. 3), la cita «para ejecutar por vía administrativa…» quedaba atribuida a ese decreto, y es del 9401-H, que lo resume | 4 | «el 9264-H (Nº 2418, h. 3) autoriza a la Dirección, en palabras del 9401-H, «para ejecutar…»» |
| 2 | 03:928–929 | Urquiza, ahora segundo del padrón: «su posición patrimonial no se movió», que suponía que antes era el primero | 5 | «conserva la segunda valuación del padrón» |
| 3 | F:56 | «casi todas con el pie de imprenta en la página anterior», dicho de las 44 ediciones de 1944 y las 90 de 1945; el pie se cotejó sólo en 1945 | 5 | «en 82 de éstas la página anterior cierra con el pie de imprenta» |
| 4 | A:244 | «y para una escuela de la Ley 4874» | 12 | «y para crear una escuela de la Ley 4874» |
| 5 | A:252 | «José Eduardo Porcel» para el nombramiento de 1944, que dice «Eduardo José» | 4 | «Eduardo José Porcel ---«José Eduardo» en los actos de 1945---» |

Resta: dos afirmaciones más allá del dato en el aspecto 5 (hallazgos 2 y 3): escala general, **90**. Dos en el aspecto 4, bajo el techo de 90 por cotejo parcial. Una en el aspecto 12: 95. Ningún error de consistencia en las 20,4 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los cinco, en el AMPLÍA 1944-1945 (`046c890`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró el cotejo de la cita contra la hoja del decreto recién ubicado; el 2, la relectura del párrafo entero después de cambiar su primera frase; el 3, la comparación con lo que el informe LEE de 1944 declaró; el 4, la lectura; el 5, el cotejo de la imagen de 1944.

**Corrección de fondo que hizo el AMPLÍA y esta ronda confirma.** El padrón de 1944 del capítulo 3 tenía 47 partidas y \$353.100 porque la lectura anterior no tomó la columna izquierda de la h6 (partidas 1 a 55): son 72 y \$675.700, y la mayor no es la de Urquiza sino la 10, de un titular particular que el libro no nombra, con \$237.400. Caen con eso el superlativo de Urquiza («el mayor propietario»), sus porcentajes y los de los apellidos de la elite (de casi el diez al cinco por ciento), el rango de la partida 80 en el capítulo 10 (de tercera a cuarta) y la frase de 22-prospectiva. La ronda volvió a sumar las dos columnas sobre la imagen: cierran con el total.

**Descartados (falsos positivos, 3).** «Las dieciocho de \$6.400 o más» (03:887): son exactamente dieciocho (la siguiente es de \$6.300). «Son los primeros datos de población de parajes del departamento que el archivo temprano publica» (04:3553): el universo es el archivo temprano leído, 1908-1945, y el antecedente de 1942 dice «sensible despoblación» sin cifra. «En dos años seguidos» (20:766): la refacción es de 1944 y su último acto de marzo de 1945; la defensa, de 1945.

**Pendientes revisados.** P50, cerrado por el AMPLÍA (el 9264-H está en el Nº 2418, h. 3). P233 (desfase de páginas de 1944 en el informe LEE), P234 (saldo de enero y febrero de 1945, dígito 3/8) y P235 (el Regis interventor de 1945 se suma al pendiente P230) siguen abiertos. P230 sigue abierto: el capítulo 4 y el apéndice E identifican al presidente municipal y al comisario de 1942-1943; esta ronda no agrega identidad y el interventor de 1945 se escribió sin unirlo.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.530/25.530 vigentes en `cac3842` | 25.471 vigentes; 59 caducas |
| Citas entre comillas en las líneas nuevas contra la imagen | 11 cadenas | 10/11 literales; 1 atribuida al decreto equivocado (hallazgo 1) |
| Superlativos, cierres y ausencias en el texto agregado | 74 líneas; 9 coincidencias nuevas, todas leídas | Todas con universo; las tres del padrón, recalculadas |
| Repaso de ventana: líneas del índice del AMPLÍA con 1944 o 1945 | 209 de 209 | Las que caían las corrigió el AMPLÍA; «el mismo año» de 20:766, corregido por el AMPLÍA |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos | 0 |
| Aritmética | 7 cuentas | 322.600 + 353.100 = 675.700; 237.400/675.700 = 35,1 %; 52.400/675.700 = 7,8 %; 26.400/675.700 = 3,9 %; 33.700/675.700 = 5,0 %; (5.018,02 + 555,78) × 0,10 = 557,38; 207,30 + 24,80 = 232,10. Cierran |
| Privacidad: personas nombradas en las 74 líneas | 74/74 | 0 caídas. Las tres partidas nuevas de particulares del cuadro van sin nombre; nombrados sólo funcionarios (interventores, comisarios, subcomisarios, jueces de paz) y los titulares que el libro ya nombraba |
| Largo de los archivos antes y después de la fase 6 | 4 archivos | ninguno cambia |
| Compilación | base `046c890` y fase 6 | Compilan; 1.021 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con edición y hoja; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 100 | 100 | El AMPLÍA corrigió la fecha del remate de Chalchanio (27, no 30 de julio) y el recuento de Las Lagunas (31 ediciones, no 23) |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | Hallazgos 1 y 5, bajo el techo de 90, aplicados; el AMPLÍA corrigió la cita de Las Lagunas («Las Carretas», no «las carreras») |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgos 2 y 3, aplicados |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin cambios |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 20,4 páginas; el padrón de 1944 queda igual en los caps. 3, 4, 10, 14 y 22-prospectiva y en los apéndices A, D y E |
| 8 | Integridad del aparato | 8 | 95 | 95 | Sin `\pendiente{}` nuevos |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | La quinta lectura del padrón (concentración) se sostiene con más fuerza: una partida tiene más de un tercio del valor |
| 11 | Aporte y originalidad | 5 | 90 | 90 | El interventor de la comuna de 1944-1945 con nombre |
| 12 | Estructura y prosa | 2 | 95 | 100 | Hallazgo 4, aplicado |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin cambios |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas |

**Nota inicial: 87,0 antes del tope y 87,0 después** (tope de 90 por la cobertura acumulada inicial del 99,7 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 81.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) en el AMPLÍA, al agregar la edición de un acto a una cita, verificar que la cita sea de ese acto y no del que lo resume: habría atrapado el hallazgo 1; (5) resolver P230, que ahora tiene un tercer cargo.

**Avance del libro:** 5 de 5 hallazgos resueltos; compila sin errores, 1.021 páginas. **Avance de la investigación:** la **tercera tesis** se refuerza: el padrón de 1944 no reparte el departamento entre «menos de cincuenta titulares», sino en setenta y dos partidas de las que una sola vale más de un tercio. La **segunda** gana un dato de población: cuarenta y dos chicos en San Francisco de los Yacones en 1945, junto a los cincuenta y uno de San Alejo. Y la intervención municipal de 1943-1946 tiene ahora su interventor hasta octubre de 1945.

**Calidad de la auditoría.** Cobertura de la ronda: 74 líneas (0,29 %; 20,4 páginas). Cobertura acumulada: 25.545 de 25.545 (100,0 %). Falsos positivos descartados: 3. Errores introducidos por la propia auditoría: 5, en el AMPLÍA de la misma sesión; atrapados por un control automático: 0.

## Ronda 83 — lecturas de Eduardo, dudas 1944-1945 (07/10/2026)

Tipo: **lecturas** (flujo v2 §5.6, palabra clave `LECTURAS`), sobre la hoja `dudas-1944-1945.html` (cuatro casos, recortes a 250 ppp de la imagen del Release con el renglón marcado; nombres de particulares tapados). Base del libro: `e75765f` (ronda 82). No hay fase 6: ninguna lectura cambia una frase del libro.

### Lecturas y su clasificación

| Caso | Edición y hoja | Pregunta | Lectura de la sesión | Lectura de Eduardo | Control | Clasificación |
|---|---|---|---|---|---|---|
| 1 | 2227 h16 | Saldo final de enero de 1945 | 19.393,06 | 19.393,06 | Ninguno decide (la serie da 19.398,06 en el caso 2) | **Decidida por Eduardo** |
| 2 | 2253 h12 | Saldo inicial de febrero de 1945 | 19.398,06 | 19.398,06 | Ninguno decide | **Decidida por Eduardo** |
| 3 | 2166 h6 | Valuación de la partida 10 del revalúo de 1944 | 237.400 | 237.400 | Parcial: la columna suma 322.600 y cierra con el total de 675.700 | **Decidida por control y confirmada** |
| 4 | 2166 h6 | Partidas 42, 43 y 47 | 14.200 / 11.200 / 9.300 | 14.200 / 11.200 / 9.300 | Parcial: la misma suma | **Decidida por control y confirmada** |

**Consecuencia de los casos 1 y 2.** Las dos lecturas coinciden con las de la sesión, y son distintas entre sí: la diferencia de \$ 5 entre el saldo final de enero y el inicial de febrero de 1945 **está en el original**, no en la lectura. La cadena de Tesorería de los informes LEE corre de enero de 1937 a noviembre de 1945 con ese único desfase, que se registra como contradicción del original (informe LEE 1945, E.9). Cierra P234.

**Consecuencia de los casos 3 y 4.** Las cifras que el AMPLÍA 1944-1945 llevó al capítulo 3 y al apéndice A (partida 10, \$237.400; Fisco \$14.200; Gobierno de la Provincia \$11.200; partida 47, \$9.300) quedan confirmadas sobre la imagen por un segundo lector. El libro no cambia.

### Notas

Sin cambios respecto de la ronda 82: **nota 88,3**, cobertura acumulada **25.545 de 25.545 (100,0 %)**. Lecturas: 4; decididas por control y confirmadas: 2; decididas por Eduardo: 2; corregidas por el control: 0; abiertas: 0.

## Ronda 84 — auditoría con fase 6 (09/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1908, 1990, 1992 y con los tres insumos de `auto/insumos-mejora/` del 9/10/2026 tratados como pendientes ya conocidos (§7.3). Base: commit `510c9dd` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1908, 1990, 1992, sobre `d87fbdc`; aplicado por `3-registrar` a las 19:05 del 09/10), con la fase 6 en `ronda-84.patch` (un commit sobre `510c9dd`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA: se audita trabajo propio, y las citas y cifras nuevas se volvieron a mirar en la imagen de las ediciones del Release.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 83 (25.545 de 25.545, sobre `d87fbdc`) se trasladaron por diff a `510c9dd`. **El AMPLÍA caduca 29 líneas y deja 38 nuevas o modificadas** (9 netas: 7 en A, 2 en F), en 15 archivos. Vigentes después del traslado: 25.516 de 25.554.

### Lectura sobre el texto (numeración de `510c9dd`)

Se leyeron **las 38 líneas, enteras** (137.595 bytes; casi todas son párrafos de una sola línea), contra los informes `BO-Salta-1908_1-22_la-caldera_LEE-1908_2026-10-08.txt`, `BO-Salta-1990_13346-13590_la-caldera_LEE-1990_2026-10-09.txt` y `BO-Salta-1992_13839-14084_la-caldera_LEE-1992_2026-10-09.txt` y, en las citas y las cifras, contra la imagen.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 9 |
| ape/D-pedidos.tex | 1 |
| ape/E-personas.tex | 2 |
| ape/F-fuentes.tex | 10 |
| cap/00-advertencia.tex | 1 |
| cap/01-planteo.tex | 2 |
| cap/02-metodo.tex | 3 |
| cap/04-siglo.tex | 2 |
| cap/05-tierra.tex | 1 |
| cap/15-hacienda.tex | 1 |
| cap/17-aguabaja.tex | 1 |
| cap/17-tierrafiscal.tex | 1 |
| cap/18-politica.tex | 1 |
| cap/20-opacidad.tex | 2 |
| cap/22-infraestructura.tex | 1 |

Contexto releído entero (no suma cobertura): 22:545 (la serie del agua del pueblo, de 1914 a 2021), 17-aguabaja:281, 18:650–680 (la ficha de intendencias), 16:255–262, 23:160–186, D:333–340, A:327, A:733–736.

**Esta ronda: 38 líneas nuevas**, 137.595 bytes sobre 3.378.526, que en las 1.029 páginas de la base equivalen a **41,9 páginas**.

Acumulado: 25.516 vigentes + 38 = **25.554 de 25.554 (100,0 %)**. La fase 6 escribe 22 líneas y quita 16 (A +5, F +2, 23-plan −1, por unión de dos renglones): **25.560 de 25.560 (100,0 %)** después de ella; las 22 se leyeron enteras al escribirlas y al compilar.

### Cotejo sobre el facsímil

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 22 (1908) | 4 | «en el departamento de la Caldera, partido del Potrero de Castillo» | Literal; el libro decía «de La Caldera»: hallazgo 1 del AMPLÍA, ya corregido en `510c9dd` |
| 22 (1908) | 4 | «no son labrados ni cercados»; «Los dueños del terreno son los señores Garzon y Pinto, vecinos de Buenos Aires»; «2ooo hectáreas» | Literales |
| 22 (1908) | 2 (p. 104) | «domiciliado en el Departamento de la Caldera» | Literal |
| 13427 | 8 | Res. 101 D: A 304.722.722 «al mes de agosto de 1989», 270 días, «Licitación Pública Internacional» | Coincide |
| 13460 | 10 | Res. 179-D del 4-6-90: presupuesto actualizado a enero de 1990 | Coincide |
| 13415 | 6 | Aviso: A 799.409.589; apertura 9/5/90 | Coincide |
| 13432 | 8 | Prórroga al 5 de junio de 1990 | Coincide |
| 13554 | 5 | Decreto 2161: 9,40 l/s del 1109/58; desborde de 1978; 1,57 l/s; desde 1986; 15 ha | Coincide |
| 13554 | 8 y 21 | Decreto 2172: contado o 10 % y hasta 24 cuotas; matrícula 1894, A 2.361.077 | Coincide |
| 13558 | 69 y 132 | Concejal de la Municipalidad de La Caldera; «QUIPILDOR HORACIO MARTIN — MUNICIP. LA CALDERA — SEC. CONC. DELIBERANTE» | Coincide |
| 14029 | 10 | Decreto 1342, «Salta, 7 de setiembre de 1992»; Res. 3729/91 y 3668/91 | Coincide |
| 14065 | 7–8 | Decreto 1745: 70 %, CO.F.A.P. y S., cólera; rescisión (cl. 3.ª y 6.ª), contratación directa del 30 % (7.ª), seis meses desde el 3 de agosto (9.ª) | Coincide; el plazo, hallazgo 1 |
| 14046 | 4 | Res. 234-D: \$258.188,20; concurso desierto del 1/7/1992; vía administrativa | Coincide |
| 13839 | 8 | Catastro 2.037, 1,18 l/s; catastros 1.824 a 1.826, 0,63 l/s | Coincide |
| 13572 | 10 | Decreto 2292: La Caldera A 37.817.589, Vaqueros A 45.476.660 | Coincide |
| 5225 (1956) | 5 | Decreto de la obra 343: «DECRETO Nº 387[?]-E, SALTA, Agosto 3 de 1956»; el siguiente de la columna, «DECRETO Nº 3872-E», es de Villa Estela; edición del 16 de agosto; «Servicios de Aguas Corrientes en la Caldera» | El número lo decide la serie (§5.6): **3871-E**, como dice la escritura 7 de 1957. Hallazgo 3. La cita, literal |

19 cotejos; 18 literales o coincidentes y 1 que corrige al libro.

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | 22:545 | «para terminarlo en seis meses», del convenio de noviembre de 1992 | 3 | «en seis meses contados desde el 3 de agosto, tres meses antes del acta» |
| 2 | 15:185 | Las tres planillas de 1990 que no cierran, como si a todas las cerrara una lectura; lista de conceptos incompleta | 5 | Una sin el renglón de La Merced y dos con un renglón dudoso o sin explicar; «haberes, dietas, aguinaldos, diferencias y adicionales» |
| 3 | A:327 | «8 ago. 1956* & Decreto 3872-E» | 3 | «3 ago. 1956* & Decreto 3871-E», con la edición (16/08/1956) y el control que decide el dígito |
| 4 | 22:545 | La usina de 1957, «pagada con un subsidio y un préstamo provinciales» | 5 | «financiada con un subsidio y un préstamo provinciales que no alcanzaban»: el contrato de 1958 suma \$609.595,08 y pone el mayor costo a cargo de la Municipalidad (insumo del Archivo Histórico) |
| 5 | 16:259 | «nadie solicitó que se calculara el Valor de Negocio del proyecto» | 5 | Acotada al 9/10/2026, con la declaración de que el pedido es del autor (insumo Naturgy) |
| 6 | 16:261 | «La segunda consulta, a la distribuidora, sigue pendiente» | 5 | Presentada el 9/10/2026, trámite 45337, sin respuesta al cierre |
| 7 | D:336 | Pedido a Naturgy formulado como pendiente de hacerse | 5 | Lo pendiente es la respuesta al trámite 45337; red cloacal y cobertura, pedidas a Aguas del Norte y al ENRESP |
| 8 | 23:183 | «Pedir el cálculo que nadie pidió para el gas» | 5 | «Que el municipio pida el cálculo del gas», con el pedido individual del autor citado |

Resta: en el aspecto 3, dos casos (1 y 3), 90. En el aspecto 5, una ausencia que caducó (5, frase, −5), dos textos desactualizados (6 y 7, −3 cada uno) y dos afirmaciones más allá del dato (2 y 4): **89**. El 8 es la misma ausencia en la propuesta y no resta aparte. Ningún error de consistencia en las 41,9 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los hallazgos 1 y 2, en el AMPLÍA 1908, 1990, 1992 (`510c9dd`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró el cotejo de la cláusula novena del acta en la imagen; el 2, la relectura de la nota del informe LEE 1990. Los hallazgos 3 a 8 son anteriores a esta sesión: el 3 y el 4 los señaló el insumo del Archivo Histórico y los decidió el cotejo; el 5 al 8 son caducidades por las gestiones del 9/10/2026.

**Incorporaciones de la fase 6 (insumos del 9/10/2026).**
- *Archivo Histórico de Salta* (`2026-10-09_archivo-historico-salta.md`, con su informe de lectura): la elección del 19/9/1915 y la denuncia de policías jujeños (fila nueva de la cronología, sin los nombres de los comisarios); el servicio de agua corriente de 1979, el convenio de enero de 1991, el sistema anunciado para mayo de 1993 y la planta de fluoración de abril de 1994 (22:545 y tres filas nuevas sin asterisco, porque son partes de prensa); plazo y material del convenio de defensas de 1985 (09:642); Mogro intendente en enero de 1991 y Quipildor en abril de 1994 (18 y su ficha); la fecha del 10.241-E (A:264); el contrato de la obra 343 (A:327) y el de la usina (22:545). El apéndice F suma la pieza con sus documentos y aclara que los partes anuncian y no prueban. **No se incorporaron**: la apertura del 20/12/1971 de la licitación D-5/71 (falta cotejar el aviso del Boletín de diciembre de 1971; P245), el pedido de 1975 de la Cámara Regional de la Producción, el acto de posesión de Lizondo de 1970, los demás datos de las escrituras de 1948 y 1949 y las láminas de 1972 (la respuesta del Archivo da la cita y los números de inventario, pero no dice «autorizamos» con todas las letras; P246).
- *Naturgy, trámite 45337* (`2026-10-09_naturgy-tramite-45337.md`): 16:259 y 261, 23:183, D:336, fila del 9/10/2026 y apéndice F.
- *Aguas del Norte y ENRESP* (`2026-10-09_pedidos-agua-cloacas.md`): 23:167, D:333, 336 y 340, la misma fila y el mismo ítem de F. No se citan la Ley 8173 ni el Decreto 35/26: su texto no se verificó. El testimonio del autor sobre su domicilio sin servicio no se usa.

**Descartados (falsos positivos, 2).** «Es el primer año posterior a 1988 que este libro lee de corrido» (fila de 1990): el universo está declarado y es cierto. «Las entradas sin asterisco … posteriores … provienen de cobertura periodística o de partes oficiales» (A:4): las filas nuevas de 1991, 1993 y 1994 son partes oficiales y van sin asterisco, como pide el encabezado.

**Pendientes revisados.** P18 avanza con el AMPLÍA (Figueroa y Chuchuy, 1908) y sigue abierto. P236 a P240, abiertos por el AMPLÍA, siguen abiertos; P238 (obra de agua potable 1990-1992) gana del Archivo el convenio de 1991 y el anuncio de 1993, y sigue abierto porque falta el acto de adjudicación y la recepción. Nuevos: P241 a P246.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.545/25.545 vigentes en `d87fbdc` | 25.516 vigentes; 29 caducas |
| Citas entre comillas en las líneas nuevas del AMPLÍA contra la imagen | 6 cadenas | 6/6 literales |
| Cifras de las líneas nuevas contra la imagen | 31 cifras en 15 ediciones | 31/31 |
| Superlativos y ausencias en el texto agregado por el AMPLÍA y la fase 6 | 60 líneas; 7 coincidencias | Todas con universo; «ningún documento lo dice» se acotó a «ninguno de estos documentos» antes de compilar |
| Menciones de cobertura (1989--2012, «noventa y seis», «cincuenta y cuatro») | 25.560/25.560 | Todas actualizadas por el AMPLÍA; el control encontró dos más (01:157 y 20:881) que el AMPLÍA ya había corregido |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos | 0 en capítulos; los del apéndice A remiten hacia atrás |
| Privacidad: personas nombradas en las líneas nuevas | 60/60 | 0 caídas. Nombrados: funcionarios (gobernadores, intendentes, secretario del Concejo, ministros), una empresa contratista y personas de 1915. Sin nombre: el concejal de 1990, los adjudicatarios de 1990, los particulares de los avisos de agua y del remate de 1992, los comisarios jujeños de 1915 |
| Compilación | base `510c9dd` y fase 6 | Compilan; 1.029 y 1.031 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |
| `git am` del parche sobre un clon limpio de `510c9dd` | 1 parche | Aplica |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con edición y hoja, o con pieza y página del Archivo; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 90 | 100 | Hallazgos 1 y 3, aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 19 cotejos sobre 15 ediciones, bajo el techo de 90 |
| 5 | Honestidad epistémica | 12 | 89 | 100 | Hallazgos 2 y 4 a 8, aplicados |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Los partes van marcados como prensa oficial; la discrepancia «S.R.L.»/«S.A.» de Lucardi, señalada |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 41,9 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Pedidos actualizados; ninguno satisfecho sigue en la lista |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | La serie del agua del pueblo gana tres puntos con fecha en el tramo 1989-2012, todos provinciales |
| 11 | Aporte y originalidad | 5 | 90 | 90 | La obra de agua potable de 1990-1993 reconstruida con dos fuentes |
| 12 | Estructura y prosa | 2 | 100 | 100 | Sin remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | La propuesta del gas queda con su destinatario |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas |

**Nota inicial: 86,4 antes del tope y 86,4 después** (tope de 90 por la cobertura acumulada inicial del 99,9 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 82.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) en el AMPLÍA, copiar los plazos con su fecha de inicio y describir los cuadros que no cierran por su causa: habría evitado los hallazgos 1 y 2; (5) cotejar el aviso de diciembre de 1971 (P245) y obtener la autorización expresa de las láminas de 1972 (P246).

**Avance del libro:** 8 de 8 hallazgos resueltos; compila sin errores, 1.031 páginas. **Avance de la investigación:** la **segunda tesis** gana el tramo 1989-1994 de la serie del agua del pueblo: licitación de 1990, convenio de 1991 con un diez por ciento a cargo de la comunidad, litigio y rescisión de 1992 y sistema anunciado para 1993, todo de la Provincia, sin el municipio como parte en los actos. La **tercera** gana un hueco cubierto en parte: dos intendentes con fecha oficial en el tramo 1987-1999. Ninguna cambia de estado.

**Calidad de la auditoría.** Cobertura de la ronda: 38 líneas (0,15 %; 41,9 páginas). Cobertura acumulada: 25.560 de 25.560 (100,0 %). Falsos positivos descartados: 2. Errores introducidos por la propia auditoría: 2, en el AMPLÍA de la misma sesión; atrapados por un control automático: 0 (y 1 superlativo atrapado por el control antes de compilar, en el texto de la fase 6).

## Ronda 85 — auditoría con fase 6 (10/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1989, 1991, 1994. En `auto/insumos-mejora/` no hay insumos nuevos (los del 9/10/2026 ya están en `usados/`). Base: commit `67d4668` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1989, 1991, 1994, sobre `d0f1dcf`; aplicado por `3-registrar` a las 09:20 del 10/10), con la fase 6 en `ronda-85.patch` (un commit sobre `67d4668`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA: se audita trabajo propio, y las citas y cifras nuevas se volvieron a mirar en la imagen de las ediciones del Release, que esta vez se alcanzó desde la nube por descarga directa.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 84 (25.560 de 25.560, sobre `d0f1dcf`) se trasladaron por diff a `67d4668`. **El AMPLÍA caduca 31 líneas y deja 42 nuevas o modificadas** (11 netas: 9 en A, 2 en F), en 17 archivos. Vigentes después del traslado: 25.529 de 25.571.

### Lectura sobre el texto (numeración de `67d4668`)

Se leyeron **las 42 líneas, enteras** (216.710 bytes; casi todas son párrafos de una sola línea), contra los informes `BO-Salta-1989_13102-13345_la-caldera_LEE-1989_2026-10-10.txt`, `BO-Salta-1991_13591-13838_la-caldera_LEE-1991_2026-10-10.txt` y `BO-Salta-1994_14331-14577_la-caldera_LEE-1994_2026-10-10.txt` y, en las citas y las cifras, contra la imagen.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 13 (4, 491–493, 497, 498, 500–502, 506, 507, 509, 514) |
| ape/D-pedidos.tex | 2 (176, 252) |
| ape/F-fuentes.tex | 7 (25, 26, 96, 111–113, 116) |
| cap/00-advertencia.tex | 1 (45) |
| cap/01-planteo.tex | 2 (119, 157) |
| cap/02-metodo.tex | 3 (28, 37, 99) |
| cap/04-siglo.tex | 1 (3671) |
| cap/05-tierra.tex | 1 (285) |
| cap/09-defensas.tex | 1 (643) |
| cap/10-expropiacion.tex | 1 (146) |
| cap/15-hacienda.tex | 1 (185) |
| cap/17-aguabaja.tex | 2 (281, 369) |
| cap/17-tierrafiscal.tex | 1 (401) |
| cap/18-politica.tex | 2 (470, 670) |
| cap/20-opacidad.tex | 2 (881, 882) |
| cap/22-infraestructura.tex | 1 (545) |
| cap/26-presencia.tex | 1 (236) |

Contexto releído entero (no suma cobertura): 17-aguabaja:345–371 (los edictos de 0,525 y la subdivisión del catastro 169 en 2022), 18:650–672 (la ficha de intendencias), 10:112–146 (la ficha de la Ley 6334 y el decreto de 2007), A:486–490 y A:514–515, D:159.

**Esta ronda: 42 líneas nuevas**, 216.710 bytes sobre 3.414.801, que en las 1.037 páginas de la base equivalen a **65,8 páginas**.

Acumulado: 25.529 vigentes + 42 = **25.571 de 25.571 (100,0 %)**. La fase 6 toca ocho líneas de esta ronda (A:491, 501, 506, 509; 05:285; 17-tierrafiscal:401; 22:545; 26:236) y no cambia el largo de ningún archivo: **25.571 de 25.571 (100,0 %)** después de ella; las ocho se releyeron enteras al escribirlas y al compilar.

### Cotejo sobre el facsímil

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 13595 | 11–12 | Decreto 2648, «Salta, 18 de diciembre de 1990»: «licitación pública internacional», once ofertas, Lucardi A 595.098.688,91 (25,5577 %), alternativa A 457.365.057,68 con 42,790897 %, 270 días; edición del 8/1/1991 | Coincide; el porcentaje de la alternativa no corresponde a su monto, como dice la fila del 18/12/1990 |
| 14382 | 10 | Decreto 240 del 10/2/1994: Res. 414/93 del 14/12/1993; acta del 30/11/1993 en La Caldera; expte. 37-50.361/90 | Coincide. El acta la firman el inspector y el representante técnico de la empresa, que no describen la obra ni su estado: se agrega en la fase 6 |
| 13217 | 4 | Decreto 820, «Salta, 29 de mayo de 1989»; convenio del 30/12/1988 con el Centro de Usuarios (capa nativa) | Coincide |
| 13244 | 9 | Decreto 1.333: A 61.834,88, cifra y letras; Caminos S.A. «por ser la adjudicataria de la obra principal» | Coincide |
| 13130 | 7 | Decreto 187: «Balvín Miguel Gallo», nacido en Vaqueros, «Senador Provincial por el departamento La Caldera en 1973, siendo reelecto en 1985» | Coincide |
| 13241 | 5 | Decreto 1.225: licencia política a Teodoro Bartolo Ruiz «con vigencia al 15 de mayo de 1987 y mientras dure su mandato como Intendente Municipal de la localidad de Vaqueros» | Coincide |
| 13139 | 5 | Decreto 259, «18-2-88»: convenio del 30/7/1987, cien metros de piedra y malla, ciento cincuenta de rama y piedra, margen derecha, Zona Cabral | Coincide |
| 13238 | 16 | Decreto 1285: 1/5/1989 a 30/4/1990, siete departamentos; plantaciones de tabaco «afectadas por granizo, vientos, vientos huracanados y lluvias torrenciales» | Fechas y departamentos coinciden; las causas, incompletas en el libro: hallazgo 2 |
| 13812 | 8–9 | Decreto 1648: deroga el 422/90 «con efecto retroactivo»; siete departamentos en el visto y seis en el art. 2 | Coincide |
| 14453 | 10 | Decreto 1163: lluvias torrenciales y granizo; Valle de Lerma (siete departamentos) y General Güemes; 1/3/1994 a 28/2/1995 | Coincide |
| 13653 | 7–8 | Decreto 250: 2 Has. 1.738,80 en el visto y 1.736,80 en el art. 1, a 300 ppp; A 191.896.280,25 − 95.374.824,53 y A 96.521.155,72; 36 renglones del anexo, 33 con prefijo 05 | Coincide; las dos superficies están así en el original |
| 13767 | 6 | Ley 6627, sancionada el 6/8/1991: fracción I, plano 148, matrícula 1575, «cota de coronamiento (1.100)»; art. 2: «el derecho a requerir en su oportunidad el espacio necesario para la construcción de un camino de perilago»; art. 6: vuelve a la Provincia como reserva natural si la entidad se disuelve | La cota coincide; «servidumbre» no es lo que dice la ley: hallazgo 3 |
| 14514 | 13 | Decreto 1975, «Salta, 08 de setiembre de 1994»: fracción A2, plano 326, matrícula 2.065, 100 ha 8.145,98 m², \$5.259,70; el visto da la cota de coronamiento «de 1.110 msnm» | Coincide; la cota del decreto no es la de la ley: hallazgo 4 |
| 14393 | 11–12 | Decreto 460 del 8/3/1994: reserva forestal y de fauna; «Matrícula Nº 05-2.065» | Coincide |
| 13838 | 10 | O.P. 86.800, Carlos Alberto Manzur, edición del 31/12/1991 | Coincide |
| 13268 | 10 | Res. 339-D del 24/8/1989: licitación del 11/12/1986, Res. 1082-D/86, A 27.850, «por los motivos expuestos en los considerandos» | Coincide |
| 13606 | 7 | Res. 24-D: Centro de Salud Nº 22, Vaqueros, «dependiente de la Dirección Primer Nivel de Atención Area Capital» | Coincide (el informe LEE la había leído sólo en la capa) |
| 14505 | 41 | Decreto 1838, «En miles de \$», «U. de O. 34 Hospital La Caldera»: 0,0, 10,0, 5,0, total 15,0 | Coincide |
| 13604 | 8 | Decreto 7, Jurisdicción 06: «Hospital La Caldera.» | Coincide |
| 13181 | 5 | Res. D.G.T. 192/88 transcripta en el Decreto 589: «Calvimonte, La Caldera, S. Agustín P/ La Merced, Mollar» | Literal |
| 14489 | 6 | Decreto 1666: la oficina del Registro Civil «se encuentra actualmente sin personal a cargo» | Literal |
| 13250 | 6 | Decreto 1385: autoriza «al Banco de Préstamos y Asistencia Social a otorgar un apoyo financiero» de A 5.000 «a favor del Colegio Secundario Nº 44 "Senado Provincial" de La Caldera» | Cifra y nombre coinciden; quien da el apoyo es el Banco, no el Ministerio: hallazgo 5 |

22 cotejos sobre 26 hojas de 22 ediciones; 18 coincidentes o literales y 4 que corrigen o completan al libro (hallazgos 2 a 5).

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | A:491 | El plan de mesas de 1989 «pone diecinueve en ocho escuelas»: el recuento del informe LEE suma las dos mesas de extranjeros, que están en las municipalidades | 3 | «diecisiete en ocho escuelas de los dos distritos municipales y dos de extranjeros en las municipalidades» |
| 2 | 05:285 y A:491 | La emergencia agropecuaria de 1989, «por el granizo en las plantaciones de tabaco» | 5 | El granizo, los vientos huracanados y las lluvias torrenciales que afectaron las plantaciones de tabaco |
| 3 | 17-tierrafiscal:401 y A:501 | La Ley 6627, «con servidumbre para un camino de perilago y reversión a reserva natural» | 5 | El derecho de la Administración General de Aguas a requerir sin indemnización el espacio para el camino, y la vuelta del inmueble a la Provincia, como reserva natural, si el club se disuelve |
| 4 | 17-tierrafiscal:401 y A:509 | «descontado el espejo de agua hasta la cota 1.100», sin decir que el decreto de 1994 la da como 1.110 | 6 | Las dos cotas, cada una con su acto |
| 5 | 26:236 y A:491 | «el Bienestar Social le da A~5.000» al Colegio Secundario Nº 44 | 5 | Un decreto del Bienestar Social autoriza al Banco de Préstamos y Asistencia Social a darle A~5.000 |

Además, una **precaución de privacidad** sin hallazgo (A:506): la lista de contribuyentes de Rentas de 1994 (RG 10/94) no dice su carácter; la fila nombraba a una titular que puede estar viva y pasa a decir «a nombre de los Serrey, seis de ellos de Manuel Serrey», cuyo heredero ya consta en el libro por el decreto de 2007. Y una **incorporación del cotejo** (22:545): el acta de recepción definitiva de 1993 no describe la obra ni su estado.

Resta: en el aspecto 3, un recuento importado del informe y no recalculado (1), −5: **95**. En el aspecto 5, tres afirmaciones que no son las del acto (2, 3 y 5): escala general, **90**. En el aspecto 6, una discrepancia entre fuentes no señalada (4), −5: **85**. Ningún error de consistencia en las 65,8 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los cinco, en el AMPLÍA 1989, 1991, 1994 (`67d4668`), escrito por esta misma sesión. **Ninguno lo atrapó un control automático**: el 1 lo encontró la relectura de la ficha A.13 del informe 1989 contra la fila; el 2 al 5, el cotejo de la imagen.

**Descartados (falsos positivos, 3).** «Es lo único de lo hallado que da su intendencia» (fila de 1989, Ruiz): el universo está declarado y en lo hallado de 1986 a 1994 no hay otro acto que lo nombre intendente. «Es el primer año posterior a 1994 que este libro lee de corrido» (fila de 2002): 1995 a 2001 no se leyeron. Las superficies 1.738,80 y 1.736,80 del Decreto 250 (10:146), que el catálogo de confusiones 6/8 pone en duda: a 300 ppp, la resolución nativa del escaneo, el visto dice 8 y el artículo 1 dice 6, y la Ley 6334 da 1.736,80; la discrepancia es del original.

**Pendientes revisados.** P238 y P244, cerrados por el AMPLÍA (adjudicación y recepción definitiva del agua potable); lo que quedaba de ellos pasó a P247, que sigue abierto. P248 (1989, 1991 y 1994 en barrido), P249 (config) y P250 (intendencias de Vaqueros), abiertos por el AMPLÍA, siguen abiertos. P236 sigue abierto. No hay pendientes nuevos.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.560/25.560 vigentes en `d0f1dcf` | 25.529 vigentes; 31 caducas |
| Citas entre comillas en las líneas nuevas contra la imagen | 5 cadenas («Calvimonte, La Caldera, S. Agustín P/ La Merced, Mollar», «actualmente sin personal a cargo», «Hospital La Caldera», «Provincia de Salta vs. Serrey», «Senado Provincial») | 5/5 literales |
| Cifras y fechas de las líneas nuevas contra la imagen | 49 en 19 ediciones | 49/49; la cota del espejo de agua difiere entre la ley y el decreto (hallazgo 4), y cada acto dice lo que el libro le atribuye |
| Superlativos y ausencias en las líneas agregadas por el AMPLÍA y la fase 6 | 42 líneas (párrafos enteros); 111 coincidencias, 6 de ellas en el texto nuevo | Las 6, con universo; las demás son del texto anterior, ya auditado |
| Repaso de ventana: frases con fórmula de ausencia o superlativo que nombran 1988–1996 | 21/21 | Las que caían las corrigió el AMPLÍA (filas de 1990 y 2002, F:96, 22:545 «ese año») |
| Menciones de cobertura («noventa y ocho», «cincuenta y seis», «salvo diez», «1990, 1992,») | 25.571/25.571 | 0 sin actualizar |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos en capítulos | 0 |
| Privacidad: personas nombradas en las líneas nuevas | 42/42 | 0 caídas y 1 precaución (A:506). Nombrados: funcionarios (gobernadores, Gallo, Ruiz), empresas y los Serrey, ya nombrados por el libro. Sin nombre: los peticionantes de agua, los rematados, la empleada del Registro Civil, los herederos de El Acheral |
| Largo de los archivos antes y después de la fase 6 | 5 archivos | ninguno cambia |
| Compilación | base `67d4668` y fase 6 | Compilan; 1.037 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |
| `git am` del parche sobre un clon limpio de `67d4668` | 1 parche | Aplica |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con decreto, edición y hoja; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 95 | 100 | Hallazgo 1, aplicado |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 22 cotejos sobre 22 ediciones, bajo el techo de 90; 5/5 citas literales |
| 5 | Honestidad epistémica | 12 | 90 | 100 | Hallazgos 2, 3 y 5, aplicados |
| 6 | Tipo y jerarquía de fuente | 5 | 85 | 90 | Hallazgo 4, aplicado |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 65,8 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Pedidos nuevos en D (edición 13.314, páginas de la 13.744, anexos de la Ley 6738, convenio de 1988, ordenanzas de Vaqueros); ninguno satisfecho sigue en la lista |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | La segunda tesis gana la adjudicación y la recepción del agua del pueblo, y en Vaqueros la entrega de la planta al centro de usuarios: todo provincial o de usuarios |
| 11 | Aporte y originalidad | 5 | 90 | 90 | La obra de agua potable de 1990-1993 queda con sus dos actos de cierre del Boletín |
| 12 | Estructura y prosa | 2 | 100 | 100 | Sin remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin cambios |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas; una precaución aplicada |

**Nota inicial: 86,6 antes del tope y 86,6 después** (tope de 90 por la cobertura acumulada inicial del 99,8 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 84.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) en el AMPLÍA, copiar del acto, y no del informe, las causas, los derechos y los recuentos, y anotar cada discrepancia entre la ley y su decreto: habría evitado los hallazgos 1 a 5; (5) cerrar con un LEE complemento los pendientes de 1989, 1991 y 1994 (P248) para poder afirmar ausencias de esos años.

**Avance del libro:** 5 de 5 hallazgos resueltos; compila sin errores, 1.037 páginas. **Avance de la investigación:** la **segunda tesis** gana los dos actos de cierre del agua del pueblo que faltaban ---la adjudicación de diciembre de 1990 y la recepción definitiva de noviembre de 1993, con un acta que no describe la obra---, y en Vaqueros la entrega de la planta nueva al centro de usuarios en 1989: ninguno tiene al municipio como parte. La **tercera** gana un senador por el departamento en 1973 y en 1985 y un intendente de Vaqueros desde 1987, cada uno por un solo acto. Ninguna cambia de estado.

**Calidad de la auditoría.** Cobertura de la ronda: 42 líneas (0,16 %; 65,8 páginas). Cobertura acumulada: 25.571 de 25.571 (100,0 %). Falsos positivos descartados: 3. Errores introducidos por la propia auditoría: 5, en el AMPLÍA de la misma sesión; atrapados por un control automático: 0.

## Ronda 86 — auditoría con fase 6 (10/10/2026)

Tipo: **auditoría con fase 6** (CORRIGE 3.6), por la palabra clave `MEJORA` (flujo v2 §7), sobre el material del AMPLÍA 1995, 1996, 1997. En `auto/insumos-mejora/` no hay insumos nuevos (sólo la carpeta `usados/`). Base: commit `07ccd23` de `ediedrich/dispositivo-caldereno` (AMPLÍA 1995, 1996, 1997, sobre `173362b`; aplicado por `3-registrar` a las 13:04 del 10/10), con la fase 6 en `ronda-86.patch` (un commit sobre `07ccd23`). La sesión que hace esta ronda es la misma que escribió el AMPLÍA y los tres informes LEE: se audita trabajo propio, y las citas y cifras nuevas se volvieron a mirar en el texto reconocido y, en los renglones decisivos, en la imagen de las ediciones del Release, bajadas a la nube por descarga directa.

### Traslado y caducidad de los tramos anteriores

Los tramos vigentes al cierre de la ronda 85 (25.571 de 25.571, sobre `173362b`) se trasladaron por diff a `07ccd23`. **El AMPLÍA caduca 24 líneas y deja 35 nuevas o modificadas** (11 netas: 9 en A, 2 en F), en 13 archivos. Vigentes después del traslado: 25.547 de 25.582.

### Lectura sobre el texto (numeración de `07ccd23`)

Se leyeron **las 35 líneas, enteras** (91.219 bytes; casi todas son párrafos de una sola línea), contra los informes `BO-Salta-1995_14578-14823_la-caldera_LEE-1995_2026-10-10.txt`, `BO-Salta-1996_14824-15073_la-caldera_LEE-1996_2026-10-10.txt` y `BO-Salta-1997_15074-15320_la-caldera_LEE-1997_2026-10-10.txt` y, en las citas y las cifras, contra el acto.

| Archivo | Líneas nuevas |
|---|---|
| ape/A-cronologia.tex | 11 (4, 509–512, 514, 515, 517–520) |
| ape/D-pedidos.tex | 2 (159, 406) |
| ape/E-personas.tex | 1 (139) |
| ape/F-fuentes.tex | 6 (26, 96, 111, 115, 116, 118) |
| cap/00-advertencia.tex | 1 (45) |
| cap/01-planteo.tex | 2 (119, 157) |
| cap/02-metodo.tex | 3 (28, 37, 99) |
| cap/04-siglo.tex | 2 (1625, 3671) |
| cap/17-tierrafiscal.tex | 1 (401) |
| cap/18-politica.tex | 2 (656, 671) |
| cap/19-resistencias.tex | 1 (657) |
| cap/20-opacidad.tex | 2 (881, 882) |
| cap/22-infraestructura.tex | 1 (545) |

Contexto releído entero (no suma cobertura): A:505–508 y A:513 (las filas de 1994 y de los años 90), 18:650–672 (la ficha de intendencias), 19:650–660, 04:1615–1626, D:150–160.

**Esta ronda: 35 líneas nuevas**, 91.219 bytes sobre 3.434.434, que en las 1.043 páginas de la base equivalen a **27,7 páginas**.

Acumulado: 25.547 vigentes + 35 = **25.582 de 25.582 (100,0 %)**. La fase 6 toca ocho líneas de esta ronda (A:510, 515, 518, 519, 520; D:406; 04:1625; 22:545) y no cambia el largo de ningún archivo: **25.582 de 25.582 (100,0 %)** después de ella; las ocho se releyeron enteras al escribirlas y al compilar.

### Cotejo sobre el acto

| Edición | Hoja | Qué se cotejó | Resultado |
|---|---|---|---|
| 14784 | 20, 22 | Actas 1705 y 1706 del Tribunal Electoral, «a los 27 días del mes de octubre» de 1995 (imagen del encabezado de la 1706) | Coincide |
| 14784 | 21 | «Departamento: La Caldera / Diputado / Mendaña, Luis Gerardo», lema F.J. (imagen) | Coincide |
| 14784 | 24 | Municipios La Caldera (Quipildor; Colque, Fernández, Blanco) y Vaqueros (Junco; Pelo, Vera, Miranda, Salvatierra) | Coincide (texto reconocido) |
| 15296 | 17, 20, 31, 33 | Actas 2224 a 2227: «a los 19 días del mes de noviembre de mil novecientos noventa y siete» (imagen de la 2227) | **La fila decía 12 de noviembre**, fecha de un aviso vecino de la misma hoja que el informe LEE tomó por la del acta: hallazgo 4 |
| 15296 | 24, 34 | Concejales de La Caldera (Fernández, Conde, Lozano) y senador (Pérez, Luis Humberto) | Coincide (imagen) |
| 14754 | 7 | Decreto 1733: «menciona una superficie en mts2. que no corresponde a la matrícula adjudicada»; 100 hectáreas 1.848,16 m² (imagen) | Coincide |
| 14794 | 27–29 | Decreto 2673 (30/10/1995): régimen de compensación de créditos y deudas «hasta el 31/12/91»; cuadro I, La Caldera, crédito 89.471,53; cuadro V, La Caldera, deuda 1.457.354,61 (imagen de las dos hojas) | Cifras coinciden; «a valores de 1991» no es lo que dice el decreto: hallazgo 1 |
| 14608 | 6, 8 | Res. 8 D: defensas en el río La Caldera, tramos I, II y III, \$171.312,03, por vía administrativa; Res. 14 D: El Gallinato, \$67.585,21 | Coincide |
| 14703 | 10 | Res. 149 D: dique Campo Alegre, \$62.065,37, tres meses, por vía administrativa | Coincide |
| 14917 | 14, 16 | Decreto 923 (13/5/1996): incorpora «Reacond. Azud de Toma Embalse Campo Alegre - La Caldera 600.000,00» (imagen del renglón) | Coincide |
| 14969 | 6–7 | Res. 130 D (15/7/1996): aprueba la «Licitación Pública realizada el día 3 de junio de 1996»; Ing. Alonso Crespo S.A., \$450.436,45, 20,37 % (imagen) | Monto y porcentaje coinciden; la licitación es del 3 de junio y no de mayo: hallazgo 2 |
| 15063 | 11 | Res. SO y SP 998: legajo «confeccionado por la Municipalidad de La Caldera, complementado por el Programa de Educación y de Salud»; \$60.004,29; adjudicación directa (imagen) | La cita coincide; el capítulo omitía el complemento del programa: hallazgo 8 |
| 15003 | 8 | Decreto 1917: convenios «firmados entre el Poder Ejecutivo Provincial y la Municipalidad de Vaqueros», cinco anexos (imagen) | Coincide |
| 15100 | 8 | Decreto 2885 (31/12/1996): bajo «Reforzar a», «Unidad de Organización 34-Hospital de La Caldera - Personal \$ 331.500,00» (imagen) | Cifra coincide; es un refuerzo de partidas de 1996, no la asignación del hospital: hallazgo 5 |
| 15146 | 12 | Decreto 1781: incorpora al presupuesto de Aguas de Salta S.A. «Aportes Reintegrables / ENOHSA»; «Depuradora La Caldera \$ 35.000» (imagen) | Cifra coincide; son aportes reintegrables incorporados al presupuesto de la empresa: hallazgo 6 |
| 15203 | 14 | Res. SO y SP 1500: «Acueducto en sistema de Vertientes - Río Wierna - localidad Vaqueros»; Reynaldo Lucardi, \$102.925,87 (imagen) | Coincide |
| 15206 | 9 | Decreto 2937, «Salta, 11 de julio de 1997»: «ubicado en el sector Noroeste del departamento La Caldera», catastro 102, 24.364 ha (imagen) | Coincide |
| 15200 | 25 | Remate «Estancia Las Nieves», «El día viernes 11 de julio de 1997 ... con la base de \$ 56.414,00» (imagen) | Coincide; es un anuncio, y la fila y el cap. 4 lo daban por hecho: hallazgo 3 |
| 15168 | 19 | Remate de 2.600 hectáreas en La Caldera, «JUDICIAL CON BASE - POR QUIEBRA», juicio de concurso preventivo «hoy Quiebra» (imagen) | La fila decía «en un concurso preventivo»: hallazgo 7 |
| 15282 | 5 | Ley 6964: exime del canon de riego el catastro 2.067, del «Hogar San Cayetano» de Vaqueros (capa nativa) | Coincide |

20 cotejos sobre 31 hojas de 17 ediciones (16 sobre la imagen, 4 sobre el texto reconocido o la capa nativa); 12 coincidentes y 8 que corrigen o completan al libro (hallazgos 1 a 8).

### Hallazgos y fase 6

| # | Línea | Qué decía | Aspecto | Cómo queda |
|---|---|---|---|---|
| 1 | A:510 | La compensación de deudas deja a La Caldera, «a valores de 1991», un crédito y una deuda; «del que Vaqueros no figura» | 3 | «por los saldos al 31 de diciembre de 1991», y «en el que Vaqueros no figura» |
| 2 | A:515 | El azud «que la Administración General de Aguas licitó en mayo; ese mes un decreto…» | 3 | Llamó a licitación en mayo y licitó el 3 de junio; en mayo un decreto le había pasado los \$600.000 |
| 3 | A:519 y 04:1625 (y D:406) | El remate del catastro 102 «se hace el 11 de julio»; «se subasta en junio y en julio» | 5 | Se anuncia otra vez para el 11 de julio, y sale a subasta en junio y otra vez en julio; si hubo venta, lo leído no lo dice. El pedido de D habla de la subasta anunciada para el 11 de julio |
| 4 | A:518 y A:520 | Actas 2224 a 2227 del «12 nov. 1997» | 3 | 19 de noviembre de 1997, en la fila y en la remisión de la fila del año |
| 5 | A:518 | «el Hospital de La Caldera es una unidad de organización del presupuesto, con \$331.500 de personal» | 5 | Un decreto del 31/12/1996, publicado en febrero, refuerza sus partidas con \$331.500 para personal |
| 6 | A:518 y 22:545 | «Aguas de Salta recibe \$35.000 del ENOHSA»; la Provincia «le pasa» ese dinero | 5 | Un decreto incorpora al presupuesto de Aguas de Salta S.A. \$35.000 de aportes reintegrables del ENOHSA |
| 7 | A:518 | Las fincas Severino se rematan «en un concurso preventivo» | 5 | En una quiebra que había empezado como concurso preventivo |
| 8 | 22:545 | La Escuela 136, «sobre un legajo que hizo la propia Municipalidad» | 5 | Un legajo de la Municipalidad que completó el Programa de Educación y de Salud de la Secretaría de Obras y Servicios Públicos |

Resta: en el aspecto 3, tres fechas o intervalos tomados de segunda mano y no rehechos sobre el acto (1, 2 y 4), −15: **85**. En el aspecto 5, cinco afirmaciones que no son las del acto, cada una en una frase (3, 5, 6, 7 y 8): escala general, observaciones repetidas, **80**. Ningún error de consistencia en las 27,7 páginas: el aspecto 7 queda en **100**.

**Errores introducidos por la propia auditoría**: los ocho, en el AMPLÍA 1995, 1996, 1997 (`07ccd23`), escrito por esta misma sesión; el 4 viene del informe LEE 1997 (ficha A.34), que tomó la fecha de un aviso vecino. **Ninguno lo atrapó un control automático**: los ocho los encontró el cotejo con el acto.

**Descartados (falsos positivos, 4).** «Se rematan» en las filas de 1995, 1996 y 1997 para remates anunciados: es la fórmula que la cronología usa en todas sus filas para el anuncio de un remate (trece filas), y sólo el catastro 102, cuyo resultado el libro pide, se corrige. «Cinco ediciones traen separatas o anexos sin paginar» (F:115): el informe 1995 cuenta seis ediciones con hojas de más, pero la sexta (14646) trae un plano y no una separata. «Lo que en lo hallado la Provincia les confía a los municipios son escuelas» (22:545): el universo está declarado, y los demás actos municipales hallados (la camioneta y el PRODISM de Vaqueros) son de la propia municipalidad. «La empresa del agua del pueblo» para Lucardi: el libro ya da la adjudicación de 1990 y la recepción de 1994.

**Pendientes revisados.** P251 a P254, abiertos por el AMPLÍA, siguen abiertos. Se abre **P255** (lee): la ficha A.34 del informe LEE 1997 da a las actas 2226 y 2227 la fecha 12-11-97, que es la de un aviso vecino de la hoja 17; las cuatro actas (2224 a 2227) son del 19-11-97.

### Controles por script (no cuentan como lectura)

| Control | Denominador | Resultado |
|---|---|---|
| Traslado de tramos anteriores por diff | 25.571/25.571 vigentes en `173362b` | 25.547 vigentes; 24 caducas |
| Citas entre comillas en las líneas nuevas contra el acto | 4 cadenas («que no corresponde a la matrícula adjudicada», «Reacondicionamiento Azud de Toma Embalse Campo Alegre», «confeccionado por la Municipalidad de La Caldera», «Cerro Nevado o Potrero de San José o de Castilla o de la Nieves» con «ubicado en el sector Noroeste del departamento»; más «aportes poblacionales», no cotejada) | 4/4 literales, sobre 5 |
| Cifras y fechas de las líneas nuevas contra el acto | 23 en 14 ediciones | 22/23; la fecha de las actas de 1997 no coincide (hallazgo 4), y dos cifras coincidentes llevaban mal su contexto (hallazgos 2 y 5) |
| Superlativos y ausencias en las líneas agregadas por el AMPLÍA y la fase 6 | 35 líneas (párrafos enteros); 65 coincidencias, 4 de ellas en el texto nuevo | Las 4: una no es superlativo («a la primera», de dos municipalidades) y tres llevan su universo («en lo leído de los tres años»); las demás son del texto anterior, ya auditado |
| Repaso de ventana: frases con fórmula de ausencia o superlativo que nombran 1994–1998 o «posterior a 1994» | Las del índice del AMPLÍA (57) | Las que caían las corrigió el AMPLÍA (F:96 y el catastro 102 en 04, 19 y D) |
| Menciones de cobertura («ciento un», «cincuenta y nueve», «cincuenta y ocho», «1994,») | 25.582/25.582 | 0 sin actualizar |
| Remisiones a capítulos posteriores sin «más adelante» | `\ref{cap:…}` nuevos en capítulos | 0 |
| Privacidad: personas nombradas en las líneas nuevas | 35/35 | 0 caídas. Nombrados: funcionarios electos (diputado, senador, intendentes, concejales, convencional), empresas, los Serrey y Urquiza ya nombrados por el libro. Sin nombre: los demandados de los remates y de la quiebra, los peticionantes de agua, el profesional del estudio topográfico |
| Largo de los archivos antes y después de la fase 6 | 4 archivos | ninguno cambia |
| Compilación | base `07ccd23` y fase 6 | Compilan; 1.043 páginas; 0 errores; 0 referencias indefinidas; `.lof` con 42 entradas |
| `git am` del parche sobre un clon limpio de `07ccd23` | 1 parche | Aplica |

### Notas

| # | Aspecto | Peso | Inicial | Final | Justificación |
|---|---|---|---|---|---|
| 1 | Rigor documental | 11 | 82 | 82 | Frases nuevas con acto, edición y hoja; escala general por P115 |
| 2 | Vigencia normativa | 8 | 100 | 100 | Sin cambios |
| 3 | Versión, fecha y origen | 6 | 85 | 100 | Hallazgos 1, 2 y 4, aplicados |
| 4 | Fidelidad de transcripción | 7 | 90 | 90 | 20 cotejos sobre 17 ediciones, bajo el techo de 90; 4/4 citas literales |
| 5 | Honestidad epistémica | 12 | 80 | 100 | Hallazgos 3, 5, 6, 7 y 8, aplicados |
| 6 | Tipo y jerarquía de fuente | 5 | 90 | 90 | Sin discrepancias nuevas |
| 7 | Consistencia interna | 9 | 100 | 100 | 0 errores en 27,7 páginas |
| 8 | Integridad del aparato | 8 | 95 | 95 | Pedidos de D actualizados (actas de 1995 y 1997 publicadas; resultado de la subasta de 1997); ninguno satisfecho sigue en la lista |
| 9 | Trazabilidad | 6 | 30 | 30 | Muestra de la ronda 42 (P40) |
| 10 | Argumentación | 9 | 70 | 70 | La segunda tesis gana 1995-1997: obras de agua y defensas de la Provincia; lo que pasa al municipio es una escuela, con un legajo que completa la Provincia |
| 11 | Aporte y originalidad | 5 | 90 | 90 | Las proclamaciones de 1995 y 1997 completan el cuadro de intendencias con acta del Boletín |
| 12 | Estructura y prosa | 2 | 100 | 100 | Sin remisiones sin marcar |
| 13 | Cartografía y figuras | 3 | 94 | 94 | Sin figuras nuevas |
| 14 | Utilidad pública | 4 | 100 | 100 | Sin cambios |
| 15 | Riesgo legal y privacidad | 5 | 90 | 90 | Sin caídas |

**Nota inicial: 85,0 antes del tope y 85,0 después** (tope de 90 por la cobertura acumulada inicial del 99,9 %, que no actúa). **Nota final: 88,3 antes y después del tope** (cobertura acumulada del 100,0 %). Distancia a 100: 3,8 puntos estructurales y 7,9 corregibles, como en la ronda 85.

Las cinco acciones que más subirían la nota final: (1) rehacer la muestra de trazabilidad con P40 resuelto: hasta +3,6; (2) cerrar con documento alguna tesis abierta: hasta +1,8; (3) P115: +0,9; (4) en el AMPLÍA, rehacer cada fecha y cada cifra sobre el acto y no sobre la ficha, y leer el encabezado del cuadro antes de dar una cifra («Reforzar a», «Aportes reintegrables»): habría evitado los hallazgos 1 a 8, como en la ronda 85; (5) cerrar con un LEE complemento los pendientes de 1995 a 1997 (P251) para poder afirmar ausencias de esos años.

**Avance del libro:** 8 de 8 hallazgos resueltos; compila sin errores, 1.043 páginas. **Avance de la investigación:** la **segunda tesis** gana 1995-1997 sin cambiar de estado: las defensas, el dique, el azud, la red colectora y el acueducto de Vaqueros son de la Provincia o de su empresa de agua, y lo que pasa a los municipios son escuelas, con un legajo municipal que completa un programa provincial. La **tercera** gana las actas de proclamación de 1995 y 1997 del Boletín (diputado, senador, intendentes y concejales de los dos municipios). El catastro 102 gana la autorización de compra de 1997, sin resultado. Ninguna cambia de estado.

**Calidad de la auditoría.** Cobertura de la ronda: 35 líneas (0,14 %; 27,7 páginas). Cobertura acumulada: 25.582 de 25.582 (100,0 %). Falsos positivos descartados: 4. Errores introducidos por la propia auditoría: 8, en el AMPLÍA de la misma sesión (uno heredado del informe LEE 1997); atrapados por un control automático: 0.
