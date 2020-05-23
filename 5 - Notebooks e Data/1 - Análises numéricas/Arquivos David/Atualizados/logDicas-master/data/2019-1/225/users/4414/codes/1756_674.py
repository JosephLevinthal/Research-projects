from numpy import*

v=array(eval(input("v:")))

print(size(v))
print(v[0])
print(v[-1])
print(max(v))
print(min(v))
print(sum(v))

j=sum(v)/size(v)
print(round(j, 2))