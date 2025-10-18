print("Fill in the blank lyrics below!")
counter = 1
while True:
  Ans = input("I want it ___ way! : ")
  if Ans == "that" or Ans == "That":
    print("You got it in", counter, "attempts!" )
    break
  else:
     print("Try again!")
     counter += 1
print("Great job! You go it in ")

Again = input("Want to do one more lyric? (yes/no) ")
if  Again == "yes" or Again == "Yes":
  print("Fill in the blank lyrics below!")
  counter = 1
  while True:
    Ans2 = input("Let it ___! Let it ___! : ")
    if Ans2 == "go" or Ans2 == "Go":
      print("You got it in", counter, "attempts!")
      break
    else:
      print("Try again!")
      counter += 1
elif Again == "no" or Again == "No":
 print("Goodbye!")

Again1 = input("Want to do one more lyric? (yes/no) ")
if  Again1 == "yes" or Again1 == "Yes":
  print("Fill in the blank lyrics below!")
  counter = 1
  while True:
    Ans3 = input("Then you're left in the dust Unless I stuck by ya You're the ___! : ")
    if Ans3 == "sunflower" or Ans3 == "Sunflower":
      print("You got it in", counter, "attempts!")
      print("Hope you enjoyed the game!")
      break
    else:
      print("Try again!")
      counter += 1
elif Again == "no" or Again == "No":
  print("Goodbye!")

  
                                       
    