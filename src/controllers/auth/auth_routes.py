from flask import Blueprint, render_template

auth_bp =  Blueprint(
    'auth_bp', __name__,
    static_folder= 'static',
    template_folder='templates',

)


@auth_bp.route('/', methods=['GET'])
def authpage():
    return render_template('authentication-login.html')

@auth_bp.route('/register', methods=['GET'])
def registerpage():
    return render_template('authentication-register.html')