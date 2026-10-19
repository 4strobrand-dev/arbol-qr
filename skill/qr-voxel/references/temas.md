# Recetas de temas

Cada receta dice qué va sobre los módulos oscuros, qué va en el borde (los tres cuadros de esquina y los oscuros fuera del elemento principal), cómo se ve el piso y qué ambiente le queda. Las paletas ya cumplen el contraste para escanear; si las cambias, mantén el elemento principal y el borde con luminancia baja (< ~0.30) y el piso alto (> ~0.80).

En la plantilla, "elemento principal" corresponde a las celdas `leaf` y "borde" a las celdas `grass`.

## Árbol (la plantilla)

- **Elemento principal:** columnas de hojas dentro de una copa redonda (`Rc ≈ 0.44·N`). Varias hojas por celda, tres "tapas" casi horizontales arriba para cubrir la celda desde la vista cenital.
- **Borde:** pasto en voxeles, rejilla de 3×3 cubos por celda con alturas escalonadas.
- **Soporte:** tronco y ramas que se afinan en la vista de arriba.
- **Variantes:** primavera (copa coral, pétalos, pájaros), verano (verde, luciérnagas), otoño (naranja, lluvia, hojas que caen), invierno (azul hielo, nieve, pasto verde pino).

## Ciudad

- **Elemento principal:** edificios. Cada celda `leaf` es una caja de 0.9 × altura × 0.9. La altura sale de la distancia al centro (más altos en el centro, como un skyline) más ruido por celda. Ventanas: un segundo `InstancedMesh` de caras pequeñas un poco más claras en los lados, nunca en el techo.
- **Zona del elemento:** casi todo el código, `Rc ≈ 0.7·N`, excepto los cuadros de esquina.
- **Borde:** parques. Cubos bajos verde oscuro con arbolitos de 1 voxel encima.
- **Piso:** calles gris muy claro. Coches como cajitas que se mueven sobre las celdas claras, desvanecidos con `vis` en la vista de arriba.
- **Sin soporte:** borra tronco y ramas.
- **Variantes (en vez de estaciones):**
  - Día: techos `#2f3b4c #3a4a5e #27313f #44546a`, parques `#2f5a3a #3a6a45`, fondo `#eef0f2`.
  - Atardecer: techos `#5a2e3a #6b3846 #4a2630 #7a4050`, parques `#3a4a2a`, fondo `#f3ece6`.
  - Noche: techos `#1f2a44 #26335a #18213a`, parques `#20402c`, fondo `#e9ecf3`, y luces de ventanas cálidas solo en isométrico.
  - Lluvia: los techos de día más la lluvia de la plantilla.
- **Sonido:** usa el canal de viento de la plantilla con el filtro más alto, como rumor de tráfico, y pájaros solo de día.

## Jardín de flores

- **Elemento principal:** flores. Tallo fino (afinado arriba como las ramas) y una corola de 3–5 pétalos planos que cubre la celda desde arriba. Alturas suaves, de 1 a 3 unidades, con ruido.
- **Zona del elemento:** `Rc ≈ 0.55·N`.
- **Borde:** setos de boj en voxeles, cubos de 1 × 0.8 × 1 verde muy oscuro `#2c4a2a #34552f #284426`.
- **Piso:** grava clara `#f2efe8 #ebe7df`.
- **Variantes:**
  - Rojas: `#b32d3a #c43a46 #a02434`.
  - Moradas: `#5b3a8a #6a4699 #4d2f78`.
  - Azules: `#2d4f9a #3a5fae #284487`.
  - Mixtas: alterna las tres por celda.
- **Ambiente:** mariposas como partículas pequeñas que revolotean (desvanecidas arriba), pétalos que caen y polen.

## Arrecife de coral

- **Elemento principal:** corales. Columnas ramificadas de cubos pequeños (2–4 niveles, cada nivel un poco más angosto) y anémonas como conos bajos. Todo dentro de la celda.
- **Zona del elemento:** `Rc ≈ 0.6·N`.
- **Borde:** rocas, cubos irregulares gris pizarra `#3a4148 #454d55 #30373d`.
- **Piso:** arena muy clara `#f5f0e4 #efe9db`.
- **Fondo:** azul muy claro y plano `#e8f1f4`, que se lee como agua sin apagar el contraste.
- **Variantes:**
  - Vivo: `#c2412f #d0562a #9e2f5a #b8432a`.
  - Profundo: `#6a2f6e #7a3a7e #522858`.
  - Atardecer: `#b54a2a #c25e30 #8f3a2a`.
- **Ambiente:** burbujas que suben (usa el sistema de polen con color blanco y velocidad mayor), peces de 2–3 voxeles que nadan en círculo (desvanecidos arriba) y un vaivén suave de los corales con el shader de viento.

## Ideas para más temas

Funciona con cualquier cosa que se pueda pensar como columnas sobre una rejilla:

- un pastel con velas,
- un estante de libros visto desde arriba,
- un campo de cultivo con tractores,
- un tablero de ajedrez con piezas,
- un pixel art de un logo con relieve.

Mantén siempre la regla de oro: lo oscuro llena su celda, lo claro queda vacío, y las esquinas van con otro material.
