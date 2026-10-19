---
name: qr-voxel
description: Crea códigos QR escaneables que son escenas voxel en 3D (un árbol, una ciudad, un jardín, un arrecife…): en isométrico se ven como un diorama animado y, al girar la cámara hacia arriba, la escena se lee como QR. Úsala cuando pidan un QR artístico, un QR en 3D o voxel, un QR que "sea" un objeto o paisaje, o una pieza tipo Árbol QR. Entrega un HTML con estaciones o variantes, ambiente animado y exportación a video, GIF e imagen.
---

# QR voxel

Un QR voxel es una escena 3D construida **sobre la rejilla del código QR**. En vista isométrica parece un diorama: un árbol, una ciudad, un jardín. Con una cámara ortográfica mirando hacia abajo, la misma escena se lee como un QR y se puede escanear con el teléfono.

La pieza de referencia es el **Árbol QR**, en `assets/plantilla.html`. Parte siempre de ella: ya resuelve la cámara, la transición, las partículas, el sonido y las exportaciones. Para un tema nuevo solo cambias lo que está marcado como `TEMA` en el código.

## La regla de oro

Todo sale de una idea: **cada módulo del QR es una celda, y lo que hay encima de la celda decide si se ve oscura o clara desde arriba.**

1. **Módulo oscuro → un elemento que llena su celda y no se sale de ella.** Una columna de hojas, un edificio, una flor, un coral. Si se sale aunque sea un poco, mancha la celda vecina y el QR deja de leerse.
2. **Módulo claro → vacío.** Nada encima, solo el piso claro. Ramas, cables, puentes o cualquier cosa que cruce celdas claras tiene que afinarse o desaparecer en la vista de arriba.
3. **Los tres cuadros de las esquinas** (los patrones de posición, 7×7 módulos más un borde de 1) **llevan un material distinto** al elemento principal: pasto alrededor de un árbol, parques alrededor de una ciudad. Son la parte más importante para el lector, así que deben verse limpios y sólidos.
4. **Zona de silencio**: deja al menos 3 módulos claros alrededor del código.
5. **Cámara ortográfica.** En perspectiva, las columnas altas se abren hacia los lados y tapan celdas vecinas. En ortográfica, desde arriba, cada columna cae exactamente en su celda sin importar la altura.

Esto es lo que hace que el truco funcione: la altura es libre. Las columnas pueden tener alturas distintas y formar una copa redonda, un horizonte de edificios o un arrecife, y desde arriba el código sigue intacto.

## Reglas de color para que escanee

Esto es lo que más falla. Los lectores convierten la imagen a grises y separan oscuro de claro; si los dos quedan cerca, no leen.

- **Lo oscuro debe ser oscuro de verdad.** Apunta a una luminancia por debajo de ~0.30 para todo lo que va sobre módulos oscuros, y por encima de ~0.80 para el piso claro. Los colores pastel, el amarillo claro, el rosa claro y el blanco no sirven como "oscuro".
- **Ojo con la iluminación.** Las caras de arriba reciben toda la luz, así que se ven más claras que el color que pusiste. Si un color queda justo, bájale un 10–15 %.
- **Sombras fuera en la vista de arriba.** Una sombra sobre un módulo claro lo oscurece. Apaga `castShadow` cuando la cámara pasa a la vista cenital (la plantilla ya lo hace).
- **Variantes estacionales u oscuras:** si una variante pide algo claro (nieve, flores blancas), ponlo en las partículas o como detalle pequeño, nunca como color principal de los módulos oscuros. Por ejemplo, en invierno el árbol usa copa azul hielo, no blanca.
- **Fondo plano**, sin degradados.

## Flujo de trabajo

1. **Elige el tema y define tres cosas:**
   - el elemento principal sobre los módulos oscuros (qué es cada columna),
   - el material de los cuadros de esquina y de los oscuros fuera del elemento principal,
   - el piso claro.
   Revisa `references/temas.md`: ahí hay recetas probadas de ciudad, jardín y arrecife.
2. **Copia `assets/plantilla.html`** y busca los comentarios `TEMA`. Ahí cambias:
   - `SEASONS`: paletas, partículas y sonido de cada variante (pueden ser estaciones, horas del día o lo que pida el tema).
   - La clasificación de celdas en `buildWorld`: qué módulos oscuros son elemento principal y cuáles son borde.
   - La construcción del elemento principal (en el árbol: tronco, ramas y columnas de hojas).
   - Los textos de la interfaz y el `<title>`.
3. **No toques** la cámara, la transición entre vistas, la exportación de video, GIF e imagen, ni la generación del QR, salvo que el usuario lo pida.
4. **Verifica el escaneo** de cada variante (ver abajo). Si una falla, oscurece su paleta y vuelve a probar.
5. **Entrega** el HTML. Si el usuario revisa desde el teléfono, recuérdale que dentro de una vista previa algunas descargas pueden estar bloqueadas, y que abierto en el navegador descarga directo.

## Cómo verificar el escaneo

Si tienes entorno de código con Python, usa el script:

```bash
pip install playwright opencv-python-headless
python -m playwright install chromium
python scripts/verificar_qr.py ruta/a/tu-pieza.html
```

Abre la página, pasa por cada variante, cambia a la vista de arriba, toma captura y la decodifica con OpenCV. Imprime qué variantes leen y cuáles no.

OpenCV es más exigente que la cámara de un teléfono: si lee en OpenCV, el teléfono lo lee seguro. Si OpenCV falla pero la imagen se ve limpia, prueba con el teléfono antes de cambiar colores.

Si no tienes entorno de código, pídele al usuario que lo pruebe con la cámara del teléfono en la vista de arriba, una variante a la vez.

## Qué incluye la plantilla

- Generación del QR con `qrcode-generator` (nivel de corrección Q, texto UTF-8), regenerado al escribir.
- Escena con three.js r128: baldosas por módulo, elemento principal, borde, partículas (lluvia, nieve, hojas que caen y se posan, polen), viento por shader.
- Transición isométrico ↔ cenital al tocar la escena o con la barra espaciadora, sin aviso en pantalla.
- Sonido ambiente generado con Web Audio (viento, lluvia, pájaros), apagado por defecto.
- Exportaciones: **Video** vertical 1080×1920 (MP4 en iPhone, WebM en algunos navegadores; incluye el sonido si está activo), **GIF** en bucle de unos 6 s con `gifenc` e **Imagen** PNG (escena a 1600 px o QR plano en alta resolución).
- Funciona como archivo suelto, en GitHub Pages y como artifact de Claude (usa la capacidad `downloads` si existe).

## Errores comunes

- **Elementos que se salen de la celda** (hojas grandes, techos anchos, ramas laterales). Limita el desplazamiento y el tamaño para que el borde quede dentro de ±0.5 del centro de la celda.
- **Colores bonitos pero claros.** La copa rosa pastel se ve preciosa y no escanea. Usa el tono más profundo de la familia.
- **Transición que no termina recta.** La vista final debe quedar exactamente cenital y sin rotación; la plantilla deshace la órbita durante la transición.
- **Detalles animados sobre módulos claros** (coches, peces, pájaros). Desvanécelos con `vis` (1 en isométrico, 0 arriba), como las partículas de la plantilla.
