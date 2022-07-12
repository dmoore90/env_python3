
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def show_car(self):
		print("Make: " + self.make)
		print("Model: " + self.model)
		print("Year: ", self.year)
