def inc(a):
	return a + 1
def dec(a):
	return a - 1
def add1(a, b):#recursive 
	if a == 0:
		return b
	else:
		return inc(add1(dec(a), b))
def add2(a, b):#tail recursion=> calls add2 and works with changed a and b
	if a == 0:
		return b
	else:
		return add2(dec(a), inc(b))
print(add1(4,5))
print(add2(4,5))