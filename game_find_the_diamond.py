from khd.minecraft import *
from random import randrange
from khd.mcpi.vec3 import Vec3

size = 4
dirtBoxPosition = Vec3()
diamondPosition = Vec3()

class MyGame( Game ) :

	def start( game ) :
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


	def checkWin( game ) :
		return swordRightClick( DIAMOND_BLOCK )

	def win( game ) :
		world.postToChat( 'Yay! You won the game! :D' )

game = MyGame()
