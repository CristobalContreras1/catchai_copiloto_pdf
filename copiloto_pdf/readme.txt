# CatchAI - Extracción y Procesamiento Modular de PDFs Técnicos

Este proyecto forma parte de un desafío técnico orientado a evaluar habilidades de arquitectura de software, procesamiento de texto y diseño de interfaces funcionales. La aplicación permite subir documentos PDF, extraer su contenido, fragmentarlo en bloques lógicos y visualizar los resultados de forma clara y escalable.

##  Propósito

Facilitar la ingestión y análisis de documentos técnicos en formato PDF, preparando el contenido para futuras tareas como búsqueda semántica, vectorización o entrenamiento de modelos NLP.

##  Estructura del Proyecto
CatchAI/ ├── interface/ │   └── main.py              # Interfaz Streamlit para carga y visualización ├── app/ │   ├── ingestion.py         # Extracción y fragmentación de texto desde PDF │   └── vectorizer.py        # Módulo para vectorización y análisis (en desarrollo) ├── assets/                  # Carpeta opcional para ejemplos o PDFs de prueba └── README.md     
 

##  Cómo ejecutar

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
