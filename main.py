import random, os, math, time

def coloredInput(text):
	print(Colors.HEADER, end='')
	val = input(text + Colors.BOLD + Colors.WARNING)
	Colors().reset()
	return val

class Icons:
	fire = "\U0001F525"
	water = "\U0001F4A7"
	earth = "\U0001F30D"
	air = "\U0001F4A8"
	damage = "\U0001F494" # broken heart
	power = "\U000026A1" # bolt
	boost = "\U0001F53C" # up arrow box
	heal = "\U0001F496" # heart with sparkles
	sparkles = u"\u2728" # sparkles
	defense = "\U0001F6E1" # shield
	accuracy = "\U0001F3AF" # target
	doublePower = "\U00002B50" # star
	cross = u"\u274C"

class Colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	GREY = '\33[90m'

	def reset(self):
		print(self.ENDC, end='')

class Format:
	COLUMNS = os.popen('stty size', 'r').read().split()[1]
	width = int(COLUMNS)

	def __init__(self):
		self.horizontal = u"\u2501"
		self.vertical = u"\u2503"
		self.topleft = u"\u250F"
		self.topright = u"\u2513"
		self.bottomleft = u"\u2517"
		self.bottomright = u"\u251B"
		self.bottomleftConnected = u"\u2523"
		self.bottomrightConnected = u"\u252B"
		self.topBorder = self.topleft + self.horizontal*(self.width-2) + self.topright
		self.bottomBorder = self.bottomleft + self.horizontal*(self.width-2) + self.bottomright
		self.bottomBorderConnected = self.bottomleftConnected + self.horizontal*(self.width-2) + self.bottomrightConnected
	
	def headerBar(self, header):
		header = header.center(self.width - 2)
		header = self.vertical + header + self.vertical
		
		print(self.topBorder)
		print(header)
		print(self.bottomBorder)
	
	def split(self, left, right, divider = " ", start = False, end = False):
		if start:
			print(self.topBorder)
		
		halfDivider = int(math.ceil(len(divider) / 2.0))
		halfSize = int(self.width / 2 - halfDivider - 1)

		row = self.vertical + left.center(halfSize) + divider + right.center(halfSize)
		while len(row) < self.width - 1:
			row = row + " "
		row = row + self.vertical

		print(row)

		if end:
			print(self.bottomBorder)
	
	def divider(self):
		print(Colors.GREY + self.horizontal * self.width + Colors.ENDC)

	def printSpellHeader(self):
		col = int((Format().width) / 6)

		name = "Name".ljust(col)
		damage = Colors.FAIL + "Damage".center(col)
		power = Colors.WARNING + "Power".center(col)
		boost = Colors.OKCYAN + "Boost".center(col)
		defense = Colors.ENDC + "Defense".center(col)
		heal = Colors.OKGREEN + "Heal".center(col) + Colors.ENDC
		row = name + damage + power + boost + defense + heal
		while len(row) < Format().width - 1:
			row = row + " "
		print(row)
		Format().divider()
	
	def pause(self, seconds = 2):
		time.sleep(seconds)
	
	def clear(self):
		os.system("clear")

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


