from dao.lost_dao import LostDao

class LostService:

    def get_all_lost_items(self):
        dao = LostDao()
        lost_items = dao.see_all_lost_items()
        return lost_items

    def new_lost_report(self, stu_id, item_name, date, address):
        dao = LostDao()
        return dao.report_lost_item(stu_id, item_name, date, address)

    def lost_item_status(self, stu_id):
        dao = LostDao()
        return dao.see_lost_item_status_using_student_id(stu_id)
