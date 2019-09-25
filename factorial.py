def factorial(n):
     '''
    Objective: find factorial of a number
    Input Parameters:
        n: an integer
    Return Values: factorial of n
    '''
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
