A=int(input("habitante da cidade A: "))
B=int(input("habitante da cidade B: "))
a=float(input("% da cidade A: "))
b=float(input("% da cidade B: "))
t=0
while(A<B):
	A=A+(A*(a/100))
	B=B+(B*(b/100))
	t=t+1
print(t)