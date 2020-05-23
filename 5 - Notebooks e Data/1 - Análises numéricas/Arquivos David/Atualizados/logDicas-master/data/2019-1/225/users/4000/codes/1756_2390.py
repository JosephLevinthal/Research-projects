from numpy import*
p = array(eval(input("Digite os presentes")))
f = array(eval(input("Digite os faltantes")))
i = 0
c = 1
while(f[i]!= max(f)):
	i = i+1
	c = c+1
print(c)