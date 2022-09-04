from ExactRatio import * # ExactRatio, decimal_to_ratio, _gcd 

def fast_sum (data, start = 0.0 ):
    """Return the sum of the data, using the exact ratio.
    """
    total = start
    for value in data:
        numerator, denominator = to_ratio(value)
        total = total * denominator + numerator
    return total / denominator 

