-- # Write your MySQL query statement below
-- SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
-- FROM Students s
-- CROSS JOIN Subjects sub
-- LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
-- GROUP BY s.student_id, s.student_name, sub.subject_name
-- ORDER BY s.student_id, sub.subject_name;



select st.student_id , st.student_name, sub.subject_name , count(ex.student_id) as attended_exams
from Students st
cross join Subjects sub
left join Examinations ex 
    on st.student_id = ex.student_id and sub.subject_name = ex.subject_name
group by st.student_id , st.student_name, sub.subject_name
ORDER BY st.student_id, sub.subject_name;
