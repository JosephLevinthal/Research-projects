from numpy import*
n = array(eval(input("digite a glicose: ")))
i = 0 
j = 0
while(i<size(n)):
	if (n[i]>99):
		print(i)
		i = i +1
		j = j + 1
	else: 
		i = i + 1
print(j)