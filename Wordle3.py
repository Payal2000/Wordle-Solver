# Importing libraries
import random

# Defining functions
def get_feedback(guess, target_word):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback.append("green")
        elif guess[i] in target_word:
            feedback.append("yellow")
        else:
            feedback.append("none")
    return feedback

# Check if the word is valid
def is_valid_word(word, wordlist):
    return word in wordlist


# Main function
def main():
    wordlist = [
    "apple", "sugar", "table", "grape", "juice", "zebra", "laser",
    "pizza", "chair", "lemon", "happy", "quiet", "truly", "crazy",
    "ocean", "vivid", "wrist", "thick", "young", "giant", "flame",
    "brave", "scent", "earth", "truck", "spoon", "queen", "music",
    "knife", "swift", "smile", "dream", "beach", "shake", "radio",
    "round", "train", "honey", "tiger", "jelly", "crown", "bloom",
    "charm", "globe", "wings", "angel", "black", "water", "storm",
    "child", "glass", "happy", "fairy", "sweet", "charm", "green",
    "cloud", "sunny", "heart", "melon", "daisy", "magic", "peace"
]

    target_word = random.choice(wordlist)
    guesses_left = 6

# Printing the rules
    print("Welcome to Wordle Solver!")
    print("Try to guess the hidden five-letter word.")
    print("Feedback: green means correct letter and position, yellow means correct letter but wrong position.")
    

# Looping the game
    while guesses_left > 0:
        guess = input(f"\nGuess {6 - guesses_left + 1}/{6}: ").lower()

        if len(guess) != 5 or not is_valid_word(guess, wordlist):
            print("Invalid guess. Please enter a valid five-letter word.")
            continue

        feedback = get_feedback(guess, target_word)
        
        print(f"Feedback: {feedback}")
        
        if feedback.count("green") == 5:
            print("Congratulations! You've solved the puzzle.")
            break
        
        guesses_left -= 1
        if guesses_left > 0:
            print(f"Guesses left: {guesses_left}")
        else:
            print(f"Out of guesses. The target word was {target_word}.")

# Running the main function
if __name__ == "__main__":
    main()
