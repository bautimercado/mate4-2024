# TP4 - Relaciones entre conjuntos

## 1. Sean los conjuntos A = {1, 0, −1} y B = {4, 3, 2, 1}. Decide si las siguientes corresponden a relaciones de A en B. Justifica.

### (a) R = {(1; 1), (0; 2)}

- Se corresponde, ya que el primer elemento de cada dupla pertenece al conjunto A y el segundo elemento de cada dupla pertenece al conjunto B.

### (b) R = {(−1; 1), (1; −1)}

- En la segunda dupla, el segundo elemento no pertenece al conjunto B. Por lo tanto esta R no se corresponde a la relación entre A y B.

### (c) R = {(−1; 1), (−1; 2), (−1; 3)}

- Es válida, ya que -1 pertenece al conjunto A y 1, 2 y 3 pertenecen al conjunto B.

### (d) R = {(4; 1)}

- No se corresponde a una relación entre A y B ya que 4 no es un componente del conjunto A.

### (e) R = ∅

- Si se corresponde, ya que el vacío se incluye en todos los conjuntos.

## 2. Sea A = {−3, −2, −1, 0, 1, 2, 3}, B = Z y la relación de A en B que viene definida en la forma: $ xRy $ si y sólo si $ y $ es el cuadrado de $ x $. Escribe R por extensión. Define R^{−1} por comprensión y por extensión.

<u>$ R $ por extensión:</u>

$$
R = \{ (-3,9), (-2, 4), (-1, 1), (0,0), (1,1), (2,4), (3,9) \}
$$

<u>$ R^{-1} $ por comprensión:</u>

$$
R^{-1} = \{ (y,x):(x,y) \in \R \} \\
R^{-1} = \{ (y,x): y \in B \land x \in A \land (y = x^2) \}
$$

<u>$ R^{-1} $ por extensión:</u>

$$
R^{-1} = \{ (9,-3), (4, -2), (1, -1), (0,0), (1,1), (4, 2), (9, 3) \}
$$

## 3. Sean los conjuntos A = {a, b, c, d, e} , V = {vocales} y B = {1, 2, 3}. Decide si las siguientes corresponden a relaciones. Justifica.

### (a) R = {(a, a, a); (a, b, c); (b, c, d)} en A × A × A

- Es una relación válida, ya que los elementos de cada tupla está en AxAxA.

### (b) R = {(a, a, a); (c, e, 2); (a, b, 1)} en A × V × B

- La relación no es válida, podemos ver que en el tercer componente de la primera tupla hay una letra (que no está en el conjunto B).
- Además, en el segundo componente de la tercera tupla hay una "b" que no pertenece al conjunto V.

### (c) R = {(a, b, 1); (e, c, 2) : (i, j, 3)} en V × A × B

- La relación no es válida, ya que en el segundo componente de la tercer tupla hay una "j" que no pertenece al conjunto A.

### (d) R = {(a, z, 3); (b, i, 2); (c, x, 1)} en A × V × B

- La relación no es válida, ya que los segundos componentes de la primera y tercera tupla no pertenecen al conjunto V.

## 4. Sea A = {1, 2, 3} y la relación R en A × A × A definida en la forma: (x, y, z) ∈ R si y sólo si x < y & y < z , siendo < el ”menor” usual entre números reales. Escribe R por extensión

$$
R = \{ (1, 2, 3) \}
$$

## 5. Para cada una de las siguientes relaciones: dar tres pares que pertenezcan y tres pares que no; indicar si son reflexivas, simétricas, antisimétricas, y/o transitivas.

### (a) En el conjunto de los números reales

#### xRy si y sólo si x ≥ 4 & y ≥ 5 .

<u>Pares que pertenecen:</u>

- $ (4,5) $
- $ (5,6) $
- $ (6,7) $

<u>Pares que no pertenecen:</u>

- $ (5,4) $
- $ (2, 10) $
- $ (hola, chau) $

No es reflexiva, no se cumple que xRx
- Contraejemplo: $ x = 4 \to (4,4) \notin R $

No es simétrica, no se cumple que xRy entonces yRx
- Contraejemplo: $ (4,5) \in R \to (5,4) \in R $
- El antecedente es verdadero pero el consecuente es falso, por lo tanto, la implicancia es falsa.

No es antisimétrica, ya que no se cumple que xRy e yRx implican x = y.
- Contraejemplo: $ (5,6) \in R \land (6,5) \in R \to 5 = 6  $
- El antecedente es verdadero pero el consecuente es falso, por lo tanto, la implicancia es falsa.

