import random

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

def choose_next_guess(wordlist):
    return random.choice(wordlist)

def update_wordlist(wordlist, guess, feedback):
    updated_wordlist = []
    for word in wordlist:
        word_feedback = get_feedback(guess, word)
        if word_feedback == feedback:
            updated_wordlist.append(word)
    return updated_wordlist

def main():
    wordlist = ["apple", "sugar", "table", "grape", "juice", "zebra", "laser"]
    target_word = random.choice(wordlist)
    guesses_left = 6

    while guesses_left > 0:
        guess = choose_next_guess(wordlist)  # Implement your strategy here
        feedback = get_feedback(guess, target_word)
        
        print(f"Guess: {guess}")
        print(f"Feedback: {feedback}")
        
        if feedback.count("green") == 5:
            print("Congratulations! You've solved the puzzle.")
            break
        
        wordlist = update_wordlist(wordlist, guess, feedback)
        guesses_left -= 1

    if guesses_left == 0:
        print(f"Out of guesses. The target word was {target_word}.")

if __name__ == "__main__":
    main()
