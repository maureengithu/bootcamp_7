
f = [(10,20,40),(10,40),(4,5,50)]

#assignment day_3
'''
x: 10, y: 20, z: 40,
x: 10, y: 40

'''
for x in f:
	if len(x) == 3:
		print "x: {}, y: {}, z: {}". format(*x)
	else:
		print "x: {}, y: {}".format(*x)