n=int(input("Digite um numero: "))
a= n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10		
soma=(((a*5 )+ (b*4) + (c*3) + (d*2 )) % 11)

print(abs(soma))