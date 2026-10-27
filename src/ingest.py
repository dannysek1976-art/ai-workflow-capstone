import os
import pandas as pd
import glob
import json

def load_data(data_dir: str = "data/") -> pd.DataFrame:
    """
    Funzione per l'acquisizione, la pulizia e l'ingestione automatizzata 
    dei dati per il caso di studio (Parte 1).
    """
    # Cerca i file JSON o CSV nella cartella dei dati
    json_files = glob.glob(os.path.join(data_dir, "*.json"))
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
    
    all_files = json_files + csv_files
    
    if not all_files:
        print("Nessun file trovato. Generazione di un dataset di esempio per il test.")
        # Dati di fallback per permettere allo script di girare correttamente
        data = {
            'invoice': ['INV-001', 'INV-002', 'INV-003'],
            'date': ['2023-01-01', '2023-01-01', '2023-01-02'],
            'price': [50.0, 120.0, 75.0]
        }
        return pd.DataFrame(data)

    dfs = []
    for f in all_files:
        if f.endswith('.json'):
            with open(f, 'r') as file:
                file_data = json.load(file)
                dfs.append(pd.DataFrame(file_data))
        elif f.endswith('.csv'):
            dfs.append(pd.read_csv(f))
            
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        
        # Pulizia degli ID delle fatture (rimozione di lettere come suggerito nelle istruzioni)
        if 'invoice' in df.columns:
            df['invoice'] = df['invoice'].astype(str).str.replace(r'[^0-9]', '', regex=True)
            
        return df
    
    return pd.DataFrame()

if __name__ == "__main__":
    df = load_data()
    print("Dati caricati con successo. Numero di righe:", len(df))
    print(df.head())
