mysql> CREATE DATABASE project3;
Query OK, 1 row affected (0.07 sec)

mysql> use project3;
Database changed
mysql> CREATE TABLE department( department_id INT PRIMARY KEY AUTO_INCREMENT, department_name VARCHAR(50) UNIQUE NOT NULL);
Query OK, 0 rows affected (0.16 sec)

mysql> DESC department;
+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| department_id   | int         | NO   | PRI | NULL    | auto_increment |
| department_name | varchar(50) | NO   | UNI | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
2 rows in set (0.04 sec)






mysql> CREATE TABLE student( student_id INT PRIMARY KEY AUTO_INCREMENT,
    -> student_name VARCHAR(50) NOT NULL,
    -> mobile_no CHAR(10) NOT NULL,
    -> department_id INT NOT NULL, FOREIGN KEY(department_id) REFERENCES department(department_id))
    -> AUTO_INCREMENT = 101;
Query OK, 0 rows affected (0.05 sec)

mysql> DESC student;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| student_id    | int         | NO   | PRI | NULL    | auto_increment |
| student_name  | varchar(50) | NO   |     | NULL    |                |
| mobile_no     | char(10)    | NO   |     | NULL    |                |
| department_id | int         | NO   | MUL | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)





mysql> CREATE TABLE status(status_id INT PRIMARY KEY, status_name ENUM('Pending', 'Founded') NOT NULL);
Query OK, 0 rows affected (0.03 sec)

mysql> DESC status;
+-------------+---------------------------+------+-----+---------+-------+
| Field       | Type                      | Null | Key | Default | Extra |
+-------------+---------------------------+------+-----+---------+-------+
| status_id   | int                       | NO   | PRI | NULL    |       |
| status_name | enum('Pending','Founded') | NO   |     | NULL    |       |
+-------------+---------------------------+------+-----+---------+-------+
2 rows in set (0.01 sec)


mysql> ALTER TABLE status MODIFY COLUMN status_name ENUM('Pending', 'Found', 'Claimed') NOT NULL;
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC status;
+-------------+-----------------------------------+------+-----+---------+-------+
| Field       | Type                              | Null | Key | Default | Extra |
+-------------+-----------------------------------+------+-----+---------+-------+
| status_id   | int                               | NO   | PRI | NULL    |       |
| status_name | enum('Pending','Found','Claimed') | NO   |     | NULL    |       |
+-------------+-----------------------------------+------+-----+---------+-------+
2 rows in set (0.00 sec)









mysql> CREATE TABLE FOUND
    -> ( found_id INT PRIMARY KEY AUTO_INCREMENT,
    -> student_id INT NOT NULL,
    -> found_item_name VARCHAR(50) NOT NULL,
    -> found_date DATE NOT NULL,
    -> address VARCHAR(70) NOT NULL,
    -> status_id INT NOT NULL,
    -> FOREIGN KEY(student_id) REFERENCES student(student_id),
    -> FOREIGN KEY(status_id) REFERENCES status(status_id))
    -> AUTO_INCREMENT = 201;
Query OK, 0 rows affected (0.06 sec)

mysql> DESC found;
+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| found_id        | int         | NO   | PRI | NULL    | auto_increment |
| student_id      | int         | NO   | MUL | NULL    |                |
| found_item_name | varchar(50) | NO   |     | NULL    |                |
| found_date      | date        | NO   |     | NULL    |                |
| address         | varchar(70) | NO   |     | NULL    |                |
| status_id       | int         | NO   | MUL | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)






mysql> CREATE TABLE lost(
    ->      lost_id INT PRIMARY KEY AUTO_INCREMENT,
    ->      student_id INT NOT NULL,
    ->      lost_item_name VARCHAR(50) NOT NULL,
    ->      lost_date DATE NOT NULL,
    ->      address VARCHAR(70) NOT NULL,
    ->      status_id INT NOT NULL,
    ->      FOREIGN KEY(student_id) REFERENCES student(student_id),
    ->      FOREIGN KEY(status_id) REFERENCES status(status_id))
    ->      AUTO_INCREMENT = 401;
Query OK, 0 rows affected (0.05 sec)

