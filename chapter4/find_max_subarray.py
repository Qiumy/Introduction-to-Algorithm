import random

def max_subarray1(nums):
	max_sum = min(nums)
	left_idx, right_idx = 0, len(nums)

	for i in range(len(nums)):
		for j in range(i, len(nums)):
			tmp_sum = 0
			for k in range(i, j+1):
				tmp_sum += nums[k]
			if tmp_sum > max_sum:
				max_sum = tmp_sum
				left_idx = i
				right_idx = j
	return (left_idx, right_idx, max_sum)


def max_subarray2(nums,low,high):
	if low == high:
		return (low, high, nums[low])

	max_sum = min(nums)
	left_idx, right_idx = 0, len(nums)

	mid = (low+high)/2
	cross_low, cross_high = mid, mid

	left_max_sum = tmp_sum = 0
	for i in range(mid,low-1,-1):
		tmp_sum += nums[i]

		if tmp_sum > left_max_sum:
			cross_low = i
			left_max_sum = tmp_sum

	right_max_sum = tmp_sum = 0
	for i in range(mid+1, high+1):
		tmp_sum += nums[i]
		
		if tmp_sum > right_max_sum:
			cross_high = i
			right_max_sum = tmp_sum

	left_low, left_high, left_sum = max_subarray2(nums,low,mid)
	right_low, right_high, right_sum = max_subarray2(nums,mid+1,high)

	if left_sum >= left_max_sum+right_max_sum and left_sum >= right_sum:
		return (left_low, left_high, left_sum)
	elif right_sum >= left_max_sum+right_max_sum and right_sum >= left_sum:
		return (right_low, right_high, right_sum)
	else:
		return (cross_low, cross_high, left_max_sum+right_max_sum)

def max_subarray3(nums):
	max_so_far = max_ending_here = 0 if max(nums)>=0 else min(nums)
	left_idx, right_idx = 0, len(nums)-1
	left_tmp_idx, right_tmp_idx = left_idx, right_idx
	for i in range(0, len(nums)):
		if max_ending_here + nums[i] > nums[i]:
			right_tmp_idx = i
		else:
			left_tmp_idx = i
		max_ending_here = max(max_ending_here+nums[i], nums[i])
		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			left_idx = left_tmp_idx
			right_idx = right_tmp_idx
	return (left_idx, right_idx, max_so_far)

if __name__ == '__main__':
	for _ in range(1):
		# nums = [2,4,-3,5,6,-5,-7,3,4]
		nums = [random.randint(-99,99) for _ in range(10)]
		# nums = [99, 29, 53, -31, 34, -92, 82, 35, 43, 78]
		print nums
		print max_subarray1(nums)
		print max_subarray2(nums,0,9)
		print max_subarray3(nums)