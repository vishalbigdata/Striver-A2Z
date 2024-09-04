with cte as 
(select
    o.sales_id
    from Orders o
    inner join Company c
            on o.com_id = c.com_id
                and c.name = 'RED'
)

select name 
from SalesPerson
where sales_id not in (select sales_id from cte)