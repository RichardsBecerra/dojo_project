from misgastos_app.config.mysqlconnection import connectToMySQL

class Item:
    def __init__ (self, data):
        self.iid = data ['iid']
        self.iname = data ['iname']
        self.itm_cid = data ['itm_cid']
        self.itm_uid = data ['itm_uid']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    def results (query, data):
        results = connectToMySQL('dojo_project').query_db(query, data)
        items = []
        for row in results:
            items.append(Item(row))
        return items

    @classmethod
    def get(cls, data):
        pass

    @classmethod
    def get_by_cid_uid(cls, data):
        query = 'select * from items where itm_cid = %(cid)s and itm_uid = %(uid)s;'
        return Item.results(query, data)

    @classmethod
    def get_all_by_uid(cls, data):
        query = 'select * from items where itm_uid = %(uid)s;'
        return Item.results(query, data)