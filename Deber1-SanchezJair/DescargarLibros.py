import requests
import os

def descargar_libro(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)

def main():
    # Lista de URLs de los libros que deseas descargar
    urls_libros = [
    "https://dev.gutenberg.org/ebooks/1342.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/84.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/46.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/11.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/6133.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/43.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1080.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/64317.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1661.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/25344.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/98.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2701.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2542.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1260.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/174.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1952.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/5200.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/16.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/844.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1232.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/120.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2852.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/219.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1400.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/205.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/76.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/345.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/74.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/16328.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/25929.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/64323.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/4014.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/514.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/23.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1250.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/408.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2591.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2097.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1497.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/45.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/158.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/160.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/4300.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2600.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/55.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/64316.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/215.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/64320.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1184.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/58585.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/76.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/40438.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2591.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/46.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1727.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1661.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/42059.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/4300.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2814.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2000.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1232.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/47475.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/6130.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1998.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/768.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/29870.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/996.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/35899.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2600.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/5740.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/39407.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/73447.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/120.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/62354.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/54023.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/1184.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/67098.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/45.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/3207.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/2852.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/5131.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/27827.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/55.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/16.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/74.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/244.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/24238.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/600.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/30254.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/205.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/23.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/514.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/7370.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/4363.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/33283.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/19926.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/73444.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/3825.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/41445.txt.utf-8",
    "https://dev.gutenberg.org/ebooks/8800.txt.utf-8"
]


    # Directorio donde guardar los libros descargados
    directorio_descargas = "descargas"

    # Crea el directorio si no existe
    if not os.path.exists(directorio_descargas):
        os.makedirs(directorio_descargas)

    # Descargar cada libro
    for idx, url in enumerate(urls_libros):
        nombre_archivo = os.path.join(directorio_descargas, f"libro_{idx + 1}.txt")
        print(f"Descargando libro {idx + 1}...")
        descargar_libro(url, nombre_archivo)
        print(f"Libro {idx + 1} descargado correctamente.")

    print("Todos los libros han sido descargados.")

if __name__ == "__main__":
    main()
