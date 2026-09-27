from database.connection import DataBase

class ReportsDao:
    def total_lost_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT count(*) FROM lost"
        cursor.execute(query)
        total_lost = cursor.fetchone()
        return total_lost[0]

    def total_claimed_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT count(*) FROM lost WHERE status_id = 3"
        cursor.execute(query)
        total_claimed = cursor.fetchone()
        return total_claimed[0]        

    def pending_lost_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT count(*) FROM lost WHERE status_id = 1"
        cursor.execute(query)
        pending_lost = cursor.fetchone()
        return pending_lost[0]        

    def total_found_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT count(*) FROM lost WHERE status_id = 2"
        cursor.execute(query)
        total_found = cursor.fetchone()
        return total_found[0]