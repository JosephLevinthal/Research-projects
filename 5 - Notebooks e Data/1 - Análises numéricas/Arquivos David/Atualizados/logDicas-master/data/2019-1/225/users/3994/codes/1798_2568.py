n = int(input("Digite os numeros: "))
for i in range(n,0,-1):
	#print(i)
	#if i/2 == n:
	#	print(2*i* "*")	
	#else:
		#print(n - i)
		s = i*'*' + 2*(n-i)*"o"+i*'*'
		print(s)
	#v = n - i/2