USE kwj2hk_db;

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    house VARCHAR(50),
    enrollment_date DATETIME
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    semester VARCHAR(50),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 10 Hogwarts students
INSERT INTO students VALUES (1, 'Harry Potter', 'Gryffindor', NOW());
INSERT INTO students VALUES (2, 'Hermione Granger', 'Gryffindor', NOW());
INSERT INTO students VALUES (3, 'Ron Weasley', 'Gryffindor', NOW());
INSERT INTO students VALUES (4, 'Draco Malfoy', 'Slytherin', NOW());
INSERT INTO students VALUES (5, 'Luna Lovegood', 'Ravenclaw', NOW());
INSERT INTO students VALUES (6, 'Cedric Diggory', 'Hufflepuff', NOW());
INSERT INTO students VALUES (7, 'Cho Chang', 'Ravenclaw', NOW());
INSERT INTO students VALUES (8, 'Neville Longbottom', 'Gryffindor', NOW());
INSERT INTO students VALUES (9, 'Pansy Parkinson', 'Slytherin', NOW());
INSERT INTO students VALUES (10, 'Ginny Weasley', 'Gryffindor', NOW());

-- 10 Hogwarts class enrollments
INSERT INTO enrollments VALUES (101, 'Defense Against the Dark Arts', 'Fall 1995', 1);
INSERT INTO enrollments VALUES (102, 'Potions', 'Fall 1995', 2);
INSERT INTO enrollments VALUES (103, 'Herbology', 'Fall 1995', 3);
INSERT INTO enrollments VALUES (104, 'Potions', 'Fall 1995', 4);
INSERT INTO enrollments VALUES (105, 'Care of Magical Creatures', 'Fall 1995', 5);
INSERT INTO enrollments VALUES (106, 'Charms', 'Fall 1995', 6);
INSERT INTO enrollments VALUES (107, 'Transfiguration', 'Fall 1995', 7);
INSERT INTO enrollments VALUES (108, 'Herbology', 'Fall 1995', 8);
INSERT INTO enrollments VALUES (109, 'Potions', 'Fall 1995', 9);
INSERT INTO enrollments VALUES (110, 'Defense Against the Dark Arts', 'Fall 1995', 10);
