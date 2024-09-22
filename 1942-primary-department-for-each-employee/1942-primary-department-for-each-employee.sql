# Write your MySQL query statement below



select distinct employee_id, department_id
from Employee
where employee_id in (
    Select employee_id
    from Employee 
    group by employee_id
    having count(*) = 1
) or primary_flag = 'Y'