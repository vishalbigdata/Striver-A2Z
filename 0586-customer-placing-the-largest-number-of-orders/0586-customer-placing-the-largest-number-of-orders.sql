
select customer_number
from
    (select customer_number , count(order_number) as cn
    from Orders
    group by customer_number
    order by count(order_number) desc
    ) a
limit 1

