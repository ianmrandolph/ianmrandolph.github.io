import replit
state = "intro"

def intro():
  global state
  replit.clear()
  print("You are LINK, the Hero of Time, on a quest to rescue\
  the Forest Medallion from the Lost Woods of Hyrule.")
  print(" ")
  print("You must traverse the winding Lost Woods to\
  reach the Temple.\
  A wrong turn will send you all the way back to the beginning!")
  print(" ")
  print("Stay safe out there!")
  print(" ")
  choice = input("Are you prepared to begin?\
  (Type y for Yes, n for No!) ")
  if choice == 'y':
    state = "entrance"
  elif choice == 'n':
    state = "go_anyway"

def go_anyway():
  global state
  replit.clear()
  print("I'm afraid you have no choice in the matter.\
  You must retreive the Medallion to save Hyrule!")
  print(" ")
  print("You pass through the dilapidated gates of the Lost Woods.\
  Down your path is a clearing in the thick brush around you.")
  print("To the left and right are paths cloaked in darkness.")
  print()
  choice = input("Will you go left or right?: ")
  if choice == "left":
    state = "skullkid"
  elif choice == "right":
    state = "room_1"

def entrance():
  global state
  replit.clear()
  print("You pass through the dilapidated gates of the Lost Woods.\
  Down your path is a clearing in the thick brush.")
  print(" ")
  print("To the left and right are paths cloaked in darkness.")
  choice = input("Will you go left or right?: ")
  if choice == "left":
    state = "skullkid"
  elif choice == "right":
    state = "room_1"

def skullkid():
  global state
  replit.clear()
  print("You take the dark path left.")
  print(" ")
  print("Sitting leisurely on a felled log is a boy of the forest,\
  the Skullkid.")
  print(" ")
  print("He greets you cheerfully: 'Hi! Welcome to the Lost\
  Woods! In order to reach the end, you should follow my advice.'")
  choice = input("Do you want to hear the SkullKid's advice? (y/n): ")
  if choice == "y":
    state = "skullkid_advice"
  elif choice == "n":
    state = "entrance"

def skullkid_advice():
  global state
  replit.clear()
  print("'This whole forest is one big maze.'")
  print(" ")
  print("'To reach the Forest Medallion, follow the clues\
  littered though each clearing in the brush.'")
  print(" ")
  print("'If you make a wrong turn, you'll end up right back\
  where you started!'")
  print(" ")
  print("'And that's all there is to it!")
  choice = input("Type 'thank you' to return to the entrance\
  and explore the Woods!: ")
  if choice == "thank you":
    state = "entrance"

def room_1():
  global state
  replit.clear()
  print("You take the path to the right, entering a clearing\
  with 3 paths, to the left, right, and dead ahead.")
  print(" ")
  print("In the center of clearing is a grand oak tree. Its roots\
  break the surface in the direction of the left path. The middle\
  path is blocked by wood planks, and the planks that once blocked\
  the rightward path are strewn about the forest floor.")

#State Machine
while(state != "end"):
  if state == "intro":
    intro()
  elif state == "entrance":
    entrance()
  elif state == "go_anyway":
    go_anyway()
  elif state == "skullkid":
    skullkid()
  elif state == "skullkid_advice":
    skullkid_advice()
