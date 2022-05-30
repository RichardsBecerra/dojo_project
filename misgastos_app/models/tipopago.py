from misgastos_app.config.mysqlconnection import connectToMySQL

class Tipopago:
    def __init__ (self, data):
        self.tpid = data ['tpid']
        self.tpname = data ['tpname']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def get(cls, data):
        pass

    @classmethod
    def get_all(cls):
        query = 'select * from tipopagos;'
        results = connectToMySQL('dojo_project').query_db(query)
        tipopagos = []
        for row in results:
            tipopagos.append(cls(row))
        return tipopagos