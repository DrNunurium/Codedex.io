import random #We need to import random module if we want to get a random item from our list of symbols

#here, we define a play function. We have a list with 4 symbols. A results variable that will randomly select 3 items (k=3) from the list
def play():
  symbols=['🍒',' 🍇', '🍉', '7️⃣']

  results = random.choices(symbols, k=3)

  print(" |" .join(results)) #We print the results with a " |" icon to visually separate items. We use .join(results) to get our 3 symbols next to each other

  if all(item == '7️⃣' for item in results): #If all items are '7️⃣' for each item in results loop, print "Jackpot". Otherwise, print "Thanks for playing"
    print("Jackpot")
  else:
    print("Thanks for playing")
    
while True: #We use a while True loop to keep calling play() function. We introduce a play_again variable with an input from the user. If play_again is Y or y, keep playing. Otherwise, stop the while loop and stop playing.
  play()
  play_again=input("Do you want to play again?(Y/N): ").upper()
  if play_again != "Y":
    break
print("Goodbye")
