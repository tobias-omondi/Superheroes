from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'hero'
    serialize_rules = ('-heropowers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(50), nullable=False) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    hero_powers = db.relationship("HeroPower", back_populates='hero')

    def __repr__(self):
        return f'<Hero {self.name} aka {self.super_name}>'


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    serialize_rules = ('-heropowers.power',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship("HeroPower", back_populates="power", primaryjoin="Power.id == HeroPower.power_id")
    
    def __repr__(self):
        return f'<Power {self.name} aka {self.description}'

    @validates('description')
    def validate_description(self, key, description):
        if description is None or len(description) < 20:
            raise ValueError('Description must be present and at least 20 characters long.')
        return description

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heropowers'
    serialize_rules = ('-hero.powers', '-power.heroes')

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(Enum('Strong', 'Weak', 'Average'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError('Strength must be one of the following values: Strong, Weak, Average')
        return strength
