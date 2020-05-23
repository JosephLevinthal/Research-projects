n = int(input("Digite o numero: "))
n1 = n//1%10
n2 = n//10%10
n3 = n//100%10
n4 = n//1000%10
var = n1*2
var2 = n2*3 
var3 = n3*4
var4 = n4*5
res = (var + var2 + var3 + var4)%11
print(res)