# Kids Hack Day Minecraft API

## Overview

This API will be used for Kids Hack Day Game Development Program. You can read
more about the program at our [Process Wiki](http://kidshackday.github.io/wiki/#!programs/game-development.md).

It should provide an abstraction layer to render mini-games inside Minecraft 
(either Pi Edition or Bukkit with Raspberry Juice plugin).

## Basic structure

We should provide a very simple structure for kids start developing straight 
away without need any programming classes before. After this moment they can
dig into the libraries to customize their games and then learn basic structures
of programming.

### Ideas for structures

### Runtime

	class Pong( Game ) :
		def setup( self ) :
			print 'run once'
		def loop( self ) :
			print 'run at a frame rate'
 
	class Game() :
		def __init__( self ) :
			self.setup()
			while True :
				self.loop()

### Procedural

	block = create_block( x, y, z, width, height, depth, material )
	def event( b ) :
		do_something( b )
	add_event( block, event )

### Listeners
	
	def listener( context ) :
		context.doSomething()
	block.addListener( listener )

### Attachments

	block = Block()
	block.add( physics.gravity )
	block.add( eventListener )
	block.setMaterial( DIAMOND_BLOCK )
	block.position( x, y, z )
	block.size( width, height, depth )
	block.draw()

## Libraries to build

- Drawing
	- Box
	- Sphere
	- Line
	- Plane
	- House
	- Terrain
	- Clear
- Interaction
	- onHit
	- onAction (right click)
	- onApproach
	- onDestroy
	- onCreate
	- onMove
	- onChange
- Game mechanics
	- Score
	- Life
	- XP
	- Controls
	- Start/Reset/Game Over
	- Players list ("Player playing")

## Libraries planned to be built

- Physics
- Hardware communication
- GPIO
- QuirkBot







