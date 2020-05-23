digito = int(input())
d4 = digito//1000
d3 = (digito%1000)//100
d2 = (digito%100)//10
d1 = digito%10
dgt_ver = (5*d4 + 4*d3 + 3*d2 + 2*d1)%11
print(dgt_ver)
