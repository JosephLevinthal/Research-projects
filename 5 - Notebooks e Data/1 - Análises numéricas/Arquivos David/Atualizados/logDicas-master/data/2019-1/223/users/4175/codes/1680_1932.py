x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

f1 = round(x1/y1,2)
f2 = round(x2/y2,2)
f3 = round(x3/y3,2)

a = round(abs(f1-f2),2)
b = round(abs(f1-f3),2)
c = round(abs(f2-f3),2)
# a = 0,12 | 1,08 - 1,2
# b = 0,01 | 1,08 - 1,07
# c = 0,13 | 1,20 - 1,07

if a < b and a < c:
	print(1,"e",2)
if b < a and b < c:
	print(1,"e",3)
if c < a and c < b:
	print(2,"e",3)