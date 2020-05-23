m = float(input(" minutos:"))
if(m<=100):
 v=m*1.2
else:
 v=(m*1.4) + 25
print(round(v,2))