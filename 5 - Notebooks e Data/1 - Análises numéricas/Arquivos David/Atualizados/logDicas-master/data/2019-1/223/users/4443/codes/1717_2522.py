n = int(input("digite um numero inteiro positivo: "))

soma = 1.5
t = n

while(t >= 1):
	soma = ((t*soma)/(2*t+1))+1
	t = t-1
pi = 2*soma
print(round(pi, 10))