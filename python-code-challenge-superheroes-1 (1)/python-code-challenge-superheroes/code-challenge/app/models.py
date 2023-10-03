from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

# add any models you may need. 
class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    serialize_rules = ('-powers.hero')
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    powers = db.relationship('HeroPowers', back_populates='hero')
    
    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "super_name": self.super_name,
        }
    
    
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules = ('-heroes.power')
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    heroes = db.relationship('HeroPowers', back_populates='power')
    
    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "description": self.description,
        }
    
    
    @validates('description')
    def validate_description(self, key, description):
      if not description:
          raise ValueError("Description must be present")
      
      if len(description) < 20:
          raise ValueError("Description must be atleast 20 characters long")
      return description
            
    
class HeroPowers(db.Model, SerializerMixin):        
    __tablename__ = 'hero_powers'
    serialize_rules = ('-power.heroes', '-hero.powers')
    
    id = db.Column(db.Integer, primary_key = True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    power = db.relationship('Power', back_populates='heroes')
    hero = db.relationship('Hero', back_populates='powers')
    
    def to_dict(self):
        return {
            "id":self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
        }
    
    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak' ,'Average']:
            raise ValueError("Strength must be Strong, Weak or Average")
        return strength  
            
        