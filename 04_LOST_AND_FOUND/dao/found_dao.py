from database.connection import DataBase

class FoundDao:

    def see_all_found_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT f.found_item_name, f.found_date, f.address, s.status_name FROM found AS f JOIN status AS s ON s.status_id = f.status_id ORDER BY f.found_date"
        cursor.execute(query)
        found_itmes = cursor.fetchall()
        return found_itmes

    def report_found_item(self, stu_id, item_name, date, address):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO found( student_id, found_item_name, found_date, address, status_id) VALUES (%s, %s, %s, %s, 2)"
        cursor.execute(query, (stu_id, item_name, date, address))
        conn.commit()
        return "Found report added successfully"    

    def see_found_item_status_using_student_id(self, stu_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT f.found_item_name, f.found_date, f.address, s.status_name FROM found As f JOIN status AS s ON f.status_id = s.status_id WHERE f.student_id = %s"
        cursor.execute(query, (stu_id,))
        found_items = cursor.fetchall()
        if found_items == []:
            return None
        else:
            return found_items        