USE kwj2hk_db;

SELECT s.name, s.house, e.course_name, e.semester
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
WHERE s.house = 'Gryffindor';
