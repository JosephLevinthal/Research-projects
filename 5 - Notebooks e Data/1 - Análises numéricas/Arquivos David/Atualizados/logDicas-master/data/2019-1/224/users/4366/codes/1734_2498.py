a=int(input("digite um numero a:"))
b=int(input("digite um numero b:"))
A=float(input("digite um numero A:"))
B=float(input("digite um numero B:"))
tA=A/100
tB=B/100
anos=0
A=a
B=b
while(B>A):
	cresA=A*tA
	cresB=B*tB
	A=A+cresA
	B=B+cresB
	anos=anos+1
print(anos)