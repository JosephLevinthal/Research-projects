from math import*
v = int(input("vezes de repeticao: "))

soma = 3
i = 0
fim = v-1
while(i < fim):
	soma += 4*(((-1)**i)/((2*i+2)*((2*i)+3)*((2*i)+4)))
	i = i + 1

print(round(soma,8))