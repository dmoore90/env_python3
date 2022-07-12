#! /usr/bin/env python3

def a_xor_b(a, b):
	ba = ""
	while ( a > 0):
		rem = str(a % 2)
		ba += rem
		a = int(a / 2)
	
	if (len(ba) < 4):
		ba += "0" * (4 - len(ba))
	ba = ba[::-1]
		
	print("ba", ba)
	bb = ""
	while ( b > 0 ):
		rem = str( b % 2 )
		bb += rem
		b = int( b / 2 )

	if(len(bb) < 4):
		bb += "0" * (4 - len(bb))
	bb = bb[::-1]
	print("bb", bb)

	nb = ""
	x = 0
	while(len(nb) < 4):
		if (ba[x] == bb[x]):
			nb += "0"
		else:
			nb += "1"
		x += 1

	dec = (int(nb[0]) * 2**3) + (int(nb[1]) * 2**2) + (int(nb[2]) * 2**1) + (int(nb[3]) * 2**0)
	print(dec)


c = "yes"
while (c == "yes"):	
	num_a = int(input("enter first number: "))
	num_b = int(input("enter second number: "))
	a_xor_b(num_a, num_b)
	c = input("continue? type yes: ")
