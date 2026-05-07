import random
from data.sentences import sentences
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
print(twss)
# number of guesses 6
for guess_num in range(1, 7):

    guess = input(f"guess{guess_num}:").upper().split()
    # word count validation
    if len(guess) > len(she_said):
        print("Too many words Solider")
        continue
    if len(guess) < len(she_said):
        print("Cmon she said more than that (More words Homie!) ")
        continue
    if guess == she_said:
        print("\n🎉 Congratulations! That's what she said")
        break
    # store the results
    result = [None] * len(she_said)
    # duplicate handling ( suggested by gpt I dont give a fuckl!!!)
    remaining = she_said.copy()
    # all correct pass
    for i in range(len(guess)):
        if guess[i] == she_said[i]:
            result[i] = "🟩"
            remaining[i] = None
    # wrong place
    for i in range(len(guess)):
        if result[i] is None:
            if guess[i] in remaining:
                result[i] = "🟨"
            # remove matching words
                remaining[remaining.index(guess[i])] = None

            else:
                result[i] = "⬜"

# display of results
    print("RESULT:")
    for word, color in zip(guess, result):
        print(f"{word:<20},{color}")

    # lose
else:
    print("\nAh You don't know")
