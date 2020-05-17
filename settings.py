import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'db',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRESQL_SCHEMA"),
        'USER': os.getenv("POSTGRESQL_USER"),
        'PASSWORD': os.getenv("POSTGRESQL_PWD"),
        'HOST': os.getenv("POSTGRESQL_HOST"),
        'PORT': os.getenv("POSTGRESQL_PORT"),
    }
}


# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'
