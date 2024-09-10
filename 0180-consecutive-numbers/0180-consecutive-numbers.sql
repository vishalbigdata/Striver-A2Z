# Write your MySQL query statement below
-- Logs table:
-- +----+-----+
-- | id | num | next   next2next
-- +----+-----+
-- | 1  | 1   |    1   1
-- | 2  | 1   |    1   2
-- | 3  | 1   |    2   1
-- | 4  | 2   |    1   2
-- | 5  | 1   |    2   2
-- | 6  | 2   |    2   null    
-- | 7  | 2   | null    null
-- +----+-----+

with cte as (
    select *
        ,lead(num,1) over () as nxt_1
        ,lead(num,2) over () as nxt_2
from Logs)

select distinct num as  ConsecutiveNums from cte 
where num = nxt_1 and num = nxt_2