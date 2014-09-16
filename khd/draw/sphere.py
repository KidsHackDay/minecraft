from khd.config import *
from khd.draw.box import *

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