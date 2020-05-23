do1 = float(input())
dq1 = float(input())
do2 = float(input())
dq2 = float(input())
do3 = float(input())
dq3 = float(input())
p1 = do1/dq1
p2 = do2/dq2
p3 = do3/dq3

if abs(p1-p3)<abs(p2-p3) and abs(p1-p3)<abs(p2-p1):
	print("1 e 3")
elif abs(p2-p3)<abs(p2-p1) and abs(p2-p3)<abs(p3-p1):
	print("2 e 3")
else:
	print("1 e 2")