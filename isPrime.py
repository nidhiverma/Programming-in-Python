def isPrime(n, i=2):
    '''
    Objective: To check whether a number is prime or not
    Input Parameter: 
        n: an integer
    Return Value:
        True if number is prime otherwise False 
    '''
    if n == 2 or i == n//2:
        return True
    elif n < 2 or n%i == 0:
        return False
    return isPrime(n, i+1)
