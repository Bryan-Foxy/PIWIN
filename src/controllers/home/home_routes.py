from flask import Blueprint, render_template, current_app
import pandas as pd

#Initialisation of Blueprint
home_bp = Blueprint(
    'home_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'

)

@home_bp.route('/home', methods=['GET'])
def homepage():
    data = pd.read_csv(current_app.config['DASHBOARD_FILE'])
    return render_template('index.html', data=data)


