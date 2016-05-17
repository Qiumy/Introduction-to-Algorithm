'''
select the smallest ith sample of nums[p:r+1]
'''
import random

def partition(nums, p, r):
	x = nums[r]
	i = p-1
	for j in range(p, r):
		if nums[j] <= x:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[i+1], nums[r] = nums[r], nums[i+1]
	return i+1

def randomoized_partition(nums, p, r):
	i = random.randint(p,r)
	nums[i], nums[r] = nums[r], nums[i]
	return partition(nums, p, r)

def randomized_select(nums, p, r, i):
	if p==r:
		return nums[p]
	q = randomoized_partition(nums, p, r)
	k = q - p + 1
	if i==k:
		return nums[q]
	elif i<k:
		return randomized_select(nums, p, q-1, i)
	else:
		return randomized_select(nums, q+1, r, i-k)


if __name__ == '__main__':
	nums = [random.randint(0,99) for _ in range(10)]
	print sorted(nums)
	idx = random.randint(0, len(nums)-1)
	print idx, randomized_select(nums, 0, len(nums)-1, idx)