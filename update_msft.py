# Installer les librairies si ce n'est pas déjà fait
# pip install yfinance pandas

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ---------- 1️⃣ Définir la période ----------
today = datetime.today()
two_years_ago = today - timedelta(days=2*365)  # environ 2 ans

# Format pour affichage/filtrage
start_date = two_years_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# ---------- 2️⃣ Télécharger les données MSFT ----------
msft = yf.Ticker("MSFT")

df = msft.history(start="2023-01-01", end="2024-12-31", interval="1d")  # données quotidiennes

#df = msft.history(start=start_date, end=end_date, interval="1d")  # données quotidiennes

# ---------- 3️⃣ Nettoyer et préparer ----------
df.reset_index(inplace=True)  # mettre la date dans une colonne normale
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]  # garder seulement les colonnes utiles

# ---------- 4️⃣ Sauvegarder en CSV ----------
csv_filename = "MSFT_2ans.csv"
df.dropna(how='all', inplace=True)
df.to_csv(csv_filename, index=False, encoding='utf-8', float_format='%.2f')
