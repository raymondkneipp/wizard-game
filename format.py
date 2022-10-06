import os, time
from colors import Colors

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
	
	def coloredInput(self, text):
		print(Colors.HEADER, end='')
		val = input(text + Colors.BOLD + Colors.WARNING)
		Colors().reset()
		return val