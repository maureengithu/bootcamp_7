def string_length(x):

	if type(x) == str:
	  
		return [len(x)]

	elif type(x) == list:
	  
		j = []
		for i in x:
		  
			if type(i) == str:
			  
				j.append(len(i))
				
			else:
			  
				return "Invalid input. Provide a list of strings"
				
		return j
		
	else:
	  
		return "Invalid data type. Add a string or a list of strings"


print string_length('Godson')
print string_length('Mia')
print string_length(['Adam', 'Frankel'])
print string_length(['Michael', 'William', 'Smith'])
print string_length([3, 4])
