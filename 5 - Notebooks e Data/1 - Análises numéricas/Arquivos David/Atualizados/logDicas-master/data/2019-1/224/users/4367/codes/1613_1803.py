n= int(input("numero de quatro digitos"))
n1= n//1000%100%10
n2= n//100%10
n3= n//10%10
n4= n%10

soma= (n4*2)+(n3*3)+(n2*4)+(n1*5)
divisao= soma%11
print(divisao)