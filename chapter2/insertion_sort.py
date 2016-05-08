import random
def insertion_sort1(nums):
	'''
	:type nums: List
	:rtype: List
	'''
	for j in range(1,len(nums)):
		key = nums[j]
		i = j-1
		while i>=0 and nums[i] > key:
			nums[i+1] = nums[i]
			i = i - 1
		nums[i+1] = key
	return nums

def insertion_sort2(nums):
	'''
	:type nums: List
	:rtype: List
	'''
	for j in range(1,len(nums)):
		key = nums[j]
		i = j-1
		while i>=0 and nums[i] < key:
			nums[i+1] = nums[i]
			i = i - 1
		nums[i+1] = key
	return nums

if __name__ == '__main__':
	nums = [random.randint(0,99) for _ in range(10)]
	print nums
	print insertion_sort1(nums)
	print insertion_sort2(nums)