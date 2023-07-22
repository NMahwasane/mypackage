def top_n (items, n):       
    """ Explain what the function does"""
    for i in range(n):
        for j in range(len(items) -1-i):
            if items[j] > items[j+1]:  # if this item is bigger than the next item
                items[j],items[j+1] = items[j+1], items[j] #swap the 2

                #get the last 2 items
                top_n = items[-n:]

                #return in descending order
                return top_n[::-1]
