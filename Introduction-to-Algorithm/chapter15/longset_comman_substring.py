'''
longest comman substring
'''

def lcs_length(x, y):
	'''
	:type x: str
	:type y: str
	:rtype int
	'''
	m = len(x)
	n = len(y)
	b = [['0' for _ in range(n+1)] for _ in range(m+1)]
	c = [[0 for _ in range(n+1)] for _ in range(m+1)]

	for i in range(m+1):
		c[i][0] = 0
	for i in range(n+1):
		c[0][i] = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1]==y[j-1]:
				c[i][j] = c[i-1][j-1]+1
				b[i][j] = '2'
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = '1'
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = '3'
	return c, b

def print_lcs(b, x, i, j):
	if i==0 or j==0:
		return
	if b[i][j]=='2':
		print_lcs(b, x, i-1, j-1)
		print x[i-1],
	elif b[i][j]=='1':
		print_lcs(b, x, i-1, j)
	else:
		print_lcs(b, x, i, j-1)

if __name__ == '__main__':
	x = 'abcde'
	y = 'acde'
	c,b = lcs_length(x,y)
	print_lcs(b,x,len(x),len(y))


