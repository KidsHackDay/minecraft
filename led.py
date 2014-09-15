from khd.minecraft import *
from pyFirmata import Arduino
from mcpi.vec3 import Vec3
from time import *

board = Arduino( '/dev/tty.usbserial-A9651BRV' )
led = True

clear( 10, 10, 10 )

pos = Vec3( 3, 0, 3 )

world.setBlock( pos.x, pos.y, pos.z, GOLD_BLOCK )

while True:
	#Get the block hit events
	blockHits = world.events.pollBlockHits()
	# if a block has been hit
	if blockHits:
		# for each block that has been hit
		for blockHit in blockHits:
			# do something with the block
			p = Vec3( blockHit.pos.x, blockHit.pos.y, blockHit.pos.z )
			if p.x == pos.x and p.y == pos.y and p.z == pos.z :
					if( led == True ) :
						board.digital[ 2 ].write( 1 )
						world.setBlock( pos.x, pos.y, pos.z, DIAMOND_BLOCK )
					else :
						board.digital[ 2 ].write( 0 )
						world.setBlock( pos.x, pos.y, pos.z, GOLD_BLOCK )
					led = not led
					sleep( 0.2 )

