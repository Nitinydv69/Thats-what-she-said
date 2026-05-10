# Imports
import random
from data.sentences import sentences
# welcome screen
# Setup
# chosing what she said
twss = random.choice(sentences)
# what she said
she_said = twss.upper().split()


def welcome_screen(she_said):

    print("\nWELCOME TO TWSS WORDLE")
    print(f"The sentence has {len(she_said)} words.")
    print("🟩 = correct word + correct place")
    print("🟨 = correct word wrong place")
    print("⬜ = word not in sentence")
    print("THE GAME BEGINS")
    print("GUESS WHAT SHE SAID")
    print(f"{twss}")


# Validation Function


def validate_guess(guess, she_said):
    if len(guess) > len(she_said):
        print("Too many words Solider")
        return False
    if len(guess) < len(she_said):
        print("Cmon she said more than that (More words Homie!) ")
        return False
    if guess == she_said:
        print("\n🎉 Congratulations! That's what she said")
    return True


# Check the guess and assign the box

def check_guess(guess, she_said):
    result = [None] * len(she_said)
    # duplicate handling ( suggested by gpt I dont give a fuckl!!!)
    remaining = she_said.copy()
    # Green Pass
    for i in range(len(guess)):
        if guess[i] == she_said[i]:
            result[i] = "🟩"
            remaining[i] = None
    # Yellow Pass
    for i in range(len(guess)):
        if result[i] is None:
            if guess[i] in remaining:
                result[i] = "🟨"
    # remove matching words
                remaining[remaining.index(guess[i])] = None
    # White Pass
            else:
                result[i] = "⬜"

    return result


# display of results
def display_result(guess, result):

    print("\nRESULT:")
    for word, color in zip(guess, result):
        print(f"{word:<20},{color}")


# hint system :
def give_hint(guess_num, she_said):

    if guess_num == 2:
        print(f"The first word is:{she_said[0]}")
    elif guess_num == 3:
        print(f"The last word is {she_said[-1]}")
    elif guess_num == 4:
        print(f"Cmon there is {she_said[-2]} in it")


# Main Game
welcome_screen(she_said)

guess_num = 1
while guess_num <= 6:
    guess = input(f"\nguess{guess_num}:").upper().split()
    if not validate_guess(guess, she_said):
        continue
    result = check_guess(guess, she_said)

    display_result(guess, result)

    if guess == she_said:
        print("\n Congratulations!! THATS WHAT SHE SAID")
        break

    use_hint = input("\nDo you want a hint? y/n: ").lower()
    if use_hint == "y":
        give_hint(guess_num, she_said)
    elif use_hint == "q":
        exit()

    guess_num += 1
else:
    print("\n GAME OVER! SHE NEVER SAID THAT")
    print(f"\n She said  {twss}")
