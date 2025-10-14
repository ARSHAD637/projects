import random

emojis = {"r": "🪨", "p": "🗞️", "s": "✂️"}
choice = ('r', 'p', 's')

while True: 
    user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower()
    
    if user_choice not in choice:
        print("Invalid")
        continue
    
    computer_choice = random.choice(choice)
    
    print(f"User choice: {emojis[user_choice]} ({user_choice})")
    print(f"Computer choice: {emojis[computer_choice]} ({computer_choice})")
    
    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p") or \
         (user_choice == "p" and computer_choice == "r"):
        print("You won")
    else:
        print("You lost")
    
    should_continue = input("Enter y to continue or n to quit (y/n): ").lower()
    if should_continue == "n":
        break
