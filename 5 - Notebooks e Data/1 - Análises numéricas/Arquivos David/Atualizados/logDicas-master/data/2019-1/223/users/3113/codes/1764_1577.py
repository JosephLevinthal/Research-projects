from numpy import*
a=array(eval(input("")))
vo=float(input(""))
n=int(input(""))
s=arange(n)
t=zeros(n)
d=((a*s**2)/2)+vo*s

print(d)