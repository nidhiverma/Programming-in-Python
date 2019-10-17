
# coding: utf-8

# In[31]:


def copyList(mylist, copy=[]):
    '''
        Objective: Function to copy a list to another list
        Input Parameters: 
            mylist: a list which is to be copied
        Return: copy of the list 
    '''
    if mylist == []:
        return copy
    copy.append(mylist[0])
    return copyList(mylist[1:], copy)


# In[33]:


mylist = [[], [1, 2], 3, [4, [5, 6], 7]]
copyList(mylist)

