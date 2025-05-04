import uctypes
import array
import machine

def funBesel(x, y, n):
    xf = array.array("f", [0,0,0,0,0]) 
    yf = array.array("f", [0,0,0,0,0])
    LR = []
    for i in range (n+1):

        xf[i] = x[0]*(1-i/n)**3 + 3*(1-i/n)**2 * (i/n)*x[1] + 3*(1-i/n)*(i/n)**2*x[2] + (i/n)**3 * x[3]

        yf[i] = y[0]*(1-i/n)**3 + 3*(1-i/n)**2 * (i/n)*y[1] + 3*(1-i/n)*(i/n)**2*y[2] + (i/n)**3 * y[3]
        LR.append([xf[i], yf[i]])
    
    
    return LR

x = array.array("f", [1,2,3,4]) 
y = array.array("f", [5,6,7,8]) 
n = 4

resultado = funBesel(x, y, n)
print("FunBesel:", list(resultado))

