x=int(input("quatro numero de digitos:"))
y=x//1000
z=(y%1000)//100
t=((z%1000)%100)//10
w=((t%1000)%100)%10
var1=(y*2)+(z*3)+(t*4)+(w*5)
var2=var1%11
print(var2)

