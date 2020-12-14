'''
Examen 2D Graficacion
Alumno: Eduardo Gonzalez Flores
No Control: 17390753
Carrera: Ingenieria en Sistemas Computacionales
'''
import numpy as np
import matplotlib.pyplot as plt


plt.axis([-75, 75, -50, 50])

plt.axis('on')
plt.grid(True)

#Definimos el centro de x - y
xc = -15
yc = 0

# Dibujamos el primer rectangulo
Ax = 15
Ay = 0
Bx = -15
By = 0
Cx = -15
Cy = -15
Dx = 15
Dy = -15

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='0.3')

# Dibujamos el segundo rectangulo
Ax = 0
Ay = 7.5
Bx = -30
By = 7.5
Cx = -30
Cy = -7.5
Dx = 0
Dy = -7.5

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='0.5')




# Dibujamos el circulo, como el ejercicio nos dice que
# el radio es el ultimo digito de nuestro control multiplicado por 5
# entonces mi ultimo digito es 3 * 5 = 15  que es equivalente a que el lado mas largo de nuestro rectangulo
# se divida entre dos

r = 15

p1 = 0*np.pi/180
p2 = 360*np.pi/180
dp = (p2-p1)/100

xlast = xc+r*np.cos(p1)
ylast = yc+r*np.sin(p1)

for p in np.arange(p1, p2+dp, dp):
    x = xc+r*np.cos(p)
    y = yc+r*np.sin(p)
    #Utilizamos 0.7l col
    plt.plot([xlast, x], [ylast, y], color='0.7', linewidth=1)
    xlast = x
    ylast = y

plt.scatter(xc, yc, s=2, color='0.7')



plt.show()
