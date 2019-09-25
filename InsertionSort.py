def sort(n, x, index):
    '''
    Objective: helper function to partially sort a list
    Input Parameters: 
        n: list of integers
        x: value to be inserted
        index: index value upto which the list n is already sorted
    Return Value: partially sorted list 
    ''' 
    '''
    Approach: Insert x into its correct position in range [0,index+1]
    '''
    if index < 0:
        n.insert(0,x)
        return n
    if x < n[index]:
        index -= 1
    elif x >= n[index]:
        n.insert(index+1,x)
        return n
    return sort(n,x,index)

def insertionSort(n, x, index = 0):
    '''
    Objective: insert an element in an unsorted list and then sort the list
    Input Parmeters: 
        n: list of integers
        x: element to be inserted
    Return Value: sorted list with element inserted
    '''
    '''
    Approach: 
        -> Insert the value x in unsorted list
        -> incrementally start sorting the list values starting with first 2 elements using sort function
        -> return the partially sorted list and update the original list and call recursion on this updated list
        -> return when the list is completely sorted
    '''
    if index == 0:
        n.insert(0,x)
    if index == len(n):
        return n
    if index < len(n)-1:
        tmp = n.pop(index+1)
        n = sort(n, tmp, index)
    return insertionSort(n, x, index+1) 
