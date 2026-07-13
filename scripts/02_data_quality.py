from pathlib import Path
import pandas as pd

# Caminho da pasta de dados
DATA_PATH = Path(__file__).resolve().parent.parent / "DATA" / "raw"

files = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "translation": "product_category_name_translation.csv",
}

for name, file in files.items():
    df = pd.read_csv(DATA_PATH / file)

    print("=" * 60)
    print(f"TABELA: {name.upper()}")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")
    print(f"Duplicados: {df.duplicated().sum()}")

    print("\nValores nulos:")
    print(df.isnull().sum())
    print()
    