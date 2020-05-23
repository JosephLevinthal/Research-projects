var1 = int(input("digite um numero de 4 digitos"))
p1= var1//1000
p2= (var1 - p1*1000)//100
p3= (var1 -(p1*1000+p2*100))//10
p4 =(var1%1000) - (p2*100+p3*10)
resultado = (p1*5 + p2*4 + p3*3 +p4*2)%11
print(resultado)