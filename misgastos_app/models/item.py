from misgastos_app.config.mysqlconnection import connectToMySQL

class Item:
    def __init__ (self, data):
        self.iid = data ['iid']
        self.iname = data ['iname']
        self.iio = data ['iio']
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
    def save(cls, data):
        query = 'insert into items (iname, iio, itm_cid, itm_uid, created_at, updated_at) values (%(iname)s, %(iio)s, %(itm_cid)s, %(itm_uid)s, now(), now())'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update items set iname = %(iname)s, updated_at = now() where iid = %(iid)s and itm_uid = %(itm_uid)s;'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def delete(cls, data):
        if 'iid' in data:
            query = 'delete from items where iid = %(iid)s and itm_uid = %(uid)s;'
        else:
            query = 'delete from items where iio = %(iio)s and itm_cid = %(cid)s and itm_uid = %(uid)s;'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def get_all_by_iio_cid_uid(cls, data):
        query = 'select * from items where iio = %(iio)s and itm_cid = %(cid)s and itm_uid = %(uid)s;'
        return Item.results(query, data)

    @classmethod
    def get_all_by_uid(cls, data):
        query = 'select * from items where itm_uid = %(uid)s;'
        return Item.results(query, data)

    @classmethod
    def new_user(cls, data):
        user_template = {'uid': 1}
        items = Item.get_all_by_uid(user_template)
        for item in items:
            item = {'iname': item.iname, 'iio': item.iio, 'itm_cid': item.itm_cid, 'itm_uid': data.uid}
            Item.save(item)
        return None