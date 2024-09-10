/* Write your T-SQL query statement below */
select score,dense_rank() OVER (order by score desc) as rank
from Scores