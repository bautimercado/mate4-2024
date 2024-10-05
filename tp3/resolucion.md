# TP3 - Teoría de Números

## 1. Probar que no hay enteros simultáneamente pares e impares.

- Sea $ a \in \Z $ múltiplo de $ b $ tal que $ b \in \Z $, si $ \exists c \in \Z : a = b*c $.
- Sea $ x \in \Z $ un número par si es múltiplo de 2.
  - Es decir que $ \exists c \in \Z : x = 2*c $.
  - Si no se cumple, x sería impar $ \nexists c \in \Z : x = 2*c $.
- Entonces, decimos que $ \exists n \in \Z : n es par e impar $.
  - n es par $ \to \exists c \in \Z : n = 2*c $
  - n es impar $ \to \nexists c \in \Z : n = 2*c $
- Llegamos a un absurdo, ya que no es posible que un número $ n \in \Z $ sea par y a la vez impar.
- Por lo tanto $ \nexists n \in \Z : n $ es par e impar. 

## 2. Analizar si las siguientes afirmaciones son verdaderas o falsas:

### (a) Si $ a|1 $ entonces $ a = 1 $ o $ a = −1 $

- $ a|1 $ si $ \exists c \in \Z : 1 = a*c $
- Para esto, las posibles combinaciones son:
  - $ a = 1 $ y $ c = 1 $
  - $ a = -1 $ y $ c = -1 $
- Es necesario que $ a = 1 $ o $ a = -1 $

### (b) $ a|b $ y $ b|c $ entonces $ a|c $

- Se da que $ a|b $ si $ \exists d \in \Z : b = a*d $,  que $ b|c $ si $ \exists e \in \Z : c = b*e $ y se da que $ a|c $ si $ \exists f \in \Z : c = a*f $ (hay que demostrar eso último).

Como $ \exists d \in \Z : b = a*d \land \exists e \in \Z : c = b*e $ entonces $ \exists f \in \Z : c = a*f $
- $ b = a*d $ y $ c = b*e $
- $ c = b*e = (a*d)*e = a * (d*e) = a * f $
- Entonces, se cumple que $ \exists f \in \Z : c = a*f \to a|c $. Por lo tanto, la afirmación es verdadera.

### (c) $ a(a − 1) $ es par
Primero, tenemos que probar que la multiplicación de un número par por cualquier otro número entero nos da como resultado otro número par.

- Si $ x $ es par, entonces $ \exists y \in \Z : x = 2*y $. Sea $ z \in \Z $.
  - $ x*z $ es par si $ \exists f \in \Z : x * z = 2 * f $.
  - $ x = 2*y $
  - $ x*z = (2*y)*z = 2*(y*z) = 2*f $
    - $ f = (y*z) \in \Z $
- Entonces, se demuestra que $ \exists f \in \Z : x*z=2*f $.

Para demostrar que $ a*(a-1) $ es par hay que considerar dos casos:
- <u>$ a $ es par:</u>
  - Si $ a $ es par, entonces $ \exists c \in \Z : a = 2*c $
  - $ a*(a-1) = (2*c) * (2*c-1) $
  - Cómo $ 2*c $ es par, $ (2c)*(2c-1) $ es par y entonces $ a*(a-1) $ es par.
- <u>$ a $ es impar: </u>
  - Si $ a $ es impar, entonces $ \nexists c \in \Z : a = 2 *c $
  - No hay entero que haga valer la igualdad, entonces se intenta aproximar a $a$ por un múltiplo de 2, haciendo uso del resto (por ej. 1).
  - Si $a$ es impar, entonces $ \exists c \in \Z : a = 2 *c+1 $
  - $ a*(a-1) = (2*c+1)*(2*c+1-1)=(2*c+1)(2*c) $
  - Cómo $2c$ es par (explicado arriba), $ (2*c+1)*(2*c) $ es par y por lo tanto $ a*(a-1) $ es par. Por lo tanto, la afimración es verdadera. 

### (d) $ x|y $ y $ y|z $ entonces $ x|yz $

