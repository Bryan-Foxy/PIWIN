from flask import Blueprint, render_template

network_bp = Blueprint(
    'network_bp', __name__,
    static_folder = 'static',
    template_folder =  'templates'
)


@network_bp.route('/network', methods=['GET'])
def networkpage():
    return render_template('network.html')