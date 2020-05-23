x = input('conta: ')

a = int(x[3])*2
b = int(x[2])*3
c = int(x[1])*4
d = int(x[0])*5

s = a + b + c + d
s = s%11

print(s)