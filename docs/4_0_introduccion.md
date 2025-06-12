Los procesos aleatorios son los terceros “objetos aleatorios” por analizar. Incorporan una segunda variable independiente, el tiempo, que los hace útiles en la descripción de fenómenos cambiantes o dinámicos tales como las señales y los sistemas.

# El problema inicial  
## Variable aleatoria

Los conjuntos  S_1 = \{todos los equipos del campeonato nacional \} o  
S_2 = {los colores favoritos de los estudiantes de esta clase}    
son útiles en la descripción de ciertos eventos, pero no permiten la *manipulación numérica*.

- Este espacio de eventos contiene conjuntos **abstractos**.  
- Necesitamos **números** para sumar, restar, multiplicar, dividir…  
- Necesitamos **funciones** para diferenciar, integrar…

> Aquí es útil, entonces, la variable aleatoria…




# Variable aleatoria

> **Definición**  
Para un espacio de eventos \( S \), una **variable aleatoria** es cualquier regla que asocia  
cada resultado elemental de \( S \) con **un número**.  
Es decir, es una **función** cuyo dominio es el espacio (quizá abstracto) de eventos o muestras,  
y cuyo rango es algún subconjunto de los números reales.

![alt text](4_mapeo_multivaluado.svg)

La notación \( X(s) = x \) significa que \( x \) es el valor asociado por \( X \) con el evento elemental \( s \).



## Pero…

### Una observación necesaria

Las variables aleatorias *ni son variables, ni son aleatorias*[^1].

!!! note "Nota"

    

    \( X(s) \) es una **función** y es *determinística*,  
    pero describe el comportamiento de un fenómeno aleatorio subyacente.

    Por tanto, se trata de un nombre poco apropiado. En inglés: *misnomer*.




# Requisitos para la construcción de variables aleatorias I

- **Un espacio de probabilidades** \( (S, P) \) para un experimento, que contiene todos los eventos elementales \( S \) y sus probabilidades asociadas \( P \).

- **Una función de mapeo** \( X \) que mapea cada \( s \in S \) a un único punto \( x \in \mathbb{R} \) (la recta real).

- **Una relación de dualidad** de la probabilidad, esto es, que si \( B \) es un subconjunto de \( \mathbb{R} \), la probabilidad del evento \( X(s) = B \) es equivalente a la del conjunto  
  \( A = X^{-1}(B) \in S \), que contiene todos los \( s \in S \) que se mapean a \( B \) bajo la función \( X \).


# Requisitos para la construcción de variables aleatorias II
![alt text](4_mapeo_VA_segmento_recta.svg)

Figura: Mapeo de un subconjunto del espacio de eventos \( S \) en un segmento de la recta real \( \mathbb{R} \).

\[
X(s \in A) = B \qquad A = X^{-1}(B) \in S \qquad P(B) = P(A)
\]



# Condiciones para que una función sea variable aleatoria I

!!! note "Nota"

    *va* será la abreviación de “variable aleatoria”, de aquí en adelante. En inglés se utiliza **rv**, de *random variable*.

Algunas condiciones debe cumplir \( X(s) \) para ser una *va*:

🔵 Una variable aleatoria es una función **_no multivaluada_**.  
Es decir, todo punto en \( S \) corresponde a solo un valor de la *va*.
(img/4_mapeo_multivaluado.svg)

_Figura: Esto **no** (atención: **no**) representa el mapeo de una *va*._




# Condiciones para que una función sea variable aleatoria II

🔵 El conjunto \( \{ X \leq x \} \) existe y es un evento para cualquier número real \( x \).  
Corresponde a los puntos \( s \) en el espacio de muestras \( S \) para los que la *va* \( X(s) \) no excede el número \( x \).

(img/4_mapeo_X_leq_x.svg)


> La probabilidad \( P\{X \leq x\} \) es igual a la suma de las probabilidades de todos los eventos elementales \( s \) correspondientes a \( \{X \leq x\} \).

# Condiciones para que una función sea variable aleatoria III

🔵 Las probabilidades de los eventos \( \{ X = \infty \} \) y \( \{ X = -\infty \} \) son cero, es decir:

\[
P\{X = -\infty\} = 0 \qquad P\{X = \infty\} = 0
\]

\( X(s) \) puede ser ya sea \( -\infty \) o \( \infty \) para algunos valores de \( s \), pero su probabilidad será cero.

*Como se especifica más adelante, esto es necesario para que su “función de densidad” tenga un área total finita.*

# Variables aleatorias **discretas** I

### Definición

Una variable aleatoria discreta es una *va* cuyos valores posibles constituyen o un  
**conjunto finito** o un **conjunto infinito *enumerable***.

### Ejemplos

- Las caras de un dado  
- La población mundial  
- Otros ejemplos que se mapean en \( \mathbb{N} \)