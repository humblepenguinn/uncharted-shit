from flask import Blueprint, render_template, request, flash, jsonify, session
import random

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

            if location_id not in data.values():
                flash("Error Invalid Location ID")

            print(len(team.visited_paths))
            if location_id == 'DEFAULT' and team.visited_paths == '-1' :
                z = open('website/riddles.json')
                riddles = json.load(z)
                riddle = random.choice(riddles[str(team.path.split(',')[0])]['riddles'])
                #team.visited_paths = '-1'
                #db.session.commit()
                f.close()

                flash(f"None Riddle: {riddle}")
                #flash(f"Do not reload the page")

            else:
                if team.visited_paths:
                    location_to_be = int(
                        team.path.split(',')[int(team.visited_paths.split(',').pop()) + 1]
                    )

                    #flash(f"Message Location To Be: {location_to_be}")
                    #flash(f"Message Visited Paths: {team.visited_paths}")
                    flash(f"Message Path: {team.path}")

                    if data[str(location_to_be)] == location_id:
                        f.close()

                        f = open("website/riddles.json")
                        data = json.load(f)
                        nextLocIndex = team.path.split(',')[int(team.visited_paths.split(',').pop()) + 2]
                        riddle = random.choice(data[str(nextLocIndex)]['riddles'])
                        # if location_to_be == -1:
                        #     riddle = random.choice(data[team.path.split(',')[0]]['riddles'])
                        # else:
                        #     riddle = random.choice(data[str(location_to_be)]['riddles'])
                        flash(f"None Riddle: {riddle}")
                        f.close()


                        if team.visited_paths:
                            team.visited_paths = team.visited_paths + f", {int(team.visited_paths.split(',').pop()) + 1}"
                            db.session.commit()
                        else:
                            team.visited_paths = "0"
                            db.session.commit()

                    else:
                        flash("Error Nikal yahan se")
                        f = open("website/riddles.json")
                        data = json.load(f)
                        riddle = random.choice(
                            data[team.path.split(',')[int(team.visited_paths.split(',').pop()) + 1]]['riddles']
                        )
                        flash(f'None Riddle: {riddle}')
                        f.close()




    return render_template("home.html")

