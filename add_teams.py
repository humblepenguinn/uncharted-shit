import pandas as pd
from main import db
from main import Team

from utils import *
import json

def add_teams():
    df = pd.read_csv("data.csv", usecols = ['HC ID'])

    data = {}

    for i in df['HC ID'].to_list():
        random_path = generate_random_path()

        db.session.add(Team(id=i, path=random_path, visited_paths=""))
        db.session.commit()

        data[i] = {"path": random_path}

    with open('data.json', 'w') as f:
        json.dump(data, f)
