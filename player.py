import random
from colors import Colors
from element import Element
from format import Format
from icons import Icons

class Player:
	def __init__(self, name = "Player", element = "random"):
		self.name = name
		self.element = self.setElement(element)
		self.health = Element(self.element).health
		self.maxHealth = self.health
		self.power = 0
		self.maxPower = 8
		self.doublePower = 50
		self.castableSpells = []
		self.defense = Element(self.element).defense
		self.spells = Element(self.element).spells
		self.boost = Element(self.element).boost
		self.accuracy = Element(self.element).accuracy
		self.icon = Element(self.element).icon
	
	def setElement(self, element = "random"):
		elements = ["fire", "water", "earth", "air"]
		if element == "random":
			el = random.randint(0, len(elements) - 1)
			return elements[el]
		else:
			return element

	def resetBoost(self):
		self.boost = 0

	def printSpells(self):
		print()
		print(("\U0001F4DC " + self.name + "'s Spells").center(Format().width))
		self.castableSpells = []
		Format().printSpellHeader()
		for spell in self.spells:
			if self.power >= spell.power:
				spell.printSpell()
				self.castableSpells.append(spell)
		print()

	def cast(self, spell, opp, match):
		match.roundHeader()

		if not spell.name == "Pass":
			if self.accuracy >= random.random():
				self.power -= spell.power
				self.health += spell.heal + (spell.heal * self.boost)
				self.defense += spell.defense

				if self.health > self.maxHealth:
					self.health = self.maxHealth

				heal = spell.heal + (spell.heal * self.boost)
				damage = spell.damage - (spell.damage * opp.defense) + (spell.damage * self.boost)
				self.boost += spell.boost # add boost after damage

				opp.health -= damage

				print(Colors.HEADER)
				print("{0} {1} casts {2}".format(Icons.sparkles, self.name, spell.name).center(Format.width))
				Colors().reset()
				Format().pause()

				if not spell.damage == 0:
					print(Colors.FAIL)
					print("{} {} takes {:.0f} damage".format(Icons.damage, opp.name, damage).center(Format().width))
					Colors().reset()
					Format().pause()
					opp.defense = 0

				if not spell.boost == 0:
					print(Colors.OKBLUE)
					print("{} {} gets {:.0%} boost".format(Icons.boost, self.name, spell.boost).center(Format().width))
					Colors().reset()
					Format().pause()

				if not spell.heal == 0:
					print(Colors.OKGREEN)
					print("{} {} get {:.0f} health".format(Icons.heal, self.name, heal).center(Format().width))
					Colors().reset()
					Format().pause()
				
				if not spell.defense == 0:
					print(Colors.ENDC)
					print("{}  {} gets {:.0%} defense".format(Icons.defense, self.name, spell.defense).center(Format().width))
					Colors().reset()
					Format().pause()

				# Reset boost after heal or damage spell
				if not spell.heal == 0 or not spell.damage == 0:
					self.resetBoost()
					self.boost += spell.boost

			else:
				print(Colors.FAIL)
				print((u"\u274C " + self.name + " fails to cast " + spell.name).center(Format().width))
				Colors().reset()
				Format().pause()
		else:
			print(Colors.WARNING)
			print((u"\u270B " + self.name + " passes").center(Format().width))
			Colors().reset()
			Format().pause()
	
	def genPower(self):
		if self.doublePower >= random.randint(1, 100):
			self.power += 2
		else:
			self.power += 1
		
		if self.power > self.maxPower:
			self.power = self.maxPower
	
	def setHealth(self, health):
		self.health = health
		self.maxHealth = self.health