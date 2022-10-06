from icons import Icons
from player import Player
from match import Match
from format import Format
from colors import Colors

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
		name = Format().coloredInput("What is your name? ")
		return name[0].upper() + name[1:]
	
	def getPlayerElement(self, name):
		Format().clear()
		Format().headerBar("Welcome " + name + "!")
		print("Please choose an element?")
		for i in range(0, len(self.wizardElements)):
			print((self.elementIcons[i] + " " + self.wizardElements[i][0].upper() + self.wizardElements[i][1:]).center(Format().width))
		element = Format().coloredInput("Select wizard element: ")

		while not element in self.wizardElements:
			if element == "":
				element = "random"
				print("Random")
				break
			print("{0}{1} Not valid element. Try again...".format(Icons.cross, Colors.FAIL))
			Colors().reset()
			element = Format().coloredInput("Select wizard element: ")
		
		return element
	
	def welcomeMessage(self):
		Format().clear()
		Format().headerBar("Welcome to The Wizard Game")