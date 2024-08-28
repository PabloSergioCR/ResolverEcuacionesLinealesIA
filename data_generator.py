import numpy as np
import pandas as pd

def generate_data(n_samples=1000):
    # Genera valores aleatorios para a y b
    a = np.random.uniform(-10, 10, n_samples)
    b = np.random.uniform(-10, 10, n_samples)
    
    # Calcula x según la fórmula ax + b = 0 => x = -b/a
    x = -b / a

    # Crea un DataFrame
    data = pd.DataFrame({'a': a, 'b': b, 'x': x})
    
    return data

if __name__ == "__main__":
    data = generate_data()
    data.to_csv("c:/Users/Pablo/Desktop/EqLinealIA/venv/src/ecuaciones.csv", index=False)