La relación es transitiva, para todo $ (x,y,z) \in \R $, se cumple que $ xRy \land yRz \to xRz $
- Vale $ xRy $ ya que $ x \ge 4 \land y \ge 5 $.
- Vale $ yRz $ ya que $ y \ge 4 \land z \ge 5 $.
- Como $ x \ge 4 $ y $ z \ge 5 $, entonces se cumple que $ xRz $.
- Entonces, tanto el antecedente como el consecuente son verdaderos, por lo tanto la implicación se cumple y se concluye con que se cumple la transitividad.

#### xRy si y sólo si y ≤ x ≤ y + 3 .

<u>Pares que pertenecen</u>

- $ (3, 1) $
- $ (2, 2) $
- $ (5, 2) $

<u>Pares que no pertenecen:</u>

- $ (0, 1) $
- $ (10, 2) $
- $ (hola, 8) $

La relación es reflexiva, para todo $ x \in \R $ se cumple que xRx.
- d Al ser una relación $ \le $, se va a cumplir, ya que todo x es menor o igual que sí misma, y la suma de ese x con 3 es mayor que si misma.

La relación no es simétrica, no se cumple que para todo $ (x,y) \in \R : xRy \to yRx$
- Contraejemplo: $ (3,1) \in R \to (1,3) \in R $
- Como el antecedente es verdadero pero el consecuente es falso, no se cumple la implicancia, por lo tanto no es simétrica.

La relación es antisimétrica, ya que se cumple que para todo $ (x,y) \in R : xRy \land yRx \to x = y $.
- Sean $ (x,y) \in R : x = y $, se cumple que $ xRy \land yRx $ (porque la relación es reflexiva).
- Sean $ (x,y) \in R : x < y $, se cumple que $ x \le y \le x+3 $ por lo tanto $ yRx $ pero no se da que $ xRy $ (porque $ x < y $). Entonces, el antecedente es falso pero la implicancia se cumple.
- Sean $ (x,y) \in R: y < x $, se cumple que $ y \le x \le y+3 $ y por lo tanto $ xRy $ pero no se da que $ yRx $ (porque $ y < x $). Entonces, el antecedente es falso pero la implicancia se cumple.

La relación no es transitiva, ya que no se cumple que para todo $ (x,y,z) \in R : xRy \land yRz \to xRz $
- Contraejemplo: $ (10, 7) \in xRy \land (7,4) \in yRz \to (10,4) \in xRz $
- Como el antecedente es verdadero y el consecuente es falso, la implicancia es falsa, por lo tanto no es transitiva.

### (b) Sean A = {1, 2, 3, 4} y P(A) el conjunto de partes de A

