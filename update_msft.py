import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ---------- 1️⃣ Définir la période ----------
today = datetime.today()
two_years_ago = today - timedelta(days=2*365)

start_date = two_years_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# ---------- 2️⃣ Télécharger les données ----------
# on désactive group_by pour éviter les multi-index
df = yf.download("MSFT", start=start_date, end=end_date, interval="1d", group_by='column', auto_adjust=False)

# ---------- 3️⃣ Nettoyer ----------
# Si les colonnes sont MultiIndex, on les aplatit
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join(filter(None, col)).strip() for col in df.columns.values]

# Mettre la date comme colonne normale
df.reset_index(inplace=True)

# Choisir uniquement les colonnes nécessaires (en adaptant le nom si nécessaire)
columns_to_keep = []
for col in df.columns:
    if 'Date' in col:
        columns_to_keep.append(col)
    elif 'Open' in col:
        columns_to_keep.append(col)
    elif 'High' in col:
        columns_to_keep.append(col)
    elif 'Low' in col:
        columns_to_keep.append(col)
    elif 'Close' in col:
        columns_to_keep.append(col)
    elif 'Volume' in col:
        columns_to_keep.append(col)

df = df[columns_to_keep]


# certains environnements renvoient 'Adj Close' au lieu de 'Close', on corrige ça
if 'Adj Close' in df.columns and 'Close' not in df.columns:
    df.rename(columns={'Adj Close': 'Close'}, inplace=True)

# garder uniquement les colonnes nécessaires si elles existent
columns_to_keep = [col for col in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'] if col in df.columns]
df = df[columns_to_keep]

# ---------- 4️⃣ Sauvegarder en Excel ----------
excel_filename = "MSFT_2ans.xlsx"
df.to_excel(excel_filename, index=False)
print(f"✅ Fichier Excel sauvegardé : {excel_filename}")

# ---------- 5️⃣ Aperçu console ----------
print(df.head())
print(f"\n✅ Période : {start_date} → {end_date}")
