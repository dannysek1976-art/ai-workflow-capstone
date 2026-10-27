# IBM AI Enterprise Workflow Capstone Project

Progetto finale basato sul flusso di lavoro di Machine Learning e MLOps.

## Struttura del Progetto
- `src/ingest.py`: Script per l'acquisizione e la pulizia automatizzata dei dati.
- `src/model.py`: Script per l'addestramento e il confronto del modello di Machine Learning.
- `src/app.py`: API basata su FastAPI con endpoint di predizione e monitoraggio dei log.
- `tests/test_api.py`: Test unitari per verificare il corretto funzionamento dell'API.
- `Dockerfile`: Configurazione per la containerizzazione dell'applicazione.

## Come avviare il progetto con Docker
1. Costruisci l'immagine Docker:
   ```bash
   docker build -t ai-capstone .
