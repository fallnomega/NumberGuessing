import random
from art import logo
# Include an ASCII art logo.
print(logo)


def generate_number():
    number = random.randrange(1, 100)
    return number

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
def compare_numbers(user_guess, actual_answer):
    if user_guess == actual_answer:
        print( "Your guess of " + str(user_guess) + " matches the answer " + str(answer) + "! Great guess Player!")
        return False
    elif user_guess > actual_answer:
        print("Too high.\nGuess again.")
        return True
    else:
        print("Too low.\nGuess again.")
        return True

print("Welcome to the Numbers Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
turns_left = 0
remaining_turns = 0
if difficulty_level == 'easy':
    remaining_turns=10
elif difficulty_level=='hard':
    remaining_turns=5
# print(f"You have {remaining_turns} attempts remaining to guess the number")
# Allow the player to submit a guess for a number between 1 and 100.
# player_guess = input("Make a guess: ")

answer = generate_number()
keep_playing = True
# player_guess=10
# answer=10



while keep_playing == True and turns_left < remaining_turns:
    turns_left += 1
    # Allow the player to submit a guess for a number between 1 and 100.
    player_guess = input("Make a guess: ")
    keep_playing = compare_numbers(int(player_guess), int(answer))
    if remaining_turns - turns_left ==0:
        print ("You've run out of guesses, you lose.")
    else:
        print(f"You have {remaining_turns - turns_left} attempts remaining to guess the number")

