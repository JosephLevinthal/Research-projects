code = int(input("codigo: "))

e = code % 10
d = (code // 10) % 10 
o = ((code // 10) // 10) % 10
c = (((code // 10) // 10) // 10) % 10 

s = (e * 2) + (d * 3) + (o * 4) + (c * 5)
dgt = s % 11

print(dgt)