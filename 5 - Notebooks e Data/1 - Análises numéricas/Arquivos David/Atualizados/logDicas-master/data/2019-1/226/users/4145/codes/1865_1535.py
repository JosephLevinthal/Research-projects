x= float(input("numero real: "))
k = int(input("repeticoes: "))
i=1
j=0
arc=0
while(j < k):
	arc =((x**i)/i)*((-1)**j) + arc
	i = i+2
	j=j+1
	
print(round(arc,6))
