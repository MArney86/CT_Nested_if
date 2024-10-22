#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest": #changed from assignment operator to equal to operator
    action = input("climb a tree or cross a river? ")
    
    if action == "climb a tree": #changed from assignment operator to equal to operator
        print("You found a bird's nest!")
    
    elif action == "cross a river": #changed from assignment operator to equal to operator and changed to elif, else doesn't take conditional statements
        print("You found a boat!")

elif place == "cave": #changed from assignment operator to equal to operator
    print("You find a hidden treasure!")

#Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    
    if action == "climb a tree":
        print("You found a bird's nest!")
    
    elif action == "cross a river":
        print("You found a boat!")

elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    
    if action == "light a torch": #added secondary conditions for the cave environment
        print("You see a shiny spot in the cave and find a hidden treasure!") #if you light the torch you find a shiny treasure
    
    elif action == "proceed in the dark":
        print("You feel around blindly and find nothing in the cave") #if you go blind you're unable to find anything

#Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    
    if action == "climb a tree":
        print("You found a bird's nest!")
    
    elif action == "cross a river":
        print("You found a boat!")
    
    else:
        pass #added as placeholder for future development

elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    
    if action == "light a torch":
        print("You see a shiny spot in the cave and find a hidden treasure!")
    
    elif action == "proceed in the dark":
        print("You feel around blindly and find nothing in the cave")
    
    else:
        pass #added as placeholder for future development

else:
    pass #added as placeholder for future development