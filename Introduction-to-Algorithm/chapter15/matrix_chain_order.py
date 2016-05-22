'''
matrix chain order
'''
def matrix_chain_prder(p):
	n = len(p)-1
	m = [[0 for _ in range(n+1)] for _ in range(n+1)]
	s = [[0 for _ in range(n+1)] for _ in range(n+1)]

	for l in range(2, n+1):
		for i in range(1, n-l+2):
			j = i+l-1
			m[i][j] = 2147483647
			for k in range(i, j):
				res = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
				if res < m[i][j]:
					m[i][j] = res
					s[i][j] = k
	return m, s

def print_optimal_parens(s, i, j):
	if i==j:
		print "A"+str(i),
	else:
		print "(",
		print_optimal_parens(s,i, s[i][j])
		print_optimal_parens(s,s[i][j]+1,j)
		print ")",

def recursive_matrix_chain(p, i, j):
	if i==j:
		return 0
	m[i][j] = 2147483647
	for k in range(i, j):
		res = recursive_matrix_chain(p,i,k)+recursive_matrix_chain(p,k+1,j)+p[i-1]*p[k]*p[j]
		if res < m[i][j]:
			m[i][j] = res
	return m[i][j]

def print_recursive_matrix_chain(p, i, j):
	n = len(p) - 1
	m = [[0 for _ in range(n+1)] for _ in range(n+1)]
	print recursive_matrix_chain(p, i, j)

def memoized_martix_chain(p):
	n = len(p)-1
	m = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(1, n+1):
		for j in range(i, n+1):
			m[i][j] = 2147483647
	return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
	if m[i][j] < 2147483647:
		return m[i][j]
	if i==j:
		m[i][j] = 0
	else:
		for k in range(i, j):
			res = lookup_chain(m, p, i, k) + \
			lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
			if res < m[i][j]:
				m[i][j] = res
	return m[i][j]

if __name__ == '__main__':
	p = [30, 35, 15, 5, 10, 20, 25]
	m, s = matrix_chain_prder(p)
	print m[1][6]
	print_optimal_parens(s,1,6)
	print
	print_recursive_matrix_chain(p, 1, 6)
	print memoized_martix_chain(p)