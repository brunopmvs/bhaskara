# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import messages

a = 0
b = 0
c = 0
z = 0


print(messages.instructions)

while True:   
    try:
        a = float(input(messages.inputA))
        break
    except ValueError:
        print(messages.notAnumberMessage)

while True:   
    try:
        b = float(input(messages.inputB))
        break
    except ValueError:
        print(messages.notAnumberMessage)

while True:   
    try:
        c = float(input(messages.inputC))
        break
    except ValueError:
        print(messages.notAnumberMessage)

while True:   
    try:
        z = float(input(messages.inputZ))
        break
    except ValueError:
        print(messages.notAnumberMessage)

c = c - z

delta = (math.pow(b,2)) - (4 * a * c)

if delta < 0 :
    print(messages.deltaNegative)
    print(messages.deltaLabel , delta)

else:
    pass

x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)

print(messages.x1Result, x1)
print(messages.x2Result, x2)
xVar=[]
yVar=[]
x = -10

while x < 10:
    yVar.append( ( a*pow(x,2) ) + ( b*x ) + c - z)
    xVar.append(x)
    x += 0.1

plt.plot(xVar, yVar)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(min(xVar)-1,max(xVar)+1)
plt.ylim(min(yVar)-1,max(yVar)+1)
#plt.axis([-10,10,-10,10])
plt.axis([ int(min(xVar))-5, int(max(xVar))+5, int(min(yVar))-5, int(max(yVar))+5])
plt.grid(True)
plt.show()
