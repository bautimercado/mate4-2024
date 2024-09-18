import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meta_df = pd.read_excel('META.xlsx', sheet_name='in')

# Convierto a Date en DateTime
meta_df['Date'] = pd.to_datetime(meta_df['Date'], format='%Y-%m-%d')

# Periodo de actualizaciones
start_date = pd.to_datetime('2024-02-02')
end_date = pd.to_datetime('2024-04-24')

# Divido el conjunto de datos
meta_all_data = meta_df.copy()
meta_no_updates = meta_df[(meta_df['Date'] < start_date) | (meta_df['Date'] > end_date)]

def regresion_lineal(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    #n = len(x)

    # Formula para Beta1
    s_xy = np.sum((x - x_mean) * (y - y_mean))
    s_xx = np.sum((x - x_mean)**2)
    s_yy = np.sum((y - y_mean)**2)

    beta_1 = s_xy / s_xx

    # Formula para Beta0
    beta_0 = y_mean - (beta_1 * x_mean)

    ss_r = s_yy - beta_1 * s_xy
    R2 = 1 - (ss_r/s_yy)
    r = s_xy/np.sqrt(s_xx*s_yy)


    return beta_0, beta_1, R2, r


# Regresión lineal para ambos conjuntos
x_all = meta_all_data['Dias'].values
y_all = meta_all_data['Precio U$D'].values
beta_0_all, beta_1_all, R2_all, r_all = regresion_lineal(x_all, y_all)

x_no_updates = meta_no_updates['Dias'].values
y_no_updates = meta_no_updates['Precio U$D'].values
beta_0_no_updates, beta_1_no_updates, R2_no_updates, r_no_updates = regresion_lineal(x_no_updates, y_no_updates)

print(f"Análisis con todos los datos:")
print(f"Pendiente (β1): {beta_1_all:.3f}")
print(f"Ordenada (β0): {beta_0_all:.3f}")
print(f"R² (Coef. de determinación): {R2_all:.3f}")
print(f"r (Coef. de correlación lineal): {r_all:.3f}\n")

print(f"Análisis sin actualizaciones:")
print(f"Pendiente (β1): {beta_1_no_updates:.3f}")
print(f"Ordenada (β0): {beta_0_no_updates:.3f}")
print(f"R² (Coef. de determinación): {R2_no_updates:.3f}")
print(f"r (Coef. de correlación lineal): {r_no_updates:.3f}")


# Graficar los resultados
plt.figure(figsize=(10,6))
plt.scatter(x_all, y_all, color='blue', label='Datos completos', alpha=0.5)
plt.scatter(x_no_updates, y_no_updates, color='green', label='Sin actualizaciones', alpha=0.5)

# Línea de regresión con todos los datos
plt.plot(x_all, beta_1_all * x_all + beta_0_all, color='blue', label='Regresión con todos los datos')

# Línea de regresión sin actualizaciones
plt.plot(x_no_updates, beta_1_no_updates * x_no_updates + beta_0_no_updates, color='green', label='Regresión sin actualizaciones')

plt.xlabel('Días desde 03/09/2023')
plt.ylabel('Precio U$D')
plt.title('Regresión lineal del precio de acciones de META')
plt.legend()
plt.savefig('regresion_lineal.png')
plt.show()