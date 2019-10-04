def gcd(a, b):
    '''
    Objective: find gcd of 2 numbers
    Input Parameters:
        a: an integer
        b: an integer
    Return Values: gcd of a and b
    '''
    if b == 0:
        return a
    return gcd(b, a % b)
