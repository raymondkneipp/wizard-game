from format import Format
from colors import Colors

class Spell:
	def __init__(self, name, damage = 0, power = 0, boost = 0, heal = 0, defense = 0):
		self.name = name
		self.damage = damage
		self.power = power
		self.boost = boost
		self.heal = heal
		self.defense = defense
	
	def printSpell(self):
		col = int((Format().width) / 6)

		name = self.name.ljust(col)
		damage = str(self.damage).center(col)
		if self.damage == 0:
			damage = "".center(col)
		power = str(self.power).center(col)
		if self.power == 0:
			power = "".center(col)
		boost = "{:.0%}".format(self.boost).center(col)
		if self.boost == 0:
			boost = "".center(col)
		defense = "{:.0%}".format(self.defense).center(col)
		if self.defense == 0:
			defense = "".center(col)
		heal = str(self.heal).center(col)
		if self.heal == 0:
			heal = "".center(col)
		row = name + Colors.FAIL + damage + Colors.WARNING + power + Colors.OKBLUE + boost + Colors.ENDC + defense + Colors.OKGREEN + heal + Colors.ENDC
		print(row)
		Format().divider()