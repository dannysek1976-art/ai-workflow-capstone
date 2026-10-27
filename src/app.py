from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import os

# Configurazione del sistema di logging per il monitoraggio
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Workflow Capstone API")

class PredictionRequest(BaseModel):
    country: str
    feature_1: float

@app.get("/")
def home():
    return {"message": "API del progetto AI Capstone attiva con successo!"}

@app.post("/predict")
def predict(request: PredictionRequest):
    logger.info(f"Richiesta di predizione ricevuta per il paese: {request.country}")
    
    # Logica di predizione basata sui dati di input
    if request.country.lower() in ["tutti", "all", "global"]:
        prediction = request.feature_1 * 2.5
    else:
        prediction = request.feature_1 * 2.0
        
    return {
        "country": request.country,
        "feature_1": request.feature_1,
        "prediction": round(prediction, 2)
    }

@app.get("/logfiles")
def get_logs():
    """Endpoint per visualizzare i log di monitoraggio richiesti dal corso."""
    if os.path.exists("app.log"):
        with open("app.log", "r") as f:
            logs = f.readlines()
        return {"logs": logs[-10:]} # Restituisce gli ultimi 10 log
    return {"message": "Nessun file di log trovato."}
