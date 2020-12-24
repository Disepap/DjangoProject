from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o**-k@8eps*bn1%)kw$i%2!md#5cjhdc&63bi#xpquuxtm5exk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'material.admin',
    'material.admin.default',
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school.apps.SchoolConfig',
    'rest_framework',
    'import_export',
    
    #'material.admin.default',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schoolsoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'schoolsoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

###Materialize admin
MATERIAL_ADMIN_SITE = {
    #'HEADER':  ('Your site header'),  # Admin site header
    #'TITLE':  ('Your site title'),  # Admin site title
    #'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR': '#875a7b',#4a104e', #'#1A1A1D',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  '#00a09d',#8a1a47', #'#950740',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE': 'images/se.jpg',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'images/white.jpg',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'images/se.jpg',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'images/purple.jpg',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  False,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        #'sites': 'send',
        'school':'apps'
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        #'site': 'contact_mail',
        'classe': 'domain',
        'eleve': 'people_outline',
        'annee':'event_available',
        'matiere':'storage',
        'moyenne':'receipt',
        'professeur':'people',
        'section':'widgets',
        'inscription':'person_add',
        
    }
}