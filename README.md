# Proyecto de CiberSeguridad
## CleverPhis
La idea de este proyecto es crear una herramienta antiphishing que con el uso de inteligencia artificial sea más efectiva la detección y prevención de los ataques.

- **Para el analisis del contenido.** Podemos utilizar algoritmos de procesamiento del lenguaje natural (NLP) para poder analizar correos electrónicos y mensajes en busca de patrones comunes en estos ataques.

-  **Para conseguir un aprendizaje automático.** Podemos implementar modelos de aprendizaje automático que se entrenen con datos históricos de ataques de phishing para mejor la detección de amenazas nuevas.



```plaintext
# cleverphis/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── data/
│   ├── phishing_dataset.csv  # Dataset para entrenar modelos
│   ├── processed/            # Archivos procesados
│   └── raw/                  # Archivos sin procesar
├── database/
│   └── init.sql              # Script de inicialización de la base de datos
├── src/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # Punto de entrada para la API y chatbot
│   │   ├── routes.py         # Rutas de la API
│   │   └── utils.py          # Funciones auxiliares (como validación de input)
│   ├── models/
│   │   ├── phishing_model.pkl # Modelo de aprendizaje automático
│   │   └── train_model.py    # Script de entrenamiento
│   ├── nlp/
│   │   ├── analyze.py        # Procesamiento del lenguaje natural
│   │   └── patterns.py       # Patrones de phishing
│   ├── database/
│   │   ├── db.py             # Configuración de la base de datos
│   │   └── queries.py        # Consultas específicas
│   └── security/
│       ├── secure_code.py    # Funciones de aseguramiento del código
│       └── validation.py     # Validaciones de datos de entrada
└── tests/
    ├── test_app.py           # Tests para la aplicación
    ├── test_nlp.py           # Tests para procesamiento de lenguaje natural
    └── test_model.py         # Tests para el modelo
```



















1. Arquitectura General
La aplicación está basada en Flask, un microframework web de Python, y utiliza PostgreSQL como base de datos para almacenar los correos electrónicos y su clasificación. Además, hace uso de modelos de machine learning entrenados para detectar correos de phishing. La estructura general de la aplicación es:

API Flask: Un servicio web que recibe correos electrónicos a través de una API RESTful.
Modelo de Machine Learning: Un modelo entrenado en un conjunto de datos de correos electrónicos para clasificar si un correo es phishing o no.
Base de Datos: Utiliza PostgreSQL para almacenar correos electrónicos y su clasificación.
2. Componentes Clave
Archivos de configuración:
docker-compose.yml: Define la configuración de los contenedores Docker. Incluye:

Un contenedor para la aplicación Flask (app), que está vinculado a un contenedor de base de datos PostgreSQL (db).
Variables de entorno para la base de datos (como usuario, contraseña y nombre de la base de datos).
Dockerfile: Especifica cómo construir la imagen del contenedor para la aplicación Flask, configurando el entorno necesario con las dependencias especificadas en requirements.txt.

requirements.txt: Lista las dependencias del proyecto, que incluyen Flask, SQLAlchemy, scikit-learn (para machine learning), y otras bibliotecas necesarias como pandas, numpy, y transformers.

