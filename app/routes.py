from app import app, controllers
from flask import render_template, request, redirect, url_for


@app.route("/")
def main():
    return render_template('home.html', active="home")

@app.route("/dashboard")
def dashboard():
    return render_template('home.html', active='dashboard')


@app.route("/add_user", methods=["GET"])
def adding_user():
    controllers.add_user_controller()
    return render_template('home.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect(url_for('show_forms'), username=username, password=password)
    else:
        return render_template('login.html')
        
        
@app.route("/show_forms/<username>/<password>")
def show_forms(username, password):
    return f'<h3>{username}, {password}</h3>'

