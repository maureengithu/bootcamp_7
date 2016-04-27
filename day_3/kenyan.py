from person import Person

class Kenyan(Person): 
	corrupt = False
	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:  #or if self.corrupt == true
			return "Yes"
		return"No"

