from database.connection import DataBase

class LostDao:

    def see_all_lost_items(self):
        db = DataBase()
        conn = db.connect()
        cursor = conn.cursor()
        query = "SELECT l.lost_item_name, l.lost_date, l.address, s.status_name FROM lost AS l JOIN status AS s ON s.status_id = l.status_id"
        cursor.execute(query)
        lost_itmes = cursor.fetchall()
        return lost_itmes

