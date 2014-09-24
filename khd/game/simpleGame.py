class Game :
	score = 0
	def __init__( self ) :
		self.start()
		try :
			while True :
				if self.checkWin() is True :
					self.win()
				elif self.checkGameOver() is True :
					self.gameOver()
				else :
					self.loop()
		except KeyboardInterrupt:
			print ''
			print 'exiting the game'

	def start( self ) :
		print 'start'

	def loop( self ) :
		return False

	def checkWin( self ) :
		return False

	def checkGameOver( self ) :
		return False

	def win( self ) :
		print 'Yay! Win!'

	def gameOver( self ) :
		print 'Game over :('
