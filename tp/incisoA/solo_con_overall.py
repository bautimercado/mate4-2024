import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Cargar el dataset
df = pd.read_csv('../players_21.csv')

# Definir las variables independientes y dependientes
#x = df['wage_eur']
x = df['overall']
y = df['value_eur']
n = len(df)

# Calcular las sumas necesarias para la regresión lineal
sum_xy = np.sum(x * y)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xx = np.sum(x ** 2)

# Calcular las sumatorias necesarias
s_xy = sum_xy - (sum_x * sum_y) / n
s_xx = sum_xx - (sum_x ** 2) / n
s_yy = np.sum(y ** 2) - (sum_y ** 2) / n

# Calcular los coeficientes de la recta de regresión
beta_1 = s_xy / s_xx
beta_0 = (sum_y / n) - beta_1 * (sum_x / n)

# Predicciones del modelo
y_pred = beta_0 + beta_1 * x

# Calcular SSr y R2
SS_r = np.sum((y - y_pred) ** 2)
R2 = 1 - (SS_r / s_yy)

# Calcular r (coeficiente de correlación)
r = s_xy / np.sqrt(s_xx * s_yy)

# Calcular la varianza residual
sigma_cuad = SS_r / (n - 2)

# Graficar los puntos originales y la recta de regresión
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label=f'Recta de regresión\nR² = {R2:.2f}, r = {r:.2f}')
plt.xlabel('Overall')
plt.ylabel('Valor en EUR')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.show()

print(f"S_XX: {s_xx:.3f}")
print(f"S_YY: {s_yy:.3f}")
print(f"S_XY: {s_xy:.3f}")
print(f"Pendiente (β1): {beta_1:.3f}")
print(f"Ordenada (β0): {beta_0:.3f}")
print(f"SS_R (Suma de residuos al cuadrado): {SS_r:.3f}")
print(f"Varianza residual (sigma²): {sigma_cuad:.3f}")
print(f"Coeficiente de determinación (R²): {R2:.3f}")
print(f"Coeficiente de correlación lineal (r): {r:.3f}")

# PRUEBA DE SIGNIFICANCIA

# Error estándar de BETA1
se_beta_1 = np.sqrt(sigma_cuad / s_xx)

# Calcular el t-statistic para beta_1 (T)
t_beta_1 = beta_1 / se_beta_1

# Grados de libertad
gl = n - 2

# t
t = stats.t.ppf(1 - 0.05/2, gl)

# Calcular el p-valor
p_value = 2 * (1 - stats.t.cdf(np.abs(t_beta_1), df=gl))

print(f"PVALOR: {p_value:.3f}")
print(f"T: {t_beta_1:.3f}")
print(f"t: {t:.3f}")
print(f"Error estándar: {se_beta_1:.3f}")
print(f"Grados de libertad: {gl}")

IC_beta_1 = [
    beta_1 - t * se_beta_1,
    beta_1 + t * se_beta_1,
]

IC_beta_0 = [
    beta_0 - t * np.sqrt(sigma_cuad * (1/n + (np.mean(x)**2/s_xx)) ),
    beta_0 + t * np.sqrt(sigma_cuad * (1/n + (np.mean(x)**2/s_xx)) )
]

print(f"Intervalo de Confianza para Beta1: {IC_beta_1}")
print(f"Intevalo de Confianza para Beta0: {IC_beta_0}")

# INCISO 3
nueva_x = np.mean(x)
nueva_y = beta_0 + beta_1 * nueva_x


IC_respuesta_media = [
    beta_0 + beta_1 * nueva_x - t * np.sqrt(sigma_cuad * (1 / n + ((nueva_x - np.mean(x)) ** 2 / s_xx))),
    beta_0 + beta_1 * nueva_x + t * np.sqrt(sigma_cuad * (1 / n + ((nueva_x - np.mean(x)) ** 2 / s_xx)))
]
ancho_IC_respuesta_media = IC_respuesta_media[1] - IC_respuesta_media[0]

IP = [
    nueva_y - t * np.sqrt(sigma_cuad * (1 + (1/n) + (((nueva_x - np.mean(x)) ** 2)/s_xx))),
    nueva_y + t * np.sqrt(sigma_cuad * (1 + (1/n) + (((nueva_x - np.mean(x)) ** 2)/s_xx)))
]
ancho_IP = IP[1] - IP[0]


print(f"INCISO 3")
print(f"INTERVALO DE CONFIANZA DE RESPUESTA MEDIA: {IC_respuesta_media}")
print(f"ANCHO: {ancho_IC_respuesta_media}")
print(f"INTERVALO DE PREDICIÓN: {IP}")
print(f"ANCHO: {ancho_IP}")
print(f"Proporción de veces que supera la incertidumbre de la predicción de la calidad a la de respuesta media de calidad para una característica fija, siendo ambas de la misma confianza y ancho mínimo: {ancho_IP/ancho_IC_respuesta_media}")