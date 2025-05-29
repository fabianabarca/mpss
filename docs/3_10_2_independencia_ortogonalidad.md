# Momentos de las variables aleatorias múltiples
---

## Introducción

Es posible determinar momentos asociados con dos o más variables aleatorias.  
La información que proveen, al igual que con las variables aleatorias individuales, es útil como descriptores generales.

Las dos métricas más importantes para momentos conjuntos son la **correlación** y la **covarianza**, que cuantifican el grado de interrelación lineal entre una variable aleatoria y otra.

---

## Valor esperado de una función de variables aleatorias

Definición:  
Si \( g(X, Y) \) es alguna función de dos variables aleatorias \( X \) y \( Y \), el valor esperado de \( g(X,Y) \) está dado por:

\[
\overline{g} = E[g(X,Y)] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(x,y)f_{X,Y}(x,y) dx dy
\]

Aunque \( g(X,Y) \) define una nueva variable aleatoria, no es necesario conocer la densidad probabilística de esta para calcular su valor esperado. En cambio, es una suma ponderada de la densidad conjunta de \( X \) y \( Y \).

---

### Ejemplo: El tarro de nueces



El PDF conjunto de la cantidad \( X \) de almendras y \( Y \) de semillas de marañón en un tarro de 1 kg es:

\[
f_{X,Y}(x,y) =
\begin{cases}
24xy 	& 0 \leq x \leq 1, 0 \leq y \leq 1, x + y \leq 1  \\
0		& \text{de otra manera}
\end{cases}
\]

Si 1 kg de almendras le cuesta a la compañía ¢6000, un kilogramo de semillas de marañón son ¢10.000 y 1 kg de maní cuesta ¢3.500. ¿Cuál es el costo esperado total del contenido del tarro?

Sea la función del costo

\[
h(X,Y) = 6000 X + 10000 Y + 3500 (1 - X - Y)
\]

Entonces,

\[
\begin{aligned}
E[h(X,Y)] &= \int_0^1 \int_0^{1-x} [6000x + 10000y + 3500(1 - x - y)] \cdot 24xy \, dy \, dx \\
&= ¢~7100
\end{aligned}
\]

que representa los costos esperados del contenido de la caja.

---

## Momentos conjuntos alrededor del origen
Los momentos conjuntos para dos variables aleatorias \( X \) y \( Y \) se denotan por \( m_{nk} \) y se definen por:

\[
m_{nk} = E[X^n Y^k]
       = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x^n y^k f_{X,Y}(x,y) \, dx \, dy
\]

Casos especiales:

- \( m_{n0} = E[X^n] \) son los momentos \( m_{n} \) de \( X \)
- \( m_{0k} = E[Y^k] \) son los momentos de \( Y \)
- \( n + k \) es el orden de los momentos. Ejemplo: \( m_{02} \), \( m_{20} \), \( m_{11} \) son los momentos de segundo orden de \( X \) y \( Y \)
- \( m_{01} = E[Y] = \overline{Y}\) y \( m_{10} = E[X] = \overline{X} \) son los valores esperados de \( X \) y \( Y \), y son las coordenadas del centro de gravedad de la función \( f_{X,Y} \).

---

### Ejemplo: Ubicación del centro de gravedad

![Ejemplo: Ubicación del "centro de gravedad"](images/10_gravedad.svg)

---

## Correlación, independencia y ortogonalidad

### Correlación de dos variables aleatorias

El momento de segundo orden \( m_{11} = E[XY] \) es denominado la  **correlación** \( X \) y \( Y \).

Recibe el símbolo especial \( R_{XY}\) por su importancia.

\[
R_{XY} = E[XY] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} xy f_{X,Y}(x,y) dx dy
\]

Interpretaciones posibles:

- “La correlación es el grado en el cual dos o más cantidades están linealmente
asociadas”.
- Pero (fundamental) "**correlación no implica causalidad.**"

---

### Ejemplo: Correlación en el tarro de nueces
**Planteamiento**

El PDF conjunto de la cantidad $X$ de almendras y la cantidad $Y$ de semillas de marañón (y la cantidad $Z$ de maní) en un tarro de 1 kg es

$$
f_{X,Y}(x,y) = 24xy \qquad 0 \leq x \leq 1, 0 \leq y \leq 1, x + y \leq 1
$$

¿Cuál es la correlación entre $X$ y $Y$?

$$
\begin{aligned}
  R_{XY} = m_{11} & = E[XY] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy ~ f_{X,Y}(x,y) \, dx \, dy \\
  & = \int_{0}^{1}\int_{0}^{1-y}xy ~ 24xy \, dx \, dy = 24 \int_{0}^{1} y^2 \int_{0}^{1-y} x^2 \, dx \, dy \\
  & = \frac{24}{3} \int_0^1 y^2(1-y)^3 \, dy \\
  & = \frac{24}{3} \left[ - \frac{y^6}{6} + 3 \frac{y^5}{5} - 3 \frac{y^4}{4} + \frac{y^3}{3} \right]_0^1 = \frac{2}{15} \approx 0.13
\end{aligned}
$$

---

### No correlación

## La **no** correlación

<div class="bloque" markdown>

**No correlación**  
Si la correlación puede escribirse en la forma:

$$
R_{XY} = E[X]E[Y]
$$

entonces $X$ y $Y$ se dice que **no** están correlacionadas.

</div>

## Independencia y ortogonalidad

### Independencia y correlación

!!! note "Independencia y correlación"
    La independencia estadística de $X$ y $Y$ es suficiente para garantizar que **no** están correlacionadas.

<small>El recíproco de esta última frase, que $X$ y $Y$ son independientes si $X$ y $Y$ no están correlacionadas, no es necesariamente cierto en general, con la sola excepción de las variables aleatorias gaussianas no correlacionadas, que son también independientes.</small>

