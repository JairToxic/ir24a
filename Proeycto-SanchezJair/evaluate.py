import os
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.metrics import precision_score, recall_score, f1_score

# Configuración del modelo
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(model, image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    features = model.predict(img_array)
    return features.flatten()

# Cargar el índice de características
with open('index.pkl', 'rb') as f:
    index = pickle.load(f)

# Función para obtener las predicciones
def predict_class(features, index):
    distances = {}
    for img_path, (stored_features, label) in index.items():
        distance = np.linalg.norm(features - stored_features)
        distances[img_path] = distance
    
    # Obtener la imagen más cercana (menor distancia)
    closest_img = min(distances, key=distances.get)
    return index[closest_img][1]

# Cargar datos de prueba y etiquetas verdaderas
def load_test_data(test_data_dir):
    test_images = []
    true_labels = []
    for class_dir in os.listdir(test_data_dir):
        class_path = os.path.join(test_data_dir, class_dir)
        if os.path.isdir(class_path):
            for image_name in os.listdir(class_path):
                image_path = os.path.join(class_path, image_name)
                features = extract_features(base_model, image_path)
                test_images.append(features)
                true_labels.append(class_dir)
    return test_images, true_labels

# Evaluar el modelo
def evaluate_model(test_data_dir):
    test_images, true_labels = load_test_data(test_data_dir)
    
    predicted_labels = [predict_class(features, index) for features in test_images]
    
    precision = precision_score(true_labels, predicted_labels, average='weighted')
    recall = recall_score(true_labels, predicted_labels, average='weighted')
    f1 = f1_score(true_labels, predicted_labels, average='weighted')

    return precision, recall, f1

# Directorio de datos de prueba
test_data_dir = './data/caltech-101-test'  # Asegúrate de ajustar esto al directorio correcto

precision, recall, f1 = evaluate_model(test_data_dir)

print(f"Precisión: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
