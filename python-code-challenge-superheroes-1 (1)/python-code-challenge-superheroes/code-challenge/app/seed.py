from random import randint, choice as rc
from app import app
from models import Hero, Power,HeroPowers, db

seed_powers = "🦸‍♀️ Seeding powers..."
powers = [
  { "name": "flight", 
    "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
  { "name": "super human senses", 
    "description": "allows the wielder to use her senses at a super-human level" },
  { "name": "super strength", 
    "description": "gives the wielder super-human strengths" },
  { "name": "elasticity", 
    "description": "can stretch the human body to extreme lengths" },
]

seed_heroes = "🦸‍♀️ Seeding heroes..."
heroes = [
  { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
  { "name": "Janet Van Dyne", "super_name": "The Wasp" },
  { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
  { "name": "Carol Danvers", "super_name": "Captain Marvel" },
  { "name": "Jean Grey", "super_name": "Dark Phoenix" },
  { "name": "Ororo Munroe", "super_name": "Storm" },
  { "name": "Kitty Pryde", "super_name": "Shadowcat" },
  { "name": "Elektra Natchios", "super_name": "Elektra" }
]

ap = "🦸‍♀️ Adding powers to heroes..."
strengths = ["Strong", "Weak", "Average"]

with app.app_context():
  Hero.query.delete()
  Power.query.delete()
  HeroPowers.query.delete()
  
  heroes_list = []
  for hero in heroes:
    hero = Hero(
      name = hero['name'],
      super_name = hero['super_name'],
    )
    heroes_list.append(hero)
  db.session.add_all(heroes_list)
  print(seed_heroes)
    
  powers_list = []  
  for power in powers:
    pow = Power(
      name = power['name'], 
      description = power['description'] )  

    powers_list.append(pow)
  db.session.add_all(powers_list)
  print(seed_powers)
  
  heroes_powers = []
  for hero in heroes_list:
    for i in range(randint(1, 3)):
      hero_powers = HeroPowers(
        hero = hero,
        power = rc(powers_list),
        strength = rc(strengths),
      )
      heroes_powers.append(hero_powers)
  db.session.add_all(heroes_powers)    
  db.session.commit() 
  print(ap)
  print("🦸‍♀️ Done seeding!")