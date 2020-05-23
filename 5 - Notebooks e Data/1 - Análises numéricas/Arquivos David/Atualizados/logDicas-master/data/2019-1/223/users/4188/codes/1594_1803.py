a=int(input("digite os quatros numeros: "))
b= a//1000
c=(a//100)%10
d=(a//10)%10
e=a%10
s=(b*5 + c*4 +d*3 + e*2)%11
print(abs(s))
