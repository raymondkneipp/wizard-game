from spell import Spell
from icons import Icons

class Element:
	def __init__(self, element):
		self.name = element
		self.defense = 0
		self.boost = 0
		self.accuracy = 1
		self.icon = "x"
		self.health = 2000

		fairy = Spell("Fairy", power = 2, heal = 80)
		passRound = Spell("Pass")

		if (self.name == "fire"):
			self.defense = 0
			self.boost = 0.45
			self.accuracy = 0.85
			self.icon = Icons.fire
			self.spells = [
				passRound,
				Spell("Enhance", power=1, boost = 0.40),
				Spell("Shield", power=1, defense = 0.10),
				fairy,
				Spell("Burn", 15, 0),
				Spell("Sparks", 40, 1),
				Spell("Fireball", 100, 2, boost=0.25),
				Spell("TNT", 155, 3),
				Spell("Hellfire", 225, 4, boost=0.50),
				Spell("Nova", 300, 5),
				Spell("Ra", 375, 6, boost=1.00),
			]
		elif (self.name == "water"):
			self.defense = .40
			self.boost = 0
			self.accuracy = 0.95
			self.icon = "\U0001F4A7"
			self.health = 4000
			self.spells = [
				passRound,
				Spell("Enhance", power=1, boost = 0.10),
				Spell("Shield", power=1, defense = 0.40),
				fairy,
				Spell("Splash", 7, 0),
				Spell("Rain", 20, 1),
				Spell("Freeze", 50, 2, defense=0.25),
				Spell("Drown", 80, 3),
				Spell("Storm", 115, 4, defense=0.50),
				Spell("Whirlpool", 150, 5),
				Spell("Thor", 225, 6, defense=1.00),
			]
		elif (self.name == "earth"):
			self.defense = .30
			self.boost = .10
			self.accuracy = 0.95
			self.icon = "\U0001F30D"
			self.health = 3000
			self.spells = [
				passRound,
				Spell("Enhance", power=1, boost = 0.20),
				Spell("Shield", power=1, defense = 0.20),
				fairy,
				Spell("Pebble", 10, 0),
				Spell("Rock", 25, 1),
				Spell("Meteor", 65, 2, defense=0.15, boost=0.10),
				Spell("Earthquake", 125, 3),
				Spell("Quicksand", 175, 4, defense=0.35, boost=0.15),
				Spell("Sinkhole", 225, 5),
				Spell("Locus", 275, 6, defense=0.75, boost=0.25),
			]
		elif self.name == "air":
			self.defense = .20
			self.boost = 0.20
			self.accuracy = 0.90
			self.icon = "\U0001F4A8"
			self.health = 3500
			self.spells = [
				passRound,
				Spell("Enhance", power=1, boost = 0.30),
				Spell("Shield", power=1, defense = 0.30),
				fairy,
				Spell("Breeze", 12, 0),
				Spell("Tornado", 33, 1),
				Spell("Windstorm", 85, 2, defense=0.20, boost=0.20),
				Spell("Sandstorm", 135, 3),
				Spell("Windmill", 200, 4, defense=0.30, boost=0.30),
				Spell("Typhoon", 275, 5),
				Spell("Bora", 325, 6, defense=0.50, boost=0.50),
			]