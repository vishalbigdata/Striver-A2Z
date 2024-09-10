# Write your MySQL query statement below

select score,dense_rank() OVER (order by score desc) as 'rank'
from Scores
