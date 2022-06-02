from misgastos_app import app
from misgastos_app.controllers import users, movimientos, forms, categorias, items

if __name__ == '__main__':
    app.run(debug=True)