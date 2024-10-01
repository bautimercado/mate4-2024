import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculos(df):
    x1 = df['wage_eur']
    x2 = df['overall']
    x3 = df['potential']
    y = df['value_eur']

    n = len(df)

    # Sumatorias
    sum_x1_x2 = np.sum(x1 * x2)
    sum_x1_x3 = np.sum(x1 * x3)
    sum_x2_x3 = np.sum(x2 * x3)
    sum_x1_y = np.sum(x1 * y)
    sum_x2_y = np.sum(x2 * y)
    sum_x3_y = np.sum(x3 * y)
    sum_x1_cuadrado = np.sum(x1**2)
    sum_x2_cuadrado = np.sum(x2**2)
    sum_x3_cuadrado = np.sum(x3**2)

    # Matrices
    X = np.column_stack((np.ones(n), x1, x2, x3))
    Y = y

    # Calculo de los coeficientes usando la fórmula de regresión múltiple (B0, B1, B2 y B3)
    B = np.linalg.inv(X.T @ X) @ X.T @ Y

    beta_0 = B[0]
    beta_1 = B[1]
    beta_2 = B[2]
    beta_3 = B[3]

    # Ecuación de y
    y_pred = X @ B

    # Calculo de indicadores
    # Variación total (STC)
    s_yy = np.sum(y ** 2) - (np.sum(y) ** 2) / n

    # Varación del residuo (SCE)
    SS_r = np.sum((y - y_pred)**2)

    # Coeficiente de determinación
    R2 = 1 - (SS_r / s_yy)

    # Coeficiente de determinación ajustado
    R2a = 1 - (1 - R2) * ((n - 1) / (n - 3 - 1))

    # Coeficiente de correlación lineal
    r_a = np.sqrt(R2a)

    # Calculo de r (correlación lineal) para cada atributo
    r_x1_y = np.corrcoef(x1, y)[0, 1]
    r_x2_y = np.corrcoef(x2, y)[0, 1]
    r_x3_y = np.corrcoef(x3, y)[0, 1]

    # Varianza
    sigma_cuadrado = SS_r / (n - 4)

    print(f"""
        RESULTADOS: \n
        sumX1: {x1.sum()},
        "sumX2": {x2.sum()},
        "sumX3": {x3.sum()},
        "sumY": {y.sum()},
        "sum_x1_cuadrado": {sum_x1_cuadrado},
        "sum_x2_cuadrado": {sum_x2_cuadrado},
        "sum_x3_cuadrado": {sum_x3_cuadrado},
        "sum_x1_x2": {sum_x1_x2},
        "sum_x1_x3": {sum_x1_x3},
        "sum_x2_x3": {sum_x2_x3},
        "sum_x1_y": {sum_x1_y},
        "sumX2Y": {sum_x2_y},
        "sumX3Y": {sum_x3_y},
        "media_y": {y.sum() / n},
        "media_x1": {x1.sum() / n},
        "media_x2": {x2.sum() / n},
        "media_x3": {x3.sum() / n},
        "n": {n},
        "Syy": {s_yy},
        "Ssr": {SS_r},
        "B0": {beta_0},
        "B1": {beta_1},
        "B2": {beta_2},
        "B3": {beta_3},
        "R2": {R2},
        "R2a": {R2a},
        "r_a": {r_a},
        r_x1_y: {r_x1_y},
        r_x2_y: {r_x2_y},
        r_x3_y: {r_x3_y},
        "sigma_cuadrado": {sigma_cuadrado},
        y: {beta_0} + {beta_1} * wage_eur + {beta_2} * overall + {beta_3} * potential
        """)

df = pd.read_csv('../players_21.csv')
calculos(df)

#print(resultados)
#B = [resultados['B0'], resultados['B1'], resultados['B2'], resultados['B3']]
#graficar(df, B)

