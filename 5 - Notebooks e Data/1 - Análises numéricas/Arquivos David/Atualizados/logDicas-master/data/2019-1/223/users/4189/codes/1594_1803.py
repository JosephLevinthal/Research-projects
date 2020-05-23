a = int(input("a:"))

a1 = a//1000
a2 = (a//100)%10
a3 = (a//10)%10
a4 =  a%10

s1= a1*5
s2= a2*4
s3=a3*3
s4=a4*2

soma = (s1+s2+s3+s4)%11
print(soma)