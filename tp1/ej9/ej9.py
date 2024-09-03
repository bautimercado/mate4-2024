import numpy as np
import matplotlib.pyplot as plt

# Función
def f(x, y):
    return x**2 + y**4 + np.exp(x * y)

# Derivadas parciales
def df_dx(x, y):
    return 2*x + y * np.exp(x * y)

def df_dy(x, y):
    return 4*y**3 + x * np.exp(x * y)

def aprox_lineal(x, y):
    x0, y0 = 1, 0
    z0 = f(x0, y0)
    dz_dx = df_dx(x, y)
    dz_dy = df_dy(x, y)
    return dz_dx * (x-x0) + dz_dy * (y-y0) + z0

# Creación de malla de puntos
x = np.linspace(0.8, 1.2, 100)
y = np.linspace(-0.1, 0.1, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z_aprox = aprox_lineal(X, Y)

# Creamos la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grafico de la función
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

# Grafico de la aproximación lineal
ax.plot_surface(X, Y, Z_aprox, alpha=0.5, color='orange')

# Punto de aproximación (1,0)
ax.scatter(1, 0, f(1, 0), color='red', s=50)

# Configuración del gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig('grafica-ej9.png', dpi=300)
plt.show()
