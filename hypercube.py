from sys import exit 
from math import log10, floor
import time
import webbrowser
import portalactions


class Scene(object):

	def enter(self):
		print "Start."
		exit(1)

		
class Engine(object):
		
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()


starttime = time.clock() 

doors = {'behind': 'Blue', 'left': 'Yellow', 'ahead': 'Red', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}

whitecount = 0
redcount = 0
blackcount = 0
bluecount = 0
yellowcount = 0
greencount = 0
orangecount = 0
purplecount = 0


class Chrome(Scene):

	def enter(self):
		print "Both of your arms ache as two burly security officers yank and " 
		print "haul you into a gleaming chrome room, completely sterile and " 
		print "spotless, silent but for the stomp of the officers' boots. As " 
		print "they drag you through the room and up the far ramp towards the "
		print "large white door, the weasly little man introduced to you as "
		print "Sinclair calls from behind in a nasally tone, \"Not to worry. You'll "
		print "either pass this test and be rewarded, or you'll fail and die! But "
		print "if you follow the clues and make a map you should be able to escape "
		print "this little test.\" \n"
		print "One of the officers taps a touchpad to the right of the white door, "
		print "the door slides suddenly open into the wall and you are pushed "
		print "forcefully through the opening into a white room. Spinning back "
		print "around you see the door suddenly and swiftly slide shut again; this "
		print "side of the door is blue. You spin back around and examine the room . . ."
		print "\n"
		return 'white'
	
		
