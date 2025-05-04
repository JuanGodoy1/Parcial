import math
import uctypes
import array
import machine

def funBesel(x, y, n):
    xf = array.array("f", [0] * (n + 1))
    yf = array.array("f", [0] * (n + 1))

    dir_xf = uctypes.addressof(xf)
    dir_yf = uctypes.addressof(yf)

    for i in range(n + 1):
        xf[i] = x[0]*(1 - i/n)**3 + 3*(1 - i/n)**2 * (i/n) * x[1] + 3*(1 - i/n)*(i/n)**2 * x[2] + (i/n)**3 * x[3]
        yf[i] = y[0]*(1 - i/n)**3 + 3*(1 - i/n)**2 * (i/n) * y[1] + 3*(1 - i/n)*(i/n)**2 * y[2] + (i/n)**3 * y[3]

        # Guardamos directamente en memoria
        machine.mem32[dir_xf + 4*i] = int(xf[i] * 1000)  # multiplicamos por 1000 para guardar como int
        machine.mem32[dir_yf + 4*i] = int(yf[i] * 1000)

    return xf, yf

# Puntos de control
p0 = array.array("f", [1, 5])
p1 = array.array("f", [2, 6])
p2 = array.array("f", [3, 7])
p3 = array.array("f", [4, 8])
p_list = [p0, p1, p2, p3]

x = array.array("f", [p[0] for p in p_list])
y = array.array("f", [p[1] for p in p_list])
n = 4

# Llamamos a la versión con memoria directa
xf, yf = funBesel(x, y, n)

LR = []

for i in range(n + 1):
    xf[i] = machine.mem32[uctypes.addressof(xf) + 4*i] / 1000
    yf[i] = machine.mem32[uctypes.addressof(yf) + 4*i] / 1000
    LR.append([xf[i], yf[i]])

# Mostrar la lista LR
print("Lista LR:")
print(LR)
