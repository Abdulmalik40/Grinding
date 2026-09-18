df_result = (
    orders.join(customers, on="customer_id", how="inner")
    .sort("order_id")
    .select("customer_id", "order_id", "amount", "name")
)

df_result.show()