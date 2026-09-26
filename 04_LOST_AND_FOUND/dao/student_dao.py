from database.connection import DataBase

class StudentDao:
    def see_all_students(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT s.student_id, s.student_name, s.mobile_no, d.department_name FROM student AS s JOIN department AS d ON d.department_id = s.department_id"
        cursor.execute(query)
        students = cursor.fetchall()
        return students
        

    def search_student_by_id(self, idd):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT s.student_id, s.student_name, s.mobile_no, d.department_name FROM student AS s JOIN department AS d ON d.department_id = s.department_id WHERE s.student_id = %s"
        cursor.execute(query, (idd,))
        student = cursor.fetchone()
        return student
        

    def add_student(self, name, mobile, dept_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO student(student_name, mobile_no, department_id) VALUES(%s, %s, %s)"
        cursor.execute(query, (name, mobile, dept_id))
        conn.commit()
        return "Student added successfully: "


    def find_student_id(self, name, mobile, dept_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT student_id FROM student WHERE student_name = %s AND mobile_no = %s AND department_id = %s"
        cursor.execute(query, (name, mobile, dept_id)) 
        student_id = cursor.fetchone()
        return student_id  

