class PrimeChecker():

	def __init__(self,number):
		self.number = number

	def is_prime(self,number):
		if number > 1:
			for j in range(2, number):
				if (number % j) == 0:
					return False
				return True
