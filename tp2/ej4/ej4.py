import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'windows': [2.5, 7.1, 5, 8.5, 7, 8.1],
    'dos': [2.3, 7.1, 4, 8, 6.6, 5]
}

df = pd.DataFrame(data)
x = df['windows'].values
y = df['dos'].values

x_mean = np.mean(x)
y_mean = np.mean(y)

s_xy = np.sum((x - x_mean) * (y - y_mean))
s_xx = np.sum((x - x_mean) ** 2)
s_yy = np.sum((y - y_mean) ** 2)

beta_1 = s_xy/s_xx
beta_0 = y_mean - (beta_1 * x_mean)

y_pred = beta_0 + beta_1 * x

print("Gráfico de la dispersion de los puntos")
print(f"Pendiente (β1): {beta_1:.3f}")
print(f"Ordenada (β0): {beta_0:.3f}")

plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label='Recta de regresión')
plt.xlabel('Windows')
plt.ylabel('DOS')
plt.title('Regresión Lineal')
plt.legend()
plt.savefig('grafico.png')
plt.show()



