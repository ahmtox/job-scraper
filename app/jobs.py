from flask_restx import Namespace, Resource
from app.scraper.google import scrape_google_jobs
from app.scraper.linkedin import scrape_linkedin_jobs

jobs_namespace = Namespace('jobs', description='Job-related operations')

@jobs_namespace.route('/google')
class GoogleJobs(Resource):
    def get(self):
        """Scrape Google Career page jobs."""
        jobs = scrape_google_jobs()
        return {'jobs': jobs}, 200

@jobs_namespace.route('/linkedin')
class LinkedInJobs(Resource):
    def get(self):
        """Scrape LinkedIn jobs."""
        jobs = scrape_linkedin_jobs()
        return {'jobs': jobs}, 200
