from khd.minecraft import *
from random import randrange
from khd.mcpi.vec3 import Vec3

size = 1
position = Vec3()

def setup() :
	# Reset diamond position
	position = Vec3( randrange( size ), randrange( size ), randrange( size ) )

	# Clear previous box
	box = Box();
	box.position( 0, 0, 0 )
	box.size( size, size, size )
	box.clear()

	# Draw the box of dirty
	box = Box()
	box.size( size + 1, size + 1, size + 1 )
	box.position( 0, 0, 0 )
	box.material = DIRT
	box.draw()

	# Put the diamond
	diamond = Box()
	box.size( 1, 1, 1 )
	box.position( position.x, position.y, position.z )
	box.material = DIAMOND_BLOCK 
	box.draw()

	# Send the instructions by chat
	world.postToChat( 'Find the diamond inside the box of dirt' )

def loop() :
	return True

def win() :
	blockHits = world.events.pollBlockHits()
	# if a block has been hit
	if blockHits:
		# for each block that has been hit
		for blockHit in blockHits:
			# do something with the block
			p = Vec3( blockHit.pos.x, blockHit.pos.y, blockHit.pos.z )
			if p.x == position.x and p.y == position.y and p.z == position.z :
				if Block( world.getBlock( p ) ) == DIAMOND_BLOCK :
					return True
	return False

def gameOver() :
	return False

setup()
while True :
	if win() is True :
		world.postToChat( 'win' )
	elif gameOver() is True :
		world.postToChat( 'game over' )
	else :
		loop();