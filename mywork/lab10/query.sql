USE kwj2hk_db;

SELECT * FROM students;

SELECT * FROM enrollments;

SELECT s.student_id, s.name, s.house, e.course_name, e.semester
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id;

SELECT house, COUNT(*) AS num_students
FROM students
GROUP BY house;
