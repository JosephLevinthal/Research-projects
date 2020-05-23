A=int(input("numero de habitabtes de um cidade A: "))
B=int(input("numero de habitabtes de um cidade B: "))
p=float(input("percentual de crescimento populacional A: "))
t=float(input("percentual de crescimento populacional B: "))

CO = 0    #contadora
while(A<B):
	A = A+(A*(p/100))
	B = B+(B*(t/100))
	CO=CO+1
print(CO)
