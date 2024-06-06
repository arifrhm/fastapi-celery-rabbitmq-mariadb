from app_init import app
from tasks import reverse_name

@app.get("/{name}")
async def hello(name: str):
    reverse_name.delay(name)
    return {"message": f"Hello, {name}! Task sent to reverse your name."}
