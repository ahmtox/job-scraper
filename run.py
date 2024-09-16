import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv  # Import dotenv to load environment variables
from app.jobs import jobs_namespace  # Import your job scraping routes

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Set the secret key from the environment variable
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Initialize Flask-RESTX API
    api = Api(app, title="Job Scraper API", version="1.0", description="API for scraping job listings")

    # Register namespaces (routes)
    api.add_namespace(jobs_namespace, path='/api/jobs')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
else:
    app = create_app()