# Installer les librairies si ce n'est pas déjà fait
# pip install yfinance pandas

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ---------- 1️⃣ Définir la période ----------
today = datetime.today()
five_years_ago = today - timedelta(days=5*365)  # environ 5 ans
start_date = five_years_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# ---------- 2️⃣ Liste des 40 tickers ----------
tickers = [
    "MSFT", "AAPL", "005930.KS", "NVDA", "0700.HK",
    "PFE", "JNJ", "ROG.SW", "MRNA", "SHL.DE",
    "JPM", "HSBA.L", "ALV.DE", "MS", "9984.T",
    "XOM", "TTE", "BP.L", "NEE", "0386.HK",
    "TSLA", "MC.PA", "BABA", "NKE", "7203.T",
    "NESN.SW", "KO", "ULVR.L", "PG", "BN.PA",
    "BA", "AIR.PA", "CAT", "SIE.DE", "DAL",
    "T", "VZ", "ORA.PA", "VOD.L"
]

# ---------- 3️⃣ Télécharger et combiner les données ----------
all_data = pd.DataFrame()  # DataFrame vide pour combiner

for ticker in tickers:
    print(f"⏳ Téléchargement des données pour {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date, interval="1d")
    df.reset_index(inplace=True)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df['Symbole boursier'] = ticker  # ajouter colonne ticker
    all_data = pd.concat([all_data, df], ignore_index=True)

# ---------- 4️⃣ Sauvegarder en CSV ----------
csv_filename = "40_entreprises_5ans.csv"
all_data.dropna(how='all', inplace=True)
all_data.to_csv(csv_filename, index=False, encoding='utf-8', float_format='%.2f')

print(f"✅ Toutes les données combinées enregistrées dans {csv_filename}")
