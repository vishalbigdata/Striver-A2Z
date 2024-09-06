# Write your MySQL query statement below
with cte as(select actor_id , director_id , count(*) 
from ActorDirector
group by actor_id, director_id
having count(*) >= 3 
order by 2 desc)
select actor_id , director_id from cte
