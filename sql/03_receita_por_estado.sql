
  -- Fase 5.3
-- Receita por Estado

SELECT
  customer_state,
  COUNT(DISTINCT order_id) AS pedidos,
  ROUND(SUM(receita), 2) AS receita,
  ROUND(SUM(receita) / COUNT(DISTINCT order_id), 2) AS ticket_medio
FROM `marketing_analytics.fact_sales`

GROUP BY
  customer_state

ORDER BY
  receita DESC;