### Ortogonalidad

!!! note "Ortogonalidad"
    Si $R_{XY} = 0$ para dos variables aleatorias $X$ y $Y$, estas se denominan ortogonales.

### En síntesis

- Si $R_{XY} = E[XY] = E[X]E[Y]$, no están correlacionadas.
- La independencia ($f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$) garantiza que no están correlacionadas, pero no a la inversa.
- Si $R_{XY} = 0$, son ortogonales.

---

## Ejemplo de correlación y ortogonalidad

**Planteamiento**  
Sea $X$ una variable aleatoria que tiene un valor medio $\overline{X} = E[X] = 3$ y varianza $\sigma_{X}^2 = 2$ y sea $Y = -6X + 22$. Determinar correlación y ortogonalidad entre $X$ y $Y$.

El segundo momento de $X$ alrededor del origen:

$$
\begin{aligned}
\sigma_{X}^2 & = E[X^2] - \left( E[X] \right)^2 \\
E[X^2] & = \sigma_{X}^2 + \left( E[X]\right)^2 \\
& = 11
\end{aligned}
$$

Con $Y = -6X + 22$:

$$
\begin{aligned}
E[Y] & = -6E[X] + 22 \\
& = -6(3) + 22 \\
& = 4
\end{aligned}
$$

Cálculo de $R_{XY}$:

$$
\begin{aligned}
R_{XY} & = E[XY] \\
& = E[X(-6X + 22)] \\
& = E[-6X^2 + 22X] \\
& = -6E[X^2] + 22E[X] \\
& = -6(11) + 22(3) \\
& = 0
\end{aligned}
$$

Por tanto, $X$ y $Y$ son ortogonales ($R_{XY} = 0$), pero $R_{XY} \neq E[X]E[Y] = 12$.

!!! important ""
    Dos variables aleatorias pueden ser ortogonales aun cuando una de ellas ($Y$) está relacionada con la otra ($X$) por una función lineal $Y = aX + b$.

---

## Momentos centrales conjuntos

### Definición

!!! note "Momentos centrales conjuntos"
    Para dos variables aleatorias $X$ y $Y$:

    $$
    \begin{aligned}
    \mu_{nk} & = E\left[ (X-\overline{X})^{n}(Y-\overline{Y})^k \right] \\
    & = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}(x- \overline{X})^{n}(y-\overline{Y})^{k}f_{X,Y}(x,y) \, dx \, dy
    \end{aligned}
    $$

**Momentos importantes**:
- $\mu_{20} = E[(X-\overline{X})^2] = \sigma_{X}^2$ (Varianza de $X$)
- $\mu_{02} = E[(Y-\overline{Y})^2] = \sigma_{Y}^2$ (Varianza de $Y$)

---

## Covarianza de dos variables aleatorias

!!! note "Covarianza"
    El momento conjunto $\mu_{11}$ es la covarianza ($C_{XY}$):

    $$
    \begin{aligned}
    C_{XY} & = E[(X-\overline{X})(Y-\overline{Y})] \\
    & = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}(x-\overline{X})(y-\overline{Y})f_{X,Y}(x,y) \, dx \, dy \\
    & = E[XY] - E[X]E[Y] \\
    C_{XY} & = R_{XY} - E[X]E[Y]
    \end{aligned}
    $$

**Propiedades**:
1. Si $X$, $Y$ son independientes o no correlacionadas: $C_{XY} = 0$
2. Si $X$, $Y$ son ortogonales: $C_{XY} = -E[X]E[Y]$
   - Si además $E[X]=0$ o $E[Y]=0$: $C_{XY} = 0$

---

## Coeficiente de correlación de Pearson

El coeficiente de correlación normalizado:

$$
\rho = \frac{\mu_{11}}{\sqrt{\mu_{20} \mu_{02}}} = \frac{C_{XY}}{\sigma_X \sigma_Y} = \frac{\mathsf{cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Expresado como:

$$
\begin{aligned}
\rho & = \frac{E[(X-\overline{X})(Y-\overline{Y})]}{\sigma_X \sigma_Y} \\
& = E\left[ \frac{(X-\overline{X})}{\sigma_X}\frac{(Y-\overline{Y})}{\sigma_Y} \right]
\end{aligned}
$$

**Rango**: $-1 \leq \rho \leq 1$

### Visualización de casos especiales del coeficiente de correlación de Pearson

![Ejemplo: Ubicación del "centro de gravedad"](images/10_pearson.svg)

---

## Funciones características conjuntas

Definición:

$$
\Phi_{X,Y}(\omega_1, \omega_2) = E\left[ e^{j\omega_1 X + j\omega_2 Y} \right] 
$$

Equivalente integral:

$$
\Phi_{X,Y}(\omega_1, \omega_2) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{X,Y}(x,y)e^{j\omega_1 x + j\omega_2 y} \, dx \, dy
$$

Transformada inversa:

$$
f_{X,Y}(x,y) = \frac{1}{(2\pi)^2}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\Phi_{X,Y}(\omega_1, \omega_2)e^{-j\omega_1 x - j\omega_2 y} \, d\omega_1 \, d\omega_2
$$

**Funciones marginales**:
- $\Phi_{X}(\omega_1) = \Phi_{X,Y}(\omega_1,0)$
- $\Phi_{Y}(\omega_2) = \Phi_{X,Y}(0,\omega_2)$

**Cálculo de momentos**:

$$
m_{nk} = \left. (-j)^{n+k}\frac{\partial^{n+k}\Phi_{X,Y}(\omega_1, \omega_2)}{\partial \omega_{1}^n \partial \omega_{2}^k}\right\vert_{\omega_1 = 0, \omega_2 = 0}
$$