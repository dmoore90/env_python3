from playsound import playsound
from car_class import Car

class DriveCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

	def startEngine(self):
		playsound('audio.mp3')

newCar = DriveCar("Scion", "TC", 2006)
newCar.startEngine()