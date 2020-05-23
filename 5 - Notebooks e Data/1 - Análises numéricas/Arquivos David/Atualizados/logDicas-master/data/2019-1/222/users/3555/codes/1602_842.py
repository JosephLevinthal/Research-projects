i=int(input())
a=i
n1=a//1000
a = a%1000
n2 = a // 100
a = a%100
n3 = a// 10
a = a%10
n4 = a//1

print(n1+n2+n3+n4)