from numpy import*
a = input("Digite um palavra meu consagrado:").lower()

a1 = a.count("a")
e = a.count("e")
i = a.count("i")
o = a.count("o")
u = a.count("u")
I = 0
C = 0 
while(I < len(a)):
	if(a[I] != a1 or e or i or o or u):
		C = C+1
	I = I + 1
print(a1+e+i+o+u)
print(C-(a1+e+i+o+u))