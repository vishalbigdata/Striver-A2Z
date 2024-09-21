# Write your MySQL query statement below

# using Self Join

-- select y.id 
-- from Weather t
-- join Weather y
-- on DATEDIFF(y.recordDate, t.recordDate) = 1 
--     and y.temperature > t.temperature

-- SUBDATE , we can use also


select w1.id  as Id
from weather w1
left join weather w2
on w1.recordDate - interval 1 day = w2.recordDate 
where w1.temperature > w2.temperature 