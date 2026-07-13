from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

files = sorted(RAW_PATH.glob("*.csv"))

print("=" * 80)
print("DATA CLEANING")
print("=" * 80)

for file in files:
    print(f"\nProcessando: {file.name}")

    df = pd.read_csv(file)

    # Remover linhas completamente vazias
    df = df.dropna(how="all")

    # Remover duplicatas
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    # Remover espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()

    



    # Remover espaços extras em colunas de texto
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for col in text_columns:
        df[col] = df[col].str.strip()







    output_file = PROCESSED_PATH / file.name
    df.to_csv(output_file, index=False)

    print(f"Linhas finais: {len(df):,}")
    print(f"Duplicatas removidas: {removed}")

print("\nLimpeza concluída.")