class White(Scene):

	def enter(self):
		global doors
		print "You are in a completely white, cube-shaped room. The whiteness "
		print "gleams from every spotless surface and you cast no shadow. The "
		print doors['behind'],"door is behind you; on the left wall is a",doors['left'], "door, the wall "
		print "ahead has a",doors['ahead'], "door, on the right wall is a",doors['right'], "door. The ceiling "
		print "has a",doors['ceiling'], "door, and the floor has a",doors['floor'], "door. To the side of the "
		print "Blue door is a small terminal with a screen and keyboard. Choose a "
		print "door or examine the terminal?"
		
		global whitecount
		whitecount += 1
	
		action = raw_input("> ")
		
		if "red" in action or "Red" in action:
			doors = {'behind': 'White', 'left': 'Yellow', 'ahead': 'Black', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'White', 'left': 'Green', 'ahead': 'Black', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'blue'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'White', 'left': 'Red', 'ahead': 'Black', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'green'
		elif "yellow" in action or "Yellow" in action:
			doors = {'behind': 'White', 'left': 'Blue', 'ahead': 'Black', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'yellow'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Blue', 'left': 'Green', 'ahead': 'Red', 'right': 'Yellow', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorfloor()
			return 'purple'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingceiling()
			return 'orange'
		elif "terminal" in action or "Terminal" in action:
			return 'terminal'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			whitecount -= 1
			return 'white' 
		

class Red(Scene):

	def enter(self):
		global doors 
		print "You enter a red room; every surface is a bright intense red that "
		print "suddenly fades slightly before returning to its original hue, "
		print "cycling, pulsing . . . beating . . . in time to your heart. Behind "
		print "you is a",doors['behind'], "door, to the left is a",doors['left'], "door, straight "
		print "ahead is a",doors['ahead'], "door, to the right is a",doors['right'], "door, in the "
		print "middle of the ceiling is a",doors['ceiling'], "door, and in the middle of the "
		print "floor is a",doors['floor'], "door. Your attention is captured by the dead "
		print "body the corner. What will you do? Open a door or examine the body?"
		
		global redcount 
		redcount += 1
		
		action = raw_input("> ")
		
		if "white" in action or "White" in action:
			doors = {'behind': 'Red', 'left': 'Green', 'ahead': 'Blue', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'white'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'black'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'Red', 'left': 'Black', 'ahead': 'Blue', 'right': 'White', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'green'
		elif "yellow" in action or "Yellow" in action:
			doors = {'behind': 'Red', 'left': 'White', 'ahead': 'Blue', 'right': 'Black', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'yellow'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorwall()
			return 'purple'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingwall()
			return 'orange'
		elif "corpse" in action or "Corpse" in action or "body" in action or "Body" in action:
			portalactions.corpse()
			redcount -= 1
			raw_input("Back to room?" )
			return 'red'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			redcount -= 1
			return 'red'
	

class Black(Scene):
	
	def enter(self):
		global doors
		print "You enter a black room; every surface, walls, ceiling, floor, seems "
		print "to glisten wetly like thick black oil and the illumination is dim. "
		print "Despite feeling slippery to walk on, no stain marks your shoes. Behind "
		print "you is a",doors['behind'], "door, to the left is a",doors['left'], "door, straight ahead "
		print "is a",doors['ahead'], "door, to the right is a",doors['right'], "door, in the middle of "
		print "the ceiling is a",doors['ceiling'], "door, and in the middle of the floor is a "
		print doors['floor'],"door. In one corner there is an inky black sculpture. What "
		print "will you do? Open a door or examine the sculpture?"
		
		global blackcount
		blackcount += 1
		
		action = raw_input("> ")
		
		if "red" in action or "Red" in action:
			doors = {'behind': 'Black', 'left': 'Green', 'ahead': 'White', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'Black', 'left': 'Yellow', 'ahead': 'White', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'blue'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'Black', 'left': 'Blue', 'ahead': 'White', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'green'
		elif "yellow" in action or "Yellow" in action:
			doors = {'behind': 'Black', 'left': 'Red', 'ahead': 'White', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'yellow'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorceiling()
			return 'purple'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingfloor()
			return 'orange'
		elif "sculpture" in action or "Sculpture" in action:
			portalactions.sculpture()
			blackcount -= 1
			raw_input("Back to room?" )
			return 'black'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			blackcount -= 1
			return 'black'
		
	
class Orange(Scene):

	def enter(self):
		global doors
		print "You enter a bright and flickering orange room with every surface "
		print "flickering with multi varied shades of orange flame; it feels warm "
		print "in here, a little uncomfortable, but the flames are surface visuals "
		print "only - they do not burn. Behind you is a",doors['behind'], "door, to the left "
		print "is a",doors['left'], "door, straight ahead is a",doors['ahead'], "door, to the right is "
		print "a",doors['right'], "door, in the middle of the ceiling is a",doors['ceiling'], "door, and "
		print "in the middle of the floor is a",doors['floor'], "door. You notice one area of "
		print "the flames doesn't flicker randomly but rather seems regular. What "
		print "will you do? Open a door or examine the pattern?"
		
		global orangecount
		orangecount += 1
		
		action = raw_input("> ")
		
		if "red" in action or "Red" in action:
			doors = {'behind': 'Black', 'left': 'Green', 'ahead': 'White', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallceiling()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'Black', 'left': 'Yellow', 'ahead': 'White', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallceiling()
			return 'blue'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'Black', 'left': 'Blue', 'ahead': 'White', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallceiling()
			return 'green'
		elif "yellow" in action or "Yellow" in action:
			doors = {'behind': 'Black', 'left': 'Red', 'ahead': 'White', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallceiling()
			return 'yellow'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.floorceiling()
			return 'black'
		elif "white" in action or "White" in action:
			doors = {'behind': 'Red', 'left': 'Green', 'ahead': 'Blue', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.ceilingceiling()
			return 'white'
		elif "pattern" in action or "Pattern" in action:
			portalactions.pattern()
			orangecount -= 1
			raw_input("Back to room?" )
			return 'orange'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			orangecount -= 1
			return 'orange'
		
	
class Yellow(Scene):

	def enter(self):
		global doors
		print "You enter an intense yellow room, the walls, ceiling, and floor of "
		print "which appear to have a dimpled waxy texture that would be smooth to "
		print "the touch. Behind you is a",doors['behind'], "door, to the left is a",doors['left'] 
		print "door, straight ahead is a",doors['ahead'], "door, to the right is a",doors['right'] 
		print "door, in the middle of the ceiling is a",doors['ceiling'], "door, and in the "
		print "middle of the floor is a",doors['floor'], "door. You notice a blood-smeared "
		print "stain on one wall. What will you do? Open a door or examine the blood "
		print "stain?"
		
		global yellowcount
		yellowcount += 1
		
		action = raw_input("> ")
		
		if "red" in action or "Red" in action:
			doors = {'behind': 'Yellow', 'left': 'Black', 'ahead': 'Green', 'right': 'White', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'Yellow', 'left': 'White', 'ahead': 'Green', 'right': 'Black', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'blue'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Yellow', 'left': 'Blue', 'ahead': 'Green', 'right': 'Red', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingwall()
			return 'orange'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Yellow', 'left': 'Blue', 'ahead': 'Green', 'right': 'Red', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorwall()
			return 'purple'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Yellow', 'left': 'Blue', 'ahead': 'Green', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'black'
		elif "white" in action or "White" in action:
			doors = {'behind': 'Yellow', 'left': 'Red', 'ahead': 'Green', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'white'
		elif "stain" in action or "Stain" in action or "blood" in action or "Blood" in action:
			portalactions.stain()
			yellowcount -= 1
			raw_input("Back to room?" )
			return 'yellow'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			yellowcount -= 1
			return 'yellow'
		
		
class Green(Scene):

	def enter(self):
		global doors
		print "You enter a green room; every surface is criss-crossed by a "
		print "complex pattern of grooves and cuts that reflect the light at "
		print "different angles, and like the inside of a giant multi-faceted "
		print "emerald gem the green hue changes as you look and when you move. "
		print "Behind you is a",doors['behind'], "door, to the left is a",doors['left'], "door, "
		print "straight ahead is a",doors['ahead'], "door, to the right is a",doors['right'], "door, "
		print "in the middle of the ceiling is a",doors['ceiling'], "door, and in the middle of "
		print "the floor is a",doors['floor'], "door. There seem to be runes chiselled in one "
		print "small section of wall. What will you do? Open a door or examine the "
		print "runes?"
		
		global greencount
		greencount += 1
		
		action = raw_input("> ")
		
		if "red" in action or "Red" in action:
			doors = {'behind': 'Green', 'left': 'White', 'ahead': 'Yellow', 'right': 'Black', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'Green', 'left': 'Black', 'ahead': 'Yellow', 'right': 'White', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'blue'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Green', 'left': 'Red', 'ahead': 'Yellow', 'right': 'Blue', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingwall()
			return 'orange'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Green', 'left': 'Red', 'ahead': 'Yellow', 'right': 'Blue', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorwall()
			return 'purple'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Green', 'left': 'Red', 'ahead': 'Yellow', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'black'
		elif "white" in action or "White" in action:
			doors = {'behind': 'Green', 'left': 'Blue', 'ahead': 'Yellow', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'white'
		elif "runes" in action or "Runes" in action:
			portalactions.runes()
			greencount -= 1
			raw_input("Back to room?" )
			return 'green'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			greencount -= 1
			return 'green'
		
		
class Blue(Scene):

	def enter(self):
		global doors
		print "You enter a blue room; blue like a bright cloudless sky, vibrant and "
		print "inviting, and with each surface seeming to possess the same airy "
		print "impermanence. Behind you is a",doors['behind'], "door, to the left is a",doors['left'] 
		print "door, straight ahead is a",doors['ahead'], "door, to the right is a",doors['right'] 
		print "door, in the middle of the ceiling is a",doors['ceiling'], "door, and in the "
		print "middle of the floor is a",doors['floor'], "door. There seems to be a tiny Sun "
		print "or independent light source of sorts  near one edge. What will you do? "
		print "Open a door or examine the little light source?"
		
		global bluecount
		bluecount += 1
		
		action = raw_input("> ")
		
		if "yellow" in action or "Yellow" in action:
			doors = {'behind': 'Blue', 'left': 'Black', 'ahead': 'Red', 'right': 'White', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'yellow'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'Blue', 'left': 'White', 'ahead': 'Red', 'right': 'Black', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'green'
		elif "orange" in action or "Orange" in action:
			doors = {'behind': 'Blue', 'left': 'Green', 'ahead': 'Red', 'right': 'Yellow', 'ceiling': 'White', 'floor': 'Black'}
			portalactions.ceilingwall()
			return 'orange'
		elif "purple" in action or "Purple" in action:
			doors = {'behind': 'Blue', 'left': 'Green', 'ahead': 'Red', 'right': 'Yellow', 'ceiling': 'Black', 'floor': 'White'}
			portalactions.floorwall()
			return 'purple'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Blue', 'left': 'Green', 'ahead': 'Red', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'black'
		elif "white" in action or "White" in action:
			doors = {'behind': 'Blue', 'left': 'Yellow', 'ahead': 'Red', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.door()
			return 'white'
		elif "sun" in action or "Sun" in action or "light" in action or "Light" in action:
			portalactions.sun()
			bluecount -= 1
			raw_input("Back to room?" )
			return 'blue'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			bluecount -= 1
			return 'blue'
		
		
class Purple(Scene):

	def enter(self):
		global doors
		print "You enter a purple room; the floor and the ceiling and every wall is "
		print "covered in plush and padded velvet that is a bright purple colour; a "
		print "hexagonal array of purple studs covers every surface, accentuating the "
		print "red velvety cushioning. Behind you is a",doors['behind'], "door, to the left is a "
		print doors['left'],"door, straight ahead is a",doors['ahead'], "door, to the right is a",doors['right'] 
		print "door, in the middle of the ceiling is a",doors['ceiling'], "door, and in the middle of "
		print "the floor is a",doors['floor'], "door. There doesn't seem to be anything else in "
		print "this room. What door do you choose?" #can add another object clue 
		
		global purplecount
		purplecount += 1
		
		action = raw_input("> ")
		
		if "yellow" in action or "Yellow" in action:
			doors = {'behind': 'Black', 'left': 'Red', 'ahead': 'White', 'right': 'Blue', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallfloor()
			return 'yellow'
		elif "green" in action or "Green" in action:
			doors = {'behind': 'Black', 'left': 'Blue', 'ahead': 'White', 'right': 'Red', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallfloor()
			return 'green'
		elif "red" in action or "Red" in action:
			doors = {'behind': 'Black', 'left': 'Green', 'ahead': 'White', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallfloor()
			return 'red'
		elif "blue" in action or "Blue" in action:
			doors = {'behind': 'Black', 'left': 'Yellow', 'ahead': 'White', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.wallfloor()
			return 'blue'
		elif "black" in action or "Black" in action:
			doors = {'behind': 'Red', 'left': 'Yellow', 'ahead': 'Blue', 'right': 'Green', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.ceilingfloor()
			return 'black'
		elif "white" in action or "White" in action:
			doors = {'behind': 'Red', 'left': 'Green', 'ahead': 'Blue', 'right': 'Yellow', 'ceiling': 'Orange', 'floor': 'Purple'}
			portalactions.floorfloor()
			return 'white'
		#elif "object" in action or "Object" in action:
			#object()
			#raw_input("Back to room?" )
			#return 'purple'
		else:
			print "\n"
			print "Aaaaaaand you still have a choice to make."
			print "\n"
			purplecount -= 1
			return 'purple'
		
		
class Terminal(Scene):
	
	def enter(self):
		
		global whitecount
		global redcount
		global blackcount
		global bluecount
		global yellowcount
		global greencount
		global orangecount
		global purplecount 
		
		if whitecount >= 1 and redcount >= 1 and blackcount >= 1 and bluecount >= 1 and yellowcount >= 1 and greencount >= 1 and orangecount >= 1 and purplecount >= 1:
			print "\n"
			print "The terminal loads the following text:"
			print "Correctly answer four questions to get back to the Chrome room."
			print "\n"
	
			print "Question #1: How many rooms are there?"
			roomnumber = raw_input("> ")
			if "8" in roomnumber or "eight" in roomnumber or "Eight" in roomnumber:
				print "\n"
				print "Correct. There are eight rooms."
				print "\n"
				
				print "Question #2: What is the shape of this building?"
				buildingshape = raw_input("> ")
				if "hypercube" in buildingshape or "Hypercube" in buildingshape or "tesseract" in buildingshape or "Tesseract" in buildingshape:
					print "\n"
					print "Correct. The three dimensional space you are familiar with "
					print "has been folded into four dimensions."
					print "\n"
					
					print "Question #3: What is outside the building?"
					outside = raw_input("> ")
					if "nothing" in outside or "Nothing" in outside or "empty" in outside or "Empty" in outside or "meaningless" in outside or "Meaningless" in outside:
						print "\n"
						print "Correct. In a manner of speaking."
						print "\n"
						
						print "Question #4: How far away is the chrome room?"
						distance = raw_input("> ")						
						if "zero" in distance or "Zero" in distance or "infinit" in distance or "Infinit" in distance or "meaningless" in distance or "Meaningless" in distance or "0" in distance:
							print "\n"
							print "Correct. Distance doesn't really mean anything in "
							print "this context, in which the space you are in has been "
							print "pinched off from all other accessible spaces."
							print "\n"
							print "You step back from terminal, the air shimmers for a "
							print "second, and the blue door turns chrome. Enter chrome door? Y/N?"
							escape = raw_input("> ")
							if "yes" in escape or "Yes" in escape or "y" in escape or "Y" in escape:
								return 'finished'
							else:
								print "\n"
								print "You step back from the terminal, the air shimmers again, and "
								print "the chrome door turns blue."
								print "\n"
								whitecount -= 1
								return 'white'
							
						else:
							print "\n"
							print "Wrong"
							print "\n"
							print "You take a step back to explore and think some more when you "
							print "hear a sudden whooshing noise and thuds as every door in the "
							print "room slides open at once. Startled you walk and look around a "
							print "little and stare in wonderment through each of the doors and "
							print "into the rooms beyond, which also have open doors. The coloured "
							print "rooms appear to extend forever, doorways getting smaller and "
							print "disappearing to faint dots, rooms repeated in sequences with "
							print "the white room you're in visible every four rooms. Looking through "
							print "the green door into the green room you see through to the black "
							print "room and on into the yellow room beyond before seeing into the "
							print "white room again; and there you are, facing away from you, looking "
							print "beyond into another sequence of the same rooms and so on. Feeling "
							print "your own eyes on the back of your head you snap your head back to "
							print "look through the opposite yellow door to try to catch a glimpse of "
							print "yourself, and instead, of course, see yourself again looking away "
							print "in the opposite direction. Leaning over and looking through the door "
							print "in the floor, down through the purple room, and further into the "
							print "black room and the orange room beyond that you see the white room "
							print "and the back of your own head leaning over the door frame looking "
							print "down, down, down."
							print "\n" 
							print "The doors suddenly snap shut and you jump back startled."
							print "\n"
							whitecount -= 1
							return 'white'
					
					else:
						print "\n"
						print "Wrong"
						print "\n"
						print "You take a step back to explore and think some more when you "
						print "hear a sudden whooshing noise and thuds as every door in the "
						print "room slides open at once. Startled you walk and look around a "
						print "little and stare in wonderment through each of the doors and "
						print "into the rooms beyond, which also have open doors. The coloured "
						print "rooms appear to extend forever, doorways getting smaller and "
						print "disappearing to faint dots, rooms repeated in sequences with "
						print "the white room you're in visible every four rooms. Looking through "
						print "the green door into the green room you see through to the black "
						print "room and on into the yellow room beyond before seeing into the "
						print "white room again; and there you are, facing away from you, looking "
						print "beyond into another sequence of the same rooms and so on. Feeling "
						print "your own eyes on the back of your head you snap your head back to "
						print "look through the opposite yellow door to try to catch a glimpse of "
						print "yourself, and instead, of course, see yourself again looking away "
						print "in the opposite direction. Leaning over and looking through the door "
						print "in the floor, down through the purple room, and further into the "
						print "black room and the orange room beyond that you see the white room "
						print "and the back of your own head leaning over the door frame looking "
						print "down, down, down."
						print "\n" 
						print "The doors suddenly snap shut and you jump back startled."
						print "\n"
						whitecount -= 1
						return 'white'
					
				else:
					print "\n"
					print "Wrong"
					print "\n"
					print "You take a step back to explore and think some more when you "
					print "hear a sudden whooshing noise and thuds as every door in the "
					print "room slides open at once. Startled you walk and look around a "
					print "little and stare in wonderment through each of the doors and "
					print "into the rooms beyond, which also have open doors. The coloured "
					print "rooms appear to extend forever, doorways getting smaller and "
					print "disappearing to faint dots, rooms repeated in sequences with "
					print "the white room you're in visible every four rooms. Looking through "
					print "the green door into the green room you see through to the black "
					print "room and on into the yellow room beyond before seeing into the "
					print "white room again; and there you are, facing away from you, looking "
					print "beyond into another sequence of the same rooms and so on. Feeling "
					print "your own eyes on the back of your head you snap your head back to "
					print "look through the opposite yellow door to try to catch a glimpse of "
					print "yourself, and instead, of course, see yourself again looking away "
					print "in the opposite direction. Leaning over and looking through the door "
					print "in the floor, down through the purple room, and further into the "
					print "black room and the orange room beyond that you see the white room "
					print "and the back of your own head leaning over the door frame looking "
					print "down, down, down."
					print "\n" 
					print "The doors suddenly snap shut and you jump back startled."
					print "\n"
					whitecount -= 1
					return 'white'
				
			else:
				print "\n"
				print "Wrong"
				print "\n"
				print "You take a step back to explore and think some more when you "
				print "hear a sudden whooshing noise and thuds as every door in the "
				print "room slides open at once. Startled you walk and look around a "
				print "little and stare in wonderment through each of the doors and "
				print "into the rooms beyond, which also have open doors. The coloured "
				print "rooms appear to extend forever, doorways getting smaller and "
				print "disappearing to faint dots, rooms repeated in sequences with "
				print "the white room you're in visible every four rooms. Looking through "
				print "the green door into the green room you see through to the black "
				print "room and on into the yellow room beyond before seeing into the "
				print "white room again; and there you are, facing away from you, looking "
				print "beyond into another sequence of the same rooms and so on. Feeling "
				print "your own eyes on the back of your head you snap your head back to "
				print "look through the opposite yellow door to try to catch a glimpse of "
				print "yourself, and instead, of course, see yourself again looking away "
				print "in the opposite direction. Leaning over and looking through the door "
				print "in the floor, down through the purple room, and further into the "
				print "black room and the orange room beyond that you see the white room "
				print "and the back of your own head leaning over the door frame looking "
				print "down, down, down."
				print "\n" 
				print "The doors suddenly snap shut and you jump back startled."
				print "\n"
				whitecount -= 1
				return 'white'
	
		else:
			print "\n"
			print "Terminal shows the following text: 'Not yet open for input.'"
			print "\n"
			whitecount -= 1
			return 'white'

		
class Finished(Scene):
	
	def enter(self):
		print "You step through the door into the chrome room, walking down "
		print "the ramp towards Sinclair, standing there with a smirk on his face, "
		print "'Well done,' he says in that nasally voice, 'Time for the next test. "
		print "But before we do, what reward would you like? Pleasure, Knowledge, "
		print "Power, or Health?'"
		reward = raw_input("> ")
		if "pleasure" in reward or "Pleasure" in reward:
			print "\n"
			print "Good choice! Enjoy your reward!"
			print "\n"
			webbrowser.open_new_tab('http://only-hot-babes.tumblr.com/image/123457018320')
		elif "knowledge" in reward or "Knowledge" in reward:
			print "\n"
			print "Good choice! Enjoy your reward!"
			print "\n"
			webbrowser.open_new_tab('https://en.wikipedia.org/wiki/Epistemology')
		elif "health" in reward or "Health" in reward:
			print "\n"
			print "Good choice! Enjoy your reward!"
			print "\n"
			webbrowser.open_new_tab('https://www.fightaging.org/introduction/')
		elif "power" in reward or "Power" in reward:
			print "\n"
			print "Good choice! Enjoy your reward!"
			print "\n"
			webbrowser.open_new_tab('https://github.com/markthebruce/Manifold-Escape')
		else:
			print "\n"
			print "Okay, no reward it is!"
			print "\n"
		
		totalrooms = whitecount + redcount + blackcount + bluecount + yellowcount + greencount + orangecount + purplecount
		totalt = (time.clock() - starttime) / 60
		totaltime = round(totalt, -int(floor(log10(totalt))))
		
		print "Congratulations you have finished the game!"
		print "You entered rooms %s times during your visit!" % totalrooms
		print "Your visit lasted for %s minutes!" % totaltime
		print "\n"
		print "Would you like to share your experience with other players? Y/N?"
		share = raw_input("> ")
		if "y" in share or "Y" in share or "yes" in share or "Yes" in share:
			print "\n"
			print "Commenting available on the page that opens."
			print "Thank you for playing. Good bye."
			webbrowser.open_new_tab('https://plus.google.com/u/0/+MarkBruce/posts/X9u2q9GFuAW')
		else:
			print "\n"
			print "Thank you for playing. Good bye."
		
		exit(1)


class Map(object):

	scenes = {'chrome': Chrome(), 
		'white': White(), 
		'red': Red(), 
		'black': Black(),
		'blue': Blue(), 
		'yellow': Yellow(),
		'green': Green(), 
		'orange': Orange(), 
		'purple': Purple(), 
		'terminal': Terminal(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene) 
		

a_map = Map('chrome')
a_game = Engine(a_map)
a_game.play()
