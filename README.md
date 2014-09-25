# Kids Hack Day Minecraft API

## Overview

This API will be used for Kids Hack Day Game Development Program. You can read
more about the program at our [Process Wiki](http://kidshackday.github.io/wiki/#!programs/game-development.md).

It should provide an abstraction layer to render mini-games inside Minecraft
(either Pi Edition or Bukkit with Raspberry Juice plugin).

## Components

The Kids Hack Day Minecraft Library is made of small components to help handling
the world blocks, rules and game mechanics.

### Minecraft Pi Python API

We include the official Python API in our Library.

### Drawing

To build 3D shapes on Minecraft world we can use one of the three basic shapes
available: Box, Line and Sphere. It also contain a module with some examples on
how to make buildings with code.

### Events

Raspberry Juice Plugin for Bukkit has so far only one event: Swords right click.
We plan to extend it to all game events but for instance we have only this method
that returns if the event occured on a specific coordinate of the world or a
block type.

### Game

In order to provide a initial structure to develop the games, we built some
objects to extend and override the needed methods. This give enough freedom to
choose which code structure and paradigms we want to use: Procedural, Object
Oriented, Event oriented, etc.

## Roadmap

- Physics
- Hardware communication
- GPIO
- QuirkBot

## Library structure

- Draw
	- Box
	- Sphere
	- Line
	- Building
		- house
- Interaction
	- swordRightClick
- Game mechanics
	- Simple Game (OO)
