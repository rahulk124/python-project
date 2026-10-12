import random
attempts = 7
number = random.randint(1, 100)
for i in range(attempts):
    print("Guess a number between 1 and 100")
    guess = int(input())
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")