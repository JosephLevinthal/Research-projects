y=int(input("Digite 4 numeros:"))
x=(y//1000)%10
t=(y//100)%10
z=(y//10)%10
u=y%10
k=u*2+z*3+t*4+x*5
r=k%11
print(r)