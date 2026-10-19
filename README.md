# Árbol QR

Un generador de código QR que es un árbol en voxeles. Visto en isométrico es un diorama con su árbol, su pasto y su clima; visto desde arriba, la copa y el pasto forman el código QR, y se puede escanear.

**Pruébalo:** https://4strobrand-dev.github.io/arbol-qr/

## Qué hace

- Escribe cualquier enlace y el árbol se reconstruye con ese QR.
- Toca la escena para pasar de la vista árbol a la vista QR y volver.
- Cuatro estaciones: primavera con pétalos, verano con luciérnagas, otoño con lluvia y hojas que caen, invierno con nieve.
- Sonido ambiente opcional: viento, lluvia y pájaros.
- Exporta **video** vertical 1080 × 1920 para Reels o TikTok, **GIF** en bucle e **imagen** PNG.

## Cómo funciona

Cada módulo oscuro del QR que cae dentro de la copa es una columna de hojas que no se sale de su celda. Los módulos oscuros fuera de la copa, incluidos los tres cuadros de las esquinas, son matas de pasto en voxeles. Los módulos claros quedan vacíos. Con una cámara ortográfica mirando hacia abajo, todo eso se lee como un QR normal.

Hecho con [three.js](https://threejs.org/), [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) y [gifenc](https://github.com/mattdesl/gifenc).

## Haz el tuyo con Claude: la skill `qr-voxel`

La carpeta [`skill/qr-voxel`](skill/qr-voxel) es una skill para Claude que le enseña el truco completo, no solo este árbol: cómo convertir cualquier escena voxel en un QR escaneable. Trae la plantilla del Árbol QR, recetas de otros temas (ciudad, jardín de flores, arrecife de coral) y un script que comprueba que cada variante se lee.

**Instalarla en Claude:**

1. Descarga [`qr-voxel.zip`](skill/qr-voxel.zip).
2. En Claude, ve a **Customize → Skills**, toca **+ → Create skill → Upload a skill** y sube el ZIP. Necesitas tener activada la ejecución de código en **Settings → Capabilities**.
3. Pídele algo como: *"Haz un QR voxel que sea una ciudad, con variantes de día, atardecer y noche, para https://tu-enlace.com"*.

## Descargas

- [`index.html`](index.html): la herramienta completa en un solo archivo. Descárgala desde el enlace al pie de la página o desde aquí, y ábrela en cualquier navegador.
- [`skill/qr-voxel.zip`](skill/qr-voxel.zip): la skill para Claude, lista para subir.

---

Hecho por [Astrobrand](https://astrobrand.org).