- Teniendo que $ x|y $ entonces $ \exists a \in \Z : y = x*a $.
- Teniendo que $ y|z $ entonces $ \exists b \in \Z : z = y*b $
- Y teniendo que $ x|yz $ entonces $ \exists c \in \Z : yz = x*c $
- Como $ \exists a \in \Z : y = x*a $ y $ \exists b \in \Z : z = y*b $ entonces $ \exists c \in \Z : yz = x*c $
  - $ y = x*a $
  - $ z = y*b $
  - $ yz = (x*a) * (y*b) = x * (a * y * b) = x * c$
    - $ c = a*y*b \in \Z $
- Por lo tanto $ \exists c \in \Z : yz = x*c \to x|yz $

## 3. Si a un número se lo divide por 5, el resto es 3 y si se lo divide por 7, el resto es 4. ¿Cuál es el resto si se lo divide por 35?

- $ n = 5*c_1+3 $
- $ n = 7*c_2+4 $
- $ n = 35*c + r \to $ Hay que ver cuál es ese r cuando se divide a nuetro n por 35.

Armamos un sistema de ecuaciones donde multiplicamos cada ecuación para obtener $ 35c_i $ en la igualdad de cada ecuación.

$$
\begin{cases}
7*n = 7*5*c_1 + 3*7 = 35*c_1 + 21 \\
5*n = 5*7*c_2 + 4*5 = 35*c_2 + 20
\end{cases}
$$

Multiplico ambas ecuaciones para que la resta entre ambas nos deje solo con n.

$$
\begin{cases}
3*(7*n) = 3 * 35 * c_1 + 21 * 3 \to 21*n = 35*(3*c_1) + 63 \\
4*(5*n) = 4 * 35 * c_2 + 20 * 4 \to 20*n = 35*(4*c_2) + 80
\end{cases}
$$

Hacemos la diferencia entre ambas ecuaciones.

$$
((21*n) = 35 * (3*c_1) + 63) - ((20*n) = 35 * (4*c_2) + 80) \to n = 35*(3*c_1 + 4*c_2) - 17
$$

- Podemos decir que $ (3*c_1 + 4*c_2) = c_3 \in \Z $ y nos queda: $ n = 35*c_3 - 17 $

Hasta el momento esto es erróneo, ya que no es correcto que el resto sea negativo (debe ser $ 0 \le r \le |35| $). Reescribimos la ecuación sumando y restando 35 a la ecuación.

$$
n = 35*(3*c_1 + 4*c_2) - 17 + 35 - 35 \to n = 35*(3*c_1 + 4*c_2) -35 + 18
$$

- Factor común de $ 35c_3 - 35 $

$$
n = 35*(c_3-1)+18
$$

- Cómo $ c = (c_3 - 1) \in \Z $

$$
n = 35*c+18
$$

Por lo tanto, el resto de 35|n es 18.

## 4. Sean a y b dos números enteros que tienen restos 4 y 7 respectivamente en la división por 11. Hallar los restos de la división por 11 de (a + b²)

- $ 11|a \to a = 11 * c_1 + 4 $
- $ 11|b \to b = 11 * c_2 + 7 $
- $ (a+b²) = 11 * c + r $

En la ecuación de $ (a+b²) $ reemplazamos las fórmulas de $ a $ y de $ b $.

$$
(a+b²) = (11*c_1+4) + (11*c_2+7)² 
$$

- Binómio al cuadrado:

$$
11*c_1 + 4 + (11*c_2)² + 2+11*c_2+7 + 7² = (11*c_1 + 11*c_2 * 11*c_2 + 2 * 11_c2 * 7) + 53 = 11 * (c_1 + c_2² + 14*c_2) + 53
$$

- Podemos decir que $ (c_1 + c_2² + 14*c_2) = c_3 \in \Z $. Nos quedaría:

$$
(a+b²) = 11 * c_3 + 53
$$

Hasta el momento esto es erróneo, ya que no es correcto que el resto sea mayor que el divisor (debe ser $ 0 \le r \le |11| $). Para obtener un valor válido, debemos reescribir la ecuación.
- Podemos escribir a 49 como $ 11+11+11+11+9 $

$$
(a+b²) = 11 * c_3 + 11 + 11 + 11 + 11 + 9
$$

- Factor común en $ 11 * c_3 + 11 + 11 + 11 + 11 $

$$
(a+b²) = 11 * (c_3 + 4) + 9
$$

- Cómo $ (c_3 + 4) = c \in \Z $, entonces:

$$
(a+b²) = 11 * c + 9
$$

Entonces, llegamos a que el resto de $ 11|(a+b²) $ es 9.

