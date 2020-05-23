from numpy import*
v = array (eval(input("faltas:")))
a = zeros(6)
s = 0 
t = 0
q =0 
qui=0
sex=0
sab = 0 
for y in v :
	if( y ==2 ):
		s+=1 
	elif ( y==3):
		t+=1
	elif(y==4):
		q+=1
	elif(y==5):
		qui+=1
	elif(y==6):
		sex+=1
	elif(y==7):
		sab+=1
a[0]=round(s/size(v)*100,1)
a[1] = round(t/size(v)*100,1)
a[2]= round(q/size(v)*100,1)
a[3]= round(qui/size(v)*100,1)
a[4]= round(sex/size(v)*100,1)
a[5]=round(sab/size(v)*100,1)
print(a)