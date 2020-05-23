conta = int(input("digite a conta"))
a = (conta//1000)*5 
b = ((conta//100)%10)*4
c = (((conta//10)%100)%10)*3
d = ((conta%100)%10)*2
e = (a+b+c+d)%11

print(int(e))
