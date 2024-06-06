from app_init import app
from celery_app import make_celery

celery = make_celery(app)


# Import the tasks to ensure they are registered with the Celery app
def show_tasks():
    import tasks
    return tasks


print(show_tasks())
