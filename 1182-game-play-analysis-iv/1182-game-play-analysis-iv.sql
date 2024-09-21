# Write your MySQL query statement below
-- select round( count(distinct T.player_id ) / count(distinct   a.player_id) , 2)
-- as fraction
-- from Activity a
-- left join 
-- (select player_id , min(event_date) as FLD
-- from Activity 
-- group by player_id) T
-- on a.player_id = T.player_id
-- and date_sub(a.event_date,interval 1 day) = T.FLD


select  round(count(distinct (player_id)) / (select count(distinct(player_id))  from Activity) , 2) as fraction
from Activity
where (player_id , date_sub(event_date  , interval 1 day)) in 
    (select player_id, min(event_date) as first_login
    from Activity 
    group by player_id)