mysql> DESC lost;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| lost_id        | int         | NO   | PRI | NULL    | auto_increment |
| student_id     | int         | NO   | MUL | NULL    |                |
| lost_item_name | varchar(50) | NO   |     | NULL    |                |
| lost_date      | date        | NO   |     | NULL    |                |
| address        | varchar(70) | NO   |     | NULL    |                |
| status_id      | int         | NO   | MUL | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)






















INSERT INTO department (department_name) VALUES
('Computer Science'),
('Information Technology'),
('Computer Applications'),
('Commerce'),
('Management'),
('Science'),
('Arts'),
('Mechanical Engineering'),
('Civil Engineering'),
('Electrical Engineering');


mysql> SELECT * FROM department;
+---------------+------------------------+
| department_id | department_name        |
+---------------+------------------------+
|             7 | Arts                   |
|             9 | Civil Engineering      |
|             4 | Commerce               |
|             3 | Computer Applications  |
|             1 | Computer Science       |
|            10 | Electrical Engineering |
|             2 | Information Technology |
|             5 | Management             |
|             8 | Mechanical Engineering |
|             6 | Science                |
+---------------+------------------------+
10 rows in set (0.00 sec)








INSERT INTO status (status_id, status_name) VALUES
(1, 'Pending'),
(2, 'Found'),
(3, 'Claimed');



mysql> SELECT * FROM status;
+-----------+-------------+
| status_id | status_name |
+-----------+-------------+
|         1 | Pending     |
|         2 | Found       |
|         3 | Claimed     |
+-----------+-------------+
3 rows in set (0.00 sec)










INSERT INTO student (student_name, mobile_no, department_id) VALUES
('Rahul Sharma', '9876543210', 1),
('Priya Verma', '9876543211', 2),
('Aman Patel', '9876543212', 3),
('Neha Jain', '9876543213', 1),
('Rohit Mehta', '9876543214', 4),
('Sneha Sharma', '9876543215', 5),
('Vikas Yadav', '9876543216', 2),
('Anjali Singh', '9876543217', 3),
('Karan Joshi', '9876543218', 6),
('Pooja Gupta', '9876543219', 1),
('Arjun Verma', '9876543220', 7),
('Nisha Patel', '9876543221', 2),
('Mohit Sharma', '9876543222', 3),
('Riya Mehta', '9876543223', 5),
('Sahil Jain', '9876543224', 4);




mysql> SELECT * FROM student;
+------------+--------------+------------+---------------+
| student_id | student_name | mobile_no  | department_id |
+------------+--------------+------------+---------------+
|        101 | Rahul Sharma | 9876543210 |             1 |
|        102 | Priya Verma  | 9876543211 |             2 |
|        103 | Aman Patel   | 9876543212 |             3 |
|        104 | Neha Jain    | 9876543213 |             1 |
|        105 | Rohit Mehta  | 9876543214 |             4 |
|        106 | Sneha Sharma | 9876543215 |             5 |
|        107 | Vikas Yadav  | 9876543216 |             2 |
|        108 | Anjali Singh | 9876543217 |             3 |
|        109 | Karan Joshi  | 9876543218 |             6 |
|        110 | Pooja Gupta  | 9876543219 |             1 |
|        111 | Arjun Verma  | 9876543220 |             7 |
|        112 | Nisha Patel  | 9876543221 |             2 |
|        113 | Mohit Sharma | 9876543222 |             3 |
|        114 | Riya Mehta   | 9876543223 |             5 |
|        115 | Sahil Jain   | 9876543224 |             4 |
+------------+--------------+------------+---------------+
15 rows in set (0.00 sec)












INSERT INTO found
(student_id, found_item_name, found_date, address, status_id)
VALUES
(102, 'Black Wallet', '2026-09-10', 'Library', 2),
(105, 'Blue Water Bottle', '2026-09-11', 'Canteen', 3),
(108, 'HP Laptop Charger', '2026-09-12', 'Computer Lab', 2),
(110, 'Black Backpack', '2026-09-13', 'Parking Area', 3),
(103, 'Silver Watch', '2026-09-14', 'Seminar Hall', 1),
(107, 'Red Umbrella', '2026-09-15', 'Main Gate', 2),
(112, 'Scientific Calculator', '2026-09-16', 'Room 204', 1),
(114, 'Blue Notebook', '2026-09-17', 'Library', 2),
(109, 'Wireless Earbuds', '2026-09-18', 'Canteen', 1),
(115, 'USB Drive', '2026-09-19', 'Computer Lab', 2);



