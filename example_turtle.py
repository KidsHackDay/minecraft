from khd.minecraft import *
from time import *

me = getMyPosition()
t = Turtle()
t.position( me.x, me.y, me.z + 1 )
t.draw()

for i in range( 0, 10 ) :
	t.forward()
	sleep( 1 )
	t.forward()
	sleep( 1 )
	t.turnLeft()
	t.forward()
	sleep( 1 )
	t.forward()
	sleep( 1 )
	t.turnLeft()
	t.forward()
	sleep( 1 )
	t.forward()
	sleep( 1 )
	t.up()
	sleep( 1 )

sleep( 10 )
t.clear()