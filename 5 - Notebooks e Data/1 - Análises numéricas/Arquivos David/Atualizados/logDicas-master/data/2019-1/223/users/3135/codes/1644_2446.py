A=int(input("senha"))
b= A//100000
c=(A//10000)%10
d=(A//1000)%10
e=(A//100)%10
f=(A//10)%10
g=A%10
Cal1=c+e+g
Cal2=b+d+f
if(Cal1 % Cal2 !=0):
    print("senha invalida")
else:
    print("acesso liberado")