
# coding: utf-8

# In[2]:


def flattenList(mylist, flat_list = []):
    '''
        Objective: Function to copy a list to another list
        Input Parameters: 
            mylist: a list which is to be copied
        Return: copy of the list 
    '''
    if mylist == []:
        return flat_list
    if type(mylist[0]) == list:
        flattenList(mylist[0], flat_list)
    else:
        flat_list.append(mylist[0])
    return flattenList(mylist[1:], flat_list)


# In[3]:


mylist = [[], [1, 2], 3, [4, [5, 6], 7]]
flattenList(mylist)

