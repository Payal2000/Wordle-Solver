# Wordle-Solver

Implementation of a Wordle solver in Python

1. **Algorithm Design and Logic:**
   The code demonstrates the design of an algorithm to solve the Wordle puzzle. It outlines the steps the solver takes to guess the target word and provide feedback based on the guesses.

2. **User Input and Validation:**
   The code incorporates user input for guessing words. It also includes validation to ensure that the user's input is a valid five-letter word composed of letters from the English alphabet.

3. **Wordlist and Data Structures:**
   The code uses a list called `wordlist` to store a collection of valid five-letter words. This list serves as the pool of potential target words for the solver to choose from.

4. **Random Selection:**
   The `random.choice` function is used to randomly select a target word from the wordlist. This demonstrates the concept of random selection in programming.

5. **String Manipulation:**
   The code involves string manipulation by comparing letters in the user's guess with the letters in the target word to provide feedback on correct letters and positions.

6. **Feedback and Decision Making:**
   The solver uses the feedback provided (green for correct letter and position, yellow for correct letter but wrong position) to decide its next guess and narrow down the possible target words.

7. **Looping and Iteration:**
   The code uses a loop to allow multiple rounds of guessing until the user either solves the puzzle or exhausts their allowed number of guesses.

8. **Conditional Statements:**
   Conditional statements are used to check whether the user's input is valid and whether the puzzle is solved.

9. **Functions and Modularity:**
   The code is organized into functions to improve readability and maintainability. This demonstrates the concept of breaking down a complex task into smaller, reusable functions.

10. **User Interaction and Output:**
    The code uses `print` statements to communicate with the user, providing instructions, feedback, and the final result.

11. **Problem Solving and Strategy:**
    The solver's approach demonstrates problem-solving skills, as it aims to systematically narrow down the possible target words through intelligent guesses based on feedback.

12. **Software Design Patterns:**
    It employs some concepts that align with software design patterns, such as validation checks, separation of concerns, and modular code structure.

