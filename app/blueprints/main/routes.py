from . import bp as main_bp
from flask import render_template

@main_bp.route('/')
def home():
    pass
    return render_template('home.jinja', title='Home')


