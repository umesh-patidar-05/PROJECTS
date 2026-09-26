from database.connection import DataBase

class DepartmentDao:

    def see_dept_id_using_dept_name(self, dept_name):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT department_id FROM department WHERE department_name = %s"
        cursor.execute(query, (dept_name,))
        dept_id = cursor.fetchone()
        return dept_id    

    def add_department(self, dept_name):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO department( department_name) VALUES (%s)"
        cursor.execute(query, (dept_name,))
        conn.commit()