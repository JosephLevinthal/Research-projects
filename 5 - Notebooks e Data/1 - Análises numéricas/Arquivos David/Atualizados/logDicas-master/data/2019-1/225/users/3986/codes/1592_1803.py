A=int(input("numero de 4 digitos: ")) 
x= A // 1000
y= A % 1000
g= y // 100
h= y % 100
k= h // 10
j= h % 10
o= j // 1
 
l= (o * 2 + k * 3 + g * 4 + x * 5) %  11
print(l)