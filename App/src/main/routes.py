from src.main import bp
from flask import render_template

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
