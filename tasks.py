from celery_init import celery

@celery.task(name='tasks.reverse_name')
def reverse_name(name: str):
    return name[::-1]
