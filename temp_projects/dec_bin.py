#! /usr/bin/env python3

def dec_bin(a):
	bn = ""
	while ( a > 0):
		rem = str(a % 2)
		bn += rem
		a = int(a / 2)

	print(bn[::-1])

