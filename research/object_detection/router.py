from fastapi import UploadFile, File, APIRouter
from deployment_script import detect
from fastapi.responses import FileResponse
import shutil


router = APIRouter()

@router.post("/detect")
async def root(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = detect(image_name=file.filename)
    return FileResponse(image)

