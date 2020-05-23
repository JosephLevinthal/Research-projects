A = int(input("cidade A:"))
B = int(input("cidade B:"))
A1 = float(input("crescimento A:"))
B1 = float(input("crescimento B:"))

J1 = A1/100
J2 = B1/100
ano = 0

while(B > A):
	A = A + (A * J1) 
	B = B + (B * J2)
	ano = ano + 1

	
print(ano)