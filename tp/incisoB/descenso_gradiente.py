import numpy as np
import pandas as pd
from IPython.core.display_functions import clear_output

df = pd.read_csv('../players_21.csv')

n = len(df)

# Matrices
X = np.column_stack((np.ones(n), df['wage_eur'], df['overall'], df['potential']))
Y = df['value_eur']

# Parámetros para el descenso del gradiente
tasa_de_aprendizaje = 1e-10
iteraciones = 60000
tolerancia = 0.0000000001

# Inicializo los coeficientes con ceros
coeficientes = np.zeros(X.shape[1])

def calcular_costo(X, Y, coeficientes):
    m = len(Y)
    predicted = X.dot(coeficientes)
    error = predicted - Y

    return np.sum(error**2)/m

iteracion = 0
convergencia = False
historial = []
ultimas_iteraciones = 10

while iteracion < iteraciones and not convergencia:
    predicted = X.dot(coeficientes)
    gradient = X.T.dot(predicted - Y) / len(Y)

    coeficientes_nuevos = coeficientes - gradient * tasa_de_aprendizaje

    cambio_en_costo = abs(calcular_costo(X, Y, coeficientes_nuevos) - calcular_costo(X, Y, coeficientes))

    # Verifico condición
    if cambio_en_costo < tolerancia:
        convergencia = True
        print("TOLERANCIA SUPERADA")
    else:
        coeficientes = coeficientes_nuevos
        iteracion += 1

    resumen = f'Iteración {iteracion}: Coeficientes = {coeficientes}, Error = {cambio_en_costo}, Tolerancia = {tolerancia}'
    print(resumen)
    historial.append(resumen)
    historial = historial[-ultimas_iteraciones:]

clear_output(wait=True)
print(f'Ultimas {ultimas_iteraciones} iteraciones:')
for l in historial:
    print(l)

print('Coeficientes finales:')
print(coeficientes)

# Predicciones
y_pred = X.dot(coeficientes)

# Cálculos
s_yy = np.sum(Y ** 2) - (np.sum(Y) ** 2) / n
ss_r = np.sum((Y - y_pred) ** 2)
R2 = 1 - (ss_r / s_yy)
R2_ajustado = 1 - (1 - R2) * (n - 1) / (n - X.shape[1] - 1)
r_a = np.sqrt(R2_ajustado)
sigma_cuadrado = ss_r / (n - X.shape[1])

# Correlación lineal para cada variable
r_x1_y = np.corrcoef(df['wage_eur'], Y)[0, 1]
r_x2_y = np.corrcoef(df['overall'], Y)[0, 1]
r_x3_y = np.corrcoef(df['potential'], Y)[0, 1]

# Resultados
print(f"""
R2: {R2}
R2 ajustado: {R2_ajustado}
Sigma cuadrado: {sigma_cuadrado}
Correlación lineal: {r_x1_y}
Correlación wage_eur - value_eur: {r_x1_y}
Correlación overall - value_eur: {r_x2_y}
Correlación potential - value_eur: {r_x3_y}
""")
