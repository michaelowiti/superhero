#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPowers


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to Super heroes'

@app.route('/heroes')
def heroes():
    heroes = []
    for hero in Hero.query.all():
        hero_dict = {
            "id": hero.id,
            "name":hero.name,
            "super_name": hero.super_name,
        }
        heroes.append(hero_dict)
    response = make_response(jsonify(heroes), 200)
    return response    

@app.route('/heroes/<int:id>', methods=['GET'])
def hero_by_id(id):
    hero = Hero.query.get(int(id))
    if not hero:
        return {"error": "Hero not found"}, 404
    powers = Power.query.join(HeroPowers).filter(HeroPowers.hero_id == id).all()
    powers_dict = [power.to_dict() for power in powers]
    
    hero_dict = {
        "name":hero.name,
        "super_name": hero.super_name,
        "powers": powers_dict,
    }

    response = make_response(jsonify(hero_dict), 200)
    return response

@app.route('/powers')
def powers():
    powers = Power.query.all()
    power_dict = [power.to_dict() for power in powers]
    
    response = make_response(jsonify(power_dict), 200)
    return response

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_by_id(id):
    power = Power.query.get(int(id))
    
    if not power:
            return {"error": "Power not found"}, 404
    
    if request.method == 'GET':
        power_dict = power.to_dict()
        response = make_response(jsonify(power_dict), 200)
        return response
    
    elif request.method == 'PATCH':
    
        for attr in request.form:
            setattr(power, attr, request.form.get(attr))
        
        try:
            db.session.add(power)
            db.session.commit()
            power_dict = power.to_dict()
            response = make_response(jsonify(power_dict), 200)
            return response    
        except:
            return {"errors": ["validation errors"]} , 404

@app.route('/hero_powers', methods=['POST'])
def post_hero_powers():
    data = request.get_json()
    new_hero_power = HeroPowers(
        strength = data["strength"],
        power_id = data["power_id"],
        hero_id = data["hero_id"],
    )    
       
    try:
        db.session.add(new_hero_power)
        db.session.commit()
        id = data["hero_id"]
        hero = Hero.query.get(int(id))
        powers = Power.query.join(HeroPowers).filter_by(hero_id = id).all()
        powers_dict = [power.to_dict() for power in powers]
    
        hero_dict = {
          "id":hero.id,
          "name":hero.name,
          "super_name":hero.super_name,
          "powers":powers_dict
        }
           
        response = make_response(jsonify(hero_dict), 200)
        return response  
    except:  
        return {"errors": ["validation errors"]} , 404  
           
        
        
    
    
if __name__ == '__main__':
    app.run(port=5555)    