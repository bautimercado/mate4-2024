import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'x': [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25],
    'y': [9.6, 20.1, 29.9, 39.1, 50.0, 9.6, 19.4, 29.7, 40.3, 49.9, 10.7, 21.3, 30.7, 41.8, 51.2]
}

df = pd.DataFrame(data)
x = df['x'].values
y = df['y'].values

x_mean = np.mean(x)
y_mean = np.mean(y)

s_xy = np.sum((x - x_mean) * (y - y_mean))
s_xx = np.sum((x - x_mean) ** 2)
s_yy = np.sum((y - y_mean) ** 2)
beta_1 = s_xy/s_xx
beta_0 = y_mean - (beta_1 * x_mean)
y_pred = beta_0 + beta_1 * x
ss_r = s_yy - (beta_1 * s_xy)
sigma_2_pred = ss_r/(len(x) - 2)
R2 = 1 - (ss_r / s_yy)
r = s_xy / np.sqrt(s_xx * s_yy)

print(f"S_XX: {s_xx:.3f}")
print(f"S_YY: {s_yy:.3f}")
print(f"S_XY: {s_xy:.3f}")
print(f"Pendiente (β1): {beta_1:.3f}")
print(f"Ordenada (β0): {beta_0:.3f}")
print(f"SS_R (Suma de residuos al cuadrado): {ss_r:.3f}")
print(f"Varianza residual (sigma²): {sigma_2_pred:.3f}")
print(f"Coeficiente de determinación (R²): {R2:.3f}")
print(f"Coeficiente de correlación lineal (r): {r:.3f}")


# Test de hipotesis

T = beta_1 / (np.sqrt(sigma_2_pred / s_xx))
print(f"T (Test de hipotesis): {T:.3f}")

plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label='Recta de regresión')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.legend()
plt.savefig('grafico.png')
plt.show()
