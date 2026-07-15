-- Fase 5.5
-- RFM Clientes

WITH clientes AS (

SELECT
  customer_unique_id,

  MAX(order_purchase_timestamp) AS ultima_compra,

  COUNT(DISTINCT order_id) AS frequencia,

  SUM(receita) AS valor_total

FROM `marketing_analytics.fact_sales`

GROUP BY
  customer_unique_id

)

SELECT

  customer_unique_id,

  DATE_DIFF(
    CURRENT_DATE(),
    DATE(ultima_compra),
    DAY
  ) AS recencia,

  frequencia,

  ROUND(valor_total,2) AS monetario,

  NTILE(5) OVER(
    ORDER BY DATE_DIFF(
      CURRENT_DATE(),
      DATE(ultima_compra),
      DAY
    ) DESC
  ) AS score_recencia,

  NTILE(5) OVER(
    ORDER BY frequencia
  ) AS score_frequencia,

  NTILE(5) OVER(
    ORDER BY valor_total
  ) AS score_monetario

FROM clientes;