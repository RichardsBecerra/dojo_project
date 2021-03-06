from misgastos_app.config.mysqlconnection import connectToMySQL

class Movimiento:
    def __init__ (self, data):
        if 'mio' in data: 
            self.mid = data ['mid']
            self.mio = data ['mio']
            self.mdate = data ['mdate']
            self.mamount = data ['mamount']
            self.mov_uid = data ['mov_uid']
            self.mov_cid = data ['mov_cid']
            self.mov_iid = data ['mov_iid']
            self.mov_tpid = data ['mov_tpid']
            self.mcomment = data ['mcomment']
            self.created_at = data ['created_at']
            self.updated_at = data ['updated_at']
        elif 'subtotal' in data:
            self.subtotal = data ['subtotal']
            self.cname = data ['cname']
        elif 'mid' in data:
            self.mid = data ['mid']
            self.mdate = data ['mdate']
            self.mamount = data ['mamount']
            self.cname = data ['cname']
            self.iname = data ['iname']
            self.tpname = data ['tpname']
            self.mcomment = data ['mcomment']

    @classmethod
    def get_by_uid_this_month(cls, data):
        query = 'select mid, mdate, mamount, cname, iname, tpname, mcomment from movimientos join categorias on mov_cid = cid join items on mov_iid = iid join tipopagos on mov_tpid = tpid where mio = %(mio)s and mov_uid = %(uid)s and mdate between subdate(curdate(), day(curdate())-1) and curdate() order by mdate desc;'
        results = connectToMySQL('dojo_project').query_db(query, data)
        movimientos = []
        for row in results:
            movimientos.append(cls(row))
        return movimientos

    @classmethod
    def get_total_by_cat(cls, data):
        query = 'select sum(mamount) as subtotal, cname from movimientos join categorias on mov_cid = cid where mio = %(mio)s and mov_uid = %(uid)s and mdate between subdate(curdate(), day(curdate())-1) and curdate() group by mov_cid;'
        results = connectToMySQL('dojo_project').query_db(query, data)
        totals = []
        for row in results:
            totals.append(cls(row))
        return totals

    @classmethod
    def save(cls, data):
        query = 'insert into movimientos (mio, mdate, mamount, mcomment, mov_uid, mov_cid, mov_iid, mov_tpid, created_at, updated_at) values (%(mio)s, %(mdate)s, %(mamount)s, %(mcomment)s, %(mov_uid)s, %(mov_cid)s, %(mov_iid)s, %(mov_tpid)s, now(), now());'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update movimientos set mio = %(mio)s, mdate = %(mdate)s, mamount = %(mamount)s, mcomment = %(mcomment)s, mov_cid = %(mov_cid)s, mov_iid = %(mov_iid)s, mov_tpid = %(mov_tpid)s, updated_at = now() where mid = %(mid)s and mov_uid = %(mov_uid)s;'
        return connectToMySQL('dojo_project').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'delete from movimientos where mid = %(mid)s and mov_uid = %(uid)s;'
        return connectToMySQL('dojo_project').query_db(query, data)
    
    @classmethod
    def get_by_mid_uid(cls, data):
        query = 'select * from movimientos where mid = %(mid)s and mov_uid = %(uid)s;'
        result = connectToMySQL('dojo_project').query_db(query, data)
        if not result:
            return False
        return cls(result[0])