def sum_digits(A):
    '''
    Takes a list A and adds the digits to give the total
    '''

    total = 0

    for j in A:

        k = str(j) 

        for l in k:

            total += int(l)
            
    return total   
    
