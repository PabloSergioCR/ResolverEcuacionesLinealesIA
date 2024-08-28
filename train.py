import pandas as pd
import tensorflow as tf
from model import build_model
from sklearn.model_selection import train_test_split

# Cargar los datos
data = pd.read_csv('c:/Users/Pablo/Desktop/EqLinealIA/venv/src/ecuaciones.csv')
X = data[['a', 'b']].values
y = data['x'].values

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir el modelo
model = build_model()

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)

# Evaluar el modelo en el conjunto de prueba
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test MAE: {test_mae}")

# Guardar el modelo
model.save('c:/Users/Pablo/Desktop/EqLinealIA/venv/src/ecuaciones_model.h5')
