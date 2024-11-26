# Proyecto de CiberSeguridad
## CleverPhis
La idea de este proyecto es crear una herramienta antiphishing que con el uso de inteligencia artificial sea más efectiva la detección y prevención de los ataques.

- **Para el analisis del contenido.** Podemos utilizar algoritmos de procesamiento del lenguaje natural (NLP) para poder analizar correos electrónicos y mensajes en busca de patrones comunes en estos ataques.

-  **Para conseguir un aprendizaje automático.** Podemos implementar modelos de aprendizaje automático que se entrenen con datos históricos de ataques de phishing para mejor la detección de amenazas nuevas.



 cleverphis/
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
