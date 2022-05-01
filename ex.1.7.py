def pow1(a,b):
	if(b>0):
		k=1
		c=0
		while c<b:
			k=k*a
			c+=1
		return k
	elif(b<0):
		b=-b
		k=1
		c=0
		while c<b:
			k=k*a
			c+=1
		return 1/(a**b)
	elif(b==0):
		return 1
	elif(a==0 and b<0):
		return False
