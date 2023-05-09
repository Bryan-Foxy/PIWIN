from flask import Blueprint, render_template

user_alert_bp = Blueprint(
    'user_alert_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

@user_alert_bp.route('/alert', methods=['GET'])
def alertpage():
    return render_template('alert.html')


@user_alert_bp.route('/user', methods=['GET'])
def userpage():
    return render_template('user.html')
