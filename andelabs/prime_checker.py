class PrimeChecker(object):
    def __init__(self, number=""):
         self.number = number

    def is_prime(self):

        if self.number != '':
            x = int(self.number)
            if x < 2:
                return True
            else:
                for i in range(2,x):
                    if x % i == 0:
                        return False
            return True
        else:
            return False