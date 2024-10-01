import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ====================
# CARGAR Y PREPARAR LOS DATOS
# ====================

# Cargar el dataset
df = pd.read_csv('../players_21.csv')

# Definir las variables independientes y dependientes
x = df['wage_eur']
y = df['value_eur']
n = len(df)

# ====================
# CÁLCULOS DE REGRESIÓN LINEAL
# ====================

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

# ====================
# INDICADORES
# ====================

SS_r = np.sum((y - y_pred) ** 2)
R2 = 1 - (SS_r / s_yy)
r = s_xy / np.sqrt(s_xx * s_yy)
sigma_cuadrado = SS_r / (n - 2)

# ====================
# VISUALIZACIÓN
# ====================

# Graficar los puntos originales y la recta de regresión
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label=f'Recta de regresión\nR² = {R2:.2f}, r = {r:.2f}')
plt.xlabel('WAGE EUR')
plt.ylabel('VALUE EUR')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.savefig('recta-regresion-lineal.png')
plt.show()

# ====================
# CÁLCULOS ESTADÍSTICOS Y RESULTADOS
# ====================

# Mostrar sumatorias y coeficientes
print(f'Sumatoria de X: {sum_x}')
print(f'Sumatoria de Y: {sum_y}')
print(f'Sumatoria de X²: {sum_xx}')
print(f'Sumatoria de X por Y: {sum_xy}')
print(f'Media de X: {np.mean(x)}')
print(f'Media de Y: {np.mean(y)}')
print(f"S_XX: {s_xx:.3f}")
print(f"S_YY: {s_yy:.3f}")
print(f"S_XY: {s_xy:.3f}")
print(f"Pendiente (β1): {beta_1:.3f}")
print(f"Ordenada (β0): {beta_0:.3f}")
print(f"SS_R (Suma de residuos al cuadrado): {SS_r:.3f}")
print(f"Varianza residual (sigma²): {sigma_cuadrado:.3f}")
print(f"Coeficiente de determinación (R²): {R2:.3f}")
print(f"Coeficiente de correlación lineal (r): {r:.3f}")

# ====================
# PRUEBA DE SIGNIFICANCIA
# ====================

se_beta_1 = np.sqrt(sigma_cuadrado / s_xx)
T_beta_1 = beta_1 / se_beta_1
gl = n - 2
t_minimo = stats.t.ppf(1 - 0.05/2, gl)
p_value = 2 * (1 - stats.t.cdf(np.abs(T_beta_1), df=gl))

print(f"PVALOR: {p_value:.3f}")
print(f"T: {T_beta_1:.3f}")
print(f"t: {t_minimo:.3f}")
print(f"Error estándar: {se_beta_1:.3f}")
print(f"Grados de libertad: {gl}")

# ====================
# INTERVALOS DE CONFIANZA
# ====================

# Intervalo de confianza para Beta1
IC_beta_1 = [
    beta_1 - t_minimo * se_beta_1,
    beta_1 + t_minimo * se_beta_1,
]

# Intervalo de confianza para Beta0
IC_beta_0 = [
    beta_0 - t_minimo * np.sqrt(sigma_cuadrado * (1/n + (np.mean(x)**2/s_xx))),
    beta_0 + t_minimo * np.sqrt(sigma_cuadrado * (1/n + (np.mean(x)**2/s_xx)))
]

print(f"Intervalo de Confianza para Beta1: {IC_beta_1}")
print(f"Intevalo de Confianza para Beta0: {IC_beta_0}")

# ====================
# INCISO 3: INTERVALOS DE PREDICCIÓN Y RESPUESTA MEDIA
# ====================

nueva_x = np.mean(x)
nueva_y = beta_0 + beta_1 * nueva_x

# Intervalo de confianza de la respuesta media
IC_respuesta_media = [
    beta_0 + beta_1 * nueva_x - t_minimo * np.sqrt(sigma_cuadrado * (1 / n + ((nueva_x - np.mean(x)) ** 2 / s_xx))),
    beta_0 + beta_1 * nueva_x + t_minimo * np.sqrt(sigma_cuadrado * (1 / n + ((nueva_x - np.mean(x)) ** 2 / s_xx)))
]
ancho_IC_respuesta_media = IC_respuesta_media[1] - IC_respuesta_media[0]

# Intervalo de predicción
IP = [
    nueva_y - t_minimo * np.sqrt(sigma_cuadrado * (1 + (1/n) + (((nueva_x - np.mean(x)) ** 2) / s_xx))),
    nueva_y + t_minimo * np.sqrt(sigma_cuadrado * (1 + (1/n) + (((nueva_x - np.mean(x)) ** 2) / s_xx)))
]
ancho_IP = IP[1] - IP[0]

print(f"INCISO 3")
print(f"INTERVALO DE CONFIANZA DE RESPUESTA MEDIA: {IC_respuesta_media}")
print(f"ANCHO: {ancho_IC_respuesta_media}")
print(f"INTERVALO DE PREDICCIÓN: {IP}")
print(f"ANCHO: {ancho_IP}")
print(f"Proporción de veces que supera la incertidumbre de la predicción: {ancho_IP / ancho_IC_respuesta_media}")
