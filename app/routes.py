from app import app, controllers, login_manager
from flask import render_template, request, redirect, url_for, flash
from app.db.models import User
from flask_login import login_user, login_required, logout_user, current_user



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
@login_required
def main():
    return render_template('home.html', active="home")

@app.route("/dashboard")
@login_required
def dashboard():
    
    return render_template('home.html', active='dashboard', user=current_user)

# refactor
@app.route("/add_user", methods=["GET"])
def adding_user():
    controllers.add_user_controller()
    return render_template('home.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        is_authenticated, user = controllers.get_and_authenticate_user_controller(username, password)
        
        if is_authenticated:
            login_user(user)
            return redirect(url_for('dashboard'))
        
        else:
            flash('Wrong password!', 'error')
            return redirect(url_for('login'))
        
    else:
        
        return render_template('login.html')
        
        


@app.route("/get_user")
def get_user_test():
    controllers.get_user_controller()
    return f'<h3>Hello</h3>'


@app.route("/logintest")
def login_test():
    user = 'martin'
    password = 'password'
    
    #Returns true if logged in 
    is_true, user = controllers.get_user_controller(user, password)
    if is_true:
        login_user(user)
        
    
    return '<h3>Hello</h3>'



@app.route("/loggedin")
@login_required
def logged_in():
    return '<h3>HELLO</h3>'

