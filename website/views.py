from flask import Blueprint, render_template, request, flash, jsonify, session
from . import db
from .models import Team
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        session.pop('_flashes', None)
        # user pressed the submit button

        # Verifying Team ID
        team_id = request.form.get('team-id')
        team = Team.query.filter_by(id=team_id).first()
        if not team:
            flash("Error: Invalid Team ID")

        # Verifying Location ID based on teams path
        if team:
            location_id = request.form.get('location-id')
            print(f"Team Path: {team.path}")

            f = open("website/locations-id.json")
            data = json.load(f)

            location_to_be = 1 if not team.visited_paths else team.visited_paths.pop() + 1

            if data[str(location_to_be)] == location_id:
                f.close()

                f = open("website/riddles.json")
                data = json.load(f)

                flash(f"Location To Be: {location_to_be}")
                flash(f"Visited Paths: {team.visited_paths}")
                flash(f"Riddle: {data[str(location_to_be)]['riddle']}")
                f.close()


                if team.visited_paths:
                    team.visited_paths = team.visited_paths.append(location_to_be)
                else:
                    team.visited_paths = [location_to_be]
                db.session.commit()

            else:
                flash("Error: Nikal yahan se OR invalid location id plz recheck")


    return render_template("home.html")

