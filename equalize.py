def equalise(nums):
	#Sort input array, Python uses timsort which is O(nlogn)
	nums.sort()

	#Get the largest number
	max = nums[-1]

	#Check if elements are equalizable
	for element in nums:
		#Ignore max
		if (element == max):
			continue

		#Everything else is less than max
		else:
			remainder = max//element
			#Stops iterations when non-factor is found
			if (remainder % 2 != 0):
				return -1 

	#All numbers can be made equal, Max is lowest common value
	return max

def to_array(string):
	nums = string.split()
	integers = [] #This is not necessary, python is dynamically typed
	
	for string_num in nums:
		integers.append(int(string_num))

	return integers 


if __name__ == '__main__':
	incorrect = [13, 5, 7, 11, 47, 53, 109]
	correct = [628, 1256, 628, 2512, 1256]

	nums = input()#628 1256 628 2512 1256

	nums_arr = to_array(nums)
	print(equalise(nums_arr))