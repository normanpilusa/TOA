#Brute force attempt
def brute(nums):
	count = 0
	#doms = ""

	for i in range(0,len(nums)):
		coord = nums[i]

		for j in range(0,len(nums)):
			next_coord = nums[j]
			
			if(i == j):
				continue
			
			if(coord[0] >= next_coord[0] and coord[1] >= next_coord[1]):
				count += 1
				#doms += str(coord)+' dominates '+ str(next_coord)+'\n'

	return count

#Uses merge sort-like algorithm to find dominating coordinates
def dominate(arr):
	
	dominated = 0

	#Null input
	if (arr == None):
		return None 

	#Single coordinate
	elif(len(arr) < 2):
		return 0 

	#Two coordinates
	elif(len(arr) == 2): 
		return 0 if (arr[0][1] > arr[1][1]) else 1

	#More than two coordinates
	else:
		mid_arr = len(arr)//2

		#Divide and sort by y-ordinate
		left = sorted(arr[:mid_arr], key=lambda k: k[1])
		right = sorted(arr[mid_arr:], key=lambda k: k[1])

		#Keep pointer for divisions/branches
		left_pointer = 0
		right_pointer = 0

		#Check domination using y-ordinate
		while(left_pointer < len(left) and right_pointer < len(right)):
			if (left[left_pointer][1] <= right[right_pointer][1]): 
				dominated += len(right) - right_pointer
				left_pointer += 1
			else:
				right_pointer += 1

		return dominated + dominate(arr[:mid_arr]) + dominate(arr[mid_arr:])



def to_array(string):
	nums = string.strip().split()
	integers = [] #This is not necessary, python is dynamically typed
	
	#Convert inputs in integers
	for string_num in nums:
		integers.append(int(string_num))

	#Create array of coordinates
	nums = []
	for i in range(0, len(integers),2):
		nums.append([integers[i], integers[i+1]])

	#Return sorted by x-ordinate
	return sorted(nums, key=lambda k: k[0])


if __name__ == '__main__':
	nums = input()

	nums_arr = to_array(nums)
	#twelve = [[0, 0], [0, 0], [0, 0], [0, 0]]
	#five = [[1, 1], [-1, -4], [1, 5],[2, 3]]
	#four = [[-5, -10], [20, 25], [30, 2], [-1, -40]]
	print(dominate(nums_arr))
