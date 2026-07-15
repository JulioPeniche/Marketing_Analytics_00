SELECT
    product_category_name,
    COUNT(DISTINCT order_id) AS pedidos,
    ROUND(SUM(payment_value), 2) AS receita,
    ROUND(AVG(payment_value), 2) AS ticket_medio
FROM
    `marketing_analytics.fact_sales`
GROUP BY
    product_category_name
ORDER BY
    receita DESC;