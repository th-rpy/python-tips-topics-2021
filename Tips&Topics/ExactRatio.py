from decimal import Decimal
import math
import functools


def to_ratio(x: float or int or Decimal):
    """Convert x exactly to (numerator, denominator) .
    >>> exact_ratio(0.75)
    (3, 4)
    """
    if isinstance(x, float):
        x = Decimal(str(x))
        return decimal_to_ratio(x)
    elif isinstance(x, int):
        return (x, 1)
    elif isinstance(x, Decimal):
        return decimal_to_ratio(x)
    else:
        raise TypeError(f"Unsupported type {type(x)}")


def decimal_to_ratio(d: Decimal):
    """Convert d to (numerator, denominator).
    >>> decimal_to_ratio(Decimal(0.25))
    (1, 4)
    """
    if isinstance(d, Decimal):
        sign, digits, exponent = d.as_tuple()
        denominator = 10**-exponent  # denominator
        digits = list(digits)  # digits of the decimal number
        numerator = functools.reduce(lambda x, y: x * 10 + y, digits)  # numerator
        if numerator == 0:
            return (0, 1)
        if sign == 1:
            numerator = -numerator
        if denominator == 1:
            return (numerator, 1)
        return (
            numerator // _gcd(numerator, denominator),
            denominator // _gcd(numerator, denominator),
        )
    else:
        raise TypeError(f"Unsupported type {type(d)}")


def _gcd(a, b):
    """Return greatest common divisor
    >>> _gcd(4, 6)
    2
    """
    while b:
        a, b = b, a % b
    return a


# Test the function
print(to_ratio(0.75))  # (3, 4)
print(decimal_to_ratio(Decimal(0.25)))  # (1, 4)
