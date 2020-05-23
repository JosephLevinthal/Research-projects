n = int(input("Insira um numero inteiro: "))

i = 0
d = 0
while(i < n):
	i = i + 1
	if((n%i) == 0):
		print(i)
		d = d + 1
if(d == 1):
	print("1 divisor")
else:
	print(d, "divisores")