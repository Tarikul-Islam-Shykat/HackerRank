N=input()
h=int(int(N)//3600)
h1=int(int(N)-(h*3600))
m=int(h1/60)
m1=int(h1-(m*60))
print(str(h)+':'+str(m)+':'+str(m1))
