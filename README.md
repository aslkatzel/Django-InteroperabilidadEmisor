# SISTEMA AUTOMATIZADO WEB PARA LA INTEROPERABILIDAD ENTRE LA FUNDACIÓN CENDITEL Y EL MPPEUCT MEDIANTE UNA APLICACIÓN REST

**Caso:** Área de Desarrollo de la Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres

**Trabajo Especial de Grado para Optar al Título de Técnico Superior Universitario en la Especialidad de Informática**

**Autor:** Jhonathan Salas Segura


## Software Utilizado

* Python 3.5.3
* Django 1.9.5
* Django REST 3.6.3
* PostgreSQL

## Software Requerido

    # apt-get install python-pip python-virtualenv
    
    # apt-get install postgresql pgadmin3

### Instalación del Sistema

    $ git clone https://github.com/aslkatzel/Web-Portafolio.git
    
    $ virtualenv -p /usr/bin/python3 entorno-emisor
    
    $ pip install -r requirements/base.txt
    
    $ python manage.py makemigrations registro
    
    $ python manage.py migrate
    
    $ python manage.py createsuperuser
    
    $ python manage.py runserver 8002

### Configuración del Sistema 

Se debe ir a la opción de **Token de Autenticación**, en donde se debe generar una clave que otorgaremos al sistema receptor para que él pueda procesar nuestros datos.


