from . import db
from sqlalchemy.sql import func

class Team(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    path = db.Column(db.String(1000))
    visited_paths = db.Column(db.String(1000))

