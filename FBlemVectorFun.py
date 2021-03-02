import numpy as n
import math

#(s)
def mag(vec):
    x = vec[0]
    y = vec[1]
    
    return math.sqrt(x**2 + y**2)

#(t)
def unit(vec):
    x = vec[0]
    y = vec[1]
    m = mag(vec)
    
    return n.array([x/m, y/m])

#(u)
def rot90(vec):
    x = vec[0]
    y = vec[1]
    
    return n.array([-y, x])

a = n.array([3, 2])
b = n.array([8, 7])
c = n.array([1, 5])

#(v)
print(2*a)
#(w)
print(a+b-c)
#(x)
#(y)
print(n.dot(a, a))
print(mag(a)*mag(a))
#(z)
print(n.dot(a, b))
print(mag(a)*mag(b))
#(æ)
a90 = rot90(a)
print(n.dot(a, a90))