s=int(input('Enter time in seconds '))
d=s//86400
r=s%86400
h=r//3600
r2=r%3600
m=r2//60
r3=r2%60
s=r3
print(s,' seconds is')
print( d,' days', h,' hrs', m,' mins', r3,' secs')
