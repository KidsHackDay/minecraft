from khd.minecraft import *
from khd.mcpi.vec3 import Vec3
from time import *

# This will make the block move when you hit it
pos = Vec3( 3, 0, 3 )

world.setBlock( pos.x, pos.y, pos.z, DIAMOND_BLOCK )

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
				if Block( world.getBlock( p ) ) == DIAMOND_BLOCK :
					if blockHit.face == 4 :
						pos.x += 1
					if blockHit.face == 5 :
						pos.x -= 1
					if blockHit.face == 3 :
						pos.z -= 1
					if blockHit.face == 2 :
						pos.z += 1
					world.setBlock( pos.x, pos.y, pos.z, DIAMOND_BLOCK )
					world.setBlock( p.x, p.y, p.z, AIR )

	sleep( 0.3 )