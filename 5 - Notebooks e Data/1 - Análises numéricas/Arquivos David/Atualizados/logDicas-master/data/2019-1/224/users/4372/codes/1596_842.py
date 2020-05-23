num = int(input("Digite 4 numeros: "))
a = num//1000 
b = (num%1000)//100
c = (num%1000)%100//10
d = (num%1000)%100%10
print(a+b+c+d)