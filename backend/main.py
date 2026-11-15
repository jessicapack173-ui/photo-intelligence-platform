from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_DIR = "photos"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {
        "project": "Privacy-Preserving Personal Photo Intelligence Platform",
        "status": "running"
    }


@app.post("/upload")
async def upload_photo(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)

    contents = await file.read()

    with open(filepath, "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "saved_to": filepath
    }