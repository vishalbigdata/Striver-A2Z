# Write your MySQL query statement below

-- select P.project_id, round(avg(E.experience_years) , 2) as average_years
-- from Project P
-- join Employee E
--     on P.employee_id = E.employee_id
-- group by P.project_id

select p.project_id , round(avg(e.experience_years) , 2) as average_years
from Project p
inner join Employee e
    on p.employee_id = e.employee_id
group by p.project_id