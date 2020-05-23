from numpy import*
v1= array(eval(input("qual a quantidade de presentes?")))
v2= array(eval(input("qual a quantidade de faltantes?")))
i=0
mes=1

while (v1[i]!=max(v1)):
	i=i+1
	mes=mes+1
print(mes)
