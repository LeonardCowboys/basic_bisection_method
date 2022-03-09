import numpy as np 
import matplotlib.pyplot as plt 

##metodo 1 

def f(x): 
	return x**2 -3 #qui va la funzione su cui applicare il metodo di bisezione 
								  #cioè un polinomio di cui voglio trovare le redici in un 
								  #intervallo scelto

#definisco la funzione bisezione a cui passo gli estremi iniziali dell'ntervallo [a,b] e la 
#tolleranza tol
def bisection(a,b,tol): 
	xl = a 
	xr = b 
	i = 1 #conto il numero di iterazioni 
	while (np.abs(xl-xr)>= tol):
		c = (xr+xl)/2.0
		prod = f(xl)*f(c)
		if prod > tol: #se qui al posto di tol si mette 0 la risposta è più accurtata!
			xl = c 
			i += 1
		else:
			if prod < tol: 
				xr = c
				i += 1
	return i,c


answer1 = bisection(-2,2,1e-13) #sostituisco i valori che servono

##metodo 2 

from scipy.optimize import fsolve 

guess = [-1,1] #la funzione fsolve ha bisogno di un guess della soluzione all'inizio, 
				 #dove guess è un array con un numero di "tentativi" per ogni radice del polinomio f(x)
answer2 = fsolve(f,guess)

#stampo le soluzioni sul terminale
print('\n')
print('bisection method gives a root of f(x) at x = ', answer1[1],'\n','with',answer1[0],'iterations\n')
print('fsolve gives the roots of f(x) at x = ', answer2,'\n')

#plotto f(x) in blu e l'asse x in rosso
x = np.linspace(-2,2,100)
x_axis = np.zeros(len(x))
plt.plot(x,f(x))
plt.plot(x,x_axis,'r-')
plt.grid()
plt.show()
