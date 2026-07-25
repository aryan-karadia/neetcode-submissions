-- Write your query below

SELECT name from customers LEFT JOIN orders on customers.id = orders.customer_id WHERE orders.customer_id IS NULL