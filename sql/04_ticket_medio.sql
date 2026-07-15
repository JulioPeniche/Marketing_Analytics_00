-- Fase 5.4
-- Ticket Médio

SELECT
  COUNT(DISTINCT order_id) AS pedidos,
  ROUND(SUM(receita), 2) AS receita_total,
  ROUND(SUM(receita) / COUNT(DISTINCT order_id), 2) AS ticket_medio
FROM `marketing_analytics.fact_sales`;