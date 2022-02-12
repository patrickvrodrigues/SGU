import os
import ldap
from django_auth_ldap.config import LDAPSearch
from decouple import config


AUTH_LDAP_SERVER_URI = 'ldap://192.168.31.115'
AUTH_LDAP_BIND_DN = "CN=bind,CN=Users,"+config('PATH_LDAP')
AUTH_LDAP_BIND_PASSWORD = config('PASSWORD_BIND')
AUTH_LDAP_USER_SEARCH = LDAPSearch(
            config('PATH_LDAP'), ldap.SCOPE_SUBTREE, "sAMAccountName=%(user)s"
            )

AUTH_LDAP_USER_ATTR_MAP = {
            "username": "sAMAccountName",
                "first_name": "givenName",
                    "last_name": "sn",
                        "email": "mail",
}
from django_auth_ldap.config import ActiveDirectoryGroupType
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
            config('PATH_LDAP'), ldap.SCOPE_SUBTREE, "(objectCategory=Group)"
            )
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr="cn")
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
            "is_superuser": "CN=django-admins,CN=Users,"+config('PATH_LDAP'),
            "is_staff": "CN=django-admins,CN=Users,"+config('PATH_LDAP'),
            }
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1  # 1 hour cache

AUTHENTICATION_BACKENDS = [
            'django_auth_ldap.backend.LDAPBackend',
            #'organization.custom_ldap.CustomLDAPBackend',
                'django.contrib.auth.backends.ModelBackend',
]
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}







# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5q&q^3twnv20a71(qi0dg#-(6btp5#i-pu&so8s5h%z#gt-%&e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuario',
    'rest_framework',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
