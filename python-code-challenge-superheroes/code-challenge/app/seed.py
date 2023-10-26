import random
from app import db
from models import Hero, Power, HeroPower

# Seed powers
def seed_powers():
    powers = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
    ]

    for power in powers:
        db.session.add(Power(name=power["name"], description=power["description"]))

    db.session.commit()

# Seed heroes
def seed_heroes():
    heroes = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"},
    ]

    for hero in heroes:
        db.session.add(Hero(name=hero["name"], super_name=hero["super_name"]))

    db.session.commit()

# Add powers to heroes
def add_powers_to_heroes():
    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    powers = Power.query.all()

    for hero in heroes:
        for i in range(random.randint(1, 4)):
            hero_power = HeroPower(strength=random.choice(strengths), hero_id=hero.id, power_id=random.choice(powers).id)
            db.session.add(hero_power)

    db.session.commit()

