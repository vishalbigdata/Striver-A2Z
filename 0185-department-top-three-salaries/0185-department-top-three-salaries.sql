
-- select dense_rank(e.salary) over(partition by e.departmentId order by e.salary desc) as rnk
-- from Employee e
-- left join Department d
--     on e.departmentId = d.id

SELECT d.name as Department, e1.name as Employee, e1.salary as Salary
from Employee e1
left join Department d
on e1.departmentId = d.id
where
    (
        select count(Distinct(e2.salary))
        from Employee e2
        where e1.departmentId = e2.departmentId
            and e1.salary < e2.salary


    ) < 3