## 5. Convertir los siguientes números de base 10 a base 8:

### (a) 98

- $ 98|8 \to 98 = 8*12+2 $
- $ 12|8 \to 12 = 8*1+4 $
- $ 1|8 \to 1 = 8*0+1 $

- 98 en base 8 es 142

### (b) 44

- $ 44|8 \to 44 = 8*5+4 $
- $ 5|8 \to 5 = 8*0+5 $

- 44 en base 8 es 54

### (c) 20

- $ 20|8 \to 20 = 8*2+4 $
- $ 2|8 \to 2 = 8*0+2 $

- 20 en base 8 es 24.

## 6. Calcular el máximo común divisor entre:

### (i) (16, 24)

Descomponemos cada entero en producto de primos y buscamos los factores que tienen en común.

- $ 16 = 2 * 2 * 2 * 2 $
- $ 24 = 2 * 2 * 2 * 3 $
- El mayor factor común y máximo común divisor entre 16 y 24 es $ 2*2*2 = 2³ = 8 $.

### (ii) (70, 50)

- $ 70 = 2 * 5 * 7 $
- $ 50 = 2 * 5 * 5 $
- El mayor factor común y máximo común divisor entre 70 y 50 es $ 2*5 = 10 $

### (iii) (121, 88)

- $ 121 = 11 * 11 $
- $ 88 = 11 * 2 * 2 * 2 $
- El mayor factor común y máximo común divisor entre 121 y 88 es 11.

### (iv) (−90, 90)

- Cómo el 90 es divisor de -90 (y de sí mismo), el MCD entre ambos es 90. 

### (v) (980, 224)

- $ 980 = 2 * 2 * 5 * 7 * 7 $
- $ 224 = 2 * 2 * 2 * 2 * 2 * 7  $
- El mayor factor común y MCD entre 980 y 224 es $ 2 * 2 * 7 = 28 $

## 7. Probar que si a y b son enteros:

### (a) a + b es coprimo con a

Queremos probar que $ (a+b,a) = 1 $. Es decir que el MCD entre $ (a+b) $ y $ a $ es 1.
- Por definición de MCD, $ (a+b,a) = d $ cumple:
  - $ d|a+b $, o sea, $ \exists m_1 \in \Z : a+b = d*m_1 $
  - $ d|a $, es decir, $ \exists m_2 \in \Z : a = d*m_2 $
- Como $ a+b = d*m_1 $, restando $ a $ a ambos lados de la ecuación nos queda:

$$
b = d * m_1 - a = d * m_1 - d * m_2 = d * (m_1 - m_2)
$$

- Podemos decir que $ m_1 - m_2 = c \in \Z$
  - $ b = d * c $
- Lo que implica que $ d|b $
- Si $ d|a + b $ y $ d|a $, entonces $ d|b $ y $ d|a $ entonces $ d|(a,b) $
- Por el enunciado, sabemos que $ (a,b) = 1 $, por lo tanto, debería ser que $ d = 1 $, entonces $ (a+b,a) = 1 $, o sea, llegamos a que $ a+b $ es coprimo con $ a $.

### (b) si a es no nulo, (a, 0) = |a|

Tenemos que $ a, 0 \in \Z $ si $ a $ es no nulo. El enunciado dice que hay un $ d \in \Z$ tal que $ d $ es el MCD de $ a $ y $ 0 $ si $ d > 0 $.
- Entonces $d|a$ y $d|0$
- Si hubiera un $ c \in Z $ tal que $c|a$ y $c|0$ entonces $c|d$.

El 0 es divisible por todos los enteros, entonces siempre se cumple que $ d|0 $, tenemos que buscar un $ d $ mayor a 0 de modo tal que $ d|a $ y que exista otro $ c $ tal que $ c|a $ y $ c|d $.
Tenemos que encontrar un $ q $ tal que $ q \in \Z : a = d * q $.
- Si $ a > 0, d = |a| $ y $ q = 1 $ se cumple que $ a = |a| * 1 $
- Si $ a < 0, d = |a| $ y $ q = -1 $ se cumple que $ a = |a| * q $

En ambos casos, el valor de $ d $ es $ |a| $. Esto es así porque para cualquier otro conjunto de valores de $ d $ y $ q $ no se cumple la igualdad $ a = d * q $ a la vez que se cumple la definción del MCD.
- Necesariamente $ d = |a| $, por lo tanto, $ a $ es distinto de 0 y $ (a,0) = |a| $ es verdadero.

