from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configure the app (you can add configuration here)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Example secret key for session or cookies
    
    # Register blueprints for routes
    from .routes import main
    app.register_blueprint(main)

    # You can add more app configuration and initialization here, such as databases or login managers

    return app
