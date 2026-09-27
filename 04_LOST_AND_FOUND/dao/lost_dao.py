from database.connection import DataBase

class LostDao:

    def see_all_lost_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT l.lost_item_name, l.lost_date, l.address, s.status_name FROM lost AS l JOIN status AS s ON s.status_id = l.status_id ORDER BY l.lost_date"
        cursor.execute(query)
        lost_itmes = cursor.fetchall()
        return lost_itmes

    def report_lost_item(self, stu_id, item_name, date, address):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "INSERT INTO lost( student_id, lost_item_name, lost_date, address, status_id) VALUES (%s, %s, %s, %s, 1)"
        cursor.execute(query, (stu_id, item_name, date, address))
        conn.commit()
        return "Lost report added successfully"

    def see_lost_item_status_using_student_id(self, stu_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT l.lost_item_name, l.lost_date, l.address, s.status_name FROM lost As l JOIN status AS s ON l.status_id = s.status_id WHERE l.student_id = %s"
        cursor.execute(query, (stu_id,))
        lost_items = cursor.fetchall()
        if lost_items == []:
            return None
        else:
            return lost_items                