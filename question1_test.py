print("Question 1")

#This function - is the fail function which will be trigger when a user gets an answer wrong
def fail():
  print("You have failed")

#This is the first question of the quiz - Focused around how cool Mr Earl is
def question1():
  print("Is Mr Earl Cool? ")
  ans1 = input()
  ans1 = ans1.lower()
  if ans1 == "yes":
    print("Correct")
    question2()
  elif ans1 == "no":
    print("Rude")
    fail()
  else:
    print("How are you not sure?")
    question1()

def question2():
  print("Is Jacob Cool? ")
  ans2 = input()
  if ans2 == "no":
    print("rude")
  elif ans2 == "yes":
    print("Correct")
  else:
    print("How are you not sure?")
    question1()
  
question1()