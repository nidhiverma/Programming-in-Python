def sumOfListElements(l, i=0):
    '''
    Objective: to find the sum of list elements using recursion
    Input Parameter: 
        l: list of elements
    Return Value: sum of list elements
    '''
    if i == len(l):
        return 0
    return l[i] + sumOfListElements(l, i+1)