### (c) (a, b) = 1 entonces ma+nb=k, con m,n y k enteros.

- Por el enunciado, sabemos que $ (a,b) = 1 $ y, que existen enteros $ m_1 $ y $ n_1 $, tal que: $ m_1a+n_1b = 1 $
  - Esto es así por la Identidad de Bézout.
- Multiplicamos $ k $ en ambos lados de la ecuación:
  $$
  k * m_1a + k * n_1b = 1k \to (km_1)a + (kn_2)b = k
  $$
- Como $ km_1 = m \in \Z $ y $ kn_2 = n \in \Z $, nos quedaría:
  $$
  ma + nb = k
  $$
- Se demostró que si $ (a,b) = 1 $ entonces $ ma+nb = k $. 

## 8. Hallar mcd(5k + 3, 3k + 2), para cualquier k entero

Hay que encontrar un $ d \in \Z: d > 0 $ tal que, para cualquier k, se cumpla que:
- $ d|5k+3 $, o sea, $ \exists c_1 \in Z : 5k + 3 = d * m_1 $
- $ d|3k+2 $, o sea, $ \exists c_2 \in Z : 3k + 2 = d * m_2 $
- Hay otro $ D $ tal que $ D|5k+3 $ y $ D|3k+2 $ entonces $D|d$

Multiplicamos en ambos lados de las dos ecuaciones para lograr que los coeficientes k tengan el mismo valor para sacar el término k cuando las restemos.
- $ 3*5k + 3*3 = 3*d*c_1 \to 15k + 9 = 3 * d * c_1 $
- $ 5 * 3c_2 + 5*2 = 5*d*c_2 \to 15k + 10 = 5*d*c_2 $

Restamos las ecuaciones:

$$
15k+9 = 3*d*c_1 - (15k + 10 = 5*d*c_2)
$$

- Resultado: $ -1 = (3*d*c_1 - 5*d*c_2) $
- Podemos decir que $ (3*c_1 - 5*c_2) = c \in \Z $ y nos quedaría: $ -1 = d(3c_1-5_c2) \to -1 = d*c $

Para que la igualdad sea válida $d = 1$ y $c=-1$ (o al reves). Con otros valores, la igualdad no se cumple
Por la definción de MCD, $ d $ _tiene_ que ser positivo, por lo que si o si $ d = 1 $.
Entonces, $ (5k+3,3k+2) = 1 $, para todo $ k $.
Por lo tanto, $ 5k+3 $ y $ 3k+2 $ son coprimos.
 

## 9. Sean a, b ∈ Z y sea p primo. Demostrar que si p|ab entonces p|a o p|b. Mostrar que esto no se cumple si p no es primo.

Teniendo que $ p|ab $ por definición de divisibilidad se cumple que $ \exists c \in Z: a * b = p * c $
Lo mismo para $ p|a $ y $ p|b $
- $ \exists d \in Z: a = p * d $
- $ \exists e \in Z: b = p * e $
Basandonos en el _Teorema Fundamental de la Aritmética_, siendo $ a $ y $ b $ distintos de 0, 1 y -1, son productos finito de números primos y la factorización es única salvo el orden:
- $ a = \varPi^n_{i=1} p^{a^i}_i  $
- $ b = \varPi^n_{j=1} q^{a^j}_j $

Si $p$ no es uno de los factores primos en la factorización de $ a $ entonces $ (a,p) = 1 $.

Con la Identidad de Bézout, sabemos que existen $ m, n \in \Z $ tales que: $ 1 = am+pn $

Si multiplicamos por $ b $ en ambos lados obtenemos:

$$
b = a*b*m + p*n*b
$$

Por hipótesis, sabemos que $ a*b=p*c $, podemos reemplazar $ a*b $ en nuestra ecuación:

$$
b = p*c*m + p*n*b \to b = p*(c*m+n*b)
$$

Podemos decir que $ (c*m+n*b) = x \in \Z $, entonces:

$$
b = p*x
$$

Por lo tanto, se cumple que $ p|b $.
Se demostró que si $ p|ab $ y $p$ no divide a $a$, entonces $p$ seguro divide a $b$.
Trivialmente, podemos demostrar que si $p|ab$ y $p$ no divide a $b$, entonces seguro $p$ divide a $a$.

