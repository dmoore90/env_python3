class FizzBuzz:
	def __init__(self, n):
		self.n = int(n)

	def buzzit(self):
		for i in range(self.n + 1):
			if i != 0:
				if i % 3 == 0 and i % 5 != 0:
					print("Fizz")
				elif i % 5 == 0 and i % 3 != 0:
					print("Buzz")
				elif i % 5 == 0 and i % 3 == 0:
					print("FizzBuzz")
				else:
					if i != 0:
						print(i)


f = FizzBuzz(int(input()))
f.buzzit()