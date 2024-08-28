import tensorflow as tf
from tensorflow.keras import layers, models

def build_model():
    model = models.Sequential([
        layers.Dense(10, activation='relu', input_shape=(2,)),
        layers.Dense(10, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['mae'])
    return model
