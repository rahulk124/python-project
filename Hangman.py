import random
words=['happy', 'sad', 'angry', 'excited', 'bored']

word=random.choice(words)
print(word)
attempts=6
guess=[]
j=0
for i in range(attempts):
    letter=input("enter a letter: ")
    if word[j]==letter:
        guess.append(letter)
        print(guess)
        j+=1

        if guess==list(word):
            print("Congratulations! You guessed the word.")
            break
    else:
        print("Incorrect guess.")
        print(guess)
else:
    print("game over. The word was:", word)