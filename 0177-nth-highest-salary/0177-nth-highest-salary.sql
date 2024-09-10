-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
-- SET N = N-1;
--   RETURN (
--         select Distinct(salary) from employee
--         order by salary desc limit 1 offset N
--  );
-- END

CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
  RETURN (
    with cte as(
        select *,dense_rank() over(order by salary desc) as rnk
        from Employee)
    select distinct ifnull(salary,null)
    from cte
    where rnk = N
 );
END