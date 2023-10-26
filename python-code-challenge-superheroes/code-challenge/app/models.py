from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model,SerializerMixin):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hero_powers = db.relationship("HeroPower")


# add any models you may need. 


class Power(db.Model,SerializerMixin):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    hero_powers = db.relationship("HeroPower", back_populates="power") 

    @validates('description')
    def validate_description(self, key, description):
        if description is None or len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long.')
        return description

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(30), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

    hero_parent = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError('Strength must be one of the following values: Strong, Weak, Average')
        return strength
