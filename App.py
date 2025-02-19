import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

while is_running:

    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! try again")

        elif guess > answer:
            print("too high try again")
        else:
            print(f"Correct! the answer was {answer}")
            print(f"you got it in {guesses} guesses")
            is_running = False
    else:
        print("Invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}.")
