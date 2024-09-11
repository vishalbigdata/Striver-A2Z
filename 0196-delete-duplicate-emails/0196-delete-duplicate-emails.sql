-- with my_cte as 
--             (select email ,min(id) as id_to_keep
--             from  Person group by Email
--             )
--             delete from Person
--             where Id not in ( select id_to_keep from my_cte )
    
-- 1 j 1 j  
-- 1 j 2 b
-- 1 j 3 j

-- 2 b 1 j
-- 2 b 2 b 
-- 2 b 3 j

-- 3 j 1 j
-- 3 j 2 b
-- 3 j 3 j


delete p1.*
from Person p1
cross join  person p2
where  p1.email = p2.email and p1.id > p2.id















