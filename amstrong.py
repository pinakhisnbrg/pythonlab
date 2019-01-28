# Name :Pinak
# Div. : P
''' write a code to find if user entered number is amstrong number'''
x=int(input("enter a number "))
y=input("enter number (taken as string) ")
e=int(x[0])**3
f=int(x[1])**3
g=int(x[2])**3
q=e+f+g

q1=x//100
r1=x%100
q2=r1//10
r2=r1%10
z=(q1**3)+(q2**3)+(r2**3)
if x==z:
	print("Amstrong number")
else :
	print("Not an Amstrong number")
if y==q:
	print ('y')
else:
	print('n')


