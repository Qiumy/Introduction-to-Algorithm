import random

def merge_sort(nums):
	'''
	:type nums: List
	:rtype : List
	'''
	if len(nums) <= 1:
		return nums
	mid = len(nums)/2
	left = merge_sort(nums[:mid])
	right = merge_sort(nums[mid:])

	return merge(left,right)

def merge(left, right):
	result = []
	i, j = 0, 0
	while i<len(left) and j<len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

if __name__ == '__main__':
	nums = [random.randint(0,99) for _ in range(10)]
	print nums
	print merge_sort(nums)