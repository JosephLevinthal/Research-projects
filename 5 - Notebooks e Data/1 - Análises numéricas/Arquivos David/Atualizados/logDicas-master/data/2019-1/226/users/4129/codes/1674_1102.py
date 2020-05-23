H = float(input("Altura do tanque: "))
h = float(input("nivel de combustivel: "))
r = float(input("raio: "))
			 
if((H < 0) or (h < 0) or (r < 0) or H < h or H < 2*r):
	print("Entradas:",H,',',h,',',r)
	print("Entradas invalidas")

			 
			 
			 