Si $p$ no es primo, no se cumple.
- Supongamos que $ p = 6 $, $ a = 2 $ y $ b = 3 $.
- $ a*b=2*3=6 \to $ se cumple que $ 6|6 $ porque $ \exists c \in \Z : 6 = 6 * c \land c = 1 $
- No se cumple que 6|2 ya que $ \nexists c \in \Z : 2=6*c $.
- Tampoco se cumple que 6|3 ya que $ \nexists c \in \Z : 3=6*c $

A través del contraejemplo, demostramos que si $ p $ no es primo, puede dividir a $ a*b $ pero no puede dividir a los factores por separado.

## 10. Hallar, si existe, un número entero $ q $ tal que $7290*q$ es el cubo de un entero.

El enunciado pide encontrar un $ q $ entero de manera tal que $ 7290 * q = x³ $

- Podemos reescribir a 7290 descomponiendolo en factores primos: $ 7290 = 2 * 3⁶ * 5 $
- Para que $ 7290  * q = x³ $, los exponentes de la descomposición de 7290 en factores primos deben ser múltiplos de 3.
  - Para 2 necesitamos elevarlo a la 2³, así que necesitamos 2²
  - 3⁶ está bien porque es múltiplo de 3.
  - Para el 5 pasa lo mismo que el 2, necesitamos 5².
- Del enunciado tenemos $ 7290 * q $. Podemos interpretar a $ q $ como lo que planteamos antes (la necesidad de cada factor primo para tener un exponente múltiplo de 3).

$$
q = 2² * 5² = 100
$$

- Entonces $ q = 100 $ para que se de que $ 7290 * q = x³ $

$$
7290 * 100 = x³ \to \sqrt[3]{7290 * 100} = \sqrt[3]{x³} \to \sqrt[3]{(2*3⁶*5) * (2²*5²)} = \sqrt[3]{x³} \\
 \sqrt[3]{2³*3⁶*5³} =  \sqrt[3]{x³} \to 2*3²*5 = x \to 90 = x \to x³ = 90³ = 729000
$$

## 11. Demostrar que dados $ a $ y $ b $ en $ Q $ tales que $ a < b $, existe otro número racional x tal que $ a < x < b $.

El enunciado nos da $ a $ y $ b $, y nos dice que $ a < b $:
- Sumando $ a $ a ambos lados de la desigualdad tenemos: $ a + a < b + a \to 2a < b+a $
- De manera trivial si sumamos b a ambos lados: $ a+b < 2b $

Ambas desigualdades poseen $ a+b $, juntandolas nos quedaría:

$$
2a < a+b < 2b
$$

- Aprovechando que tenemos $ 2a $ y $ 2b $, podemos multiplicar $ \frac{1}{2} $ a toda la expresión.

$$
\frac{2a}{2} < \frac{a+b}{2} < \frac{2b}{2} \to a < \frac{a+b}{2} < b
$$

- Encontramos al otro número racional $ x $, siendo $ x = \frac{a+b}{2} \land a < x < b $.

## 12. Probar que no existe un número racional cuyo cubo sea igual a 2.

Sea $ r = \frac{p}{q} $ con $ p \in \Z $, $ q \in \Z \land q \ne 0 $, siendo $ \frac{p}{q} $ el _representante canónico_ de r (fracción irreducible).

- Si $ r³ = 2 $ entonces $ (\frac{p}{q}³) = 2 \to \frac{p³}{q³} = 2 $.
- Despejando $ q³ $ quedaría: $ p³ = 2 * q³ $
- Podemos ver que $ p³ $ es un número par (el cubo de un número impar es impar). Lo podemos ver como $ p = 2*c $ siendo $ c \in \Z $.
- Sustituimos:
$$
(2c)³ = 2q³ \to 8c³ = 2q³
$$
- Despejamos al 2:
$$
4c³ = q³ \to 2*2*c³ = q³
$$
- Podemos ver que $ q³ $ es divisible por 2, entonces también es par y lo podemos escribir como $ q = 2*d $ siendo $ d \in \Z $.
- $ p $ y $ q $ son pares, lo que se contradice con lo que dijimos al principio, que $ \frac{p}{q} $ no es una fracción irreducible. Entonces, llegamos a que no existe un número racional cuyo cubo sea igual a 2.

