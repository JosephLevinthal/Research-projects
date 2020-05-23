from numpy import*
t = array(eval(input("Digite o tempo: ")))
p = array(eval(input("Digite o percentual: ")))
i=0
g=0
while(i<size(t)):
	x = ((5*p[i])/100)
	g += (t[i])*x
	i= i+1
print(round(g,2))
	
	