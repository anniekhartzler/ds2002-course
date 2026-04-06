USE kwj2hk_db;

INSERT INTO students (student_id, name, house, enrollment_date) VALUES
(11, 'Seamus Finnigan', 'Gryffindor', '2026-03-08 16:32:04'),
(12, 'Padma Patil', 'Ravenclaw', '2026-03-08 16:32:04');

INSERT INTO enrollments (enrollment_id, course_name, semester, student_id) VALUES
(111, 'Charms', 'Fall 1995', 11),
(112, 'Astronomy', 'Fall 1995', 12),
(113, 'Transfiguration', 'Fall 1995', 11);
