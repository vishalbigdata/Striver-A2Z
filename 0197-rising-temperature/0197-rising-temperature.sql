# Write your MySQL query statement below
select y.id 
from Weather t
join Weather y
on DATEDIFF(y.recordDate, t.recordDate) = 1 
    and y.temperature > t.temperature
