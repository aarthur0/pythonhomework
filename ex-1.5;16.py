def sum1(a,b):
	if(a<b):
		s1=a
		while a<b:
			s1=s1+(a+1)
			a+=1
		return s1
	elif(a>b):
		s2=b
		while(b<a):
			s2=s2+(b+1)
			b+=1
		return s2
	else:
		return a

