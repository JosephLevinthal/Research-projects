x=input("digite uma string: ").upper()
t=(len(x))
a=x.count("A",0,t)
b=x.count("E",0,t)
c=x.count("I",0,t)
e=x.count("O",0,t)
d=x.count("U",0,t)
n=a+b+c+d+e
print(n)
print(t-n)