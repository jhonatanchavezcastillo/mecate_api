Fuente: https://www.youtube.com/watch?v=GE0Q8YNKNgs&t=2s
#API Mecate
#Instalacción del ambiente de desarrollo
1.- Instalar Python 3.10.6
2.- Crea un entorno virtual dentro de tu proyecto
    pip install virtualenv
3.- Crear la carpeta venv para poder usar el entorno virtual
    python -m virtualenv venv
4.- Por seguridad sugiero que habilites el uso de este script en tu pc solo lo que dura la sesión del PowerShell para evitar ejcución de Scripts maliciosos.
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
4.- Activar el entorno virtual
    .\venv\Scripts\activate
5.- Instalar django 5.0 (Framework para Python)
    pip install django 
6.- Instalar Django Rest Framework para poder usar un módulo con funcionalidades para crear nuestra API-REST
    pip install djangorestframework
7.- Crear proyecto dentro del directorio actual
    django-admin startproject projectcrud .
8.- Correr el servidor #http://127.0.0.1:8000/ #controll + C para detener
    python manage.py runserver
9.- Crear una aplicación carpeta appcrud
    python manage.py startapp appcrud
10.- Agregar en setting la aplicación para que el proyecto django reconozca la app appcrud
    Abre el archivo projectcrud/settings.py y agrega en el array INSTALLED_APPS el nombre de tu aplicación: "appcrud" y añadir el módulo "rest_framework"

#Crear modelo de proyectos
1.- Dentro de appcrud/models.py crear las tablas
2.- Crear las migraciones 
    python manage.py makemigrations
3.- Ejecutar migraciones
    python manage.py migrate
3.- Crear nuestros endpoint #fuente https://www.django-rest-framework.org/
4.- Crear un modelo especial de Rest Framework mediante la creación del archivo appcrud/serializers.py
5.- Crear archivo appcrud/api.py

#Crear archivo de ruteo
1.- Crear archivo appcrud/urls.py 
2.- Permitir que nuestro proyecto reconozca las rutas de nuestra appcrud
	Abrir el archivo projectcrud/appcrud.py e importar las rutas

#Subir a repositorio de Git
1.- Crear en raíz el archivo .gitignore para seleccionar los archivos que no se van a subir al repo.
2.- git add . 
3.- git commit -m "first commit"
4.- Subir al repositorio en GitHub

#Desplegar proyecto en servidor de render.com
#Fuente https://docs.render.com/deploy-django
1.- Crea una cuenta en render.com
2.- Importa la librería os de python en projectcrud/setting.py
    #from pathlib import Path
    import os
3.- Actualizar SECRET_KEY en project/setting.py
    SECRET_KEY = os.environ.get('SECRET_KEY', default='Your secret key')
4.- Actualizar DEBUG en project/setting.py para que no arroje información en producción
    DEBUG = 'RENDER' not in os.environ
5.- Actualizar Allow_host en project/setting.py
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
6.- Generar base de datos en render.com (PostgreSQL)
7.- Instalar dos módulos para base de datos
    pip install dj-database-url psycopg2-binary

    - #dj-database-url Comprueba si existe una variable de entorno llamada DATABASE, si existe lo asigna a nuesta base de datos.

    -#psycopg2-binary Módulo para conectarnos a PostgresSql
8.- Importar dj_database_url en project/setting.py
    import dj_database_url
9.- Actualizar en project/setting.py
    DATABASES = {
        'default': dj_database_url.config(
            # Replace this value with your local database's connection string.
            default='postgresql://postgres:postgres@localhost:5432/mysite',
            conn_max_age=600
        )
    }
10.- En este paso, configuraremos WhiteNoise para que proporcione estos activos estáticos desde el servidor web de Render.
    pip install whitenoise[brotli]
11.- Añade el módulo whitenoise en project/setting.py
    #Agregar en MIDDLEWARE 
     'whitenoise.middleware.WhiteNoiseMiddleware',
12.- Agregar en project/setting.py para crear carpeta con archivos estáticos
STATIC_URL = 'static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
13.- Crear en raíz un build.sh con todos los comandos de ejecución instalación del proyecto.
14.- Genera un archivo requirements.txt con todos los módulos que usamos 
    pip freeze > requirements.txt
15.- Otorgar permisos de ejecución a build.sh desde terminal git bash
    chmod a+x build.sh
16.- Instalar módulo gunicorn para poder mostrar contenido estático como imágenes, css.
    pip install gunicorn
17.- Añadir gunicorn en el requirements.txt
    pip freeze > requirements.txt
18.- Actualizar los archivos de git
    git status
    git add .
    git commit -m "Proyecto listo para subir a render.com"
    git push origin master
19.- Crear repositorio en nuestro repositorio de GitHub
20.- Agregar comando en terminal
    git remote add origin git@github.com:jhonatanchavezcastillo/mecate_api.git

    git push -u origin master #subir a github proyecto
21.- Seleccionar el repo desde render.com
    Ir a la cuenta de github para seleccinoar el repo

    ir a https://dashboard.render.com/select-repo?type=web
    y conectar con el repo.
22.- En la interface de render agregar lo siguiente
    Build Command: ./build.sh
    Start Command: gunicorn projectcrud.wsgi
    Enviroment Variable:
        DATABASE_URL = "internal DataBase URL" # Esto lo encuentras en el panel

        SECRET_KEY = "Busca una en randomkeygen.com"

        PYTHON_VERSION = "Mi versión de python" #python --version
23.- URL DEL SERVIDOR: https://mecate-api.onrender.com/


#Consumir servicios externos
1.- Crear un archivo appcrud/services.py y agregar la función para consumo externo
2.- Crea un archivo appcrud/views.py para importar la función de services.py
3.- Agregar la url en archivo appcrud/urls.py

#Habilitar peticiones "Corse"
pip install django-cors-headers

