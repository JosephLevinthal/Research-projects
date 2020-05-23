a=int(input("numero1:"))
b=int(input("numero2:"))
c=int(input("numero3:"))
if(a>b and a>c):
	maior=a
if(b>a and b>c):
	maior=b
if(c>a and c>b):
	maior=c
print(maior)