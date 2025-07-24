from app import app, controllers, login_manager
from flask import render_template, request, redirect, url_for, flash, session
from app.db.models import User
from flask_login import login_user, login_required, logout_user, current_user



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

#when starting app, have a dedicated home page for not signing in


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have successfully logged out.')
    return redirect(url_for('login'))

@app.route("/")
@login_required
def main():
    return render_template('home.html', active="home")


@app.route("/dashboard")
@login_required
def dashboard():
    
    return render_template('home.html', active='dashboard', user=current_user)



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
        is_login = True
        return render_template('login.html', is_login=is_login)
    
    
@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")
        
        if confirm_password != password:
            flash('Passwords DO NOT match. Please try again.')
            return redirect(url_for('register'))

        controller_result = controllers.add_user_controller(username, password)
        if controller_result.is_success:
            flash(controller_result.message)
            return redirect(url_for('login'))
        
        flash(controller_result.message)
        return redirect(url_for('register'))
    
    
    return render_template('register.html')
        
        



