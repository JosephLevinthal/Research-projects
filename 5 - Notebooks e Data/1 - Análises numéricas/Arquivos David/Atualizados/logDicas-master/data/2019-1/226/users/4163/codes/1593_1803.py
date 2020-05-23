x = int(input("numero do cartao: "))

a = x//1000
b = x//100%10
c = x//10%10
d = x%10

m = a * 5
n = b*4
o = c*3
p = d*2
s= m+n+o+p 
v = (s%11)  
print(v)
