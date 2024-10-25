# Write your MySQL query statement below
-- select e1.name as Employee 
-- from Employee e1
-- join Employee e2
-- on e1.ManagerId = e2.id
-- where e1.salary > e2.salary

-- +----+-------+--------+-----------++----+-------+--------+-----------+
-- | id | name  | salary | managerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+

-- | id | name  | salary | managerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+

-- select e1.name as Employee 
-- from Employee e1
-- join Employee e2 
--     on e1.managerId = e2.id
-- where e1.salary > e2.salary


select a.name as Employee 
from employee a, employee b
where a.managerId = b.id and a.salary > b.salary