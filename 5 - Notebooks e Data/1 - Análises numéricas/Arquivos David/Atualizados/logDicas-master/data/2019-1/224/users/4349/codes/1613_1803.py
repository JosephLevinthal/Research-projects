a= int(input("numero de quatro digitos: "))
w= (a//1000)
f= (a//100)%10
j= (a//10)%10
s= (a//1)%10
x= (s*2 + j* 3 + f*4 + w*5)%11

print(x)