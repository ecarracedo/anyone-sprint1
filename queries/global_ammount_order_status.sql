-- TODO: This query will return a table with two columns; order_status, and
-- Ammount. The first one will have the different order status classes and the
-- second one the total ammount of each.
SELECT oo.order_status AS order_status,
COUNT(oop.payment_value) AS Ammount
FROM (SELECT * FROM olist_orders oo WHERE oo.order_status IS NOT NULL ) oo
	JOIN olist_order_payments oop ON oo.order_id = oop.order_id
GROUP BY oo.order_status
ORDER BY oo.order_status  ASC