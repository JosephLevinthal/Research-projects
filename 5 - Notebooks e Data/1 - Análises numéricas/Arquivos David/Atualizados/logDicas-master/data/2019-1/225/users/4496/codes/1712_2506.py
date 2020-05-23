qt = int(input())
pc = float(input())
qtv = int(input())

t = 0
while(qt < 12000 and qt > 0):
	qt = qt + ((qt * pc) / 100) - qtv
	t = t + 1
if(qt >= 200):
	print("LIMITE")
else:
	print("EXTINCAO")
print(t)