'''
use List to store a heap: nums
'''

def parent(i):
	return (i-1)/2
def left(i):
	return 2*i+1
def right(i):
	return 2*(i+1)

def max_heapify(nums, pos, heapsize):
	'''
	contain a heap
	'''
	l = left(pos)
	r = right(pos)
	largest = pos
	if l < heapsize and nums[l] > nums[pos]:
		largest = l
	if r < heapsize and nums[r] > nums[largest]:
		largest = r
	if largest != pos:
		nums[pos], nums[largest] = nums[largest], nums[pos]
		max_heapify(nums, largest, heapsize)

def build_max_heap(nums):
	'''
	bulid a max heap
	'''
	for i in range((len(nums)-1)/2,-1,-1):
		max_heapify(nums, i, len(nums))

def heap_sort(nums):
	'''
	use a heap to sort
	'''
	build_max_heap(nums)
	heapsize = len(nums)
	for i in range(len(nums)-1,0,-1):
		nums[0], nums[i] = nums[i], nums[0]
		heapsize -= 1
		max_heapify(nums,0,heapsize)

def insert(nums, x):
	nums.append(-2172738173)
	increase_key(nums, len(nums)-1, x)

def maxinum(nums):
	return nums[0]

def extract_max(nums):
	if len(nums) < 0:
		print "error, heap underflow"
		return
	max_num = nums[0]
	nums[0] = nums[len(nums)-1]
	nums.pop()
	max_heapify(nums,0, len(nums))
	return max_num

def increase_key(nums, i, key):
	if key<nums[i]:
		print "error, new key is smaller than current key"
	nums[i] = key
	while i>0 and nums[parent(i)]<nums[i]:
		nums[i], nums[parent(i)] = nums[parent(i)], nums[i]
		i = parent(i)
		

if __name__ == '__main__':
	nums = [16,4,10,14,7,9,3,2,8,1]
	max_heapify(nums,1,len(nums))
	print nums

	nums = [12,34,2,5,7,23,8,9]
	heap_sort(nums)
	print nums

	nums = [12,34,2,5,7,23,8,9]
	build_max_heap(nums)
	print nums

	insert(nums, 15)
	print nums

	print extract_max(nums)
	print nums