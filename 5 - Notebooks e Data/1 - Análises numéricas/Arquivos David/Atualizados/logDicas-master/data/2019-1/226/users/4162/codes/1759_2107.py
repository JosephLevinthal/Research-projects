from numpy import*
st=input("insira sua string: ").upper()
a=st.count("A")
e=st.count("E")
i=st.count("I")
o=st.count("O")
u=st.count("U")
r=a+e+i+o+u
s=len(st)
print(r)
print(s-r)
