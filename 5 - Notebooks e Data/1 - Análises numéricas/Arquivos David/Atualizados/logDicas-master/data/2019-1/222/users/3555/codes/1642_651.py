alt = float(input())
sex = input()

h = ((72.7)*alt) - (58)
m = ((62.1)*alt) - (44.7)

if(sex == 'M'):
	print(round(h,2))
if(sex == 'F'):
	print(round(m,2))