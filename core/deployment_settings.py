import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR
ALLOWED_HOSTS=[os.environ.get("RENDER_EXTERNAL_HOSTNAME")]
CSRF_TRUSTED_ORIGINS=['https://'+os.environ.get("RENDER_EXTERNAL_HOSTNAME")]
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
MIDDLEWARE = [
     "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


# 
STORAGES:{
    "default":{
        "BACKEND":"django.core.files.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"
    }

}

# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        # default='postgresql://postgres:postgres@localhost:5432/mysite',
        default=os.environ['DATABASE_URL'],
        conn_max_age=600)
}