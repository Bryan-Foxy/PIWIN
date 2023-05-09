from flask import Blueprint, render_template

virtual_bp = Blueprint(
    'virtual_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

@virtual_bp.route('/virtual', methods=['GET'])
def virtualpage():
    return render_template('virtual.html')