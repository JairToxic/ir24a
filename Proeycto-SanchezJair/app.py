from flask import Flask, request, render_template, send_from_directory, abort, url_for
import os
import pickle
from image_search import search_similar

app = Flask(__name__)

# Configura el directorio donde se guardan las imágenes
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['IMAGE_FOLDER'] = 'static/data/caltech-101'

# Cargar el índice desde el archivo
index_path = 'index.pkl'
index = None
if os.path.exists(index_path):
    with open(index_path, 'rb') as f:
        index = pickle.load(f)
    print(f'Índice cargado desde {index_path}.')
    print(f'Número de imágenes indexadas: {len(index)}')
else:
    print(f'No se encontró el archivo {index_path}. Asegúrate de que esté en el mismo directorio que app.py.')

# Ruta para servir imágenes desde el directorio 'static/caltech-101'
@app.route('/static/data/caltech-101/<category>/<filename>')
def image_file(category, filename):
    file_path = os.path.join(app.config['IMAGE_FOLDER'], category, filename)
    if os.path.exists(file_path):
        return send_from_directory(os.path.join(app.config['IMAGE_FOLDER'], category), filename)
    else:
        abort(404)  # Devolver error 404 si el archivo no se encuentra

# Ruta para la vista principal
@app.route('/', methods=['GET', 'POST'])
def index_view():
    categories = list(set(v[1] for v in index.values())) if index else []
    return render_template('index.html', categories=categories)

# Ruta para buscar imágenes similares a una imagen cargada
@app.route('/search_image', methods=['POST'])
def search_image():
    if index is None:
        return "Error: El índice no se ha cargado correctamente.", 500

    file = request.files.get('file')
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        try:
            # Guarda el archivo cargado
            file.save(file_path)
            print(f"Archivo guardado en {file_path}")

            if not os.path.isfile(file_path):
                return "Error: No se pudo guardar el archivo.", 500

            # Busca imágenes similares
            similar_images = search_similar(file_path, index)
            print(f"Imágenes similares encontradas: {similar_images}")

            # Procesa las imágenes similares
            processed_images = []
            for img_path, (sim, category) in similar_images:
                img_name = os.path.basename(img_path)
                # Normaliza las rutas de los archivos a usar barras diagonales
                processed_images.append((os.path.join(category, img_name).replace('\\', '/'), sim, category))

            print(f"Imágenes similares procesadas: {processed_images}")

            return render_template('results.html', query_image=url_for('static', filename='uploads/' + file.filename), similar_images=processed_images)
        except Exception as e:
            print(f"Error al procesar la imagen: {str(e)}")
            return f"Error: {str(e)}", 500

    return render_template('index.html')

@app.route('/search_word', methods=['POST'])
def search_word():
    if index is None:
        return "Error: El índice no se ha cargado correctamente.", 500

    category = request.form.get('category')
    if category:
        similar_images = search_similar(None, index, category)
        processed_images = []
        for img_path, sim_data in similar_images:
            sim, cat = sim_data
            img_name = os.path.basename(img_path)
            if img_path in index:
                category = index[img_path][1]
                # Asegúrate de que sim sea un número flotante
                try:
                    sim = float(sim)
                except ValueError:
                    sim = 0.0
                processed_images.append((os.path.join(category, img_name).replace('\\', '/'), sim, category))
        print(f"Imágenes similares procesadas: {processed_images}")  # Depuración
        return render_template('results.html', similar_images=processed_images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
