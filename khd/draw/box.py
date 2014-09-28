from khd.config import *
import numpy

class Box :

	def __init__( this ) :
		this.x = 0
		this.y = 0
		this.z = 0
		this.width = 1
		this.height = 1
		this.depth = 1
		this.material = DIRT
		this.data = 1

	def position( this, x = 0, y = 0, z = 0 ) :
		this.x = x
		this.y = y
		this.z = z

	def size( this, width = 2, height = 2, depth = 2 ) :
		this.width = width
		this.height = height
		this.depth = depth

	def material( this, material = DIRT, data = 1 ) :
		this.material = material
		this.data = data

	def draw( this ) :
		for x in range( this.x, ( this.x + this.width ) ):
			for z in range( this.z, ( this.z + this.depth ) ):
				for y in range( this.y, ( this.y + this.height ) ):
					world.setBlock( x, y, z, this.material, this.data )

	def clear( this ) :
		m = this.material
		this.material = AIR
		this.draw()
		this.material = m