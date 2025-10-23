import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ---------- 1️⃣ Définir la période ----------
today = datetime.today()
two_years_ago = today - timedelta(days=2*365)

start_date = two_years_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# ---------- 2️⃣ Télécharger les données ----------
df = yf.download("MSFT", start=start_date, end=end_date, interval="1d", group_by='ticker', auto_adjust=False)

# ---------- 3️⃣ Nettoyer ----------
# Si les colonnes sont multi-indexées, on les aplatit
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# On remet la date comme colonne normale
df.reset_index(inplace=True)

# On garde seulement les colonnes utiles
df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

# ---------- 4️⃣ Sauvegarder en fichier Excel ----------
excel_filename = "MSFT_2ans.xlsx"
df.to_excel(excel_filename, index=False)
print(f"✅ Fichier Excel sauvegardé : {excel_filename}")

# ---------- 5️⃣ Aperçu ----------
print(df.head())
