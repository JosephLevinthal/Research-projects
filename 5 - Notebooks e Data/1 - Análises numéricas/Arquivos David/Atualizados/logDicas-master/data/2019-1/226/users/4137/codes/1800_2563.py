from numpy import*

n = array(eval(input("Notas:")))

while(size(n)>1):
	soma = 0
	for i in n:
		if(i >= 5 and i < 7):
			soma = soma + 1
	n = array(eval(input("Notas:")))
	print(soma)