# Development:
```python
DEBUG = True
ALLOWED_HOSTS = ['*']
#CRSF_TRUSTED_ORIGINS = ['https://tomasteawita.com', 'https://www.tomasteawita.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres!',
        'HOST': 'postgre_db',
        'PORT': '5435'
    }
}
```

# Deployment:
```python
DEBUG = True
ALLOWED_HOSTS = ['tomasteawita.com', 'www.tomasteawita.com', 'localhost', '62.72.24.205']
CRSF_TRUSTED_ORIGINS = ['https://tomasteawita.com', 'https://www.tomasteawita.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tomasteawita_blog_db',
        'USER': 'tomasteawita',
        'PASSWORD': 'TomasteawitaProyecta2002!',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```