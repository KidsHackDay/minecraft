from khd.config import *
import numpy

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