from misgastos_app.config.mysqlconnection import connectToMySQL

class Categoria:
    def __init__ (self, data):
        self.cid = data ['cid']
        self.cname = data ['cname']
        self.cio = data ['cio']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def get(cls, data):
        pass

    @classmethod
    def get_all_by_cio(cls, data):
        query = 'select * from categorias where cio = %(cio)s order by cname;'
        results = connectToMySQL('dojo_project').query_db(query, data)
        categorias = []
        for row in results:
            categorias.append(cls(row))
        return categorias
