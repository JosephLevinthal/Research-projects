a = int(input())
b = int(input())
x = float(input())
y = float(input())

ac = x /100
bc = y/100

ano = 0

while (a<b):
	a = a +(a*ac)
	b = b +(b*bc)
	ano = ano +1
	
print(ano)