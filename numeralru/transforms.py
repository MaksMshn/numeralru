from math import floor

from .constants import (Case,
                        Gender,
                        LARGE_NUMBERS,
                        HUNDREDS,
                        TENS,
                        MINORS)


def small_num(number, gender, case, animate):
    """ numeralize numbers less than 1000"""
    if (number==0):
        return ""

    results = []

    hundreds = floor(number/100)
    if HUNDREDS[hundreds]:
        results.append(HUNDREDS[hundreds][case])
    two_digit_num = number - 100*hundreds

    # if number is larger than 20...
    tens = floor(two_digit_num/10)
    if TENS[tens]:
        results.append(TENS[tens][case])

    # numbers < 20 are more difficlut due to exceptions...
    if two_digit_num >= 20:
        minors = two_digit_num % 10
    else:
        minors = two_digit_num
    if minors:
        minors = MINORS[minors][case]
        # gender dependent cases
        if not isinstance(minors, str):
            minors = minors[gender]
            if not isinstance(minors, str):
                # living not living dependent
                minors = minors[0 if animate else 1]
        results.append(minors)

    return " " .join(results)


def pluralize(n, one, two, five):
    """
    Pluralize noun depending on the number
    n before it.

    Params
    ------
    n: int
        Number before noun
    one: string
        Word in the form after one,
        e.g. "рубль"
    two: string
        Word in the form after two,
        e.g. "рубля"
    five: string
        Word in the form after five,
        e.g. "рублей"
    Retuns
    ------
    out: string
        Either one, two, or five depending
        on the n.
    """
    n = floor(abs(n)) % 100
    if n > 10 and n < 20:
        return five
    n = n % 10
    if n == 1:
        return one
    if n >= 2 and n <= 4:
        return two
    return five


def numeralize(number, gender=Gender.masculine,
      case=Case.nominative, animate=False, long=True):
    """
    Spell out integer in russian. Case and gender aware.
    Suports abs(number) < 10**36

    Params
    ------
    number: int
        Number to spell out
    
    gender: int (default 0)
        One of the three genders. Conveniently summarized using
        Gender class (Gender.masculine, Gender.feminine, Gender.neuter)
        Default is masculine

    case: int (default 0)
        One of the six russian cases. Represented by Case class. 
        Default is nominative.

    animate: boolean (default False)
        Whehter object to which numeral reffers is alive

    long: boolean (default True)
        Whether "один" should be added in front of large numbers 
        E.g.: "одна тысяча сто" vs "тысяча сто" for 1100

    Returns
    -------
    word: str

    """
    sign = True if int(number) < 0 else False
    norm = abs(int(number))

    # check if we are dealing with zero
    if norm == 0:
        return MINORS[0][case]

    results = []

    rest = norm
    ord = 0
    while rest > 0:
        current = rest%1000
        rest = floor(rest/1000)

        if current:
            words = LARGE_NUMBERS[ord]
            numeral = small_num(current,
                        words[0] if words else gender,
                        case,
                        False if words else animate)
            if numeral:
                results.insert(0, numeral)
                if ord: # numbers are larger than 1000
                    # case + 1 since words[0] = gender
                    one, two, five = words[case + 1]
                    plural = pluralize(current, one, two, five)
                    results.insert(1, plural)
                    if not long and not rest and current == 1:
                        # remove "один" in front of number
                        results.pop(0)
        # move to the next order
        ord += 1

    if sign:
        results.insert(0, "минус")

    return " ".join(results)
