"""Initialize Flask app."""
from flask import Flask, render_template
import secrets
from .config import Config


def page_not_found(e):
    return render_template('404.html'), 404


def page_internal_server(e):
    return render_template('500.html'), 500


def create_app(config_class=Config):
    """Create Flask application."""
    secret = secrets.token_urlsafe(32)
    global redis_instance
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_internal_server)
    app.config.from_object(config_class)
    app.secret_key = secret
    app.debug = True


    with app.app_context():
        # Import parts of our application
        from .controllers.home import home_routes
        from .controllers.auth import auth_routes
        from .controllers.network import network_routes
        from .controllers.physic import physic_routes
        from .controllers.virtual import virtual_routes
        from .controllers.ai import ai_routes
        from .controllers.user_alert import user_alert_routes


        # blueprints registration
        app.register_blueprint(home_routes.home_bp, url_prefix='')
        app.register_blueprint(auth_routes.auth_bp, url_prefix='')
        app.register_blueprint(network_routes.network_bp, url_prefix='')
        app.register_blueprint(physic_routes.physic_bp, url_prefix='')
        app.register_blueprint(virtual_routes.virtual_bp, url_prefix='')
        app.register_blueprint(ai_routes.ai_bp, url_prefix='')
        app.register_blueprint(user_alert_routes.user_alert_bp, url_prefix='')

        
        return app


def get_redis_instance():
    global redis_instance
    return redis_instance
