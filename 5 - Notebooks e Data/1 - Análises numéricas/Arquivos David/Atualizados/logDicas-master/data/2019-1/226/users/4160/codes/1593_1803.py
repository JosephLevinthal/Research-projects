x = int(input(" Digite um numero de quatro digitos: "))
a = x // 1000 
b= a * 5 
c = (x // 100 - (a *10)) * 4
d = (x // 10 - (x // 100) * 10) * 3
e = (x - (x // 10) * 10) * 2 

soma = b + c + d + e    
print(soma % 11)