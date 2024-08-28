Proyecto de Regresión Lineal con TensorFlow
Este proyecto utiliza TensorFlow para construir y entrenar un modelo de regresión lineal que predice el valor de x en la ecuación lineal ax + b = 0 a partir de los coeficientes a y b. El modelo se entrena utilizando datos generados artificialmente y se guarda en un archivo HDF5.

Estructura del Proyecto
bash
Copiar código
EqLinealIA/
├── data/                   # Directorio para datos generados
├── models/                 # Directorio para modelos guardados
├── venv/                   # Entorno virtual (no se debe modificar)
  ── src/                    # Código fuente
│   ├── data_generator.py   # Script para generar datos de entrenamiento
│   ├── model.py            # Definición del modelo
│   ├── train_model.py      # Script para entrenar el modelo
│   └── test_model.py       # Script para probar el modelo
├── README.md               # Este archivo
└── requirements.txt        # Dependencias del proyecto
Instalación
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/tu_repositorio.git
cd EqLinealIA
Crear y activar el entorno virtual:

Windows:
bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:
bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instalar las dependencias:

bash
Copiar código
pip install -r requirements.txt
Uso
Generar los datos: Ejecuta el script data_generator.py para crear un archivo CSV con datos sintéticos:

bash
Copiar código
python src/data_generator.py
Entrenar el modelo: Ejecuta el script train_model.py para construir y entrenar el modelo de regresión:

bash
Copiar código
python src/train_model.py
Probar el modelo: Ejecuta el script test_model.py para evaluar el modelo entrenado con datos de prueba:

bash
Copiar código
python src/test_model.py
Archivos
data_generator.py: Genera datos sintéticos y guarda un archivo CSV en el directorio data/.
model.py: Contiene la función build_model() que define la arquitectura del modelo.
train_model.py: Entrena el modelo con datos generados y guarda el modelo entrenado en models/.
test_model.py: Carga el modelo entrenado, realiza predicciones y calcula el error en comparación con los valores reales.
requirements.txt: Lista de dependencias del proyecto.
Requisitos
Python 3.6 o superior
TensorFlow 2.x
pandas
numpy
scikit-learn
Para instalar las dependencias, asegúrate de tener un entorno virtual activo y usa el comando pip install -r requirements.txt.

Notas
Asegúrate de que el directorio data/ y el directorio models/ existen antes de ejecutar los scripts. El script data_generator.py creará el directorio data/ automáticamente si no existe, pero el directorio models/ debe ser creado manualmente si no existe.
El modelo y los datos generados están diseñados para fines de demostración y pueden no ser adecuados para aplicaciones del mundo real sin ajustes adicionales.
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request si tienes mejoras o sugerencias.

Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
