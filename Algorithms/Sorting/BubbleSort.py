def bubble(mylist, i, j):
    '''
    Objective: helper function to partially sort a list by placing the smallest value at the first position of the unsorted list
    Input Pamameter: 
        mylist: a list of integers
        j: upper index of bubble sort
        i: lower index of bubble
    Return Value: partially sorted list
    '''
    if j == i:
        return mylist
    if mylist[j] < mylist[j-1]:
        tmp = mylist[j]
        mylist[j] = mylist[j-1]
        mylist[j-1] = tmp
    bubble(mylist, i, j-1)
    
def bubbleSort(mylist, start=0, end=-1):
    '''
    Objective: function to sort a list using bubble sort
    Input Parameters: 
        mylist: list of integers
    Return Value: sorted list
    '''
    if end == -1:
        end = len(mylist)-1
    if start == end:
        return mylist
    else:
        n = bubble(mylist, start, end)
        bubbleSort(mylist, start+1, end)

lst1 = [10, 60, 30, 20, 80, 5, 96, 33]
bubbleSort(lst1)
print(lst1)
