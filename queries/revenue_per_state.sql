-- TODO: This query will return a table with two columns; customer_state, and 
-- Revenue. The first one will have the letters that identify the top 10 states 
-- with most revenue and the second one the total revenue of each.
-- HINT: All orders should have a delivered status and the actual delivery date 
-- should be not null. 
SELECT 
	 oc.customer_state AS customer_state,
	 SUM(payment_value ) AS Revenue
FROM
	(SELECT * FROM olist_orders oo WHERE order_status = 'delivered' 
	AND oo.order_delivered_customer_date IS NOT NULL ) oo
	 	JOIN olist_customers oc  ON oo.customer_id = oc.customer_id
	 	JOIN olist_order_payments oop ON oo.order_id = oop.order_id
	Group by customer_state
	ORDER BY Revenue DESC
	LIMIT 10