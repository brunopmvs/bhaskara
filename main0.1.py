# -*- coding: utf-8 -*-
import myPlot
import math
import messages

def askValue(msgInput, msgError):
    while True:   
        try:
            var = float(input(msgInput))
            break
        except ValueError:
            print(msgError)
    return(var)

print(messages.instructions)

a = askValue(messages.inputA, messages.notAnumberMessage)
b = askValue(messages.inputB, messages.notAnumberMessage)
c = askValue(messages.inputC, messages.notAnumberMessage) 
z = askValue(messages.inputZ, messages.notAnumberMessage)
c -= z

delta = (math.pow(b,2)) - (4 * a * c)

if delta < 0 :
    print(messages.deltaNegative)
    print(messages.deltaLabel , delta)
    
else:
	x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
	x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
	print(messages.x1Label, x1)
	print(messages.x2Label, x2)

myPlot.myPlotter(a, b, c, z)




