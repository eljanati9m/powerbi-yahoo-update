import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ---------- 1️⃣ Définir la période ----------
today = datetime.today()
two_years_ago = today - timedelta(days=2*365)

start_date = two_years_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# ---------- 2️⃣ Télécharger les données MSFT ----------
df = yf.download("MSFT", start=start_date, end=end_date, interval="1d", group_by="column")

# ---------- 3️⃣ Nettoyer et préparer ----------
df.reset_index(inplace=True)
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]  # colonnes souhaitées

# ---------- 4️⃣ Sauvegarder en CSV ----------
csv_filename = "MSFT_2ans.csv"
df.to_csv(csv_filename, index=False)
print(f"✅ CSV sauvegardé : {csv_filename}")

# ---------- 5️⃣ Aperçu ----------
print(df.head())
