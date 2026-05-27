# Imports
import random
from data.questions import questions

# Question System


def get_questions_for_level(level):

    return [
        question
        for question in questions
        if question["difficulty"] <= level
    ]


def get_random_question(level):

    available_questions = get_questions_for_level(level)

    return random.choice(
        available_questions
    )


# ==========================
# Validation


def validate_guess(
    guess,
    she_said
):

    if len(guess) > len(she_said):

        print(
            f"❌ Too many words! "
            f"She said "
            f"{len(she_said)} "
            f"words."
        )

        return False

    if len(guess) < len(she_said):

        print(
            f"❌ Too few words! "
            f"She said "
            f"{len(she_said)} "
            f"words."
        )

        return False

    return True


# Guess Checking

def check_guess(
    guess,
    she_said,
    correct_words
):

    result = [None] * len(
        she_said
    )

    remaining = (
        she_said.copy()
    )

    # GREEN PASS
    for i in range(
        len(guess)
    ):

        if (
            guess[i]
            == she_said[i]
        ):

            if (
                guess[i]
                not in correct_words
            ):

                correct_words.append(
                    guess[i]
                )

            result[i] = "🟩"

            remaining[i] = None

    # YELLOW PASS
    for i in range(
        len(guess)
    ):

        if result[i] is None:

            if (
                guess[i]
                in remaining
            ):

                result[i] = "🟨"

                remaining[
                    remaining.index(
                        guess[i]
                    )
                ] = None

            else:

                result[i] = "⬜"

    return result


# Hint System


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
    correct_words,
    guessed_words
):

    possible_hints = []

    for word in she_said:

        if (
            word
            not in used_hints
            and word
            not in correct_words
            and word
            not in guessed_words
        ):

            possible_hints.append(
                word
            )

    if (
        len(
            possible_hints
        ) == 0
    ):

        return (
            used_hints,
            False,
            None
        )

    hint = random.choice(
        possible_hints
    )

    used_hints.append(
        hint
    )

    return (
        used_hints,
        True,
        hint
    )
