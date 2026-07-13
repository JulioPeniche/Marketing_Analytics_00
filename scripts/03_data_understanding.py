from pathlib import Path
import pandas as pd

# Caminho da pasta raw
RAW_PATH = Path("data/raw")

# Arquivos CSV
files = sorted(RAW_PATH.glob("*.csv"))

print("=" * 80)
print("DATA UNDERSTANDING")
print("=" * 80)

for file in files:
    print(f"\n📄 Tabela: {file.stem}")

    df = pd.read_csv(file)

    print(f"Linhas: {df.shape[0]:,}")
    print(f"Colunas: {df.shape[1]}")

    print("\nColunas:")
    print(df.columns.tolist())

    print("\nTipos:")
    print(df.dtypes)

    print("\nPrimeiras linhas:")
    print(df.head(3))

    print("-" * 80)
    