def find_missing(list1, list2):
  if list1 == [] or list2 == []:
    return 0
  
  j = []
  if len(list1) < len(list2):
    for i in list2:
      if not i in list1:
        j.append(i)
    if j == []:
    	return 0
    return j
      
  else:
  	for i in list1:
  		if not i in list2:
  			j.append(i)
        if j == []:
        	return 0
        return j
print find_missing([2], [2])
print find_missing([4, 6, 8], [4, 6, 8, 10])
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])