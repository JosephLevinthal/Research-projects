i1D=float(input())
i1d=float(input())
i2D=float(input())
i2d=float(input())
i3D=float(input())
i3d=float(input())

face1=(i1D/i1d)
face2=(i2D/i2d)
face3=(i3D/i3d)

a=abs(face1-face2)
b=abs(face1-face3)
c=abs(face2-face3)
if(c<b and c<a):
	print("2 e 3 ")
elif(b<a and b<c):
	print("1 e 3 ")
elif(a<b and a<c):
	print("1 e 2")

