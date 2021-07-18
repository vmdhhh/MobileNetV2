from fastapi import FastAPI
import research.object_detection.router as router

app = FastAPI()
app.include_router(router.router, prefix='/mobilenetv2')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'YOLO is all ready to go!'