import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2 + (1/2)*y - 2


def grad_f(x, y):
    df_dx = 2 * x
    df_dy = 2 * y + 1 / 2
    return np.array([df_dx, df_dy])


tolerancia = 0.0001
paso = 0.1
x0 = np.array([10.0, 2.0])
history = []
x_current = x0

while True:
    # Me quedo con los puntos actuales
    history.append((x_current[0], x_current[1], f(x_current[0], x_current[1])))

    # Calculo del gradiente en el punto actual
    grad = grad_f(x_current[0], x_current[1])

    # Actualizo el punto en función del tamaño del peso
    x_next = x_current - paso * grad

    # Verifico la condición de corte
    # Si la norma del gradiente es menor que la tolerancia
    if np.linalg.norm(grad) < tolerancia:
        break

    # Actualizo el punto
    x_current = x_next

# Paso los resultados que se fueron obteniendo a un DataFrame para su visualización
df_history = pd.DataFrame(history, columns=['x', 'y', 'f(x, y)'])

print(f"Resultado final: x = {x_current[0]}, y = {x_current[1]}")
print(f"Valor de f(x, y) en el mínimo: {f(x_current[0], x_current[1])}")
print(f"Cantidad de iteraciones: {len(history)}")

# Grafico de la trayectoria del gradiente
plt.figure(figsize=(10, 6))
plt.plot(df_history['x'], df_history['y'], 'o-', label='Trayectoria del descenso')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Descenso del Gradiente de f(x, y)')
plt.grid(True)
plt.legend()
plt.savefig('descenso_gradiente-con-paso-01.png')
plt.show()