## 13. Indique la parte real Re(z) y la parte imaginaria Im(z) de los siguientes complejos:

### a) $ \sqrt{-49} $

$$
\sqrt{-49} = \sqrt{49} * \sqrt{-1} = 7 * \sqrt{-1} = 7*i = 0 + 7i
$$

- $ Re(z) = 0 $
- $ Im(z) = 7 $

### b) $ \sqrt{-20} $

$$
\sqrt{-20} = \sqrt{5} * \sqrt{4} * \sqrt{-1} = 2*\sqrt{5}*i = 0 + 2\sqrt{5}i
$$

- $ Re(z) = 0 $
- $ Im(z) = 2\sqrt{5} $

### c) $ \sqrt{-\frac{9}{16}} $

$$
\sqrt{-\frac{9}{16}} = \sqrt{\frac{9}{16}} * \sqrt{-1} = \frac{3}{4} * \sqrt{-1} = 0 + \frac{3}{4}i
$$

- $ Re(z) = 0 $
- $ Im(z) = \frac{3}{4} $

### d) $ z = −8 $

$$
z = -8 = -8 + 0i
$$

- $ Re(z) = -8 $
- $ Im(z) = 0 $

### e) $ z = 7i $

$$
z = 7i = 0 + 7i
$$

- $ Re(z) = 0 $
- $ Im(z) = 7 $

### f) $ z = (3 + i) + (5 − 4i) $

$$
z = (3+i)+(5-4i) = 8-3i
$$

- $ Re(z) = 8 $
- $ Im(z) = -3 $

### g) $ z = 3i − (5 − 2i) $

$$
z = 3i - (5-2i) = -5 +5i
$$

- $ Re(z) = -5 $
- $ Im(z) = 5 $

### h) $ \frac{1+3i}{3−i} $ 

$$
\frac{1+3i}{3−i} = \frac{1+3i}{3−i} * \frac{3+i}{3+i} = \frac{(1+3i)*(3+i)}{(3-i)*(3+i)} = \frac{3+i+9i+3i²}{9+3i-3i-i²} = \frac{3+10i+3i²}{9-i²} 
$$

- Por definición de $ i² = -1 $

$$
\frac{3+10i+3*(-1)}{9-(-1)} = \frac{10i}{10} = i
$$

- $ Re(z) = 0 $
- $ Im(z) = 1 $

### i) $ \frac{1−i}{(1+i)²} $

$$
\frac{1-i}{(1+i)²} = \frac{1-i}{1²+2*1*i+i²}
$$

- Por definición $ i² = -1 $

$$
\frac{1-i}{2i} = \frac{1-i}{2i} * \frac{-2i}{-2i} = \frac{(1-i)*(-2i)}{-4i²} = \frac{-2i+2i²}{4} = \\ \frac{-2i-2}{4} = -\frac{2}{4}i-\frac{2}{4} = -\frac{1}{2}i-\frac{1}{2}
$$

- $ Re(z) = -\frac{1}{2} $
- $ Im(z) = -\frac{1}{2} $

## 14. La suma de un número complejo y su conjugado es −8 y la suma de sus módulos es 10. De qué números complejos se trata?

Sabemos que $ z = a + i*b $
- Siendo $ a, b \in \R $
- El conjugado es $ \bar{z} = a - i*b $
- Del enunciado tenemos que $ z + \bar{z} = -8 $ y $ |z| + |\bar{z}| = 10 $.

$$
z + \bar{z} = -8 \to a+ib+(a-ib) = -8 \to 2a = -8 \to a = -4
$$

$$
|z| + |\bar{z}| = 10 \to \sqrt{a^2+b^2} + \sqrt{a^2+(-b^2)} = 10 \to 2*\sqrt{a^2+b^2} = 10 \to \sqrt{a^2+b^2} = 5
$$

- Reemplazando $ a = -4 $

$$
\sqrt{16+b^2} = 5 \to 16+b^2 = 25 \to b^2 = 9 \to b = \sqrt{9} \to |b| = \pm 3
$$

Entonces, tenemos dos z:
- $ z_1 = -4 + 3i $
- $ z_2 = -4 - 3i $

## 15. Encuentre $ x $ e $ y $ tales que:

### a) $  x − 15i = 9 + 5yi $

