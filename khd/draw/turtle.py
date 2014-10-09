from khd.config import *
from khd.draw.box import *
from math import *

class Turtle() :
	material = DIRT
	box = Box()
	path = []

	speeds = [ Vec3( 0, 0, 1 ), Vec3( 1, 0, 0 ), Vec3( 0, 0, -1 ), Vec3( -1, 0, 0 ) ]
	# Index on speeds
	direction = 0
	# Initial speed
	speed = speeds[ direction ]

	def position( self, x = 0, y = 0, z = 0 ) :
		self.box.x = int( x )
		self.box.y = int( y )
		self.box.z = int( z )
		self.updatePath()

	def updatePath( self ) :
		self.path.append( Vec3( self.box.x, self.box.y, self.box.z ) )

	def material( self, material = DIRT ) :
		self.material = material

	def draw( self ) :
		self.updatePath()
		self.box.draw()

	def forward( self ) :
		self.box.x = self.box.x + self.speed.x
		self.box.z = self.box.z + self.speed.z
		self.draw()

	def back( self ) :
		self.box.x = self.box.x - self.speed.x
		self.box.z = self.box.z - self.speed.z
		self.draw()

	def up( self ) :
		self.box.y = self.box.y + 1
		self.draw()

	def down( self ) :
		self.box.y = self.box.y - 1
		self.draw()

	def turnLeft( self ) :
		self.direction = int( abs( fmod( self.direction + 1, len( self.speeds ) ) ) )
		self.speed = self.speeds[ self.direction ]
	
	def turnRight( self ) :
		self.direction = int( abs( fmod( self.direction - 1, len( self.speeds ) ) ) )
		self.speed = self.speeds[ self.direction ]


	def clear( self ) :
		oldBox = self.box
		self.box.material = AIR
		for i in self.path :
			self.box.position( i.x, i.y, i.z )
			self.box.draw()
		self.box = oldBox
		self.path = []