import mcpi.minecraft as minecraft
from mcpi.block import *
from math import *
import numpy

# world = minecraft.Minecraft.create( 'khdminecraft.no-ip.org', 4711 );
world = minecraft.Minecraft.create();

# DRAWING
class Box :

	def __init__( this ) :
		this.x = 0
		this.y = 0
		this.z = 0
		this.width = 2
		this.height = 2
		this.depth = 2
		this.material = DIRT

	def position( this, x = 0, y = 0, z = 0 ) :
		this.x = x
		this.y = y
		this.z = z

	def size( this, width = 2, height = 2, depth = 2 ) :
		this.width = width
		this.height = height
		this.depth = depth

	def material( this, material = DIRT ) :
		this.material = material

	def draw( this ) :
		for x in range( this.x, ( this.x + this.width ) ):
			for z in range( this.z, ( this.z + this.depth ) ):
				for y in range( this.y, ( this.y + this.height ) ):
					world.setBlock( x, y, z, this.material, this.material )

	def clear( this ) :
		m = this.material
		this.material = AIR
		this.draw()
		this.material = m

class Line( Box ) :
	
	def __init__( this ) :
		this.x1 = 0
		this.y1 = 0
		this.z1 = 0
		this.x2 = 0
		this.y2 = 0
		this.z2 = 0
		this.material = DIRT

	def position( this, x1 = 0, y1 = 0, z1 = 0,  x2 = 0, y2 = 0, z2 = 0) :
		this.x1 = x1;
		this.y1 = y1;
		this.z1 = z1;
		this.x2 = x2;
		this.y2 = y2;
		this.z2 = z2;

	def begin( this, x = 0, y = 0, z = 0 ) :
		this.x1 = x
		this.y1 = y
		this.z1 = z

	def end( this, x = 0, y = 0, z = 0 ) :
		this.x2 = x
		this.y2 = y
		this.z2 = z

	def size( this ) :
		print 'Line has no size'

	def draw( this ) :
		begin = numpy.array( ( this.x1, this.y1, this.z1 ) )
		end = numpy.array( ( this.x2, this.y2, this.z2 ) )
		length = numpy.linalg.norm( begin - end )
		xStep = ( this.x2 - this.x1 ) / length
		yStep = ( this.y2 - this.y1 ) / length
		zStep = ( this.z2 - this.z1 ) / length
		for i in range( 0, int( length ) ) :
			x = int( xStep * i ) + this.x1
			y = int( yStep * i ) + this.y1
			z = int( zStep * i ) + this.z1
			world.setBlock( x, y, z, this.material, this.material )

class Sphere( Box ) :
	def draw( this ) :

		xRadius = this.width / 2
		yRadius = this.height / 2
		zRadius = this.depth / 2

		for x in range( xRadius * -1, xRadius ):
			for y in range( yRadius * -1, yRadius ):
				for z in range( zRadius * -1, zRadius ):
					if x**2 + y**2 + z**2 < xRadius**2:
						world.setBlock( this.x + x, this.y + y, this.z + z, this.material )


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

def clear( this, x = 0, y = 0, z = 0, width = 30, height = 30, depth = 30, ) :
	box = Box();
	box.position( x, y, z )
	box.size( width, height, depth )
	box.clear()