class Match:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.round = 1
	
	def newRound(self):
		self.player1.genPower()
		self.player2.genPower()

		self.roundHeader()
	
	def begin(self):
		while self.player1.health > 0 and self.player2.health > 0:
			self.newRound()
			
			self.player1.printSpells()

			spellToCast = coloredInput("\U0001FA84 What spell do you want to cast? ")

			valid = False
			while not valid:
				for spell in self.player1.castableSpells:
					if spellToCast.lower() == spell.name.lower():
						valid = True
						self.player1.cast(spell, self.player2, self)
						pass
				if not valid:
					print(Colors.FAIL + Icons.cross + " Can not cast spell, try again..." + Colors.ENDC)
					spellToCast = coloredInput("\U0001FA84 What spell do you want to cast? ")
			
			if self.player2.health <= 0:
				continue
				
			self.player2.printSpells()

			self.player2.cast(self.player2.castableSpells[random.randint(0, len(self.player2.castableSpells)-1)], self.player1, self)

			self.round += 1
		
		if self.player1.health <= 0:
			print(Colors.FAIL)
			print((u"\u274C You LOST on round " + str(self.round)).center(Format().width))
			Colors().reset()
		elif self.player2.health <= 0:
			print(Colors.OKGREEN)
			print((u"\u2705 You WON on round " + str(self.round)).center(Format().width))
			Colors().reset()
		
	def roundHeader(self):
		Format().clear()
		print(Colors.BOLD)
		print(("\U0001F551 Round " + str(self.round)).center(Format().width))
		Format().divider()

		print((self.player1.icon + " " + self.player1.name).ljust(int(Format().width/2)-2) + "\U0001F19A" + (self.player2.name + " " + self.player2.icon).rjust(int(Format().width/2)-2))
		Colors().reset()


		print(Colors.OKGREEN)
		p1h = "{} {:,} / {:,}".format(Icons.heal, math.ceil(self.player1.health), self.player1.maxHealth).ljust(int(Format().width/2)-4) + "Health"
		p2h = "{:,} / {:,} {}".format(math.ceil(self.player2.health), self.player2.maxHealth, Icons.heal).rjust(int(Format().width/2)-4)
		print(p1h + p2h)

		p1percent = math.floor(self.player1.health / self.player1.maxHealth * 100)
		p2percent = math.floor(self.player2.health / self.player2.maxHealth * 100)
		maxSpace = (Format().width-2) / 2
		p1p = p1percent * maxSpace / 100
		p2p = p2percent * maxSpace / 100
		full1 = u"\u2588"*int(p1p)
		full2 = u"\u2588"*int(p2p)
		empty1 = int(maxSpace - len(full1)) * u"\u2591"
		empty2 = int(maxSpace - len(full2)) * u"\u2591"
		print(full1 + empty1 + "  " + full2 + empty2)

		print(Colors.OKBLUE)
		p1b = "{} {:.0%}".format(Icons.boost, self.player1.boost).ljust(int(Format().width/2)-4) + "Boost"
		p2b = "{:.0%} {}".format(self.player2.boost, Icons.boost).rjust(int(Format().width/2)-3)
		print(p1b + p2b)

		print(Colors.ENDC)
		p1d = "{}  {:.0%}".format(Icons.defense, self.player1.defense).ljust(int(Format().width/2)-4) + "Defense"
		p2d = "{:.0%} {}".format(self.player2.defense, Icons.defense).rjust(int(Format().width/2)-4)
		print(p1d + p2d)

		print(Colors.HEADER)
		p1a = "{} {:.0%}".format(Icons.accuracy, self.player1.accuracy).ljust(int(Format().width/2)-5) + "Accuracy"
		p2a = "{:.0%} {}".format(self.player2.accuracy, Icons.accuracy).rjust(int(Format().width/2)-5)
		print(p1a + p2a)



		print(Colors.OKCYAN)
		p1x = "{} {:d}%".format(Icons.doublePower, self.player1.doublePower).ljust(int(Format().width/2)-9) + "X2 Power Chance"
		p2x = "{:d}% {}".format(self.player2.doublePower, Icons.doublePower).rjust(int(Format().width/2)-8)
		print(p1x + p2x)

		print(Colors.WARNING)
		print("{0} {1} / {2}".format(Icons.power, self.player1.power, self.player1.maxPower).ljust(int(Format().width/2)-4) + "Power" + "{1} / {2} {0}".format(Icons.power, self.player2.power, self.player2.maxPower).rjust(int(Format().width/2)-3))

		Colors().reset()
		Format().divider()


class Game:
	wizardElements = ["fire", "water", "earth", "air", "random"]
	elementIcons = [Icons.fire, Icons.water, Icons.earth, Icons.air, "?"]

	def __init__(self):
		self.welcomeMessage()
		player1Name = self.getPlayerName()
		player1Type = self.getPlayerElement(player1Name)


		p1 = Player(player1Name, player1Type)
		p2 = Player("Enemy")

		m = Match(p1, p2)
		m.begin()
	
	def getPlayerName(self):
		name = coloredInput("What is your name? ")
		return name[0].upper() + name[1:]
	
	def getPlayerElement(self, name):
		Format().clear()
		Format().headerBar("Welcome " + name + "!")
		print("Please choose an element?")
		for i in range(0, len(self.wizardElements)):
			print((self.elementIcons[i] + " " + self.wizardElements[i][0].upper() + self.wizardElements[i][1:]).center(Format().width))
		element = coloredInput("Select wizard element: ")

		while not element in self.wizardElements:
			if element == "":
				element = "random"
				print("Random")
				break
			print("{0}{1} Not valid element. Try again...".format(Icons.cross, Colors.FAIL))
			Colors().reset()
			element = coloredInput("Select wizard element: ")
		
		return element
	
	def welcomeMessage(self):
		Format().clear()
		Format().headerBar("Welcome to The Wizard Game")

g = Game()

# TODO
# simplify input validation with do while loop
# icons class
# gui
# multiplayer
# 1v1, 1v2, 1v3...
# critical
# use print format