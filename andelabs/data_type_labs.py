def data_type(data):

	if type(data) == str:

		return len(data)

	elif type(data) == bool:

		return data

	elif type(data) == int:
	  
		if data < 100:
		  
			return "less than 100"
			
		elif data > 100:
		  
			return "more than 100"
			
		else:
		  
			return data
			
	elif type(data) == list:
	  
		if len(data) > 2:
		  
			return data[2]
			
		else:
		  
			return None
			
	else:
	  
		return "no value"

print data_type(None)
print data_type([1,2,3])
print data_type([1,2])
print data_type(True)
print data_type(3)
print data_type(200)
print data_type("Andela")