import math, random
from format import Format
from colors import Colors
from icons import Icons

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

			spellToCast = Format().coloredInput("\U0001FA84 What spell do you want to cast? ")

			valid = False
			while not valid:
				for spell in self.player1.castableSpells:
					if spellToCast.lower() == spell.name.lower():
						valid = True
						self.player1.cast(spell, self.player2, self)
						pass
				if not valid:
					print(Colors.FAIL + Icons.cross + " Can not cast spell, try again..." + Colors.ENDC)
					spellToCast = Format().coloredInput("\U0001FA84 What spell do you want to cast? ")
			
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