import random
from sentences import sentences
# chosing what she said
twss = random.choice(sentences)
# what she said
she_said = twss.upper().split()
# welcome box
print("\nWELCOME TO TWSS WORDLE")
print(f"The sentence has {len(she_said)} words.")
print("🟩 = correct word + correct place")
print("🟨 = correct word wrong place")
print("⬜ = word not in sentence")
print("THE GAME BEGINS")
print("GUESS WHAT SHE SAID")

# number of guesses 6
for guess_num in range(1, 7):

    guess = input(f"guess{guess_num}:").upper().split()
    # word count validation
    if len(guess) > len(she_said):
        print("Too many words Solider")
        continue
    elif len(guess) < len(she_said):
        print("Cmon she said more than that (More words Homie!) ")
    # store the results
    result = [None] * len(she_said)

    correct_words = {

        word for word, correct in zip(guess, she_said) if word == correct
    }
    misplaced_words = set(guess) & set(she_said) - correct_words
    wrong_words = set(guess) - set(she_said)

    if guess == she_said:
        print("CORRECT!")
        break
    else:
        if len(guess) > len(twss):
            print("need more words")
        elif len(guess) > len(twss):
            print("calm down solider, less words more meaning")
        else:
            break

        print("Correct words: ", ",".join(sorted(correct_words)))
        print("misplaced words:", ",".join(sorted(misplaced_words)))
        print("Wrong words:", ",".join(sorted(wrong_words)))

else:
    print(f"the sentence was:  {twss}")
