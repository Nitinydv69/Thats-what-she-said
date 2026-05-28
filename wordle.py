# Imports

from game_engine import (
    get_random_question,
    validate_guess,
    check_guess,
    give_hint,
    get_max_hints,
    calculate_score
)

# Welcome Screen


def welcome_screen(she_said):

    print("\n🎮 WELCOME TO TWSS WORDLE")
    print(f"📝 The sentence has {len(she_said)} words.")
    print("🟩 = correct word + correct place")
    print("🟨 = correct word wrong place")
    print("⬜ = word not in sentence")
    print("❌ Type 'q' anytime to quit.")

    print("\nTHE GAME BEGINS")
    print("GUESS WHAT SHE SAID")


# Display Results


def display_result(
    guess,
    result
):

    guess_text = (
        " ".join(guess)
    )

    result_text = (
        " ".join(result)
    )

    print("\n📊 RESULT")

    print(
        guess_text
    )

    print(
        result_text
    )

# display guess history :


def display_guess_history(
    guess_history
):

    if not guess_history:
        return

    print("\n📜 GUESS HISTORY")

    for i, (
        guess,
        result
    ) in enumerate(
        guess_history,
        start=1
    ):

        formatted_guess = ""

        for word in guess:
            formatted_guess += (
                f"{word:<12}"
            )

        formatted_result = ""

        for emoji in result:
            formatted_result += (
                f"{emoji:<12}"
            )

        print(
            f"\n{i:>2}. "
            f"{formatted_guess}"
        )

        print(
            "    "
            f"{formatted_result}"
        )


player_level = 1
questions_completed = 0
total_score = 0
question = get_random_question(player_level)

sentence = question["sentence"]
category = question["category"]
difficulty = question["difficulty"]
image = question["image"]

she_said = sentence.upper().split()

hint_left = get_max_hints(player_level)
hints_used = 0

used_hints = []
correct_words = []
guessed_words = []
guess_history = []
guess_num = 1

# Game Loop


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
    guess_history = []
    guessed_words = []
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
        display_guess_history(
            guess_history
        )

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
        for word in guess:
            if word not in guessed_words:
                guessed_words.append(word)

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
        guess_history.append(
            (guess, result)
        )

        display_guess_history(
            guess_history
        )

        # WIN
        if guess == she_said:

            print(
                "\n🎉 THAT'S WHAT "
                "SHE SAID 😭"
            )
            score_gained = (
                calculate_score(
                    guess_num,
                    difficulty,
                    hints_used
                )
            )

            total_score += (
                score_gained
            )

            print(
                f"\n🏆 +"
                f"{score_gained} "
                f"POINTS"
            )

            print(
                f"⭐ TOTAL SCORE: "
                f"{total_score}"
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

        if guess_num < 6:

            if hint_left > 0:

                print(
                    f"\n💡 You have "
                    f"{hint_left} hints left"
                )

                use_hint = input(
                    "Want a hint? (y/n): "
                ).lower()

                if use_hint == "y":

                    (
                        used_hints,
                        hint_given,
                        hint
                    ) = give_hint(
                        she_said,
                        used_hints,
                        correct_words,
                        guessed_words
                    )

                    if hint_given:

                        print(
                            f"\n💡 Hint: "
                            f"'{hint}' "
                            f"is in the sentence"
                        )

                        hint_left -= 1
                        hints_used += 1
                        print(
                            f"💡 Hints left: "
                            f"{hint_left}"
                        )

                elif use_hint == "n":

                    print(
                        "👍 No hint used"
                    )

            else:

                print(
                    "\n❌ No hints left!"
                )

        # ALWAYS move to next guess
        guess_num += 1

    # ==========================
    # LOSS CONDITION
    # ==========================

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
            "\nPlay again? (y/n): "
        ).lower()

        if play_again != "y":
            break
