import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def regresion_lineal(atributo, y, df):
    x = df[atributo]
    n = len(y)

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
    plt.xlabel(atributo.upper())
    plt.ylabel('VALUE EUR')
    plt.title('Regresión Lineal Simple')
    plt.legend()
    plt.show()

    # ====================
    # PRUEBA DE SIGNIFICANCIA
    # ====================
    se_beta_1 = np.sqrt(sigma_cuadrado / s_xx)
    T_beta_1 = beta_1 / se_beta_1
    gl = n - 2
    t_minimo = stats.t.ppf(1 - 0.05 / 2, gl)
    p_value = 2 * (1 - stats.t.cdf(np.abs(T_beta_1), df=gl))

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
        beta_0 - t_minimo * np.sqrt(sigma_cuadrado * (1 / n + (np.mean(x) ** 2 / s_xx))),
        beta_0 + t_minimo * np.sqrt(sigma_cuadrado * (1 / n + (np.mean(x) ** 2 / s_xx)))
    ]

    return {
        'n': n,
        'Media de x': np.mean(x),
        'Media de y': np.mean(y),
        'Sxx': s_xx,
        'Syy': s_yy,
        'Sxy': s_xy,
        'B1': beta_1,
        'B0': beta_0,
        'SS_R': SS_r,
        'Estimación de la varianza': sigma_cuadrado,
        'R²': R2,
        'r': r,
        'P-Valor': p_value,
        'Intervalo de confianza para B1': IC_beta_1,
        'Intervalo de confianza para B0': IC_beta_0,
    }

df = pd.read_csv('https://drive.google.com/uc?id=1HghsI0AMXFYHWjvKAd3vfmYZZPop9fVZ')

atributos = [
    'overall',
    'potential',
    'wage_eur'
]

y = df['value_eur']
for a in atributos:
    print(regresion_lineal(a, y, df))
