
def brute(ans, n):
	cal = int(n*n + 5*n +18)
	num = 3

	while(cal != ans):
		num+=1
		cal = int(num*num + 5*num +18)

	return num

if __name__ == '__main__':
	print(brute(7363094, 10000))