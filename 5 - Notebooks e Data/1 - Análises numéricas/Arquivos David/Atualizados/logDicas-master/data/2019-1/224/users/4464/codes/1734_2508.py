n = int(input("Insira a quantidade de termos desejada para a serie: "))

pi = 3
i = 1

while(i < n):
	den = (i*2)*(i*2+1)*(i*2+2)
	pi = pi + (-1)**(i+1) * 4  / den
	i = i + 1
	
print(round(pi,8))