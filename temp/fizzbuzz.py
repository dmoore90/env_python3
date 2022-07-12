#! /usr/bin/env python3

# fizz buzz

n = int(input('enter number'))
x = 1

while (x <= n):
	if (( x % 3 == 0 ) and ( x % 5 != 0 )):
		print("Fizz")
	elif (( x % 5 == 0 ) and ( x % 3 != 0 )):
		print("Buzz")
	elif (( x % 5 == 0 ) and ( x % 3 == 0 )):
		print("FizzBuzz")
	else:
		print(x)
	x += 1

