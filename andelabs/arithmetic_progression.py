def arith_geo (A): 

  if len(A) == 0:
    return 0

  elif is_arithmetic(A):
    return "Arithmetic"

  elif is_geometric(A): 
    return "Geometric"

  else:
    return -1

def is_arithmetic(A):
    difference = A[1] - A[0]
    for index in range(len(A)-1):
        if not (A[index + 1] - A[index] == difference):
             return False
    return True

def is_geometric(A):
  ratio = A[1]/float(A[0])
  for index in range(len(A)-1):
    if not (A[index + 1] / float(A[index]) == ratio):
      return False
  return True