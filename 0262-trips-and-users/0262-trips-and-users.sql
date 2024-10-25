# Write your MySQL query statement below


with unbanned_trips as (
select
       t.request_at as Day,
       t.status
from trips t
join users u1 on (t.client_id = u1.users_id and u1.banned = 'No' and u1.role = 'client')
join users u2 on (t.driver_id = u2.users_id and u2.banned = 'No' and u2.role = 'driver')
where t.request_at  between '2013-10-01' and '2013-10-03'
)
select Day,
Round(sum(case when status in ('cancelled_by_client', 'cancelled_by_driver') then 1 else 0 end) / count(*), 2) as "Cancellation Rate"
from unbanned_trips 
group by Day

