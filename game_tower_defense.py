from khd.minecraft import *
from random import randrange
from time import sleep

class MyGame( Game ) :
	tick = 0
	tickRound = 25
	# Size of stage
	stageSize = 30;
	# tower position and size
	towerPos = Vec3( 14, 0, 14 )
	towerSize = Vec3( 3, 10, 3 )
	# This is the amount of blocks per round
	level = 1
	# This is where we'll store our blocks properties
	blocks = [] 

	# Let's draw our stage
	def start( game ) :
		# Clear the area
		area = Box()
		area.position( 0, 0, 0 )
		area.size( 40, 30, 40 )
		area.clear()

		# Draw a big stone floor with 3 blocks of height
		floor = Box()
		floor.material = STONE
		floor.position( 0, -1, 0 )
		floor.size( 32, 3, 32 )
		floor.draw()
		# Now we'll remove the central part of our floor to make borders around
		floor.position( 1, 0, 1 )
		floor.size( 30, 2, 30 )
		floor.clear()

		tower( game.towerPos.x, game.towerPos.y, game.towerPos.z, game.towerSize.x, game.towerSize.y, game.towerSize.z )

	def loop( game ) :
		# Check if someone hit a block
		blockHits = world.events.pollBlockHits()
		# if a block has been hit
		if blockHits:
			# for each block that has been hit
			for blockHit in blockHits:
				p = Vec3( blockHit.pos.x, blockHit.pos.y, blockHit.pos.z )
				# Check if the action was in one of game blocks
				if game.blocks.count( p ) != 0 :
					b = Box()
					b.size( 1, 1, 1 )
					b.position( p.x, p.y, p.z )
					b.clear()
					del game.blocks[ game.blocks.index( p ) ]
		
		# Check if the blocks are empty and add one more round of blocks
		if len( game.blocks ) == 0 :
			world.postToChat( 'round ' + str( game.level ) )
			for i in range( 0, game.level ) :
				p = Vec3( randrange( game.stageSize - 1 ) + 1, 0, 1 )
				while game.blocks.count( p ) != 0 :
					p = Vec3( randrange( game.stageSize ), 0, 1 )
				game.blocks.append( p )
			game.level = game.level + 1

		if game.tick > game.tickRound :
			game.tick = 0
			# Draw blocks
			for block in game.blocks :
				b = Box()
				b.size( 1, 1, 1 )
				b.position( block.x, block.y, block.z )
				b.clear()
				# Move them to the center of stage
				if block.x < 15 :
					block.x = block.x + 1
				if block.x > 15 :
					block.x = block.x - 1
				if block.z < 15 :
					block.z = block.z + 1
				if block.z > 15 :
					block.z = block.z - 1
				b.position( block.x, block.y, block.z )
				b.draw()
		game.tick = game.tick + 1

	def checkGameOver( game ) :
		for block in game.blocks :
			if block.x == int( game.stageSize / 2 ) and block.z == int( game.stageSize / 2 ) :
				return True
			else :
				return False

	def gameOver( game ) :
		world.postToChat( 'Game over :/' )
		# Reset and restart
		game.blocks = []
		game.level = 1
		game.start()

game = MyGame()