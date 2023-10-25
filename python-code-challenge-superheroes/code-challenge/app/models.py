from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)

    # add any models you may need. 

    powers = db.relationship('Power', secondary='hero_powers', back_populates='heroes')

class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)

    heroes = db.relationship('Hero', secondary='hero_powers', back_populates='powers')

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), primary_key=True)

    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heroes')

db.create_all()
