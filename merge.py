def merge(arr):

	if (arr == None or len(arr) < 2):
		return arr

	elif (len(arr) == 2):
		if arr[0] > arr[1]:
			return [arr[1], arr[0]]
		else:
			return [arr[0], arr[1]]
	else:
		right = merge(arr[0:len(arr)//2])
		left =  merge(arr[len(arr)//2:])
		out = []

		r = 0
		l = 0
		re = len(right)
		le = len(left)

		while(r < re and l < le):
			if( right[r] > left[l]):
				out.append(left[l])
				l+=1
			else:
				out.append(right[r])
				r+=1

		#Copy remaining elements (One of these loops wont run)
		while(r < re):
			out.append(right[r])
			r+=1

		while(l < le):
			out.append(left[l])
			l+=1

		return out

if __name__ == '__main__':
	arr = [3,2,3,1]#[2, 1, 6, 0, 4, 5, 9, 7, 8, 11]
	print("Input => "+str(arr))
	print("Output => "+ str(merge(arr)))