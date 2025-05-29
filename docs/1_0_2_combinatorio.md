# Algunos resultados útiles del análisis combinatorio

## Regla de la multiplicación

En un diagrama tipo árbol donde el $i$-ésimo nivel tiene $n_i$ ramas, entonces la cantidad de posibles combinaciones en $r$ niveles es:

$$
n_1 \times n_2 \cdots \times n_r
$$

**Ejemplo**

- ¿Cuántas combinaciones posibles hay con cuatro sabores de helados y tres conos distintos?
- ¿Cuántas combinaciones posibles hay con cuatro sabores de helados, tres conos distintos y diez *toppings*?

---

## Posibles arreglos de un mazo de cartas con 52 cartas

**Regla de la multiplicación:**

$$
\textbf{52!} = 80\,658\,175\,170\,943\,878\,571\,660\,636\,856\,403\,766\,975\,289\,505\,440\,883\,277\,824\,000\,000\,000\,000
$$

Este número es **grande**.

---

## Combinatoria enumerativa: contar (números grandes)

En muchos análisis de la situación que se estudia, es necesario "contar" todos los resultados elementales posibles de un experimento. Este puede ser un número muy grande.

Los principales tipos son **combinaciones**, **permutaciones**, **particiones** y **composiciones**.

---

## Combinaciones

Es la selección de $k$ ítemes de una colección de $n$ elementos, *donde el orden no importa*.

$$
_n\mathbf{C}_k \equiv \binom{n}{k} \equiv \frac{n!}{k! (n-k)!}
$$

Se lee $_n\mathbf{C}_k$ como “de $n$ escoge $k$” y $\binom{n}{k}$ es el **_coeficiente binomial_**.

**Ejemplo**

Para hacer un grupo de cinco personas de una clase de 30 alumnos hay

$$
_{30}\mathbf{C}_5 \equiv \binom{30}{5} \equiv \frac{30!}{5! (30-5)!} = 142\,506
$$

combinaciones posibles.

> Fuentes: **MathWorld** (<http://mathworld.wolfram.com/Combination.html>) y **Wikipedia** (<https://en.wikipedia.org/wiki/Combination>)

---

## Permutaciones

Es el arreglo de $k$ ítemes de una colección de $n$ elementos, *donde el orden sí importa*.

$$
_n\mathbf{P}_k \equiv \frac{n!}{(n-k)!}
$$

Se lee $_n\mathbf{P}_k$ como "de $n$ escoge $k$".

**Ejemplo**

Para hacer una *junta directiva* de cinco personas de una clase de 30 alumnos hay

$$
_{30}\mathbf{P}_5 \equiv \frac{30!}{(30-5)!} = 17\,100\,720
$$

permutaciones posibles.

> Fuentes: **MathWorld** (<http://mathworld.wolfram.com/Permutation.html>) y **Wikipedia** (<https://en.wikipedia.org/wiki/Permutation>)

---

## Particiones

Sean $r_{1}, ..., r_{l}$, con $l$ un entero positivo, números tales que $r_{1}+r_{2}+\cdots+r_{l} = n$. Entonces, la cantidad de formas en las que una población de $n$ elementos puede ser particionada en $l$ sub-poblaciones donde la primera contiene $r_{1}$ elementos, la segunda $r_{2}$ y así sucesivamente, es:

$$
\frac{n!}{r_{1}!r_{2}! \cdots r_{l}!}
$$

Este coeficiente es conocido como **_coeficiente multinominal_**.

**Ejemplo**

Un vendedor de autos tiene 6 carros disponibles de distinto modelo cada uno y los quiere acomodar en grupos de 1, 2 y 3 carros respectivamente por un tema de espacio. ¿De cuántas formas distintas los puede acomodar?

$$
n_E = \frac{6!}{1!\times 2! \times 3!} = 60
$$

> Fuente: Stark, H., Woods, J. (2012) *Probability, Statistics, and Random Processes for Engineers*. Nueva Jersey: Pearson.

---

## Composiciones

Una composición en análisis combinatorio es un arreglo ordenado de $k$ elementos no negativos que suman $n$. Es por tanto una partición en la que el orden sí importa.

Por ejemplo, hay ocho composiciones de 4:

$$
\begin{aligned}
4 &= 4 \\\\
  &= 3+1 \\\\
  &= 2+2 \\\\
  &= 2+1+1 \\\\
  &= 1+3 \\\\
  &= 1+2+1 \\\\
  &= 1+1+2 \\\\
  &= 1+1+1+1
\end{aligned}
$$

Un entero positivo $n$ tiene $2^{(n-1)}$ composiciones.

El número de composiciones de $n$ en $k$ partes (donde 0 no es una parte) está dado por:

$$
\begin{aligned}
\mathbf{C}_k(n) &= {n-1 \choose k-1} \\\\
                &= \frac{(n-1)!}{(k-1)!(n-k)!}
\end{aligned}
$$

> Fuente: Stover, Christopher y Weisstein, Eric W. "Composition". De MathWorld -- A Wolfram Web Resource. <http://mathworld.wolfram.com/Composition.html>

---

## Otros ejemplos

- Una “mano de poker” consiste en cinco cartas escogidas de un mazo de 52 cartas:

  $$
  _{52}\mathbf{C}_5 \equiv \binom{52}{5} \equiv \frac{52!}{5! (52-5)!} = 2\,598\,960
  $$

- Las placas de carros en el país tienen tres consonantes y tres números, ¿cuántas placas son posibles? ¿Se agotarán pronto?

  $$
  21 \times 21 \times 21 \times 10 \times 10 \times 10 = 9\,261\,000
  $$

- Las campanas de una iglesia, tocadas al estilo inglés.

---

## Videos y referencias en internet

Cuando sea posible, las presentaciones tendrán referencias a videos o artículos útiles... o al menos entretenidos.

- ▶ **How secure is 256 bit security?**, *3Blue1Brown*: <https://youtu.be/S9JGmA5_unY>
- ▶ **Mathematical Impressions: Change Ringing**, *SimonsFoundation*: <https://youtu.be/3lyDCUKsWZs>


  Muchas veces los videos serán en inglés, quizá con subtítulos. Aunque espero que no sea un inconveniente, ojalá sirva de gentil recordatorio de la importancia de seguir aprendiendo inglés.