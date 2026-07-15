SELECT
  EXTRACT(YEAR FROM order_purchase_timestamp) AS ano,
  EXTRACT(MONTH FROM order_purchase_timestamp) AS mes,
  COUNT(DISTINCT order_id) AS pedidos,
  ROUND(SUM(payment_value),2) AS receita
FROM
  `marketing_analytics.fact_sales`
GROUP BY
  ano, mes
ORDER BY
  ano, mes;
  