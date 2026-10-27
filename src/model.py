import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src.ingest import load_data

def train_model():
    """
    Funzione per l'addestramento del modello di Machine Learning (Parte 2).
    Prende i dati, crea le variabili e addestra un modello Random Forest.
    """
    df = load_data()
    
    # Controlliamo di avere i dati necessari
    if df.empty or 'price' not in df.columns:
        print("Uso dati di supporto per l'addestramento.")
        X = pd.DataFrame({'feature_1': [10, 20, 30, 40, 50], 'feature_2': [5, 15, 25, 35, 45]})
        y = pd.Series([100, 200, 300, 400, 500])
    else:
        # Preparazione delle feature basata sui dati storici
        df['feature_1'] = range(len(df))
        if 'price' in df.columns:
            y = df['price']
            X = df[['feature_1']]
        else:
            return None

    # Divisione dei dati per il training e il test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Addestramento del modello
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Valutazione
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"Modello addestrato con successo. Errore (MSE): {mse}")
    
    return model

if __name__ == "__main__":
    train_model()
