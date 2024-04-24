import os
from flask import Flask, render_template, request

app = Flask(__name__)

def buscar_palabra(palabra, libros):
    resultados = {}
    for libro in libros:
        with open(os.path.join("descargas", libro), 'r', encoding='utf-8') as f:
            contenido = f.read()
            if palabra.lower() in contenido.lower():
                resultados[libro] = contenido.replace(palabra, f"<span style='background-color: yellow'>{palabra}</span>")
    return resultados

def resaltar_coincidencias(contenido, palabra):
    return contenido.replace(palabra, f"<span style='background-color: yellow'>{palabra}</span>")

@app.route('/', methods=['GET', 'POST'])
def index():
    palabra = None
    libros_con_coincidencias = {}
    if request.method == 'POST':
        palabra = request.form['palabra']
        libros = os.listdir("descargas")
        libros_con_coincidencias = buscar_palabra(palabra, libros)
    return render_template('index.html', palabra=palabra, libros_con_coincidencias=libros_con_coincidencias)

@app.route('/libro/<nombre_libro>')
def mostrar_libro(nombre_libro):
    with open(os.path.join("descargas", nombre_libro), 'r', encoding='utf-8') as f:
        contenido = f.read()
    palabra = request.args.get('palabra')
    if palabra:
        contenido = resaltar_coincidencias(contenido, palabra)
    return render_template('mostrar_libro.html', nombre_libro=nombre_libro, contenido=contenido, palabra=palabra)



if __name__ == '__main__':
    app.run(debug=True)
