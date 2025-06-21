from app import app, controllers
from flask import render_template


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
    