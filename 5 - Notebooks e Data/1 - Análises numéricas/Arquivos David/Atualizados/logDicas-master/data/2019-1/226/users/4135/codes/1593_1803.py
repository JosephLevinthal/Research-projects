d = int (input("Digite um numero com 4 digitos:"))
n1 = (d%10)*2
#print (n1)
N2 = d//10
n2 = (N2%10)*3
#print (n2)
N3 = d//100
n3 = (N3%10)*4
#print (n3)
N4 = d//1000
n4 = (N4%10)*5
#print (n4)
dig_ident = (n1+n2+n3+n4)%11
print (dig_ident)

