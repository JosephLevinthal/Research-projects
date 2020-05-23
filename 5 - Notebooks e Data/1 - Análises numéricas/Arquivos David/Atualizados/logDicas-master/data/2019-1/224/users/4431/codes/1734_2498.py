x=float(input("Digite os habitantes da cidade A: "))
y=float(input("Digite os habitantes da cidade B: "))
z=float(input("Percentual de crescimento populacional de A: "))
h=float(input("Percentual de cresicmento populaciona de B: "))
z=z/100
h=h/100
k=0
while(x<y):
		x=(x*z)+x
		y=(y*h)+y
		k=k+1
print(k)