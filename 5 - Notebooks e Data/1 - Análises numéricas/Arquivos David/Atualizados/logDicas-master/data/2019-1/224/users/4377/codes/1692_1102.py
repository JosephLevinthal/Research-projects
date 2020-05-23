#alturadotanque
al=float(input("H"))
#niveldecomb
n=float(input("n"))
#raio
r=float(input("r"))


from math import*
if(al and n and r>0):
	if(2*r >= al or n> al):
		print("Entradas:", al, ",", n , ",",r)
		print("Entradas invalidas")
	elif(n<r):
		v=( pi/3 * n ** 2) * (3* r -n)
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	elif(n==r):
		v=(4/3 * pi * r **3)/2
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	elif(r< n < (al-r)):
		l=n-r
		v=v=(4/3 * pi * r **3)/2 + pi*r**2*l
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	elif(n==(al-r)):
		l=n-r
		v=v=(4/3 * pi * r **3)/2 + pi*r**2*l
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	elif(n>(al-r)):
		w=al-n
		l=al-2*n
		ar=(pi/3*w**2)*(3*r-w)
		tot=4/3*pi*r**3+pi*r**2*l
		v=tot-ar
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	elif(n==al):
		l=al-2*r
		v=(4/3 *pi*r**3)+ pi*r**2*l
		v=v*1000
		print("Entradas:", al, ",", n , ",",r)
		print("Volume:", round(v,3), "litros")
	else:
		print("Entradas:", al, ",", n , ",",r)
		print("Entradas invalidas")
else:
	print("Entradas:", al, ",", n , ",",r)
	print("Entradas invalidas")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


		
		
		
		
		
		
		