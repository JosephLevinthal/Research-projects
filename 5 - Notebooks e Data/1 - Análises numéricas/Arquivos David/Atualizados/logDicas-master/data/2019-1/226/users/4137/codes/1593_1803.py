n1 = int(input("Numero da conta:"))
n2 = n1%10 #quarto numero da conta
d1= n1//10
dd = d1%10 #terceiro numero da conta
d2= n1//100
dd1 = d2%10 #segundo numero da conta
d3 = n1//1000
dd2 = d3%10 #primeiro numero da conta
n3 = n2*2
n4 = dd*3
n5 = dd1*4
n6 = dd2*5
dig = n3+n4+n5+n6
digv = dig%11
print(digv)