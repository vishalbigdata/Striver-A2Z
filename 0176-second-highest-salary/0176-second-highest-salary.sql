-- select max(salary) as SecondHighestSalary
-- from Employee
-- where salary not in (select max(salary) from Employee)
with cte as(
select *,
DENSE_RANK() over(order by salary desc) as r
from Employee)
select ifnull((select salary
from cte where r = 2 limit 1 ), null) as SecondHighestSalary