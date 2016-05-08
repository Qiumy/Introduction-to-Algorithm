'''
quick sort
randomized partition & partition
'''
import random

def quick_sort(nums, p, r):
	if p<r:
		q = partition(nums, p, r)
		quick_sort(nums, p, q-1)
		quick_sort(nums, q+1, r)

def partition(nums, p, r):
	x = nums[r]
	i = p-1
	for j in range(p, r):
		if nums[j] <= x:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[i+1], nums[r] = nums[r], nums[i+1]
	return i+1

def randomoized_quicksort(nums, p, r):
	if p<r:
		q = randomoized_partition(nums, p, r)
		randomoized_quicksort(nums, p, q-1)
		randomoized_quicksort(nums, q+1, r)

def randomoized_partition(nums, p, r):
	i = random.randint(p,r)
	nums[i], nums[r] = nums[r], nums[i]
	return partition(nums, p, r)

def tail_recursive_quicksort(nums, p, r):
	while p<r:
		# partition and sort left subarray
		q = partition(nums, p, r)
		tail_recursive_quicksort(nums, p, q-1)
		p = q+1

if __name__ == '__main__':
	nums = [random.randint(-34,40) for _ in range(20)]
	# nums = [3,4,23,12,3,6,7]
	print nums
	# quick_sort(nums,0,len(nums)-1)
	# randomoized_quicksort(nums, 0, len(nums)-1)
	tail_recursive_quicksort(nums, 0, len(nums)-1)
	print nums
