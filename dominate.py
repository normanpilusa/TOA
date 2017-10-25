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

#Attempt 2, looks like DAC but it is not
def dom(index, nums):
	if (index >= len(nums)):
		return 0
	else:
		count = 0
		coord = nums[index]

		for i in range(0,len(nums)):
			next_coord = nums[i]

			if(i == index):
				continue

			elif(coord == next_coord and i > index):
				continue #Avoid counting twice

			elif(coord[0] >= next_coord[0] and coord[1] >= next_coord[1]):
				count += 1 

		return count + dominate(index+1, nums)

def dominate():
	pass

def to_array(string):
	nums = string.split()
	integers = [] #This is not necessary, python is dynamically typed
	
	for string_num in nums:
		integers.append(int(string_num))

	nums = []
	for i in range(0, len(integers)):
		if(i%2 != 0):
			nums.append([integers[i], integers[i-1]])

	return nums

if __name__ == '__main__':
	nums = input()

	nums_arr = to_array(nums)
	#twelve = [[0, 0], [0, 0], [0, 0], [0, 0]]
	#five = [[1, 1], [-1, -4], [1, 5], [2, 3]]
	#four = [[-5, -10], [20, 25], [30, 2], [-1, -40]]
	#print(brute(five))
	#print(brute(four))

	#print(dominate(0,twelve))
	print(dom(0,nums_arr))