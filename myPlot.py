import matplotlib.pyplot as plt

def myPlotter(a, b, c, z):
	xVar=[]
	yVar=[]
	x = -10
		
	while x < 10:
		yVar.append( ( a*pow(x,2) ) + ( b*x ) + c - z)
		xVar.append(x)
		x += 0.1

	#Plotting
	plt.plot(xVar, yVar)
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.xlim(min(xVar)-1,max(xVar)+1)
	plt.ylim(min(yVar)-1,max(yVar)+1)
	plt.axis([ int(min(xVar))-5, int(max(xVar))+5, int(min(yVar))-5, int(max(yVar))+5])
	plt.grid(True)
	plt.show()