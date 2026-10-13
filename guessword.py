import random
list=['apple', 'banana', 'cherry']
attempts = 5
word = random.choice(list)
print(word)
for i in range(attempts):
    print("Guess a word from the list:")
    guess = input()
    if guess == word:
        print("Congratulations! You guessed the word.")
        break
    else:
        print("Sorry, that's not the word.")
        print(f"You have {attempts - i - 1} attempts left.")
