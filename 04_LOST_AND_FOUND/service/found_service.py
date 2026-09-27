from dao.found_dao import FoundDao

class FoundService:

    def get_all_found_items(self):
        dao = FoundDao()
        found_items = dao.see_all_found_items()
        return found_items

    def new_found_report(self, stu_id, item_name, date, address):
        dao = FoundDao()
        return dao.report_found_item(stu_id, item_name, date, address)    

    def lost_item_status(self, stu_id):
        dao = FoundDao()
        return dao.see_found_item_status_using_student_id(stu_id)
    