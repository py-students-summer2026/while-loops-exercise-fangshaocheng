"""
99 Bottles of Beer - while loop with flag version.

Sings the song "99 Bottles of Beer on the Wall" using a while loop whose
continuation is controlled directly by a boolean flag variable.
"""


def get_starting_number():
    """
    Asks the user how many bottles of beer to start with, repeating the
    question until a valid response (an integer 1 or greater) is given.

    :return: the starting number of bottles as an int
    """
    while True:
        response = input("How many bottles of beer on the wall? ")
        try:
            number = int(response)
        except ValueError:
            continue
        if number >= 1:
            return number


def bottles(count):
    """
    Returns the correctly pluralized bottle phrase for a given count.

    :param count: number of bottles
    :return: e.g. "no more bottles", "1 bottle", "5 bottles"
    """
    if count == 0:
        return "no more bottles"
    elif count == 1:
        return "1 bottle"
    else:
        return f"{count} bottles"


def sing(num_bottles):
    """
    Outputs the lyrics to the song, starting from num_bottles, using a while
    loop controlled by a boolean flag variable.

    :param num_bottles: number of bottles to start singing with
    """
    current = num_bottles
    singing = True
    while singing:
        remaining = current - 1
        take = "Take it down" if current == 1 else "Take one down"

        if remaining == 0:
            ending = "no more bottles of beer on the wall!"
        else:
            ending = f"{bottles(remaining)} of beer on the wall."

        print(f"{bottles(current)} of beer on the wall, {bottles(current)} of beer.")
        print(f"{take}, pass it around, {ending}")
        print()

        if current <= 1:
            singing = False

        current -= 1
