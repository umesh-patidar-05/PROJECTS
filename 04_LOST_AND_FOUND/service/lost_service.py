from dao.lost_dao import LostDao

class LostService:
    def get_all_lost_items(self):
        dao = LostDao()
        lost_items = dao.see_all_lost_items()
        return lost_items