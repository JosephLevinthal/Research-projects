from numpy import*
v = array(eval(input("matrix: ")))
if(shape(v)[0]==3 and shape(v)[1]==3):
	n = zeros(3)
	x = 0
	for i in range(3):
		for j in range(3):
			if(j>i):
				n[x]=v[i,j]
				x=x+1
	r = sum(n)
	print(round(r, 2))
			
			
		
		
