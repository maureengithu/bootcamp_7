
class Car(object):

	def __init__(self, cartype, model, name, ):
		self.type = cartype
		self.model = model
		self.name = name

	def __repr__(self):
		return "<object: {}, {}, {}".format(self.type, self.model, self.name)