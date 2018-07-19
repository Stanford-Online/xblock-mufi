"""
Settings for mufi xblock
"""
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS = (
    'django_nose',
    'xblockmufi',
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

SECRET_KEY = 'xblockmufi_SECRET_KEY'
