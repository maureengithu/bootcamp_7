a = [10, 40, -9, 45, 60, 89]

print a 

for i in a:
	#print in reverse

	i = len(a)

while i > 0:

	print a[i - 1]

	i -= 1

for index in range(len(a) - 1, -1, -1):

	print a[index]


b = [(2,4),(5,10),(6,20),(50,50)]

'''
x: 2, y: 4
x: 5, y: 10

'''

for x in b: 

	print "x: {}, y: {}".format(*x)

for x, y in b:

	print "x: {}, y: {}".format(x , y)