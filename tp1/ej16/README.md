# 16. Dada la función $$f(x,y) = x2 + y2 + 12 y − 2$$

## (a) Hallar el mínimo de la función de dos formas:

### i. Analítica: Calculando los puntos estacionarios.

Hecha en papel.

### ii. Numérica: Mediante el método de descenso del gradiente. Utilizar tolerancia de 0.0001, tamaño de paso 0.4 y punto de inicio x_0 = (10, 2).

## (b) ¿Cuántas iteraciones fueron necesarias para la convergencia del método del gradiente? Realice la búsqueda nuevamente pero con tamaño de paso 0.1 ¿Cuántas iteraciones fueron necesarias para la convergencia en este caso?

- Se hicieron 9 iteraciones.
- Con un tamaño de paso 0.1, se requirieron de 56 iteraciones.

## (c) ¿Qué ocurre si utilizamos el mismo tamaño de paso (0.4) de este punto para hallar el mínimo de la función del punto anterior?

- En este caso, el algoritmo entra en un loop infinito, debido a que la condición de corte nunca llega a ser verdadera (se va a puntos cada vez mayores).

## d) (Para pensar) A raíz del inciso anterior ¿Siempre se puede elegir el mismo tamaño de paso para cualquier función que estudiemos? ¿Qué ocurre cuando éste parámetro es muy grande o muy pequeño?

- No siempre se puede elegir el mismo tamaño de paso para cualquier función. Si el tamaño de paso es grande, se tienen menos iteraciones pero el código podría no funcionar.