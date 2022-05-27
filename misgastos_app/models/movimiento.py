from misgastos_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Movimiento:
    def __init__ (self,data):
        self.mid = data ['mid']
        self.mio = data ['mio']
        self.mdate = data ['mdate']
        self.mamount = data ['mamount']
        self.mov_uid = data ['mov_uid']
        self.mov_cid = data ['mov_cid']
        self.mov_iid = data ['mov_iid']
        self.mov_tpid = data ['mov_tpid']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']