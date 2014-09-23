from khd.minecraft import *
from random import randrange
from khd.mcpi.vec3 import Vec3

size = 4
dirtBoxPosition = Vec3()
diamondPosition = Vec3()

def setup() :
	# Reset diamond position
	dirtBoxPosition = Vec3( 5, 5, 5 )
	diamondPosition.x = randrange( size ) + dirtBoxPosition.x;
	diamondPosition.y = randrange( size ) + dirtBoxPosition.y;
	diamondPosition.z = randrange( size ) + dirtBoxPosition.z;

	# Clear previous box
	box = Box();
	box.position( dirtBoxPosition.x, dirtBoxPosition.y, dirtBoxPosition.z )
	box.size( size, size, size )
	box.clear()

	# Draw the box of dirty
	box = Box()
	box.position( dirtBoxPosition.x, dirtBoxPosition.y, dirtBoxPosition.z )
	box.size( size, size, size )
	box.material = DIRT
	box.draw()

	# Put the diamond
	diamond = Box()
	box.position( diamondPosition.x, diamondPosition.y, diamondPosition.z )
	box.size( 1, 1, 1 )
	box.material = DIAMOND_BLOCK 
	box.draw()

	# Send the instructions by chat
	world.postToChat( 'Find the diamond inside the box of dirt' )
	world.postToChat( 'and rigth click it with a sword' )

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