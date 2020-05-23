import math
n = int(input())
somatorio = 1
cont = 1
if(n==1):
    print(round(somatorio,8))
else:
   while(1):
       somatorio += 1/math.factorial(cont)
       cont = cont + 1
       if(cont == n):
           break
print(round(somatorio,8))