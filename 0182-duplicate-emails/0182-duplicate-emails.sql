# Write your MySQL query statement below
select email as Email from
(select email , count(*)
from Person
group by email
having count(*) > 1 ) a
