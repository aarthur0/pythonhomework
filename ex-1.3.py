def foo(a,b,c):
	if a==min(a,b,c):
		return (c**2+b**2)
	elif b==min(a,b,c):
		return (c**2+a**2)
	else:
		return (a**2+b**2)
