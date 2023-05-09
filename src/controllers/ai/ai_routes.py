from flask import Blueprint, render_template

ai_bp = Blueprint(
    'ai_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

@ai_bp.route('/model', methods=['GET'])
def modelpage():
    return render_template('model.html')