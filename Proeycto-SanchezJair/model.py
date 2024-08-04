

# Importa el módulo TensorFlow y las clases y funciones necesarias de Keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from datos import train_generator, validation_generator, batch_size  # Importa los generadores de datos y el tamaño del batch

# Define las dimensiones de entrada de las imágenes (altura y anchura)
img_height, img_width = 150, 150

# Crea un modelo secuencial de Keras, que es una forma de construir redes neuronales capa por capa
model = Sequential([
    # Capa de convolución: extrae características locales de las imágenes
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    # Capa de agrupamiento máximo: reduce las dimensiones espaciales de las características
    MaxPooling2D((2, 2)),
    
    # Capa de convolución adicional
    Conv2D(64, (3, 3), activation='relu'),
    # Otra capa de agrupamiento máximo
    MaxPooling2D((2, 2)),
    
    # Otra capa de convolución
    Conv2D(128, (3, 3), activation='relu'),
    # Otra capa de agrupamiento máximo
    MaxPooling2D((2, 2)),
    
    # Aplana las características 2D en un vector 1D para la capa densa
    Flatten(),
    
    # Capa densa completamente conectada: realiza la clasificación final
    Dense(512, activation='relu'),
    
    # Capa de salida con activación softmax: produce probabilidades para cada clase
    Dense(102, activation='softmax')  # 102 clases en total
])

# Compila el modelo: configura el optimizador, la función de pérdida y las métricas para la evaluación
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Imprime un resumen del modelo: muestra la arquitectura del modelo y los parámetros
model.summary()

# Número de épocas para el entrenamiento
epochs = 4

# Entrena el modelo usando los generadores de datos proporcionados
history = model.fit(
    train_generator,  # Generador para los datos de entrenamiento
    steps_per_epoch=train_generator.samples // batch_size,  # Número de pasos por época (batches por época)
    validation_data=validation_generator,  # Generador para los datos de validación
    validation_steps=validation_generator.samples // batch_size,  # Número de pasos de validación por época
    epochs=epochs  # Número total de épocas para entrenar el modelo
)

# Guarda el modelo entrenado en un archivo con formato HDF5
model.save('modelo_caltech101.h5')