mysql> SELECT * FROM found;
+----------+------------+-----------------------+------------+--------------+-----------+
| found_id | student_id | found_item_name       | found_date | address      | status_id |
+----------+------------+-----------------------+------------+--------------+-----------+
|      201 |        102 | Black Wallet          | 2026-09-10 | Library      |         2 |
|      202 |        105 | Blue Water Bottle     | 2026-09-11 | Canteen      |         3 |
|      203 |        108 | HP Laptop Charger     | 2026-09-12 | Computer Lab |         2 |
|      204 |        110 | Black Backpack        | 2026-09-13 | Parking Area |         3 |
|      205 |        103 | Silver Watch          | 2026-09-14 | Seminar Hall |         1 |
|      206 |        107 | Red Umbrella          | 2026-09-15 | Main Gate    |         2 |
|      207 |        112 | Scientific Calculator | 2026-09-16 | Room 204     |         1 |
|      208 |        114 | Blue Notebook         | 2026-09-17 | Library      |         2 |
|      209 |        109 | Wireless Earbuds      | 2026-09-18 | Canteen      |         1 |
|      210 |        115 | USB Drive             | 2026-09-19 | Computer Lab |         2 |
+----------+------------+-----------------------+------------+--------------+-----------+
10 rows in set (0.00 sec)















INSERT INTO lost
(student_id, lost_item_name, lost_date, address, status_id)
VALUES
(101, 'Black Wallet', '2026-09-09', 'Library', 2),
(104, 'Blue Water Bottle', '2026-09-10', 'Canteen', 3),
(106, 'HP Laptop Charger', '2026-09-11', 'Computer Lab', 2),
(111, 'Black Backpack', '2026-09-12', 'Parking Area', 3),
(113, 'Silver Watch', '2026-09-13', 'Seminar Hall', 1),
(101, 'Red Umbrella', '2026-09-14', 'Main Gate', 2),
(108, 'Scientific Calculator', '2026-09-15', 'Room 204', 1),
(105, 'Green Notebook', '2026-09-16', 'Library', 1),
(110, 'Wireless Earbuds', '2026-09-17', 'Canteen', 1),
(115, 'Student ID Card', '2026-09-18', 'Main Gate', 1),
(103, 'Blue Backpack', '2026-09-19', 'Classroom 101', 1),
(109, 'Black Pen Drive', '2026-09-20', 'Computer Lab', 1);



mysql> SELECT * FROM lost;
+---------+------------+-----------------------+------------+---------------+-----------+
| lost_id | student_id | lost_item_name        | lost_date  | address       | status_id |
+---------+------------+-----------------------+------------+---------------+-----------+
|     401 |        101 | Black Wallet          | 2026-09-09 | Library       |         2 |
|     402 |        104 | Blue Water Bottle     | 2026-09-10 | Canteen       |         3 |
|     403 |        106 | HP Laptop Charger     | 2026-09-11 | Computer Lab  |         2 |
|     404 |        111 | Black Backpack        | 2026-09-12 | Parking Area  |         3 |
|     405 |        113 | Silver Watch          | 2026-09-13 | Seminar Hall  |         1 |
|     406 |        101 | Red Umbrella          | 2026-09-14 | Main Gate     |         2 |
|     407 |        108 | Scientific Calculator | 2026-09-15 | Room 204      |         1 |
|     408 |        105 | Green Notebook        | 2026-09-16 | Library       |         1 |
|     409 |        110 | Wireless Earbuds      | 2026-09-17 | Canteen       |         1 |
|     410 |        115 | Student ID Card       | 2026-09-18 | Main Gate     |         1 |
|     411 |        103 | Blue Backpack         | 2026-09-19 | Classroom 101 |         1 |
|     412 |        109 | Black Pen Drive       | 2026-09-20 | Computer Lab  |         1 |
+---------+------------+-----------------------+------------+---------------+-----------+
12 rows in set (0.00 sec)