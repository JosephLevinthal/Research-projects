x=int(input("digite quatro digios:   "))
y=x//10
c=x%10
q=y%10
p=y%100
h=p//10
t=y//100
c=c*2
q=q*3
h=h*4
t=t*5
r=(c+q+h+t)%11
print(r)