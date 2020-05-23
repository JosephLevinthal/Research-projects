nhab1=int(input("numero de habitantes:"))
nhab2=int(input("numero de habitantes:"))
cre1=float(input("crescimento populacional:"))
cre2=float(input("crescimento populacional:"))

while(nhab1>=nhab2):
	cont=1
	nhab1=nhab1+(nhab1*(cre1/100))
	nhab2=nhab2+(nhab2*(cre2/100))
	
print(cont)