A=int(input("Numero de habitantes de uma cidade A: "))
B=int(input("Numero de habitantes de uma cidade B: "))
a=float(input("Percentual de crescimento populacional da cidade A: "))
b=float(input("Percentual de crescimento populacional da cidade B: "))

x=A
y=B
n=0
s=a/100
d=b/100

while(x<y):
	o = x * s 
	i = y * d
	x = x + o
	y = y + i
	n = n+1
print(n)