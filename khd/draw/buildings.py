from khd.config import *
from khd.draw.box import *

def house( x, y, z, width = 5, heigth = 4, depth = 4 ) :
	wallMaterial = WOOD
	floorMaterial = STONE
	roofMaterial = WOOD_PLANKS

	wall = Box()
	wall.material = wallMaterial
	# wall
	wall.position( x, y + 1, z )
	wall.size( width, heigth, 1 )
	wall.draw()
	# wall
	wall.position( x + width - 1, y + 1, z )
	wall.size( 1, heigth, depth )
	wall.draw()
	# wall
	wall.position( x, y + 1, z + depth - 1  )
	wall.size( width, heigth, 1 )
	wall.draw()
	# wall
	wall.position( x, y + 1, z )
	wall.size( 1, heigth, depth )
	wall.draw()
	# floor
	floor = Box()
	floor.material = floorMaterial
	floor.position( x, y, z )
	floor.size( width, 1, depth )
	floor.draw()
	# roof
	roof = Box()
	roof.material = roofMaterial
	roof.position( x, heigth + 1, z )
	roof.size( width, 1, depth )
	roof.draw()
	roof.position( x + 1 , heigth + 2, z + 1 )
	roof.size( width - 2, 1, depth - 2 )
	roof.draw()
	roof.position( x + 2 , heigth + 3, z + 2 )
	roof.size( width - 4, 1, depth - 4 )
	roof.draw()