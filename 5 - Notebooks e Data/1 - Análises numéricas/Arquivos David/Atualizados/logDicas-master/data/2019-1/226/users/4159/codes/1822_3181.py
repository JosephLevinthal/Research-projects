from numpy import*
j = array(eval(input("ultima jogada: ")))
y = arange(37)
g = zeros(37, dtype = int)
for x in range(size(j)):
	for i in range(37):
		if(j[x]==y[i]):
			g[i] = g[i]+1		
print(g)
		
	
	