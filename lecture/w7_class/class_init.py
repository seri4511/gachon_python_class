class Ball:
	def __init__(self, color, size, direction):
		self.color = color 
		self.size = size 
		self.direction = direction
	def bounce(self):	
		if self.direction == 'down': self.direction = 'up'
		else:  self.direction = 'down'

		print "Bounce to", self.direction

myBall = Ball('red', 'small','down')
yourBall = Ball('red', 'small','up')

for i in range(0,3):
	myBall.bounce()
	yourBall.bounce()