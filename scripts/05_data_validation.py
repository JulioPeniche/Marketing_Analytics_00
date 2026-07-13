from pathlib import Path
import pandas as pd

PROCESSED_PATH = Path("data/processed")

# Carregar tabelas


customers = pd.read_csv(
    PROCESSED_PATH / "olist_customers_dataset.csv"
)

orders = pd.read_csv(
    PROCESSED_PATH / "olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    PROCESSED_PATH / "olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    PROCESSED_PATH / "olist_order_payments_dataset.csv"
)

reviews = pd.read_csv(
    PROCESSED_PATH / "olist_order_reviews_dataset.csv"
)

products = pd.read_csv(
    PROCESSED_PATH / "olist_products_dataset.csv"
)

sellers = pd.read_csv(
    PROCESSED_PATH / "olist_sellers_dataset.csv"
)

















print("=" * 80)
print("DATA VALIDATION")
print("=" * 80)

# ------------------------------------------------------------------
# Chaves primárias duplicadas
# ------------------------------------------------------------------

print("\nDuplicidade de chaves:")

print(
    f"customers.customer_id: "
    f"{customers['customer_id'].duplicated().sum()}"
)

print(
    f"orders.order_id: "
    f"{orders['order_id'].duplicated().sum()}"
)

print(
    f"products.product_id: "
    f"{products['product_id'].duplicated().sum()}"
)

print(
    f"sellers.seller_id: "
    f"{sellers['seller_id'].duplicated().sum()}"
)

# ------------------------------------------------------------------
# Integridade referencial
# ------------------------------------------------------------------

print("\nRegistros órfãos:")

orders_without_customer = (
    ~orders["customer_id"].isin(customers["customer_id"])
).sum()

items_without_order = (
    ~order_items["order_id"].isin(orders["order_id"])
).sum()

payments_without_order = (
    ~payments["order_id"].isin(orders["order_id"])
).sum()

reviews_without_order = (
    ~reviews["order_id"].isin(orders["order_id"])
).sum()

print(f"Orders sem Customer: {orders_without_customer}")
print(f"Order Items sem Order: {items_without_order}")
print(f"Payments sem Order: {payments_without_order}")
print(f"Reviews sem Order: {reviews_without_order}")

print("\nValidação concluída.")
