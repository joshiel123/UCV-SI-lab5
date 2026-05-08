from fastapi import FastAPI, UploadFile
import shutil
from lab5_metrics.services.metrics_service import analizar
app = FastAPI()
@app.post("/analyze-metrics")
def analyze(file: UploadFile):
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = analizar(path)
    return result
