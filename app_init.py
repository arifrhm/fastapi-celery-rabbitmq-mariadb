from fastapi import FastAPI

app = FastAPI()
app.config = {
    'CELERY_BROKER_URL': 'amqp://guest:guest@rabbitmq:5672//',
    'CELERY_RESULT_BACKEND': 'db+mysql+pymysql://root:password@db:3306/fastapi_db'
}
