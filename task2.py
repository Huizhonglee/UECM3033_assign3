import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def g(y,t):
	a=1.0
	b=0.2
	d=[a*(y[0]-y[0]*y[1]),b*(-y[1]+y[0]*y[1])]
	return d

y=np.array([0.10,1.0])                 
t=np.linspace(0, 5, 1000)
sol=sp.integrate.odeint(g,y,t)

#Plot graph of y0 and y1 against t
plt.plot(t,sol)
plt.plot(t, sol[:,0], label='prey y0', color="red")
plt.plot(t, sol[:,1], label='predator y1', color="blue")
plt.axis([0,5,0,1])
plt.xlabel('Year')
plt.ylabel('y')
plt.title('y0 and y1 against t (1)')
plt.legend(loc='best')
plt.grid()
plt.show()

#Plot graph of y1 against y0
plt.plot(sol[:,0], sol[:,1],label='Predator vs Prey')
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey(y0)')
plt.ylabel('Predator(y1)')
plt.title('Predator vs Prey (1)')
plt.legend(loc='best')
plt.grid()
plt.show()

#sensitivity with the initial conditon y0=0.11, y1=1.0
y=np.array([0.11,1.0])
t=np.linspace(0,5,1000) 
sol=sp.integrate.odeint(g,y,t)

#Plot graph of y0 and y1 against t
plt.plot(t,sol)
plt.plot(t, sol[:,0], label='prey y0', color="red")
plt.plot(t, sol[:,1], label='predator y1', color="blue")
plt.axis([0,5,0,1])
plt.xlabel('Year')
plt.ylabel('y')
plt.title('y0 and y1 against t (2)')
plt.legend(loc='best')
plt.grid()
plt.show()

#Plot graph of y1 against y0
plt.plot(sol[:,0],sol[:,1],label='Predator vs Prey')
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey(y0)')
plt.ylabel('Predator(y1)')
plt.title('Predator vs Prey(2)')
plt.legend(loc='best')
plt.grid()
plt.show()