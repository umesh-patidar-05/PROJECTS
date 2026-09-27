from dao.reports_dao import ReportsDao



class ReportsService:

    def all_lost_itmes(self):
        dao = ReportsDao()
        return dao.total_lost_items()

    def all_claimed_items(self):
        dao = ReportsDao()
        return dao.total_claimed_items()

    def all_pending_items(self):
        dao = ReportsDao()
        return dao.pending_lost_items()

    def all_found_items(self):
        dao = ReportsDao()
        return dao.total_found_items()