from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
import os

# * create new folder estarted get image
def create_directory_get():
    folder = Path("inicio")

    if not folder.exists():
        folder.mkdir()
        return folder
    else:
        return folder
    
# * create folder set imagees
def create_directory_set():
    folder = Path("termino")

    if not folder.exists():
        folder.mkdir()
        return folder
    else:
        return folder
    

def convertir_a_jpg(archivo_webp, archivo_jpg, nuevo_tamano=None):
    imagen = Image.open(archivo_webp)
    
    # Redimensionar la imagen si se especifica un nuevo tamaño
    if nuevo_tamano:
        imagen = imagen.resize(nuevo_tamano)
    
    imagen_rgb = imagen.convert("RGB")
    imagen_rgb.save(archivo_jpg, "JPEG")


def main():
    print("start")
    load_dotenv()
    width = int(os.getenv("IMG_WIDTH"))
    height = int(os.getenv("IMG_HEIGHT"))
    folder_start = create_directory_get()
    folder_finish = create_directory_set()

    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(folder_finish):
        os.makedirs(folder_finish)
    
    # Obtener la lista de archivos en la carpeta de origen
    archivos_webp = os.listdir(folder_start)

    # Recorrer los archivos en la carpeta de origen
    for archivo_webp in archivos_webp:
        # Verificar si el archivo es una imagen WebP
        if archivo_webp.endswith(".webp"):
            # Construir la ruta completa de la imagen WebP
            ruta_webp = os.path.join(folder_start, archivo_webp)

            # Construir la ruta completa de la imagen JPG de destino
            nombre_jpg = os.path.splitext(archivo_webp)[0] + ".jpg"
            ruta_jpg = os.path.join(folder_finish, nombre_jpg)

            # Convertir la imagen WebP a JPG con redimensionamiento (opcional)
            nuevo_tamano = (width, height)  # Tamaño personalizado para redimensionar la imagen
            convertir_a_jpg(ruta_webp, ruta_jpg, nuevo_tamano)
        
        print("La conversión de imágenes WebP a JPG se ha completado.")
    else:
        print("La carpeta de origen no existe.")

    print("finish")

if __name__ == "__main__":
    main()