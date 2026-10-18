from typing import Never

from .exceptions import CutByKuchisakeOnnaError


def ask_question() -> Never:
    print("Answer only with 'yes' or 'no'.")
    answer: str = input("Am I beautiful?")

    while answer not in {"yes", "no"}:
        answer: str = input("Am I beautiful?")

    answer_bool: bool = True if answer == "yes" else False

    if answer_bool is True:
        raise CutByKuchisakeOnnaError("Kuchisake Onna Sama doesn't like your answer.")

    if answer_bool is False:
        raise CutByKuchisakeOnnaError("Kuchisake Onna Sama doesn't like your answer.")
