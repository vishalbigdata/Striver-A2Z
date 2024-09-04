# Write your MySQL query statement below
SELECT 
    x , y, z,
    case when  ( (x + y) > z and abs(x-y) < z )
            or ( (y + z) > x and abs(y-z) < x )
            or ( (x + z) > y and abs(x-z) < y )
        then 'Yes'
    else 'No'
    end as triangle
        
FROM Triangle
