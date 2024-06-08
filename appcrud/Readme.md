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
