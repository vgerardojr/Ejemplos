# Django ajustes de proyecto recetario.
# -*- encoding: utf-8 -*-
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
    ('FLTSB', 'fltsimonbolivar@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Agregar 'postgresql_psycopg2', 'mysql', 'sqlite3' o 'oracle'.
        'NAME': 'recetario.db',                      # O la ruta al archivo de base de datos si se utiliza sqlite3.
        # Los siguientes ajustes no se utilizan con sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Vacío para localhost a través de sockets de dominio o '127 .0.0.1 'para localhost a través de TCP.
        'PORT': '',                      # Se establece en una cadena vacía para el valor predeterminado.
    }
}

# Hosts / nombres que son válidos para este sitio de dominio, necesarios si DEBUG es False
# Ver https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Zona horaria local para esta instalación. Las opciones se pueden encontrar aquí:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# aunque no todas las opciones pueden estar disponibles en todos los sistemas operativos.
# En un entorno Windows, esta debe estar en la zona horaria del sistema.
TIME_ZONE = 'America/Caracas'

# Código de idioma para esta instalación. Todas las opciones se pueden encontrar aquí:
# 
LANGUAGE_CODE = 'es-VE'

SITE_ID = 1

# Si lo ajusta a False, Django hará algunas optimizaciones para no
# cargar la maquinaria de internacionalización.
USE_I18N = True

# Si lo ajusta a False, Django no formateará fechas, números y
# calendarios de acuerdo a la localización actual.
USE_L10N = True

# Si lo ajusta a False, Django no utilizará datetimes zona horaria con conciencia.
USE_TZ = True

# Ruta del sistema de archivos absoluta al directorio que contiene los archivos subidos por los usuarios.
# Ejemplo: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'carga')

# URL que controla los medios de comunicación sirven de MEDIA_ROOT. Asegúrese de utilizar una
# barra diagonal.
# Ejemplos: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Ruta absoluta a los archivos estáticos del directorio se debe recoger al.
# No coloque nada en este directorio usted mismo, almacenar sus archivos estáticos
# en apps' "static/" subdirectorios aplicaciones estáticas STATICFILES_DIRS.
# Ejemplo: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefijo para los archivos estáticos.
# Ejemplo: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Ubicaciones adicionales de archivos estáticos
STATICFILES_DIRS = (
    # Ponga las cadenas aquí, como "/ home / html / estática" o "C :/ www / django / static".
    # Siempre utilice barras inclinadas, incluso en Windows.
    # No te olvides de utilizar rutas absolutas, no rutas relativas.
)

# Lista de clases del buscador que saben cómo encontrar archivos estáticos en
# diferentes lugares.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Haga esto privado, y no lo comparta con nadie.
SECRET_KEY = '6%li_&5s)*kj96@is57i8r^ur0h6s653v#amj1%25=t6spbc^^'

# Lista de callables que saben cómo importar plantillas de diversas fuentes.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Elimine el comentario de la línea siguiente para la protección de clickjacking simple:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recetario.urls'

# Python ruta de puntos para la aplicación WSGI utilizado por runserver de Django.
WSGI_APPLICATION = 'recetario.wsgi.application'

TEMPLATE_DIRS = (

 os.path.join(RUTA_PROYECTO,'plantillas'),
    # Poner direccion aquí, como "/ home / html / django_templates" o "C :/ www / django / templates".
    # Utilice siempre barras inclinadas, incluso en Windows.
    # No te olvides de usar rutas absolutas, no las rutas relativas.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',

    # Elimine el comentario de la siguiente línea para habilitar el administrador:
    'django.contrib.admin',
    # Elimine el comentario de la siguiente línea para habilitar la documentación de administración:
    'django.contrib.admindocs',
)

# Una muestra de la configuración del registro. El único registro tangible
# realizado por esta configuración es enviar un correo electrónico a
# los administradores del sitio en cada error HTTP 500 cuando DEBUG = False.
# Ver http://docs.djangoproject.com/en/dev/topics/logging para
# más detalles sobre cómo personalizar la configuración de registro.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}