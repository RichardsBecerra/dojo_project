from misgastos_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Movimiento:
    def __init__ (self, data):
        if 'mid' in data:
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
        if 'subtotal' in data:
            self.subtotal = data ['subtotal']
            self.cname = data ['cname']
        if 'mdate' in data:
            self.mdate = data ['mdate']
            self.mamount = data ['mamount']
            self.cname = data ['cname']
            self.iname = data ['iname']
            self.tpname = data ['tpname']
            self.mcomment = data ['mcomment']

    @classmethod
    def get_by_uid_this_month(cls, data):
        query = 'select mdate, mamount, cname, iname, tpname, mcomment from movimientos join categorias on mov_cid = cid join items on mov_iid = iid join tipopagos on mov_tpid = tpid where mio = %(mio)s and mov_uid = %(uid)s and mdate between subdate(curdate(), day(curdate())-1) and curdate() order by mdate desc;'
        results = connectToMySQL('dojo_project').query_db(query, data)
        movimientos = []
        for row in results:
            movimientos.append(cls(row))
        return movimientos

    @classmethod
    def get_total_by_cat(cls, data):
        query = 'select sum(mamount) as subtotal, cname from movimientos join categorias on mov_cid = cid where mio = 0 and mov_uid = %(uid)s and mdate between subdate(curdate(), day(curdate())-1) and curdate() group by mov_cid;'
        results = connectToMySQL('dojo_project').query_db(query, data)
        totals = []
        for row in results:
            totals.append(cls(row))
        return totals
