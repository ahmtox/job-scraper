from flask_restx import Namespace, Resource
from datetime import datetime
from app.scraper.google import scrape_google_jobs
from app.scraper.linkedin import scrape_linkedin_jobs
from app.database import get_session
from app.models import Job

jobs_namespace = Namespace('jobs', description='Job-related operations')

@jobs_namespace.route('/google')
class GoogleJobs(Resource):
    def get(self):
        """Scrape Google Career page jobs."""
        session = get_session()
        
        # Get the most recent job from Google in the DB
        latest_job = session.query(Job).filter_by(platform='Google').order_by(Job.timestamp.desc()).first()
        
        # Scrape new jobs from Google
        new_jobs = scrape_google_jobs()
        
        # Compare timestamps
        if latest_job and new_jobs:
            if latest_job.timestamp >= datetime.utcnow():
                return {'jobs': []}, 200  # No new data, return empty list

        return {'jobs': new_jobs}, 200  # Return new data if available

@jobs_namespace.route('/linkedin')
class LinkedInJobs(Resource):
    def get(self):
        """Scrape LinkedIn jobs."""
        session = get_session()

        # Get the most recent job from LinkedIn in the DB
        latest_job = session.query(Job).filter_by(platform='LinkedIn').order_by(Job.timestamp.desc()).first()

        # Scrape new jobs from LinkedIn
        new_jobs = scrape_linkedin_jobs()

        # Compare timestamps
        if latest_job and new_jobs:
            if latest_job.timestamp >= datetime.utcnow():
                return {'jobs': []}, 200  # No new data, return empty list

        return {'jobs': new_jobs}, 200  # Return new data if available
