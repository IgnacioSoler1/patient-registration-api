Patient Registration API
========================

Este es un proyecto de API para el registro de pacientes, desarrollado con FastAPI y SQLAlchemy. Permite registrar pacientes, almacenar sus datos y enviar correos electrónicos de confirmación.

📁 Estructura del Proyecto
--------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   PATIENT-REGISTRATION-API  │── app  │   ├── api  │   │   ├── patients.py         # Endpoints relacionados con los pacientes  │   ├── db  │   │   ├── database.py         # Configuración de la base de datos  │   ├── models  │   │   ├── patient.py          # Definición del modelo de paciente  │   ├── schemas  │   │   ├── patient.py          # Esquemas para validación de datos  │   ├── services  │   │   ├── email.py            # Función para enviar correos electrónicos  │   ├── config.py               # Configuración de variables de entorno  │   ├── main.py                 # Punto de entrada de la API  │── .env                        # Variables de entorno  │── .gitignore                   # Archivos a ignorar en Git  │── compose.yaml                 # Configuración para Docker Compose  │── Dockerfile                   # Configuración para contenedor Docker  │── README.md                    # Documentación del proyecto  │── requirements.txt              # Dependencias del proyecto   `

🚀 Instalación y Configuración
------------------------------

### 1️⃣ Clonar el repositorio

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/tu-usuario/patient-registration-api.git  cd patient-registration-api   `

### 2️⃣ Crear entorno virtual e instalar dependencias

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   python3 -m venv env  source env/bin/activate  # En Windows usa `env\Scripts\activate`  pip install -r requirements.txt   ``

### 3️⃣ Configurar variables de entorno

Renombrar el archivo .env.example a .env y completar los valores necesarios.

### 4️⃣ Ejecutar la API

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uvicorn app.main:app --reload   `

La API estará disponible en http://127.0.0.1:8000.

📌 Endpoints
------------

### 1️⃣ Registro de Paciente

**POST** /register

*   **Descripción:** Registra un nuevo paciente y almacena su información en la base de datos.
    
*   **Cuerpo de la solicitud:**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "name": "Juan Pérez",    "email": "juan@example.com",    "phone": "+598 91234567",    "document_blob": ""  }   `

*   **Respuesta exitosa (201):**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "id": 1,    "name": "Juan Pérez",    "email": "juan@example.com",    "phone": "+598 91234567"  }   `

*   **Errores posibles:**
    
    *   400 Email ya registrado.
        

### 2️⃣ Obtener Lista de Pacientes

**GET** /patients

*   **Descripción:** Retorna todos los pacientes registrados.
    
*   **Respuesta exitosa (200):**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   [    {      "id": 1,      "name": "Juan Pérez",      "email": "juan@example.com",      "phone": "+598 91234567"    }  ]   `

### 3️⃣ Obtener Paciente por ID

**GET** /patients/{patient\_id}

*   **Descripción:** Retorna los datos de un paciente en base a su ID.
    
*   **Respuesta exitosa (200):**
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "id": 1,    "name": "Juan Pérez",    "email": "juan@example.com",    "phone": "+598 91234567"  }   `

*   **Errores posibles:**
    
    *   404 Paciente no encontrado.
        

🛠 Tecnologías Utilizadas
-------------------------

*   **FastAPI** → Framework para APIs rápidas y eficientes
    
*   **SQLAlchemy** → ORM para manejo de base de datos
    
*   **SQLite/PostgreSQL** → Base de datos utilizada
    
*   **Docker** → Contenedorización del proyecto
    
*   **Postman** → Para probar los endpoints