from celery import Celery

def make_celery(app):
    celery = Celery(
        'fastapi_celery',
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery
