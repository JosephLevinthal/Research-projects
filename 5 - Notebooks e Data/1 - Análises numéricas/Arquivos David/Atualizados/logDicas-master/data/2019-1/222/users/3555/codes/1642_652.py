n = int(input())
if( 100 <= n <= 999):
	 ne = n%100
	 if( (n % ne) == 0 ):
	 	 print("SIM")
	 else:
		 print("NAO")