var1=int(input())
a=(var1%10)
b=(var1//10)%10
c=((var1//10)//10)%10
d=(var1//1000)
var2=(a*2)+(b*3)+(c*4)+(d*5)
var3=var2%11
print(var3)
