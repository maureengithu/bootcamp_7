def super_sum(*args):
	'''
	Returns a sum of numbers.
	eg. 
	super_sum* ==> "Error"
	super_sum(1,2,3) ==> 6
	super_sum("string") ==> 0
	super_sum([1,2,3]) ==> 6
	super_sum([10], [20,30]) ==> 60
	'''
	total = 0
	
	if not args:
		return 0

	else:	
		for x in args:
			if type(x) == list:

				total += sum(x)
		
			else:
				total += x

		return total