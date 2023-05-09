from flask import Blueprint, render_template

physic_bp = Blueprint(
    'physic_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

@physic_bp.route('/physic', methods=['GET'])
def physicpage():
    return render_template('physics.html')