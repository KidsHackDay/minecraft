from khd.config import *

def getMyPosition() :
	pos = world.player.getPos()
	pos.x = int( pos.x )
	pos.y = int( pos.y )
	pos.z = int( pos.z )
	return pos;