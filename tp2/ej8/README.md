# 8) En un departamento de informática, un grupo de investigación dedicado al estudio de las comunicaciones por la red desea conocer la relación entre el tiempo de transmisión de un fichero y la información útil del mismo. Para ello se han hecho algunos experimentos en los que se enviaban paquetes de distintas longitudes (bytes) de información útil y se median los tiempos (en milisegundos) que tardaban desde el momento en que se enviaban hasta que llegaban al servidor. Los resultados del experimento se resumen en los siguientes estadísticos:

$$
S_{xx} = 47.990 \quad \bar{x} = 194 \quad \hat{\beta_0} = 27,3275 \quad
\Sigma x²_i = 424.350 \quad \Sigma x_iy_i = 183.760 \quad \Sigma y²_i = 81.715
$$

# Se pide estudiar la relación entre las variables tiempo (𝑦) y longitud (𝑥) de los ficheros. Para ello, se pide:

## a) Obtener la recta de regresión del tiempo en función de la longitud de los ficheros. Interpretar los resultados obtenidos.

La formula de recta de regresión líneal es:

$$ \hat{y} = \beta_0 + \beta_1x $$

- Según los datos dados en el enunciado, lo único que falta es la pendiente $ \hat{\beta_1} $

Por la teoría, sabemos que $ S_{xx} $ se puede expresar como:

$$ 
S_{xx} = \Sigma^n_{i=1} x²_i - \frac{(\Sigma^n_{i=1} x_i)²}{n} \to 
S_{xx} = \Sigma^n_{i=1} x²_i - \frac{(\Sigma^n_{i=1} x_i) * (\Sigma^n_{i=1} x_i)}{n} 
\to S_{xx} = \Sigma^n_{i=1} x²_i - \frac{(\Sigma^n_{i=1} x_i)}{n} * \Sigma^n_{i=1} x_i \to 
S_{xx} = \Sigma^n_{i=1} x²_i - \bar{x} * \Sigma^n_{i=1} x_i 
$$  

Reemplazando los valores dados:

$$ 47.990 = 424.350 - 194 * \Sigma^n_{i=1} x_i \to \frac{376.36}{194} = \Sigma^n_{i=1} x_i \to \Sigma^n_{i=1} x_i = 1.94  $$

A partir de esto, podemos usar la formula de $ \bar{x} $, reemplazar los valores y despejar n:

$$ \bar{x} = \frac{\Sigma^n_{i=1}}{n} \to 194 = \frac{1.94}{n} \to n = 100 $$ 

Usando la formula de $ S_{yy} $:

$$ S_{yy} = \Sigma (y_i - \bar{y})² = \Sigma y²_i - \frac{(\Sigma y_i)²}{n} $$

Reemplazando los valores conocidos:

$$ 81.715 - \frac{(\Sigma^n_{i=1} y_i)²}{100}$$

Me quedé sin ideas :sad:

## b) Indicar el valor que toma el coeficiente de determinación y correlación lineal. Interpretar los resultados.

## c) Estudiar la significación del modelo.

## d) Obtener el intervalo de confianza, al 95%, para la pendiente de la recta,

## e) ¿Cuál será el tiempo de transmisión para un fichero que tiene una longitud 250 bytes?
