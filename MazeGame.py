#Student Name: Abaseen Ahmadzai
#Student Num: 101228053


import pygame

#function to load the image 
def display():
	#loads image from COMMAND LINE
	img = pygame.image.load("a10img.PNG")

	#gets the images dimensions
	(wid, hgt) = img.get_size()

	#creates a window using said dimensions
	window = pygame.display.set_mode((wid, hgt))

	#images gets blit and shown on the screen
	new = window.blit(img,(0,0))

	pygame.display.update()

	#pygame.time.delay(10000)

display()

#list that contains all the areas in the house
names =["Main Walkway", "Driveway", "Front Yard", "Main Hallway", "Garage", "Bathroom 1", 
	"Kitchen", "Hallway 2", "Living Room", "Basement", "Storage Room", "Upstairs", "Bedroom 1",
	"Bathroom 2", "Bedroom 2", "Office", "Bedroom 3", "Pool", "Dog House", "Fence"]
	

#list that contains all the descriptions of each area of the house
descriptions = ["Basically an entrance pathway to the house. Flowers and other plants appear on the sides here for a nice 'view'", "This is where we park our cars. A nightmare in the winter when trying to clean up all that snow!", "This is where our family likes to just relax and enjoy the outside. Can't ever really get used to the smell of freshly cut grass!", "This is the first hallway in the house since it leads to the entrance. In this house, this is where people put their shoes as to not get the whole house dirty!", "The garage is where all our tools and garbage is kept before garbage day. We also park our cars here in the winter too!", "This is one of the 2 bathrooms in the house right beside the entrance. I personally will never use this bathroom because I know how many kids use it and don't clean up.", "The kitchen is where all the magic happens aka the cooking. Probably the largest area in the house.", "This '2nd' hallway comes after the first one and is a common area for people to stand and talk. This part of the house has a nice view of the outdoors as the door is right there!", "The living room is where really all the entertainment is including the TV. We also eat dinner in the living room and honestly it's the most comfortable place in the house.", "The basement is the one part under the entire house. It's pretty scary at night or just in the dark. Somehow I always manage to think soemthing is chasing me as I sprint up the stairs after I turn the lights off.", "The storage room is where we keep all our canned food and stuff. Kind of serves as a pantry but also where the washer and dryer is.", "Upstairs is the 3rd level of the house which can also serve as the 3rd hallway in the house. From here we have access to many rooms and this is where a lot of the familuy pictures are too, on the walls.", "This is my parents bedroom, which is connected to a bathroom. It's the largest room upstairs and also has some very cozy carpets.", "The 2nd bathroom in the house and the largest. I use this bathroom as it is much cleaner!", "This is my bedroom, I have posters of NBA players and other things too. My computer is here as well as a lot of manga like 'Blue Lock' you should check it out!", "The office is a sacred space for my father, it's where he gets most of his work done. I use it sometimes since it is very quiet and easy to focus in there.", "The final bedroom is for my younger siblings and it contains a bunkbed and lots of toys. I used to sleep in there when my siblings would get scared just to comfort them.", "The Pool is the first thing you see when you go into the backyard, I love it! Putting in all the chlorine is always a hassle though. The Pool is pretty big and was bought off Kijiji, don't remember for how much.", "I don't own a dog, but if I did, this is probably where they'd live. Actually no that'd be cruel but I would name the dog spike and the dog house would be very comfy and cozy for him.", "Ah, the fence, oh how many balls have been lost because the neighbor didn't throw them back. This fence sperates us with the neighbors and always needs to be repainted!"]

#adjacency list showing what room you can go to from whatever room
graph = [[1,2,3],[0,4],[0],[0,4,5,7],[1,3],[3],[7,11],
		[3,6,8,17],[7,9],[8,10],[9],[6,12,14,15,16],[11,13],
		[12],[11,15],[11,14],[11],[7,18,19],[17],[17]]

#multi-dimesnional list corresponding with the list above to see what direction is which way from each area
directions = [["west", "east", "north"], ["east", "north"], ["west"], ["south","west", "east", "north"],["south", "east"], ["west"], ["west", "east"], ["south", "east", "west", "north"], ["east", "west"], ["east", "south"], ["north"], ["west", "north", "east", "south-east", "south"], ["south", "east"], ["west"], ["west", "south"], ["north-west", "north"], ["north"],["south", "east", "north"], ["west"], ["south"]]

#Function for the actual game 	
def game(names, descriptions, graph, directions, curr_location):
	#list that appends items when 'taken'
	items = [] #assume infinite supply of the 3 items :)
	while True:

		print()
		print("You are currently in ", curr_location, ".", sep = '')
		print("------------------")
		
		indx_location = names.index(curr_location)
		print(descriptions[indx_location])
		
		print()
		
		exits = []
		print("From this location, you could go to any of the following:")
		count = 0 #used for the direction list
		
		print()
		
		#checks to see if element is in the index location and then goes through a counter controlled loop to display each exit
		for each in (graph[indx_location]):
			print("\t", names[each], "(",directions[indx_location][count],")")
			exits.append(names[each])
			count+=1
		print()
		
		#user input on what they want to do
		choice = input("What would you like to do?\n1)Type the room name you'd like to go to\n2)Type 'help' for an explanation\n3)Type 'inventory' to open your inventory and see what you got!\n4)Type 'quit' to quit the game\n")
		
		#'special' words like quit or inventory are mentioned here as to not be in the same category as the ones that display the exits
		if not (choice in exits):
			if(choice=="quit"):
				break
			elif(choice=="inventory"):
				print()
				print("Here are your items thus far!", items)
			elif(choice== "help"):
				print()
				print("So this is a text based adventure that you can explore. There are roughly 20 areas you can navigate through and you do this by typing where you want to go with the option displayed on where to go, type and use the map as a guide. There are 3 items to collect, have fun!")
			else:
				print()
				print("This place either isn't an exit or doesn't exist, try again.") #if whatever you typed isn't a special word or a place, or it is a place but not a place you can get to
		
		#These branches are for picking up items 'take', if you type anything else other than the keyword 'take' (case sensitive) then you don't pick up the item
		elif(choice == "Basement"):
			curr_location = choice
			print()
			take = input("Woah! Look, you aquired some old socks, nice! Type 'take' to get the socks! or something else to not... ")
			if(take=="take"):
				items.append("Old Socks")
			else:
				print()
				print("Oh well, leave those on the floor then")
		elif(choice=="Dog House"):
			print()
			curr_location = choice
			take = input("Wowwwww! Spike's bone! Better not let him see you with it! Type 'take' to pick it up, or something else to not... ")
			if(take=="take"):
				items.append("Spike's bone")
			else:
				print()
				print("Oh well, leave it on the ground then!")
		elif(choice=="Kitchen"):
			print()
			curr_location = choice
			take = input("Someone's hungry! Type 'take' to pick up the apple, or something else to not ")
			if(take=="take"):
				items.append("apple")
			else:
				print("Let the apple rot then I guess :I")

		else:
			curr_location = choice
		print()



print()

#UI
print("Welcome to the ultimate, most best-est RPG minus the game and role-playing of course. We hope you enjoy this awesome text based adventure game, pretty self explanatory if you need help type 'help' at any point and the instructions will guide you!")

#curr_location = "Main Walkway" > BLACK STAR ON MAP IS WHERE PLAYER IS 
game(names, descriptions, graph, directions, "Main Walkway")

#ITEMS ARE: APPLE, OLD SOCKS, BONE



