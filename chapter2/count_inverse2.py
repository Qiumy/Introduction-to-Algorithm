import random

def count_inverse(nums):
	'''
	:type nums: List
	:rtype : int
	'''
	if len(nums) <= 1:
		return 0
	mid = len(nums)/2

	left = nums[:mid]
	right  = nums[mid:]
	merge(left,right)
	cnt1 = count_inverse(left)
	cnt2 = count_inverse(right)

	return cnt1 + cnt2 + merge(left,right)

def merge(left, right):
	i, j = 0, 0
	count = 0
	result = []
	len_l = len(left)
	len_r = len(right)
	while i<len(left) and j<len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			count += len_l - i
	result += left[i:]
	result += right[j:]
	return count

if __name__ == '__main__':
	# nums = [random.randint(0,99) for _ in range(5)]
	nums = [8, 2, 3, 6, 1, 9, 5] 
	print nums
	print count_inverse(nums)
	print nums