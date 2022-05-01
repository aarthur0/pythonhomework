#((m / (n ** 2)) + (2 * n)) / 3
def cube_root(k):
	croot=1
	while not wellguessed(croot,k):
		croot=improve(croot,k)
	return croot
def wellguessed(a,b):
	if abs(a**3-b)<0.00001:
		return True
	else:
		return False
def improve(m,n):
	return ((m / (n ** 2)) + (2 * n)) / 3
print(cube_root(8))
