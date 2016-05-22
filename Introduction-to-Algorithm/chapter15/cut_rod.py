'''
cur rod
'''

def cut_rob(p, n):
	'''
	:type p: List
	:type n: int
	:rtype: int
	'''
	res = -2147483648
	if n == 0:
		return 0

	for i in range(n):
		res = max(res, p[i]+cut_rob(p,n-1-i))
	return res

def memoized_cut_rod(p, n):
	r = [-2147483648]*n
	return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
	if r[n-1] >= 0:
		return r[n-1]
	if n==0:
		res = 0
	else:
		res = -2147483648
		for i in range(n):
			res = max(res,p[i]+memoized_cut_rod_aux(p, n-1-i, r))
	r[n-1] = res
	return res

def bottom_up_cut_rod(p, n):
	r = [0]*(n+1)
	r[0] = 0
	for j in range(1,n+1):
		res = -2147483648
		for i in range(1,j+1):
			res = max(res, p[i-1]+r[j-i])
		r[j] = res
	return r[n]

def extended_bottom_up_cut_rod(p, n):
	r = [0]*(n+1)
	s = [0]*(n+1)
	for j in range(1, n+1):
		res = -2147483648
		for i in range(1, j+1):
			if res < p[i-1]+r[j-i]:
				res = p[i-1] + r[j-i]
				s[j] = i
		r[j] = res
	return r, s 

def print_cut_rob_solution(p, n):
	r, s = extended_bottom_up_cut_rod(p, n)
	print r[n],":",
	while n>0:
		print s[n],
		n = n - s[n]

if __name__ == '__main__':
	p = [1,5,8,9,10,17,17,20,24,30]
	print cut_rob(p, 8)
	print memoized_cut_rod(p, 8)
	print bottom_up_cut_rod(p, 8)
	print_cut_rob_solution(p, 7)