En el lado izquierdo de la igualdad:
- $ Re(z) = x $
- $ Im(z) = -15 $

En el lado derecho de la igualdad:
- $ Re(z) = 9 $
- $ Im(z) = 5y $

Igualamos las partes reales y las partes imaginarias:
- $ x = 9 $
- $ -15 = 5y $

Ya tenemos que $ x = 9 $. Ahora despejamos a $ y $:

$$
y = \frac{-15}{5} \to y = -3
$$


### b) $ 2x + 3yi = 6 + yi $

En el lado izquierdo de la igualdad:
- $ Re(z) = 2x $
- $ Im(z) = 3y $

En el lado derecho de la igualdad:
- $ Re(z) = 6 $
- $ Im(z) = y $

Igualamos las partes reales y las partes imaginarias:
- $ 2x = 6 \to x = \frac{6}{2} \to x = 3 $
- $ 3y = y \to 3y - y = 0 \to 2y = 0 \to y = 0/2 \to y = 0 $

## 16. Hallar, si existe, x real tal que Re(z) = Im(z) siendo $ z = \frac{x+2i}{4−3i} $

Al ser una fracción, no podemos separar a la parte real de la parte imaginaria (por el denominador).
Multiplicamos por el conjugado del denominador:

$$
\frac{x+2i}{4−3i} * \frac{4+3i}{4+3i} = \frac{(x+2i)*(4+3i)}{(4-3i)*(4+3i)} = \frac{4x+3xi+2i*4+6i^2}{16+3i4-3i4-9i^2} = \\
\frac{4x+3xi+8i-6}{25} = \frac{4x-6+i*(3x+8)}{25}
$$

Al hacer esto, podemos separar la parte real de la parte imaginaria:
- $ Re(z) = \frac{4x-6}{25} $
- $ Im(z) = \frac{3x+8}{25} $

Ahora, igualamos ambas partes:

$$
\frac{4x-6}{25} = \frac{3x+8}{25} \to \frac{4x-6}{25} - (\frac{3x+8}{25}) = 0 \to \frac{x - 14}{25} = 0 \to x - 14 = 0 * 25 \\
\to x-14 = 0 \to x = 14
$$

Entonces, llegamos a que $ x = 14 $

## 17. Encontrar, si existe, un valor de k real para que el complejo $ \frac{2−(1+k)i}{1−ki} $ sea un número real.

Igual que antes, multiplicamos por el conjugado del denominador.

$$
\frac{2−(1+k)i}{1−ki} * \frac{1+ki}{1+ki} = \frac{(2−(1+k)i)*(1+ki)}{(1-ki)*(1+ki)} = \frac{2(1+ki)-(1+k)i(1+ki)}{1^2-(ki)^2} = \\
\frac{2(1+ki)-(1+k)(i+ki^2)}{1+k^2} = \frac{2(1+ki-(1+k)(i-k))}{1+k^2} = \frac{2+2ki-(i-k+ki-k^2)}{1+k^2} = \frac{2+2ki-i+k-ki+k^2}{1+k^2} = \frac{(2+k+k^2)+(2k-1-k)*i}{1+k^2}
$$

No tenemos la parte imaginaria en el denominador, además pudimos separar a la parte real de la parte imaginaria.

Para que $ z $ sea un número real, la parte imaginaria debería ser cero. Lo que significaría que $ i $ en el numerador sea igual a 0.

$$
\frac{(2k-1-k)}{1+k^2} = 0 \to 2k-1k = 0 * (1+k^2) \to 2k-1-k = 0 \to k = 1
$$

Encontramos real de k, donde si $ k = 1 $, la parte imaginaria es igual a 0.

## 18. Calcular las siguientes potencias:

### a) $ i^{489} $

$$
i^{489} = i^{4*122+1} = i^{4*122} * i^1 = (i^4)^{122} * i = 1^{122} * i = i
$$

### b) $ −i^{1026} $ 

$$
-i^{1026} = -1 * i^{1026} = -1 * i^{4*256+2} = -1 * (i^4)^{256} * i^2 = -1 * 1^{256} * -1 = 1
$$

### c) $ (3i)^{168} $

$$
(3i)^{168} = (3i)^{4*42} = 3^{168} * (i^4)^{42} = 3^{168} * 1^{42} = 3^{168}
$$

