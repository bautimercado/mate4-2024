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
- Por lo tanto $ \nexists n \in \Z : n$ es par e impar. 

## 2. Analizar si las siguientes afirmaciones son verdaderas o falsas:

### (a) Si $ a|1 $ entonces $ a = 1 $ o $ a = −1 $

- $ a|1 $ si $ \exists c \in \Z : 1 = a*c$
- Si $ a = -1 \to -1|1 $ entonces $ \exists d \in \Z : 1 = -1 * d $
- Si $ a = 1 \to 1|1 $ entonces $ \exists c \in \Z : 1 = 1 * c $

Como $ \exists c \in \Z : 1 = a*c $.
- Entonces $ -1|1 $ o $ 1|1 $.
- También $ \exists d \in \Z:1=-1*d \lor \exists e \in \Z: 1=1*e $

- Teniendo que $ 1 = -1 * d \to \frac{1}{-1} = d \to -1 = d $
- Y teniendo que $ 1 = 1 * e \to \frac{1}{1} = e \to 1 = e $ 
- Se demostró que $ \exists d = -1 \in \Z : 1 = (-1) * (-1) $ y que $ \exists e = 1 \in \Z : 1 = 1 * 1 $
- Por lo tanto, si $ a|1 $ entonces $ a = 1 $ o $ a = -1 $
- Conclusión: La afirmación es verdadera.

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

### (c) (a, b) = 1 entonces ma+nb=k, con m,n y k enteros.

## 8. Hallar mcd(5k + 3, 3k + 2), para cualquier k entero

## 9. Sean a, b ∈ Z y sea p primo. Demostrar que si p|ab entonces p|a ´o p|b Mostrar que ´esto no se cumple si p no es primo.

## 10. Hallar, si existe, un n´umero entero q tal que 7290q es el cubo de un entero.

## 11. Demostrar que dados a y b en Q tales que a < b, existe otro n´umero racional x tal que a < x < b.

## 12. Probar que no existe un n´umero racional cuyo cubo sea igual a 2.

## 13. Indique la parte real Re(z) y la parte imaginaria Im(z) de los siguientes complejos:

### a) $ \sqrt{-49} $ 

### b) $ \sqrt{-20} $

### c) $ \sqrt{-\frac{9}{16}} $ 

### d) $ z = −8 $

### e) $ z = 7i $

### f) $ z = (3 + i) + (5 − 4i) $

### g) $ z = 3i − (5 − 2i) $

### h) $ \frac{1+3i}{3−i} $ 

### i) $ \frac{1−i}{(1+i)²} $

## 14. La suma de un n´umero complejo y su conjugado es −8 y la suma de sus m´odulos es 10. De qu´e n´umeros complejos se trata?

## 15. Hallar, si existe, x real tal que Re(z) = Im(z) siendo z = x+2i 4−3i

## 16. Encontrar, si existe,un valor de k real para que el complejo 2−(1+k)i 1−ki sea un n´umero real.

## 17. Calcular las siguientes potencias:

### a) i489 

### b) −i1026 

### c) (3i)168

## 18. Dados los siguientes n´umeros complejos, encontrar la forma m´as adecuada para realizar las operaciones pediddas:

$$ 
z_1 = 3 + 3i \quad z_2 = −1 + i \quad z_3 = 5 + 4i \quad z_4 = 9 \quad z_5 = 5i \quad z_6 = −7 \\
z_7 = −4 − 4i \quad z_8 = −8i \quad z_9 = 2 − 2i \quad z_{10} = 3 − 4i
$$

### a) $ z_1 + z_7 $
### b) $ z_5 − z_3 $
### c) $ z_9*z_6 $ 
### d) $ z_8/z_{10} $ 
### e) $ z_3 + z_6 $
### f) $ z_2 − z_6 $
### g) $ z_3*z_{10} $
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