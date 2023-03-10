from data import get_wordle_guesses, get_wordle_answers
from solve import filter_answers, next_best_guesses, value

default_guess = "arise" # default guess if user doesn't enter anything

valid_user_guesses = get_wordle_guesses() # all valid guesses user can make
program_guesses = get_wordle_answers() # guesses the program can recommend, otherwise program takes too long to run
answers = get_wordle_answers() # will be filtered so can't use same list as program_guesses

def valid_result(result):
    if len(result) != 5:
        return False
    for i in range(5):
        if result[i] != '0' and result[i] != '1' and result[i] != '2':
            return False
    return True

if __name__ == "__main__":
    print()
    print("Wordle Bot")
    print()
    print("When entering the results of your guesses, use \'0\' for gray, \'1\' for yellow, and \'2\' for green, i.e. \'02100\'")
    print()
    print("You can use your own guess at any time, or press \'enter\' to use the program's recommended guess")
    print()
    guess = str(input("What is your initial guess?\n"))
    if guess == "":
        guess = default_guess
        print("Using default initial guess: \'", default_guess, "\' \n(you can change this in play.py)", sep='')
    while guess not in valid_user_guesses:
        print("Invalid Guess, Try Again")
        guess = str(input("What is your initial guess?\n"))
        if guess == "":
            guess = default_guess
    print()
    for i in range(6):
        print("Turn", i + 1)
        print("Guess: \"" + guess + "\"")
        result = str(input("Result: "))
        while not valid_result(result):
            print("Invalid Result, Try Again")
            result = str(input("Result: "))
        result = [int(x) for x in result]
        answers = filter_answers(guess, result, answers)
        if len(answers) == 0:
            print()
            print("The answer is not in our list of possible answers.")
            print()
            break
        if len(answers) == 1:
            print()
            print("Turn", i + 2)
            print("The answer is \"" + answers[0] + "\"")
            print()
            break
        best_guesses = next_best_guesses(program_guesses, answers)
        val = round(value(best_guesses[0], answers) / len(answers), 2)
        print("Number of possible answers left:", len(answers))
        if len(answers) <= 10:
            print("The possible answers are", answers)
        if len(best_guesses) == 1:
            print("The best guess is \"" + best_guesses[0] + "\"")
            print("This guess is expected to eliminate", val, "possible answers")
        else:
            print("The best guesses are", best_guesses)
            print("These guesses are expected to eliminate", val, "possible answers")
        guess = str(input("Next guess: "))
        if guess == "":
            guess = best_guesses[0]
        while guess not in valid_user_guesses:
            print("Invalid Guess, Try Again")
            guess = str(input("Next guess: "))
            if guess == "":
                guess = best_guesses[0]
        print()
 