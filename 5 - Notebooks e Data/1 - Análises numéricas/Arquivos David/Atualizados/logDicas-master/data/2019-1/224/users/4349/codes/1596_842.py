entrada= int(input("numero de quatro digitos: "))
a= int(entrada//1000%100%10)
b= int(entrada//100%10)
c= int(entrada//10%10)
d= int(entrada%10)
somadosdigitos= a+b+c+d
print(somadosdigitos)
