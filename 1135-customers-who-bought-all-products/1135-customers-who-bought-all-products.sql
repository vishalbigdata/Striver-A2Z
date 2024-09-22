# Write your MySQL query statement below
SELECT customer_id 
FROM customer
GROUP BY customer_id
having count(distinct product_key) = (select count(product_key) from Product)