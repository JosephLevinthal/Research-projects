senha= int(input("digite sua senha: "))
x1=senha//1 % 10
x2=senha//10%10
x3=senha//100%10
x4=senha//1000%10
var1= x1*2
var2=x2*3
var3=x3*4
var4=x4*5
soma= ((var1+var2+var3+var4)%11)
print(soma)
