from pathlib import Path
import pandas as pd

# Caminhos
PROCESSED_PATH = Path("data/processed")
ANALYTICS_PATH = Path("data/analytics")

ANALYTICS_PATH.mkdir(parents=True, exist_ok=True)

# Carregar tabelas
customers = pd.read_csv(PROCESSED_PATH / "olist_customers_dataset.csv")
orders = pd.read_csv(PROCESSED_PATH / "olist_orders_dataset.csv")
order_items = pd.read_csv(PROCESSED_PATH / "olist_order_items_dataset.csv")
payments = pd.read_csv(PROCESSED_PATH / "olist_order_payments_dataset.csv")
reviews = pd.read_csv(PROCESSED_PATH / "olist_order_reviews_dataset.csv")
products = pd.read_csv(PROCESSED_PATH / "olist_products_dataset.csv")
sellers = pd.read_csv(PROCESSED_PATH / "olist_sellers_dataset.csv")

print("=" * 80)
print("CREATE FACT SALES")
print("=" * 80)

print(f"Customers:    {customers.shape}")
print(f"Orders:       {orders.shape}")
print(f"Order Items:  {order_items.shape}")
print(f"Payments:     {payments.shape}")
print(f"Reviews:      {reviews.shape}")
print(f"Products:     {products.shape}")
print(f"Sellers:      {sellers.shape}")



# ------------------------------------------------------------------------------
# JOIN: Orders + Customers
# ------------------------------------------------------------------------------

fact_sales = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print("\nApós JOIN Orders + Customers")
print(f"Shape: {fact_sales.shape}")


# ------------------------------------------------------------------------------
# JOIN: Fact Sales + Order Items
# ------------------------------------------------------------------------------

fact_sales = fact_sales.merge(
    order_items,
    on="order_id",
    how="left"
)

print("\nApós JOIN com Order Items")
print(f"Shape: {fact_sales.shape}")


# ------------------------------------------------------------------------------
# JOIN: Fact Sales + Products
# ------------------------------------------------------------------------------

fact_sales = fact_sales.merge(
    products,
    on="product_id",
    how="left"
)

print("\nApós JOIN com Products")
print(f"Shape: {fact_sales.shape}")



# ------------------------------------------------------------------------------
# JOIN: Fact Sales + Sellers
# ------------------------------------------------------------------------------

fact_sales = fact_sales.merge(
    sellers,
    on="seller_id",
    how="left"
)

print("\nApós JOIN com Sellers")
print(f"Shape: {fact_sales.shape}")



# ------------------------------------------------------------------------------
# Agrupar pagamentos por pedido
# ------------------------------------------------------------------------------

payments = (
    payments
    .groupby("order_id", as_index=False)
    .agg(
        payment_value=("payment_value", "sum")
    )
)

print("\nPayments agrupado")
print(payments.shape)





# ------------------------------------------------------------------------------
# JOIN: Fact Sales + Payments
# ------------------------------------------------------------------------------

fact_sales = fact_sales.merge(
    payments,
    on="order_id",
    how="left"
)

print("\nApós JOIN com Payments")
print(f"Shape: {fact_sales.shape}")





# ------------------------------------------------------------------------------
# Agrupar reviews por pedido
# ------------------------------------------------------------------------------

reviews = (
    reviews
    .groupby("order_id", as_index=False)
    .agg(
        review_score=("review_score", "mean")
    )
)

print("\nReviews agrupado")
print(reviews.shape)







# ------------------------------------------------------------------------------
# JOIN: Fact Sales + Reviews
# ------------------------------------------------------------------------------

fact_sales = fact_sales.merge(
    reviews,
    on="order_id",
    how="left"
)

print("\nApós JOIN com Reviews")
print(f"Shape: {fact_sales.shape}")



#### Novas**Add1

# ------------------------------------------------------------------------------
# Converter datas
# ------------------------------------------------------------------------------

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "shipping_limit_date",
]

for col in date_columns:
    fact_sales[col] = pd.to_datetime(
        fact_sales[col],
        errors="coerce"
    )




# #### Novas**Add2------------------------------------------------------------------------------
# Corrigir nomes das colunas
# ------------------------------------------------------------------------------

fact_sales = fact_sales.rename(
    columns={
        "product_name_lenght": "product_name_length",
        "product_description_lenght": "product_description_length",
    }
)











# ####------------------------------------------------------------------------------
# Validação final
# ------------------------------------------------------------------------------

print("\nFact Sales")
print(fact_sales.info())

print("\nPrimeiras linhas")
print(fact_sales.head())



# ------------------------------------------------------------------------------
# Converter colunas de data
# ------------------------------------------------------------------------------

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "shipping_limit_date",
]

for col in date_columns:
    fact_sales[col] = pd.to_datetime(
        fact_sales[col],
        errors="coerce"
    )




    # ------------------------------------------------------------------------------
# Renomear colunas
# ------------------------------------------------------------------------------

fact_sales = fact_sales.rename(
    columns={
        "product_name_lenght": "product_name_length",
        "product_description_lenght": "product_description_length",
    }
)








# ------------------------------------------------------------------------------
# Salvar fact_sales
# ------------------------------------------------------------------------------

output_file = ANALYTICS_PATH / "fact_sales.csv"

fact_sales.to_csv(
    output_file,
    index=False
)

print("\nFact Sales criada com sucesso!")
print(f"Arquivo salvo em: {output_file}")