from khd.config import *
from types import *
from khd.mcpi.vec3 import Vec3
from khd.mcpi.block import Block

def swordRightClick( arg ) :
	blockHits = world.events.pollBlockHits()
	# if a block has been hit
	if blockHits:
		# for each block that has been hit
		for blockHit in blockHits:
			# do something with the block
			p = Vec3( blockHit.pos.x, blockHit.pos.y, blockHit.pos.z )
			if isinstance( arg, Vec3 ) is True :
				return arg.x == p.x and arg.y == p.y and arg.z == p.z
			if isinstance( arg, Block ) is True:
				return Block( world.getBlock( p ) ) == arg
	return False
