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

def tower( x, y, z, width, height, depth ) :
	# Draw a big tower in middle of our stage
	tower = Box()
	tower.material = STONE_BRICK
	tower.position( x, y, z )
	tower.size( width, height, depth )
	tower.draw()

	# Tower roof
	roof = Box()
	roof.material = STONE_BRICK
	roof.position( tower.x - 1, tower.height, tower.z - 1 )
	roof.size( tower.width + 2, 1, tower.depth + 2 )
	roof.draw()

	# Tower roof detail ;)
	roofTop = Box()
	roofTop.material = STONE_BRICK
	roofTop.size( 1, 1, 1 )

	for i in range( 0, roof.width ) :
		if i % 2 == 0 :
			roofTop.position( ( tower.x - 1 ) + i, tower.height + 1, tower.z - 1 )
			roofTop.draw()

	for i in range( 0, roof.width ) :
		if i % 2 == 0 :
			roofTop.position( ( tower.x - 1 ) + i, tower.height + 1, tower.z + tower.depth )
			roofTop.draw()

	for i in range( 0, roof.depth ) :
		if i % 2 == 0 :
			roofTop.position( tower.x - 1, tower.height + 1, ( tower.z - 1 ) + i )
			roofTop.draw()
			roofTop.position( tower.x + tower.width, tower.height + 1, ( tower.z - 1 ) + i )
			roofTop.draw()

	# Draw 4 torchs around the tower
	torch = Box()
	torch.material = TORCH
	torch.size( 1, 1, 1 )
	# First torch
	torch.position( tower.x + 1, 2, tower.z - 1 )
	torch.draw()
	# Second torch
	torch.position( tower.x + 1, 2, tower.z + tower.depth )
	torch.draw()
	# Third
	torch.position( tower.x - 1, 2, tower.z + 1 )
	torch.draw()
	# Fourth
	torch.position( tower.x + tower.width, 2, tower.z + 1 )
	torch.draw()