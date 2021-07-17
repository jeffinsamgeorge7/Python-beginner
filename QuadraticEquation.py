#Root of Quadriatic Equation
import math
print('enter a,b,c')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=(b*b)-(4*a*c)
r1=-b+math.sqrt(d)/2*a
r2=-b-math.sqrt(d)/2*a 
if d>>0:
    print('The roots are real and distinct')
    print(r1)
    print(r2)
elif d>>0:
    print('The roots are imaginary')
else:
    print('The roots are equal')