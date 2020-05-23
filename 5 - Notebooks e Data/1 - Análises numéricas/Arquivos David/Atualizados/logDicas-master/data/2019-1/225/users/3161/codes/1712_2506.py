qt = int(input())
pt = float(input())
qv = int(input())

t = 0

while(qt < 12000 and qt > 0):
	qt = qt + ((qt * pt) / 100) - qv
	t = t + 1
	
if(qt >= 12000): 
	print("LIMITE")
elif(qt <= 0):
	print("EXTINCAO")
	
print(t)