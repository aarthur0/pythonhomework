#recutsion
def f(n):
	if n<3:
		return n
	else:
		return f(n-1)+f(n-2)+f(n-3)
#tail recursion
def f1(n1,k):
	k=n1
	if n1<3:
		return k
	else:
		return f1(n1,(3*k-6))
print(f(5))