$$
P(A) = \{ (\empty),(1),(2),(3),(4),(1,2),(1,3),(1,4),(2,1),(2,2)(2,3),(2,4), \\ (3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(1,1,1)(1,1,2),(1,1,3), \\ (1,1,4),..., (1,2,3,4) \}
$$

#### En P(A), xRy si y sólo si x ∩ y = ∅

<u>Pares que pertenecen</u>

- {(1),(2,3)}
- {(2),(3,4)}
- {(1,2,3),(4)}

<u>Pares que no pertenecen:</u>

- ({2,2},{2,2})
- ({1,1},{1,1})
- ({1,2,3},{3,2,1})

La relación no es reflexiva, no se cumple que para todo $ x \in P(A) $ que $ xRx $.
- Contraejemplo: $ (\{1\}) \in P(A) $ pero $ (\{1\},\{1\}) \notin R$.

La relación si es simétrica, se da que para todo $ (x,y) \in P(A) : xRy \to yRx $
- Si $ xRy $ vale, entonces se cumple que $ x \cap y = \empty $.
- Como la intersección es conmutativa, se puede $ y \cap x = \empty $, entonces $ yRx $.
- Por lo tanto $ xRy \to yRx $.

La relación no es antisimétrica, no se cumple que para todo $ (x,y) \in P(A) : xRy \land yRx \to x = y $.
- Contraejemplo: $ (\{1,2\}, \{3,4\}) \in R \land (\{3,4\},\{1,2\}) \in R \to \{1,2\} = \{3,4\} $
- Como el antecedente es verdadero y el consecuente es falso, la implicación es falsa, por lo tanto no es antisimétrica

La relación no es transitiva, no se cumple que para todo $ (x,y,z) \in P(A): xRy \land yRz \to xRz $
- Contraejemplo: $ (\{1,4\},\{2\}) \in R \land (\{2\},\{3,4\}) \in R \to (\{1,4\},\{3,4\}) \in R $.
- Como el antecedente es verdadero y el consecuente es falso, la implicancia es falsa, por lo tanto no es simétrica.

#### En P(A), xRy si y sólo si X ⊂ Y

Lo dejo para el repaso

<u>Pares que pertenecen</u>



<u>Pares que no pertenecen:</u>



## 6. Determinar si las siguientes relaciones definidas en A = {a, b, c, d} son reflexivas, simétricas, antisimétricas y transitivas:

### R0 = ∅

### R1 = {(a, a); (a, b); (d, c); (c, d)}

### R2 = {(a, a); (b, b); (a, b); (b, a); (d, d); (c, c)}

### R3 = {(a, a); (a, b); (b, a); (b, c); (c, b); (b, b)}

### R4 = A × A

## 7. Escribir la matriz y los digrafos asociados a las relaciones anteriores

## 8. Sea A = {a, b, c, d}

### (a) Dar un ejemplo de una relaci´on R no reflexiva en A

### (b) Dar un ejemplo de una relaci´on R sim´etrica en A

### (c) Dar un ejemplo de una relaci´on R no transitiva en A

### (d) Dar un ejemplo de una relaci´on R no sim´etrica en A

### (e) Dar un ejemplo de una relaci´on R antisim´etrica en A

## 9. Demostrar que si R es sim´etrica y transitiva y aRb para ciertos a y b, entonces aRa y bRb.

## 10. Sea A un conjunto arbirtario. Sea R = ∆A (diagonal de A) . Analizar qu´e propiedades tiene R.

## 11. Proponer una relaci´on en el conjunto de los n´umeros naturales. Mostrar que propiedades tiene (reflexividad, simetr´ıa, etc...)

## 12. Proponer una relaci´on en el conjunto de los alumnos de Inform´atica. Mostrar que propiedades tiene (reflexividad, simetr´ıa, etc...)

## 13. Dada una relaci´on binaria R sobre un conjunto A, se define la relaci´on complemento de R, ¯R por: a ¯Rb si y s´olo si a no est´a relacionada con b por R

### • Dar un ejemplo de una relaci´on R y su complemento

### • Probar que si R ⊂ S entonces ¯S ⊂ ¯R

## 14. Dada R una relaci´on binaria sobre A, probar que:

### (a) R es reflexiva si y s´olo si R−1 tambi´en lo es

### (b) R es sim´etrica si y s´olo si R−1 = R

### (c) R es sim´etrica si y s´olo si R−1 y ¯R tambi´en lo son

### (d) R es antisim´etrica si y s´olo si R ∩ R−1 ⊂ ∆A

## 15. Se dice que una relaci´on R sobre un conjunto A es asim´etrica si cada vez que a est´a relacionado con b no se da que b est´e relacionado con a Dar un ejemplo de una relaci´on asim´etrica

## 16. Probar que dada una relaci´on R sobre un conjunto A, R es asim´etrica si y s´olo si R ∩ R−1 = ∅

## 17. Sean R y S dos relaciones en A. Probar que:

### (a) Si R ⊂ S entonces R−1 ⊂ S−1

### (b) Si R y S son reflexivas entonces R ∪ S y R ∩ S tambi´en lo son

### (c) Si R y S son sim´etricas entonces R ∪ S y R ∩ S tambi´en lo son

## 18. Establecer las propiedades de las siguientes relaciones en H el conjunto de los seres humanos:

### (a) Sea R la relaci´on en H definida por xRy si y s´olo si x es hermano de y

### (b) Sea R la relaci´on en H definida por xRy si y s´olo si x es hijo de y

### (c) Se dice que una persona a es descendiente de una persona b si es hijo, nieto, bisnieto, etc.. R es la relaci´on en H definida por xRy si y s´olo si x es descendiente de y

## 19. Establecer las propiedades de las siguientes relaciones:

### (a) Sea N el conjunto de los n´umeros naturales. Sea ≤ la relaci´on en N dada por x ≤ y si y s´olo si x es menor o igual a y

### (b) Sea N el conjunto de los n´umeros naturales. Sea | la relaci´on en N dada por x|y si y s´olo si x divide a y

### (c) Igual al anterior pero en el conjunto de los enteros.

## 20. Dado un conjunto de n´umeros reales A probar que la relaci´on sobre A × A dada por (a, b)R(c, d) si y s´olo si a ≤ c y b ≤ d es un orden. Es total?

21. Analizar que tipo de orden es el usual en el conjunto de los n´umeros rales. ¿qu´e pasa
con los n´umeros complejos?¿est´an ordenados?
22. Probar que el orden lexicogr´afico es un orden total
23. Sea S = {a, b, c} y sea A = P (S) el conjunto de partes de S. Mostrar que A est´a
parcialmente ordenado por el orden ⊂ (inclusi´on de conjuntos).
Hallar el diagrama de Hasse.
3
24. Sea D12 = {1, 2, 3, 4, 6, 12} (el conjunto de los divisores de 12). Hallar el diagrama de
Hasse de D12 con la relaci´on ”divide”
25. Describa las parejas ordenadas por las relaciones de cada uno de los siguientes diagra-
mas de Hasse. Determinar, si existen, los elementos m´aximo, m´ınimo y cotas inferiores
y superiores
a
b c d e f
g h i
j
1
a b c d
0
26. Sea R una relaci´on de equivalencia en un conjunto no vac´ıo A. Seam a.b ∈ A, entonces
[a] = [b] si y s´olo si aRb
27. Determinar si cada una de las siguientes colecciones de conjuntos es una partici´on para
el conjunto A = {1, 2, 3, 4, 5, 6, 7, 8, }
• {{4, 5, 6}; {1, 8}; {2, 3, 7}}
• {{4, 5}; {1, 3, 4}; {6, 8}; {2, 7}}
• {{1, 3, 4}; {2, 6}; {5, 8}}
28. Considerando el conjunto A de los alumnos que cursan Mate 4, indicar cu´ales de las
siguientes son particiones de A.
(a) P = {{alumnos que aprobaron CADP}; {alumnos que aprobaron OC};
{alumnos que no aprobaron ISO ni Redes}}
(b) P = {{alumnos que est´an cursando Programaci´on Distribuida }; {alumnos que cursan Sistemas y Organiz
{alumnos que est´an cursando L´ogica e Inteligencia Artificial}}
29. Sean A = {1, 2, 3, 4} y R = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (4, 3), (4, 4)}.
Mostrar que R es una relaci´on de equivalencia y hallar las clases de equivalencia.
¿ Cu´al es la partici´on que induce R sobre A ?
30. Dados el conjunto A = {a, b, c, d, e} y una partici´on P = {{a, c}; {b}; {d, e}} .
Escribir por extensi´on la relaci´on de equivalencia sobre A inducida por P .
4
31. Sean A = {1, 2, 3, 4, 5, 6} y R = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4), (4, 5), (5, 4), (5, 5), (6, 6)}.
Mostrar que R es una relaci´on de equivalencia y determinar las clases de equivalencia.
¿ Qu´e partici´on de A induce R ?
32. Sea ∼ una relaci´on definida en Z × (Z0) dada por: (a, b) ∼ (c, d) si y s´olo si ad = bc
Probar que es de equivalencia. Hallar la clase de equivalencia del elemento (1, 4) .
Mostrar que puede identificarse cada clase de equivalencia con un n´umero racional
(Esta es la forma de construir al conjunto de los racionales como conjunto cociente).
33. Hallar las clases de equivalencia m´odulo 3 y 5 de los n´umeros 387, 25 y 649
34. Hallar las respectivas clases de 13, 6, 11 y −49 m´odulo 4
35. Averiguar si son congruentes m´odulo 3 entre s´ı los siguientes pares de n´umeros: (2, 1024),
(101, 512), (1501, 1348).
36. Analizar para qu´e valores de m se hacen verdaderas las siguientes congruencias:
5 ≡m 4, 1 ≡m 0, 1197 ≡m 286, 3 ≡m −3
37. Probar que la relaci´on de congruencia m´odulo m es una relaci´on de equivalencia
38. Probar: todo n´umero es congruente, m´odulo n, con el resto de su divisi´on por n
39. Probar que dos enteros son congruentes m´odulo m si y s´olo si los respectivos restos de
su divisi´on por m son iguales.
40. Probar las siguientes propiedades para todo a, b, c ∈ Z :
(a) a ≡n a
(b) a ≡n b ⇒ b ≡n a
(c) a ≡n b y b ≡n c ⇒ a ≡n c
(d) a ≡n b ⇔ a + c ≡n b + c
(e) a ≡n b ⇒ ac ≡n bc
(f) a ≡n b ⇒ (a, n) = (b, n)
(g) a ≡n 0 ⇔ n|a