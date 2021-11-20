# Log all SQL
LOGGING = {
    "version": 1,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django.db.backends": {"level": "DEBUG"}},
    "root": {"handlers": ["console"]},
}
