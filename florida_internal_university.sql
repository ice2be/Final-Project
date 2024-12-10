USE florida_international_university;

CREATE TABLE Student (
-- adds new student ID
student_id INT PRIMARY KEY,
  Fname VARCHAR(45),
  Lname VARCHAR(45),
  major VARCHAR(45),
  address VARCHAR(255),
  phone_number VARCHAR(20),
  user_email VARCHAR(255),
  date_of_birth DATE,
  user_password VARCHAR(255) NOT NULL
);

CREATE TABLE Course (
  course_ID INT PRIMARY KEY,
  course_name VARCHAR(45),
  instructor_ID VARCHAR(255),
  start_time TIME,
  end_time TIME,
  room_number VARCHAR(10)
);

CREATE TABLE Enrolment (
  enrolment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  grade VARCHAR(2),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Schedule (
  student_id INT,
  course_id INT,
  start_time TIME,
  end_time TIME,
  room_number VARCHAR(10),
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Department (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(255),
  major VARCHAR(255)
);

CREATE TABLE Professor (
  professor_id INT PRIMARY KEY,
  FName VARCHAR(45),
  LName VARCHAR(45),
  address VARCHAR(255),
  phone_number VARCHAR(20),
  email VARCHAR(255)
);

INSERT INTO Student (student_id, Fname, Lname, major, address, phone_number, user_email, date_of_birth, user_password)
VALUES 
(1, 'Jonthan', 'Smith','Computer Science', '123 Main Street', '213-231-973', 'jsmith@fiu.edu', '1996-11-07', 'Password123'),
(2, 'Nicole', 'Smith', 'Nursing','123 Main Street', '543-287-938', 'nicolesmith@hotmail.com', '2005-10-01','Password321');

INSERT INTO Course (course_ID, course_name, instructor_ID, start_time, end_time, room_number)
VALUES (1, 'Introduction to Programming', '01', '09:00:00', '11:00:00', 'Room 101'),
	   (2, 'Database Management', '02', '12:00:00', '1:00:00', 'Room 202');
       
INSERT INTO Enrolment (enrolment_id, student_id, course_id, grade)
VALUES (1, 1, 1, 'A');

INSERT INTO Enrolment (enrolment_id, student_id, course_id, grade)
VALUES (2, 2, 1, 'A');

INSERT INTO Schedule (student_id, course_id, start_time, end_time, room_number)
VALUES (1, 1, '09:00:00', '11:00:00', 'Room 101'),
       (2, 1, '09:00:00', '11:00:00', 'Room 101');

INSERT INTO Department (department_id, department_name, major)
VALUES (1, 'Computer Science', 'Computer Science'),
       (2,'Nursing', 'School Of Medecine');
       
INSERT INTO Professor (professor_id, FName, LName, address, phone_number, email)
VALUES (1, 'Carlos', 'Smith', '123 Main Street', '123-456-7890', 'carlossmith@fiu.edu'),
	   (2, 'Victoria', 'Smith', '321 Main Street', '123-456-7990', 'victoriasmith@fiu.edu');


-- Test student to delete. 
INSERT INTO Student (student_id, Fname, Lname, major, address, phone_number, email, date_of_birth, user_password)
VALUES (3, 'John', 'Smith', 'Nursing','123 Main Street', '123-456-7890', 'johnSmith@test.com', '1990-01-01','Password321');

UPDATE Student
SET address = '456 Elm Street'
WHERE student_id = 1;

-- Deletes tester student.  
DELETE FROM Student
WHERE student_id = 3;

-- Checking table for deleted student.  
SELECT *
FROM Student;

SELECT Fname, Lname
FROM Student;

UPDATE Student
SET password = 'Password13'
WHERE student_id = 1;

UPDATE Student
SET password = 'Password31'
WHERE student_id = 2;

-- Checking table for deleted student.  
SELECT *
FROM Student;

SELECT *
FROM Student;



