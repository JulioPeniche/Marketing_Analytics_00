-- Fase 5.6
-- Métodos de Pagamento

SELECT

  payment_type,

  COUNT(DISTINCT order_id) AS pedidos,

  ROUND(SUM(receita),2) AS receita,

  ROUND(
    SUM(receita) / COUNT(DISTINCT order_id),
    2
  ) AS ticket_medio

FROM `marketing_analytics.fact_sales`

GROUP BY
  payment_type

ORDER BY
  receita DESC;