from misgastos_app import app
from functools import wraps
from misgastos_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'uid' in session:
            return f(*args, **kwargs)
        else:
            return redirect ('/')
    return decorator

@app.route ('/')
def index():
    return render_template('index.html')

@app.route ('/register')
def register():
    return render_template('register.html')

@app.route ('/registerme', methods=['POST'])
def registerme():
    
    if User.validate_data(request.form):
        pass
    else:
        return redirect ('/register')
    
    if User.get(request.form):
        flash (f'The Email {request.form["email"]} is already registered, please try another one')
        return redirect ('/register')
    else:
        hash = bcrypt.generate_password_hash(request.form['password'])
        new_user = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hash,
        }
        User.save(new_user)
        flash ('Register is done, now please login')
        return redirect ('/')

@app.route ('/login', methods=['POST'])
def login():
    user = User.get(request.form)
    
    if not user:
        flash ('Invalid Email or Password')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ('Invalid Email or Password')
        return redirect('/')
    
    session['uid'] = user.uid
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    session['email'] = user.email
    return redirect('/panel')

@app.route ('/user/account')
@login_required
def user_account():
    uid = {'uid': session['uid']}
    user = User.get(uid)
    return render_template ('account.html', user = user)

@app.route ('/user/update', methods=['POST'])
@login_required
def user_update():
    validated = False
    if User.validate_data(request.form):
        if session['email'] != request.form['email']:
            if not User.get(request.form):
                validated = True
            else:
                flash (f'The Email {request.form["email"]} is already registered, please try another one')
        else:
            validated = True
        if validated:
                User.update(request.form)
                session['first_name'] = request.form['first_name']
                session['last_name'] = request.form['last_name']
                session['email'] = request.form['email']
                flash('Updated user account')
                return redirect('/panel')
    return redirect('/user/account')