# Name : Pinak
# Div. : P
''' Find if entered number is a palindrome'''
x=int(input("Enter a number "))
q1=x//100
r1=x%100
q2=r1//10
r2=r1%10
z=(r2*100)+(q2*10)+(q1)
if x==z :
	print x, " is a palindrome"
else :
	print x, " is not a palindrome"


