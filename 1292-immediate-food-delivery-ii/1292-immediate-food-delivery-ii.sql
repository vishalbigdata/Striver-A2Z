SELECT
    ROUND((COUNT(
        CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 END) / COUNT(*)) * 100, 2)  immediate_percentage
FROM Delivery d
WHERE d.order_date = (
    SELECT
    MIN(order_date)
    FROM Delivery
    WHERE customer_id = d.customer_id
    );

-- OR
-- SELECT ROUND(AVG(temp.order_date=temp.customer_pref_delivery_date) * 100, 2) immediate_percentage
-- FROM (
--     SELECT *, RANK() OVER(partition by customer_id ORDER BY order_date) od
--     FROM Delivery) temp
-- WHERE temp.od = 1


-- Select round(avg(if(d.order_date = d.customer_pref_delivery_date , 1 , 0 )) * 100 ,2) as immediate_percentage
-- from Delivery d
-- left join
-- (select customer_id , min(order_date) as fod
-- from Delivery
-- group by customer_id) f
-- on d.customer_id = f.customer_id
-- where d.order_date = f.fod

