qt = int(input())
pt = float(input())

t = 0

while(qt < 8000 and qt > 0):
	qv = int(input())
	qt = qt + ((qt * pt) / 100) - qv
	t = t + 1
	
if(qt >= 8000):
	print("MAXIMO")
elif(qt <= 0):
	print("ZERO")

print(t)