from dao.matching_dao import MatchingDao

class MatchingService:
    def matching_found_items(self, item_name, address):
        dao = MatchingDao()
        match_items = dao.possible_match(item_name, address)
        if len(match_items) == 0:
            return None
        else:
            return match_items


    def confirm_lost_item(self, item_name, address, date):
        dao = MatchingDao()
        confirm = dao.confirm_lost_detail(item_name, address, date)
        return confirm

    def lost_table_status_change(self, status_id, lost_id):
        dao = MatchingDao()
        change_status = dao.change_status_to_found(status_id, lost_id)
        return change_status

    def confirm_student_in_lost(self, stu_id): 
        dao = MatchingDao()
        lost_items  = dao.check_student_in_lost(stu_id)
        if lost_items == []:
            return None
        else:
            return lost_items
        
    def found_table_status_change(self, status_id, found_id):
        dao = MatchingDao()
        change_status = dao.change_status_to_claimed_found(status_id, found_id)
        