Flask API:
main.py: El archivo principal de la aplicación Flask. Configura la aplicación, inicializa las rutas y ejecuta el servidor.
routes.py: Define la ruta /analyze que recibe una solicitud POST con el contenido de un correo electrónico y devuelve si es phishing o no. Se utiliza la función analyze_email de nlp/analyze.py para el análisis y la función save_email de database/queries.py para almacenar los resultados.
Análisis de correos electrónicos:
analyze.py: Contiene la lógica para analizar un correo electrónico usando un modelo de clasificación de phishing entrenado. Este modelo se carga desde un archivo .pkl (entrenado previamente en train_model.py) y se utiliza para predecir si el contenido del correo es phishing.
Entrenamiento del modelo de phishing:
train_model.py: Este archivo entrena un modelo de machine learning para detectar correos de phishing utilizando un conjunto de datos en data/phishing_dataset.csv. El modelo usa un vectorizador TF-IDF para convertir el texto en una representación numérica y luego entrena un clasificador RandomForest. Los archivos del modelo y el vectorizador entrenados se guardan en src/models/.
Base de datos:
db.py: Configura la conexión a la base de datos PostgreSQL usando SQLAlchemy.
queries.py: Define la función save_email, que se utiliza para guardar los correos electrónicos analizados en la base de datos, junto con la clasificación (si es phishing o no).
Seguridad:
secure_code.py: Contiene una función para hashear el contenido de los correos electrónicos, lo que puede ser útil para almacenar de forma segura los datos sensibles, como el contenido de los correos.
Pruebas:
test_app.py: Realiza pruebas unitarias para verificar que la ruta /analyze funciona correctamente.
3. Flujo de la Aplicación
Inicio de la Aplicación: Cuando se ejecuta la aplicación (main.py), Flask se inicia y expone una API REST en el puerto 5000.
Recepción del Correo: Un cliente realiza una solicitud POST a la ruta /analyze con el contenido de un correo electrónico en formato JSON.
Análisis del Correo: El contenido del correo se pasa a la función analyze_email (en analyze.py), que usa el modelo previamente entrenado para predecir si el correo es phishing o no.
Almacenamiento del Resultado: El correo, junto con su clasificación, se guarda en la base de datos PostgreSQL mediante la función save_email.
Respuesta: El servidor devuelve una respuesta JSON que indica si el correo es phishing o no.
4. Base de Datos
La base de datos PostgreSQL contiene una tabla llamada phishing_emails (definida en init.sql), donde se almacenan los correos electrónicos y su clasificación. La tabla tiene los siguientes campos:

id: Un identificador único para cada correo.
email_content: El contenido del correo.
is_phishing: Un valor booleano que indica si el correo es phishing.
created_at: La fecha y hora en que se guardó el correo.
5. Modelo de Machine Learning
El modelo de clasificación de phishing se entrena usando un conjunto de datos de correos electrónicos etiquetados (en data/phishing_dataset.csv). El modelo es un clasificador RandomForest, que se entrena con características extraídas del texto de los correos utilizando un TF-IDF Vectorizer. Este modelo se guarda como un archivo .pkl y se carga cada vez que se realiza una predicción.

En resumen, la aplicación toma correos electrónicos, los procesa para detectar phishing utilizando un modelo de machine learning, guarda los resultados en una base de datos y expone una API para interactuar con estos servicios. La estructura está diseñada para ser escalable y segura, con pruebas automáticas que garantizan el correcto funcionamiento de la API.
    
    


## Uso de IA

![](https://i.postimg.cc/QdrDmBwX/ollama.png)

Ollama nos permite ejecutar modelos de lenguaje a gran escala de manera local.
Esta aplicación nos facilita la generación de contenido y el análisis avanzado de datos, utilizando redes neuronales profundas para comprender y producir lenguaje natural.


## Uso de Ollama
Hemos elegido el modelo Codellama con el que trabajaremos en adelante.

Podemos iniciarlo e interactuar con este desde la terminal.


`# ollama run codellama:latest` 

![](https://i.postimg.cc/kGBJ0kvq/terminal.png)


## Open WeubUI
Tenemos la posibilidad de configurar una interfaz web para trabajar con nuestro modelo.
Para ello vamos a ejecutar un contenedor Docker con la imagen `ghcr.io/open-webui/open-webui:main` y lo configuramos de la siguiente manera:

`# docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main`


Una vez hecho esto, desde el navegador accedemos a `http://localhost:3000` y accedemos a la interfaz web donde acedemos con nuestras credenciales para poder operar con el modelo de IA que estamos trabajando.

![](https://i.postimg.cc/brWyp3mb/web1.png)

![](https://i.postimg.cc/CMQLGxw1/web2.png)
