from khd.config import *
from khd.draw.box import *

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