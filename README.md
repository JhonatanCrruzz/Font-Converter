# Convertir fuentes TTF a WOFF2

Este proyecto es un script en Python que convierte fuentes en formato **TTF** a **WOFF2**, un formato más optimizado para la carga rápida de sitios web. Utiliza la librería `fontTools` para realizar la conversión de manera sencilla y eficiente.

## Requisitos

- Python 3.x
- La librería **fontTools** para la manipulación de fuentes. Puedes instalarla usando pip:

  ```bash
  pip install fonttools


¿Cómo funciona?
El script realiza las siguientes acciones:

1. Solicita al usuario la ruta de la carpeta donde se encuentran las fuentes en formato .ttf.
2. Verifica si la ruta proporcionada es válida y si contiene archivos .ttf.
3. Convierte cada archivo .ttf en la carpeta a .woff2.
4. Elimina los archivos .ttf después de convertirlos con éxito.

Uso
1. Asegúrate de tener Python instalado en tu máquina.
2. Instala las dependencias necesarias:
  pip install fonttools
3. Ejecuta el script:
  python convertir_fuentes.py
4. Ingresa la ruta de la carpeta que contiene los archivos .ttf cuando se te solicite. El script convertirá todos los archivos .ttf en esa carpeta a .woff2 y eliminará los archivos .ttf originales.

Ejemplo de salida:
  Ingresa la ruta de la carpeta con las fuentes .ttf: /ruta/a/mi/carpeta
  Convertido fuente1.ttf a fuente1.woff2
  Archivo eliminado: fuente1.ttf
  Convertido fuente2.ttf a fuente2.woff2
  Archivo eliminado: fuente2.ttf

Consideraciones
- Este script solo convierte archivos .ttf que se encuentren en la carpeta especificada.
- Los archivos .woff2 generados se almacenan en la misma carpeta donde están los archivos .ttf.
- Los archivos .ttf se eliminan después de la conversión exitosa. Si prefieres conservar los archivos .ttf, puedes eliminar o modificar la línea os.remove(archivo_ttf).

Contribución
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request. ¡Cualquier mejora es bienvenida!
