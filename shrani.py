import os
import requests
import pandas as pd

URL = r"https://cwur.org/2023.php" 
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "univerze.csv")

# prenos HTML-ja
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
odg = requests.get(URL, headers=headers)
odg.raise_for_status()#preveri napako HTML-ja

# pandas tabela
tables = pd.read_html(odg.text)

print(f"Najdenih tabel: {len(tables)}")
df = tables[0]
df.columns = df.columns.map(lambda c: c.strip() if isinstance(c, str) else c)

# Shrani datoteko kot csv
df.to_csv(CSV_PATH, index=False, encoding="utf-8")
print("Podatki shranjeni v:", CSV_PATH)