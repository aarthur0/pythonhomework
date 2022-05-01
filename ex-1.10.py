def ackermann(x, y):
	if y == 0:
		return 0
	elif x == 0:
		return 2 * y
	elif y == 1:
		return 2
	else:
		return ackermann(x - 1, ackermann(x, y - 1))
def a1(n):
	return ackermann(0, n)# returns 2*n
def a2(n):
	return ackermann(1, n)#returns 2*ackermann(1, n - 1))
# ackermann(1, n - 1) returns the same until n-1 is 1 and the final result is 2**n 
def a3(n):#returns ackermann(1,ackermann(1.n-1))
	#-->ackermann(0,ackermann(1,ackermann(1.n-1)-1 )) and so on
	return ackermann(2, n)
print(a1(5),a2(5),a3(4))