## 19. Dados los siguientes n´umeros complejos, encontrar la forma más adecuada para realizar las operaciones pediddas:

$$ 
z_1 = 3 + 3i \quad z_2 = −1 + i \quad z_3 = 5 + 4i \quad z_4 = 9 \quad z_5 = 5i \quad z_6 = −7 \\
z_7 = −4 − 4i \quad z_8 = −8i \quad z_9 = 2 − 2i \quad z_{10} = 3 − 4i
$$

### a) $ z_1 + z_7 $

$$
z_1 + z_7 = (3+3i) + (-4 -4i) = -1-i
$$

### b) $ z_5 − z_3 $

$$
z_5 - z_3 = (5i) - (5+4i) = -5+i
$$

### c) $ z_9*z_6 $ 

$$
z_9*z_6 = (2-2i) * (-7+0i) = -14 + 14i
$$

### d) $ z_8/z_{10} $ 

$$
\frac{z_8}{z_{10}} = \frac{-8i}{3-4i} = \frac{-8i}{3-4i} * \frac{3+4i}{3+4i} = \frac{(-8i)*(3+4i)}{(3-4i)*(3+4i)} \\
= \frac{-24i-32i^2}{9+12i-12i-16i^2} = \frac{32-24i}{25} = \frac{32}{25} - \frac{24}{25}i
$$

### e) $ z_3 + z_6 $

$$
z_3 + z_6 = (5+4i) + (−7+0i) = -2+4i
$$

### f) $ z_2 − z_6 $

$$
z_2 - z_6 = (−1 + i) - (−7+0i) = 6+i
$$

### g) $ z_3*z_{10} $

$$
z_3 * z_{10} = (5+4i) * (3−4i) = 15-20i+12i-16i^2 = 15 - 8i + 16 = 31 - 8i
$$

### h) $ z_1³ $



### i) $ z_9⁹ $



### j) $ z^{15}_5 $



### k) $ z³_{10} $



### l) hallar las ra´ıces cuartas de z2



### m) hallar las ra´ıces c´ubicas de z4



### n) hallar las ra´ıces s´eptimas de i



# Ejercicios Adicionales

## 1. Sean a y b dos enteros coprimos, demostrar que :
### (a) (a, a + 1) = 1
### (b) a + b y ab son coprimos
### (c) a|c y b|c entonces ab|c

## 2. Demostrar que : Si (a, b) = d ; a|c y b|c entonces ab|cd
## 3. El resto de la divisi´on de un n´umero por 7 es 2; si se lo divide por 3, su resto es 1. ¿Cu´al es el resto si se lo divide por 21?

## 4. * Intente codificar (en el lenguaje que Ud prefiera) el algoritmo de Euclides. Pruebe que funciona con alguno de los ejercicios

## 5. * Investigue que dice La criba de Erat´ostenes y trate de escribir un c´odigo que realice el procedimiento.

## 6. Sean u y v n´umeros racionales. Probar que:

### (a) u + v ∈ Q y u − v ∈ Q
### (b) u.v ∈ Q
### (c) Si u es no nulo, u−1 ∈ Q

## 7. Dados a, b, c, d ∈ Z , suponiendo que los denominadores no se anulen y que a b = c d no es cero, probar:

### (a) $ \frac{a}{c} = \frac{b}{d} $ y $ \frac{b}{a} = \frac{d}{c}$

### (b) $ \frac{a+b}{b} = \frac{c+d}{d} $ 

### (c) $ \frac{a-b}{b} = \frac{c-d}{d} $ 

## 8. Demostrar que si p es primo y n ∈ N , entonces n √p es irracional

## 9. La suma de dos n´umeros complejos es 6, el m´odulo del primero es √13 y el del segundo es 5. De qu´e n´umeros complejos se trata?

## 10. Demostrar que para cualquier complejo z vale que

### • z.z = |z|2

### • z + z = 2Re(z)

### • z − z = 2Im(z)i

## 11. Encontrar el valor de h para que el complejo $ \frac{1+3hi}{7+(h−2)i} $ sea un imaginario puro.

## 12. Realizar las operaciones con los complejos del ´ultimo ejercicio (antes de los adicionales):

### *) hallar las ra´ıces c´ubicas de z5

### **) hallar las ra´ıces quintas de z6

### ***) hallar las ra´ıces s´eptimas de z8