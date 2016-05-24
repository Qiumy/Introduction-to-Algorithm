'''
kmp
'''

def getNext(str):
	'''
	:type str: str
	:rtype: List
	'''
	n = len(str)
	res = [0]*n
	k = -1
	res[0] = -1
	j = 0
	while j<n-1:
		if k==-1 or str[j]==str[k]:
			k += 1
			j += 1
			res[j] = k
		else:
			k = res[k]
	return res

def kmp(s, p, p_next):
	'''
	:type s: str
	:type p: str
	:type p_next: List
	:rtype int
	'''
	res = -1
	plen = len(p)
	slen = len(s)
	i, j = 0, 0
	while i<slen:
		if j==-1 or s[i]==p[j]:
			i += 1
			j += 1
		else:
			j = p_next[j]

		if j == plen:
			res = i - plen
			break
	return res

if __name__ == '__main__':
	p_next = getNext("abaabcabc")
	print kmp("babcdefgh", "cdef", p_next)