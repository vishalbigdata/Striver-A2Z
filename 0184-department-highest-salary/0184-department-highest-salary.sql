# Write your MySQL query statement below
-- select d.name as Department,e.name as Employee, e.salary as Salary
-- from Employee e
-- join Department d
-- on e.departmentId = d.id
-- where (e.departmentId,e.salary) in 
--     (select departmentID,max(salary)
--     from Employee
--     group by DepartmentId)

with cte as (
select d.name as Department , e.name as Employee, e.salary as Salary, 
max(E.salary) over (PARTITION BY e.departmentId) as max_salary
from Employee e
left join Department d
on e.departmentId = d.id )

select Department, Employee , Salary
from cte 
where salary = max_salary
