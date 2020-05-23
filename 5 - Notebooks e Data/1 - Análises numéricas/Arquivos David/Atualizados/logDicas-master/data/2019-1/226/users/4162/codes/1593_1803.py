num=int(input("insira sua conta: "))
a= num//1 % 10
b=num//10%10
c= num//100%10
d=num//1000%10
cal=a*2+b*3+c*4+d*5
result=cal%11
print(result)
print(a,b,c,d)