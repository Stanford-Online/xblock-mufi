"""
Stub settings for xblock
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}
LOCALE_PATHS = [
    'xblockmufi/translations',
]
SECRET_KEY = 'SECRET_KEY'
