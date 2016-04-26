def sum_digits(A):
    total = 0
    for j in A:
        k = str(j) 
        for l in k:
            total += int(l)
    return total

print sum_digits([10, 30,45])    
    
