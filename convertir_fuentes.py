import os
from fontTools.ttLib import TTFont

# Función para convertir TTF a WOFF2
def convertir_ttf_a_woff2(archivo_ttf, archivo_woff2):
    font = TTFont(archivo_ttf)
    font.flavor = 'woff2'
    font.save(archivo_woff2)

# Pedir la ruta de la carpeta al usuario
carpeta_fuentes = input("Ingresa la ruta de la carpeta con las fuentes .ttf: ")

# Verificar que la carpeta existe
if not os.path.isdir(carpeta_fuentes):
    print("La ruta proporcionada no es válida o no es una carpeta.")
else:
    # Recorrer todos los archivos en la carpeta
    for archivo in os.listdir(carpeta_fuentes):
        if archivo.endswith(".ttf"):  # Solo convertir archivos .ttf
            archivo_ttf = os.path.join(carpeta_fuentes, archivo)
            archivo_woff2 = os.path.join(carpeta_fuentes, archivo.replace(".ttf", ".woff2"))

            # Convertir la fuente a WOFF2
            try:
                convertir_ttf_a_woff2(archivo_ttf, archivo_woff2)
                print(f"Convertido {archivo} a {archivo.replace('.ttf', '.woff2')}")
            except Exception as e:
                print(f"Error al convertir {archivo}: {e}")
            os.remove(archivo_ttf)
            print(f"Archivo eliminado: {archivo}")