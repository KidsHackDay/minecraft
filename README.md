# Kids Hack Day Minecraft Library

## Overview

This library will be used for Kids Hack Day Game Development Program. You can read more about the program at our [Process Wiki](http://kidshackday.github.io/wiki/#!programs/game-development.md).

It should provide an abstraction layer to render mini-games inside Minecraft (either Pi Edition or Bukkit with Raspberry Juice plugin).

## Components

The Kids Hack Day Minecraft Library is made of small components to help handling the world blocks, rules and game mechanics.

### Minecraft Pi Python API

We include the official Python API in our Library.

### Drawing

To build 3D shapes on Minecraft world we can use one of the three basic shapes available: Box, Line and Sphere. It also contain a module with some examples on how to make buildings with code.

### Events

Raspberry Juice Plugin for Bukkit has so far only one event: Swords right click. We plan to extend it to all game events but for instance we have only this method that returns if the event occured on a specific coordinate of the world or a block type.

### Game

In order to provide a initial structure to develop the games, we built some objects to extend and override the needed methods. This give enough freedom to choose which code structure and paradigms we want to use: Procedural, Object Oriented, Event oriented, etc.

## How to run this code?

Independent of where are you running your code, you will need to download, extract and navigate to your extracted folder with your terminal.

1. You can download the [KHD Minecraft Library](https://github.com/KidsHackDay/minecraft/archive/master.zip) 

2. Unzip it wherever you want. We suggest you to unzip in your desktop folder in order to be easy to see. 

3. Navigate with the terminal to the folder you unziped. On Mac or Linux you can tipe `cd ~/Desktop/minecraft-master` and to confirm you are on the right folder, type `ls` and you should see a list of files ended with `.py`, this are our files. If you are on Windows, well, it's complicated... Check it out [here](http://www.computerhope.com/issues/ch000928.htm) where is your Desktop folder path and then navigate to there with your terminal (usually called prompt DOS or something).

### Raspberry Pi

If you are running Minecraft Pi Edition, you need only to start your game and run the code.

### MacOS or Linux

1. Most of this OS come already with python installed, if don't [install it](https://www.google.se/search?q=how+to+install+python&oq=how+to+install+python&aqs=chrome..69i57j0l3.3600j0j7&sourceid=chrome&es_sm=93&ie=UTF-8).

2. Connect to a Bukkit server with Raspberry Juice plugin (enter in touch if you want to connect on KHD server) or [setup your local server](http://wiki.bukkit.org/Setting_up_a_server).

3. Download Raspberry Juice Plugin and unzip the `.jar` file inside the `Plugin` folder of your Bukkit server installation.

4. Run or reset your Bukkit server.

5. Type `python example_happy_rainbow.py` in your terminal (which should be on our minecraft-master folder) and check in your world if a big colorfull rainbow appeared around your spawn area.

### Windows

Well again, it's complicated... You might need to [install Python first](https://www.google.se/search?q=how+to+install+python&oq=how+to+install+python&aqs=chrome..69i57j0l3.3600j0j7&sourceid=chrome&es_sm=93&ie=UTF-8), then add it to your system path and then follow the MacOS or Linux steps. 

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
