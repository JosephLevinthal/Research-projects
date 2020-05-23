from numpy import*
o=input("string com sigla de origem das pessoas separdas por virgula: ").split(',')
ac= 0
am=0
pa=0
ro=0
rr=0
np=0
for ch in o:
	if ch=="AC":
		ac= ac + 1
		
	elif ch == "AM":
		am= am + 1
		
	elif ch== "PA":
		pa= pa +1
		
	elif ch== "RO":
		ro= ro + 1
	
	elif ch== "RR":
		rr= rr + 1
		
vo=zeros(5, dtype=int)
vo[0]=ac
vo[1]=am
vo[2]=pa
vo[3]=ro
vo[4]=rr
print(max(vo))
print(vo)