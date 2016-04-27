def hello(name, age, class_=''):
	'''
	Explains attributes of an individual
	'''
	if class_ != '':
		return "I am {}, {} y/o, and {} class".format(name, age, class_) 
	return "I am {}, and I'm {}".format(name, age)

people = [
			("jane", 23, 'high'),
			("joe", 25, 'low'),
			("Brian", 60),
			("Betty", 45),
			]
#for name, age in people:
	#print hello(name, age)
# use of unpacking

for person in people :
	print hello(*person)

def super_sum(*args):

	'''
	Takes in variable number of items,
	and returns the sum.
	e.g super_sum(10, 20) = 30
		super_sum(10,20,40) = 70
		super_sum(1, 4, 5, 6, 7) = 23

	'''


	total = 0
	for i in args:
		total += i

	return total

print super_sum(10,20)
print super_sum(1, 4, 5, 7)
a= [10, 40, 60]
print super_sum(*a)
