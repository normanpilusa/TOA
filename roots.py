#Program to find all the square roots of a number x under arithmetic modulo n. 
#It finds all the integers a, 0 < a < n, such that a^2 = x mod n.

import sys

def roots(x, n):
	mod = x % n
	roots = ""
	
	for number in range(n):
		square = number*number
		
		if(square == mod):
			roots += str(number) + " "
			
		elif(square > n):
			if square % n == mod: roots += str(number) + " "
			
	return roots

if __name__ == '__main__':
	n = int(raw_input())
	x = int(raw_input())
	
	print roots(x, n)
	



