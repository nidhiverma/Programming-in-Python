def insert(l, n, i=0):
    '''
    Objective: To insert a number in a sorted list of integers using recursion
    Input Parameters: 
        l: a sorted list of integers
        n: number to be inserted
    Return Value:
         a sorted list with number inserted
    '''
    # if n is larger than the largest element of list
    if n > l[-1]:
        l.append(n)
        return l
    # if correct position of n is found 
    if l[i] >= n:
        l.insert(i,n)
        return l
    return insert(l, n, i+1)
    
