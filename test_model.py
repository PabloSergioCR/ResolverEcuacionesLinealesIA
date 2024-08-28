import numpy as np
import tensorflow as tf

# Cargar el modelo entrenado, especificando la función de pérdida si es necesario
model = tf.keras.models.load_model(
    'c:/Users/Pablo/Desktop/EqLinealIA/venv/src/ecuaciones_model.h5',
    custom_objects={'MeanSquaredError': tf.keras.losses.MeanSquaredError()}
)

# Definir una función para hacer predicciones
def test_model(model, a, b):
    # Preparar la entrada en el formato adecuado
    input_data = np.array([[a, b]])
    prediction = model.predict(input_data)
    return prediction[0][0]

# Probar el modelo con valores nuevos
a_test = 5
b_test = -3

# Predicción del modelo
x_pred = test_model(model, a_test, b_test)

# Valor esperado (solución exacta)
x_real = -b_test / a_test

print(f"Para la ecuación {a_test}x + ({b_test}) = 0:")
print(f"Valor predicho por el modelo: {x_pred}")
print(f"Valor real: {x_real}")

# Medir el error
error = abs(x_pred - x_real)
print(f"Error absoluto: {error}")

