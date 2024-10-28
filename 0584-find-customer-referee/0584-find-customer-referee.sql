/* Write your T-SQL query statement below */




select name 
from customer
where coalesce(referee_id,-1) <> 2