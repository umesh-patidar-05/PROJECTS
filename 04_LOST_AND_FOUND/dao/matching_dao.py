from database.connection import DataBase

class MatchingDao:

    def possible_match(self, item_name, address):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT f.found_item_name, f.found_date, f.address, s.student_name, s.mobile_no, f.found_id FROM found AS f JOIN student AS s ON s.student_id = f.student_id WHERE f.found_item_name = %s AND f.address = %s AND f.status_id = 2"
        cursor.execute(query, (item_name, address))
        match_items = cursor.fetchall()
        return match_items

         
    def confirm_lost_detail(self, item_name, address, date):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM lost WHERE lost_item_name = %s AND address = %s AND lost_date = %s "
        cursor.execute(query, (item_name, address, date))
        confirm = cursor.fetchone()
        return confirm

    def change_status_to_found(self, status_id, lost_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "UPDATE lost SET status_id = %s WHERE lost_id = %s"
        cursor.execute(query, (status_id, lost_id,))
        conn.commit()
        return "match confirmed."

    def check_student_in_lost(self, stu_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM lost WHERE student_id = %s AND status_id = 2"
        cursor.execute(query, (stu_id,))
        items = cursor.fetchall()
        return items



    def change_status_to_claimed_found(self, status_id, found_id):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "UPDATE found SET status_id = %s WHERE found_id = %s"
        cursor.execute(query, (status_id, found_id))
        conn.commit()
        