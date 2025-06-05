from app import app
from flask import render_template

@app.route("/")
def main():
    return render_template('home.html', active="home")

@app.route("/dashboard")
def dashboard():
    return render_template('home.html', active='dashboard')