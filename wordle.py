# ==========================
# Imports
# ==========================

import random
from data.questions import questions


# ==========================
# Question System
# ==========================

def get_questions_for_level(level):

    return [
        question
        for question in questions
        if question["difficulty"] <= level
    ]


def get_random_question(level):

    available_questions = get_questions_for_level(level)

    return random.choice(available_questions)


# ==========================
# Welcome Screen
# ==========================

def welcome_screen(she_said):

    print("\n🎮 WELCOME TO TWSS WORDLE")
    print(f"📝 The sentence has {len(she_said)} words.")
    print("🟩 = correct word + correct place")
    print("🟨 = correct word wrong place")
    print("⬜ = word not in sentence")
    print("❌ Type 'q' anytime to quit.")

    print("\nTHE GAME BEGINS")
    print("GUESS WHAT SHE SAID")


# ==========================
# Validation
# ==========================

def validate_guess(guess, she_said):

    if len(guess) > len(she_said):
        print(
            f"❌ Too many words! "
            f"She said {len(she_said)} words."
        )
        return False

    if len(guess) < len(she_said):
        print(
            f"❌ Too few words! "
            f"She said {len(she_said)} words."
        )
        return False

    return True


# ==========================
# Guess Checking
# ==========================

def check_guess(guess, she_said, correct_words):

    result = [None] * len(she_said)

    # duplicate handling
    remaining = she_said.copy()

    # GREEN PASS
    for i in range(len(guess)):

        if guess[i] == she_said[i]:

            if guess[i] not in correct_words:
                correct_words.append(guess[i])

            result[i] = "🟩"
            remaining[i] = None

    # YELLOW PASS
    for i in range(len(guess)):

        if result[i] is None:

            if guess[i] in remaining:

                result[i] = "🟨"

                # remove duplicate match
                remaining[
                    remaining.index(guess[i])
                ] = None

            else:
                result[i] = "⬜"

    return result


# ==========================
# Display Results
# ==========================

def display_result(guess, result):

    print("\n📊 RESULT:")

    for word, color in zip(guess, result):
        print(f"{word:<20} {color}")


# ==========================
# Hint System
# ==========================

def get_max_hints(level):

    if level <= 2:
        return 3

    elif level <= 5:
        return 2

    elif level <= 7:
        return 1

    else:
        return 0


def give_hint(
    she_said,
    used_hints,
    correct_words
):

    possible_hints = []

    for word in she_said:

        if (
            word not in used_hints
            and word not in correct_words
        ):
            possible_hints.append(word)

    if len(possible_hints) == 0:

        print("❌ No useful hints left :(")
        return used_hints, False

    hint = random.choice(possible_hints)

    print(
        f"\n💡 Hint: "
        f"'{hint}' is in the sentence"
    )

    used_hints.append(hint)

    return used_hints, True


# ==========================
# Game Setup
# ==========================

player_level = 1
questions_completed = 0

question = get_random_question(player_level)

sentence = question["sentence"]
category = question["category"]
difficulty = question["difficulty"]
image = question["image"]

she_said = sentence.upper().split()

hint_left = get_max_hints(player_level)

used_hints = []
correct_words = []

guess_num = 1


# ==========================
# Game Start
# ==========================

welcome_screen(she_said)

print(f"\n🎮 Level: {player_level}")
print(f"📂 Category: {category}")
print(f"💡 Hints Available: {hint_left}")

print("\n💭 Think carefully...")
print("👀 This one might be sus")


# ==========================
# Main Game Loop
# ==========================

# ==========================
# Game Loop
# ==========================

player_level = 1
questions_completed = 0

while True:

    # Get new question
    question = get_random_question(
        player_level
    )

    sentence = question["sentence"]
    category = question["category"]
    difficulty = question["difficulty"]
    image = question["image"]

    she_said = (
        sentence.upper().split()
    )

    hint_left = get_max_hints(
        player_level
    )

    used_hints = []
    correct_words = []

    guess_num = 1

    # Welcome screen
    welcome_screen(
        she_said
    )

    print(
        f"\n🎮 Level: "
        f"{player_level}"
    )

    print(
        f"📂 Category: "
        f"{category}"
    )

    print(
        f"💡 Hints Available: "
        f"{hint_left}"
    )

    print(
        "\n💭 Think carefully..."
    )

    print(
        "👀 This one might be sus"
    )

    # Guess loop
    while guess_num <= 6:

        guess = input(
            f"\n📝 Guess "
            f"{guess_num} "
            f"({len(she_said)} words): "
        ).strip()

        # Quit
        if guess.lower() == "q":

            print(
                "👋 Goodbye!"
            )

            exit()

        guess = (
            guess.upper().split()
        )

        # Validate
        if not validate_guess(
            guess,
            she_said
        ):
            continue

        # Check guess
        result = check_guess(
            guess,
            she_said,
            correct_words
        )

        display_result(
            guess,
            result
        )

        # WIN
        if guess == she_said:

            print(
                "\n🎉 THAT'S WHAT "
                "SHE SAID 😭"
            )

            questions_completed += 1

            print(
                f"✅ Questions solved:"
                f" {questions_completed}/10"
            )

            # LEVEL UP
            if (
                questions_completed
                >= 10
            ):

                player_level += 1

                questions_completed = 0

                print(
                    f"\n🔥 LEVEL UP!"
                )

                print(
                    f"You are now "
                    f"Level "
                    f"{player_level}"
                )

            input(
                "\nPress Enter "
                "for next question..."
            )

            break

        # Hints
        if (
            guess_num < 6
            and hint_left > 0
        ):

            print(
                f"\n💡 You have "
                f"{hint_left} hints left"
            )

            use_hint = input(
                "Want a hint? "
                "(y/n): "
            ).lower()

            if use_hint == "y":

                (
                    used_hints,
                    hint_given
                ) = give_hint(
                    she_said,
                    used_hints,
                    correct_words
                )

                if hint_given:
                    hint_left -= 1

        guess_num += 1

    # LOSS
    else:

        print(
            "\n💀 GAME OVER!"
        )

        print(
            "SHE NEVER "
            "SAID THAT 😭"
        )

        print(
            f"\n✅ She said:"
            f" '{sentence}'"
        )

        play_again = input(
            "\nPlay again?"
            " (y/n): "
        ).lower()

        if play_again != "y":
            break
