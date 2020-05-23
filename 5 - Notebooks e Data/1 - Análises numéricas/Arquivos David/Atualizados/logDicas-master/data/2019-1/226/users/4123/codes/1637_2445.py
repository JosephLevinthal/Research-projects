esc =  input()
temp = float(input())
if esc == "C":
	temp = (9*temp/5 + 32)
else:
	temp = 5/9*(temp-32)
print(round(temp,2))