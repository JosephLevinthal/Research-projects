x=int(input("Digite um numero inteiro de 4 digito: "))
y=x//1000
z=(x//100)%10
c=(x//10)%10
t=x%10
r=((y*5)+(z*4)+(c*3)+(t*2))%11
print(r)
