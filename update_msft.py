import pandas as pd
from datetime import datetime
import yfinance as yf

# Télécharger les données Microsoft (2 ans)
ticker = "MSFT"
data = yf.download(ticker, period="2y")

# Sauvegarder dans OneDrive (chemin du fichier synchronisé)
output_path = "MSFT_2ans.csv"
data.to_csv(output_path)

print(f"✅ Données mises à jour : {datetime.now()}")
