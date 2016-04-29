 #"olly olly in come free"

def word_occurance(sentence):
	occurance = {}
	for j in sentence.split():
		try: 
			occurance[j] += 1
		except KeyError:
			occurance[j] = 1
	#for i, j in occurance.iteritems():
	return occurance

print word_occurance("testing 1 2 testing") 