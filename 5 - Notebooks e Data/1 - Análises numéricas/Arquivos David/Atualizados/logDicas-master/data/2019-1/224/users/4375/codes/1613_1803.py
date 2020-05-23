num = int(input("Digite 4 digitos: "))
a = (num//1000) * 5 
b = ((num%1000)//100) * 4 
c = ((num%1000)%100//10) * 3 
d = ((num%1000)%100%10) * 2
dv = (a + b + c + d) % 11
print(dv)