n = int(input("Quantidade de termos desejada na serie: "))

pi = (4/1)
den = 1

while(den < n):
	pi = pi + (-1)**den * 4/(den*2+1)
	den = den + 1
	
print(round(pi,8))