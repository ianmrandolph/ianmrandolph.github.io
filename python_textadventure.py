import replit
state = "intro"

def intro():
  global state
  replit.clear()
  print("You are the protagonist of the story.")
  choice = input("Will you make choice A or B? type a for a and b for b: ")
  if choice == 'a':
    state = "a_path"
  elif choice == 'b':
    state = "b_path"

def a_path():
  global state
  print("Choice c or d? c for c and d for d: ")

def b_path():
  global state
  print("This is b state")

#State Machine
while(state != "end"):
  if state == "intro":
    intro()
  elif state == "a_path":
    a_path()
  elif state == "b_path":
    b_path()