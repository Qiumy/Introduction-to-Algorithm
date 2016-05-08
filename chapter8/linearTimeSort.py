'''
linear time sort O(n)
'''
import random

def counting_sort(nums, k):
	'''
	sort nums and the output is res
	the samples of the nums are between 0 to k
	:type nums: list
	:type k: int
	:rtype: list
	'''
	res = [0]*len(nums)
	tmp = [0]*(k+1)
	for i in range(0, len(nums)):
		tmp[nums[i]] = tmp[nums[i]] + 1

	# tmp array now contains the number of elements equal to i
	for i in range(1, k+1):
		tmp[i] = tmp[i] + tmp[i-1]

	# tmp array now contains the number of element less than or equal to i
	for i in range(len(nums)-1, -1, -1):
		res[tmp[nums[i]]-1] = nums[i]
		tmp[nums[i]] = tmp[nums[i]] - 1

	return res

def radix_sort(nums, d):
	'''
	use a stable sort to sort array nums on digit i
	'''
	res = nums
	for i in range(d-1, -1, -1):
		res = sorted(res, key=lambda num: str(num)[i])
		# print "---", res
	return res

def bucket_sort(nums):
	'''
	the samples of the nums are belong [0,1)
	'''
	n = len(nums)
	res = [[] for _ in range(n)]
	ans = []
	for i in range(0, n):
		res[int(nums[i]*10)].append(nums[i])

	for i in range(0, n):
		res[i].sort()
		ans.extend(res[i])
	return ans

if __name__ == '__main__':
	nums = [random.randint(0,10) for _ in range(10)]
	print nums
	print counting_sort(nums, 10)

	nums = [random.randint(100,900) for _ in range(10)]
	print nums
	print radix_sort(nums,3)

	nums = [random.random() for _ in range(10)]
	print bucket_sort(nums)
