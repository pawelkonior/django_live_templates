STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]
