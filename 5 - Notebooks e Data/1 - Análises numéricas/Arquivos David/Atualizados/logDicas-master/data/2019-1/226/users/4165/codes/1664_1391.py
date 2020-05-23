k = float(input("qual a quantidade de enegia utilizada: "))
baixa = float( 0.60 * k + 5.00 )
alta = float( 0.75 * k + 16.00)
if(k <= 150):
	print(round(baixa, 2))
else:
	print(round(alta, 2))