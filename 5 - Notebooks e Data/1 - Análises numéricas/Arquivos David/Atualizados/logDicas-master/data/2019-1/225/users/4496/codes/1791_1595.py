from numpy import*
notas = array(eval(input("notas: ")))

a = max(notas)
b = min(notas)
c = size(notas)
d = sum(notas[-b])

print(round(sum(d/c),2))