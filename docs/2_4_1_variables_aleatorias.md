## El problema inicial: Variable aleatoria

Los conjuntos \( S_1 = \{ \text{todos los equipos del campeonato nacional} \} \) o  
\( S_2 = \{ \text{los colores favoritos de los estudiantes de esta clase} \) son útiles en la descripción de ciertos eventos, pero no permiten la *manipulación numérica*.


- Este espacio de eventos contiene conjuntos **abstractos**.
- Necesitamos **números** para sumar, restar, multiplicar, dividir...
- Necesitamos **funciones** para diferenciar, integrar...

> Aquí es útil, entonces, la variable aleatoria...

---

## Variable aleatoria

### Definición

Para un espacio de eventos \( S \), una **variable aleatoria** es cualquier regla que asocia cada resultado elemental de \( S \) con **un número**. Es decir, es una **función** cuyo dominio es el espacio (quizá abstracto) de eventos o muestras, y cuyo rango es algún subconjunto de los números reales.

![Figura](images/4_asoc_VA.svg)

La notación \( X(s) = x \) significa que \( x \) es el valor asociado por \( X \) con el evento elemental \( s \).

---

## Pero… Una observación necesaria

Las variables aleatorias *ni son variables, ni son aleatorias*\  
> \( X(s) \) es una **función** y es *determinística*, pero describe el comportamiento de un fenómeno aleatorio subyacente.

> (Por tanto, se trata de un nombre poco apropiado. En inglés: *misnomer*.)



---

## Requisitos para la construcción de variables aleatorias

- **Un espacio de probabilidades** \((S, P)\): contiene todos los eventos elementales \( S \) y sus probabilidades asociadas \( P \).
- **Una función de mapeo** \( X \): que mapea cada \( s \in S \) a un único punto \( x \in \mathbb{R} \).
- **Una relación de dualidad** de la probabilidad: si \( B \subseteq \mathbb{R} \), entonces  
  la probabilidad del evento \( X(s) = B \) es equivalente a la del conjunto  
  \( A = X^{-1}(B) \in S \), que contiene todos los \( s \in S \) que se mapean a \( B \) bajo \( X \).

![Figura](images/4_mapeo_VA_segmento_recta.svg)

\[
X(s \in A) = B \qquad A = X^{-1}(B) \in S \qquad P(B) = P(A)
\]

---

## Condiciones para que una función sea variable aleatoria

> **Nota**: *va* será la abreviación de “variable aleatoria”. En inglés se utiliza **rv**, de *random variable*.

Algunas condiciones debe cumplir \( X(s) \) para ser una *va*.

1. Una variable aleatoria es una función **no multivaluada**: todo punto en \( S \) corresponde a un solo valor de la *va*.

    ![Figura](images/4_mapeo_multivaluado.svg)

    > Esto **no** representa el mapeo de una *va*.

---

2. El conjunto \( \{X \leq x\} \) existe y es un evento para cualquier número real \( x \).  
   Corresponde a los puntos \( s \) en \( S \) para los que \( X(s) \leq x \).

   ![Figura](images/4_mapeo_X_leq_x.svg)

   > La probabilidad \( P\{X \leq x\} \) es igual a la suma de las probabilidades de todos los \( s \) correspondientes a \( \{X \leq x\} \).

---

3. Las probabilidades de los eventos \( \{X = \infty\} \) y \( \{X = -\infty\} \) son cero:

\[
P\{X = -\infty\} = 0 \qquad P\{X = \infty\} = 0
\]

\( X(s) \) puede ser \( -\infty \) o \( \infty \) para algunos \( s \), pero su probabilidad será cero.

> Como se especifica más adelante, esto es necesario para que su "función de densidad" tenga un área total *finita*.

---

## Variables aleatorias **discretas**

Una variable aleatoria discreta es una *va* cuyos valores posibles constituyen un:

- conjunto **finito**, o
- conjunto infinito **enumerable**.

### Ejemplos

- Las caras de un dado
- La población mundial
- Otros ejemplos que se mapean en \( \mathbb{N} \)

![Figura](images/4_VA_discreta.svg)

> En una variable aleatoria discreta, la asignación de probabilidades se hace en valores discretos, ya sean finitos o infinitos enumerables. En este caso, están mapeados en un subconjunto de \( \mathbb{N} \).

### Variables aleatorias continuas

Una **variable aleatoria continua** es aquella que cumple con las siguientes condiciones:

1. Su conjunto de valores posibles está formado por todos los números dentro de un intervalo de la recta real (por ejemplo, de \( 0 \) a \( +\infty \)), o por la unión disjunta de varios intervalos.
2. Ningún valor individual tiene una probabilidad positiva. Es decir, para cualquier valor \( c \), se cumple que:

\[
P(X = c) = 0
\]

#### Ejemplo

La estatura de los habitantes de un país es una variable aleatoria continua.  
Pero, ¿cuál es la probabilidad de que una persona mida **exactamente** \( 52\pi \) cm?

> La respuesta es cero. En una variable aleatoria continua, la probabilidad de que ocurra un valor exacto es cero.

---

![Figura](images/4_dist_rayleigh.svg)

**Figura:** En una variable aleatoria continua, la asignación de probabilidades se hace en una sección o toda la recta real. Debido a que hay infinitos posibles resultados, la probabilidad de ocurrencia de exactamente un valor en particular es cero.