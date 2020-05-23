from numpy import*

x =  array(eval(input("Digite seu vetor")))

print(size(x))
print(x[0])
print(x[-1])
print(max(x))
print(min(x))
print(sum(x))
print(round(sum(x)/size(x), 2))