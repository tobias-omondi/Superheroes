#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api,Resource

from models import db, Hero,Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Home(Resource):
    def get(self):
        response_dict = {
            "message": "Welcome to my API of Super heroes"
        }
        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(Home, "/")

# def home():
#     return

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    json_heroes = []
    for hero in heroes:
        json_hero = [{
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }]
        json_heroes.append(json_hero)

    response = make_response(jsonify(json_heroes), 200)
    return response



# @app.route('/')
# def home():
#     return ''


    
    


if __name__ == '__main__':
    app.run(port=5552, debug= True)
