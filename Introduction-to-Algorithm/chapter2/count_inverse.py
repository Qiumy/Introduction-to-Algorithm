import random

def merge(left, right, nums, n): 
    '''
    :type nums: List
    :rtype : int
    ''' 
    cnt = cnt_l = cnt_r =0  
    count = 0 
    len_l = len(left)
    len_r = len(right)
    while cnt < n:  
        if cnt_l == len_l:  
            while cnt < n:  
                nums[cnt] = right[cnt_r]  
                cnt = cnt + 1  
                cnt_r = cnt_r + 1  
        elif cnt_r == len_r:  
            while cnt < n:  
                nums[cnt] = left[cnt_l]  
                cnt = cnt + 1  
                cnt_l = cnt_l + 1  
        else:  
            if left[cnt_l] > right[cnt_r]:  
                nums[cnt] = right[cnt_r]  
                count = count + len_l - cnt_l  
                cnt = cnt + 1  
                cnt_r = cnt_r + 1  
            else:  
                nums[cnt] = left[cnt_l]  
                cnt = cnt + 1  
                cnt_l = cnt_l + 1  
    return count  
  
def count_inverse(nums):  
    n = len(nums)  
    if n == 1: return 0  
    n1 = n/2  
    n2 = n - n1  
    left = nums[:n1]  
    right = nums[n1:]  
    count1 = count_inverse(left)  
    count2 = count_inverse(right)  
    count = count1 + count2 + merge(left, right, nums, n)  
    return count  

if __name__ == '__main__':
	nums = [random.randint(0,99) for _ in range(10)]
	# nums = [8, 2, 3, 6, 1, 9, 5]  #10
	print nums
	print count_inverse(nums)
	print nums