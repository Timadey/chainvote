"""
Django settings for chainvote project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cm^sia%a1pq8hlw^0c_c&t_szkl3aaiixg2lt@zt6)k=e5$#7-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'dids.apps.DidsConfig',
    'voting.apps.VotingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'chainvote.urls'

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

WSGI_APPLICATION = 'chainvote.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# import ipfshttpclient
# import os
# import json

# from web3 import Web3

# web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
# client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
# identity_contract_file = os.path.join(os.getcwd(), "../voting_identity/build/contracts/DecentralizedIdentity.json")
# request_contract_file = os.path.join(os.getcwd(), "../voting_identity/build/contracts/VerifiableCredentialIssuer.json")
# credential_contract_file= os.path.join(os.getcwd(), "../voting_identity/build/contracts/VerifiableCredentialRequest.json")

# with open(identity_contract_file, 'r') as file:
#     identity_data = json.load(file)
# with open(request_contract_file, 'r') as file:
#     request_data = json.load(file)
# with open(credential_contract_file, 'r') as file:
#     credential_data = json.load(file)

# IDENTITY_CONTRACT_ABI = identity_data['abi']
# IDENTITY_CONTRACT_ADDRESS = '0xf0d10CFF06AE60599f6402F5aC2aA361E0B02C8a'

# REQUEST_CONTRACT_ABI = request_data['abi']
# REQUEST_CONTRACT_ADDRESS = '0xF70ac27FbeaE7EBB5788C18794adc73126A6bAea'

# CREDENTIAL_CONTRACT_ABI = credential_data['abi']
# CREDENTIAL_CONTRACT_ADDRESS = '0x33970254CC70BA399830f45fC9f0E3EA55C77572'

# request_contract = web3.eth.contract(address=REQUEST_CONTRACT_ADDRESS, abi=REQUEST_CONTRACT_ABI)
# credential_contract = web3.eth.contract(address=CREDENTIAL_CONTRACT_ADDRESS, abi=CREDENTIAL_CONTRACT_ABI)
# identity_contract = web3.eth.contract(address=IDENTITY_CONTRACT_ADDRESS, abi=IDENTITY_CONTRACT_ABI)

