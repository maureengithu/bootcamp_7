 #"olly olly in come free"

def words(strings):

	occurance = {}
	for j in strings.split():
		if j.isdigit():
			j = int(j)

		if occurance.get(j):
			occurance[j] += 1
		else:
			occurance[j] = 1

	return occurance

print words("testing 1 2 testing") 