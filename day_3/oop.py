from person import Person
from kenyan import Kenyan

p = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 40)

print p.say_hello()

a = [('jane', 23), ('joe', 50), ('jackie', 34), ('jacob', 23), ('jee', 18), ('josh', 60)]

b = []

for name,age in a:
	person = Person(name, age)
	b.append(person)

print b

for j in b: 
	print j.say_hello()

print p.name
print p.age
print p2.people_count

#kenyan.py
k = Kenyan('Anita Waiguru', 20)

k.probe(False)

print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()
print k.corrupt