"""Comprueba que cada variante de una pieza QR voxel se pueda escanear.

Abre el HTML en Chromium sin ventana, pasa por cada botón de variante (los que
tienen atributo data-s), cambia a la vista de arriba tocando la escena, toma una
captura del lienzo y la decodifica con OpenCV.

Uso:
    pip install playwright opencv-python-headless
    python -m playwright install chromium
    python verificar_qr.py pieza.html [--esperado https://ejemplo.com] [--capturas carpeta]

Requiere conexión a internet para cargar three.js y las demás librerías desde CDN.
OpenCV es más exigente que la cámara de un teléfono: si aquí lee, el teléfono lee.
"""
import argparse
import asyncio
import pathlib
import sys

import cv2
from playwright.async_api import async_playwright


async def revisar(ruta, esperado, carpeta):
    url = pathlib.Path(ruta).resolve().as_uri()
    detector = cv2.QRCodeDetector()
    resultados = []
    async with async_playwright() as p:
        nav = await p.chromium.launch(args=['--use-gl=swiftshader', '--ignore-gpu-blocklist'])
        pag = await nav.new_page(viewport={'width': 700, 'height': 1000})
        await pag.goto(url)
        await pag.wait_for_selector('#stage canvas', timeout=30000)
        await pag.wait_for_timeout(2500)
        variantes = await pag.eval_on_selector_all('[data-s]', 'bs => bs.map(b => b.dataset.s)')
        if not variantes:
            variantes = [None]
        for v in variantes:
            if v:
                await pag.click(f'[data-s="{v}"]')
                await pag.wait_for_timeout(1500)
            await pag.click('#stage')
            # El renderizado por software es lento: se espera de más para que la transición termine
            await pag.wait_for_timeout(4000)
            archivo = carpeta / f'qr_{v or "unica"}.png'
            await pag.locator('#stage canvas').screenshot(path=str(archivo))
            texto, _, _ = detector.detectAndDecode(cv2.imread(str(archivo)))
            ok = bool(texto) and (esperado is None or texto == esperado)
            resultados.append((v or 'única', ok, texto))
            await pag.click('#stage')
            await pag.wait_for_timeout(1500)
        await nav.close()
    return resultados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('html', help='ruta del archivo HTML de la pieza')
    ap.add_argument('--esperado', help='texto que debe contener el QR (por defecto, cualquiera)')
    ap.add_argument('--capturas', default='capturas_qr', help='carpeta donde guardar las capturas')
    a = ap.parse_args()
    carpeta = pathlib.Path(a.capturas)
    carpeta.mkdir(parents=True, exist_ok=True)
    resultados = asyncio.run(revisar(a.html, a.esperado, carpeta))
    fallas = 0
    for nombre, ok, texto in resultados:
        estado = 'LEE   ' if ok else 'NO LEE'
        detalle = texto if texto else '(sin lectura)'
        print(f'{estado}  {nombre:<12} {detalle}')
        fallas += 0 if ok else 1
    print(f'\nCapturas en: {carpeta.resolve()}')
    if fallas:
        print('Oscurece la paleta del elemento principal o del borde en las variantes que no leen y vuelve a probar.')
    sys.exit(1 if fallas else 0)


if __name__ == '__main__':
    main()
