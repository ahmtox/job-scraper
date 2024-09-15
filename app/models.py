from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String, nullable=True)
    platform = Column(String, nullable=False)  # e.g. 'Google', 'LinkedIn'
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Job(title='{self.title}', platform='{self.platform}')>"
