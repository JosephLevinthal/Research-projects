from numpy import*
v = array(eval(input("Notas: ")))

v1 = min(v)
v2 = size(v)
v3 = v2 - 1

v4 = sum(v)-min(v)
v5 = v4/v3
v6 = round(v5,2)

print(v6)