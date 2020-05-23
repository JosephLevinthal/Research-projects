num=int(input("digite o numero: "))
i=0
p=0
q=0
while(num!=0):
	i= i +1
	if (num%2==0):
		p= num/100 * i
	else:
		q= num/100 * i
print(round(p, 2))
print(round(q, 2))