import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.exp(x**2+y**2)

def plano_tangente(x, y, x0, y0, z0, dz_dx, dz_dy):
    return dz_dx * (x-x0) + dz_dy * (y-y0) + z0

# Punto de calculo
x0 = -1
y0 = 1
z0 = f(x0, y0)

# Derivadas parciales
dz_dx = 2 * x0 * np.exp(x0**2+y0**2)
dz_dy = 2 * y0 * np.exp(x0**2+y0**2)

# Creación de malla de puntos para graficar la función y al plano tangente
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z_tangente = plano_tangente(X, Y, x0, y0, z0, dz_dx, dz_dy)

# Creación de gráfica 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar función
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

# Graficar plano tangente
ax.plot_surface(X, Y, Z_tangente, alpha=0.5, color='orange')

# Punto de tangencia
ax.scatter(x0, y0, z0, color='red', s=50)

# Configuraciones de la gráfica
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig('grafica-ej8.png', dpi=300)
plt.show()