from khd.minecraft import *

# This is where you are
steve = getMyPosition()

class MyGame( Game ) :

	tower1 = Vec3( steve.x + 5, steve.y, steve.z + 5 )
	tower2 = Vec3( steve.x + 80, steve.y, steve.z + 80 )
	towerSize = Vec3( 5, 15, 5 )

	def start( game ) :
		# Clear the arena
		arena = Box()
		arena.size( 90, 17, 90 )
		arena.position( steve.x, steve.y, steve.z )
		arena.clear()

		# The red tower
		tower( game.tower1.x, game.tower1.y, game.tower1.z, game.towerSize.x, game.towerSize.y, game.towerSize.z )
		# Put a red wool on top of tower 1
		redWool = Box()
		redWool.material = WOOL.id
		redWool.data = 14
		redWool.x = game.tower1.x + int( game.towerSize.x / 2 )
		redWool.y = game.tower1.y + game.towerSize.y + 1
		redWool.z = game.tower1.z + ( game.towerSize.z / 2 )
		redWool.draw()

		# The blue tower
		tower( game.tower2.x, game.tower2.y, game.tower2.z, game.towerSize.x, game.towerSize.y, game.towerSize.z )
		# Put a red wool on top of tower 1
		blueWool = Box()
		blueWool.material = WOOL.id
		blueWool.data = 11
		blueWool.x = game.tower2.x + int( game.towerSize.x / 2 )
		blueWool.y = game.tower2.y + game.towerSize.y + 1
		blueWool.z = game.tower2.z + ( game.towerSize.z / 2 )
		blueWool.draw()

		print 'start'

	def checkWin( game ) :
		# Check if the red wool is on the roof of the red tower
		redIn = False
		blueIn = False
		for x in range( 0, game.towerSize.x ) :
			for z in range( 0, game.towerSize.z ) :
				b = world.getBlockWithData( game.tower1.x + x, game.towerSize.y + 1, game.tower1.z + z )
				if b.id == WOOL.id and b.data == 14 :
					redIn = True
				if b.id == WOOL.id and b.data == 11 :
					blueIn = True
		if redIn == True and blueIn == True :
			game.winner = 'Red'
			return True

		redIn = False
		blueIn = False
		for x in range( 0, game.towerSize.x ) :
			for z in range( 0, game.towerSize.z ) :
				b = world.getBlockWithData( game.tower2.x + x, game.towerSize.y + 1, game.tower2.z + z )
				if b.id == WOOL.id and b.data == 14 :
					redIn = True
				if b.id == WOOL.id and b.data == 11 :
					blueIn = True
		if redIn == True and blueIn == True :
			game.winner = 'Blue'
			return True

		return False

	def win( game ) :
		world.postToChat( 'YAY! Team ' + game.winner + ' won!' )
		return False


game = MyGame()