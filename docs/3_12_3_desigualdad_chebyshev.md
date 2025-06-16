### Presentación

[12 - Teorema del límite central: Desigualdades de Chebyshev y Markov y ley de los grandes números](https://www.overleaf.com/read/zhzxhphdwrwp#cfe351)

### Secciones
- Desigualdad de Chebyshev (19 - 29)

# Desigualdad de Chebyshev

## Premisas para la desigualdad de Chebyshev

Sea $W$ una variable aleatoria con media 0. Esta es **cualquier** VA.

![F:media_cero](mpss/docs/images/12_media_cero.svg)

* La media de $W$ es 0, pero cualquier realización simple de $W$ puede estar bastante alejada de 0.
* La varianza es una medida de la dispersión de los valores de $W$ alrededor de 0.
* Entre mayor el valor de la varianza de $W$, más probable es que el valor de $W$ puede estar lejos de 0.

> Dada la varianza $\sigma^2$, ¿qué tan cercanos a $\mu = 0$ los valores de $W$ podrían estar?


## La desigualdad de Chebyshev I

Fíjese un número $\epsilon > 0$ y búsquese la probabilidad de que $W$ está más alejada que $\epsilon$ de su media $\mu = 0$. Supóngase que $W$ tiene una función de densidad $f_W(w)$, entonces:

$$
P(\vert W \vert \geq \epsilon ) = \int_{\vert w \vert \geq \epsilon}f_W(w) dw = \int_{w^2 \geq \epsilon^2} \frac{\epsilon^2}{\epsilon^2}f_W(w) dw
$$

$f_{Xi}(X_i) = \lambda_ie^{-\lambda_iX}$

![F:epsilon](mpss/docs/images/12_epsilon.svg)

## La desigualdad de Chebyshev II

Es esperable que la probabilidad $P(\vert W \vert \geq \epsilon)$ debería hacerse más grande conforme $\sigma^2$ se hace más grande, puesto que los valores de $W$ están más dispersos.

$$
\begin{aligned}
\int_{w^2 \geq \epsilon^2} \frac{\epsilon^2}{\epsilon^2}f_W(w) dw & \leq \int_{w^2 \geq \epsilon^2}\frac{w^2}{\epsilon^2}f_W(w) dw \\
      & \leq \int_{-\infty}^{\infty}\frac{w^2}{\epsilon^2}f_W(w) dw \\
    & = \frac{1}{\epsilon^2}\int_{-\infty}^{\infty} w^2 f_W(w) dw \\
    & = \frac{E[W^2]}{\epsilon^2} \\
P(\vert W \vert \geq \epsilon) & \leq \frac{\sigma^2}{\epsilon^2}
\end{aligned}
$$


## La desigualdad de Chebyshev III

* La primera desigualdad es porque el intervalo de integración contiene los puntos $w$ donde $w^2 \geq \epsilon^2$ y, por lo tanto, el integrando será mayor si $\epsilon^2$ se reemplaza por $w^2$.
* La segunda desigualdad viene de aumentar el intervalo de integración de los puntos $w$ donde $w^2 \geq \epsilon^2,$ a la recta numérica de $-\infty$ a $+\infty$.
* $E[W^2]$ (el segundo momento ordinario) es igual en este caso a la varianza $\sigma^2$ (el segundo momento central) porque la media es cero y $\sigma^2 = E[W^2] - E^2[W]$.

> **Desigualdad de Chebyshev**
>
> Si $E[W] = 0$ y dado cualquier número positivo $\epsilon,$ el evento que $W$ difiera en por lo menos $\epsilon$ de cero, está acotado por la probabilidad:
>
> $$
> P(\vert W \vert \geq \epsilon ) \leq \frac{\sigma^2}{\epsilon^2}
> $$

## Generalización de la desigualdad de Chebyshev

Si $\mu = E[X] \neq 0$ pero $W = X - \mu$, entonces $E[W] = 0$, y el desarrollo anterior aplica a $X$:

<br>

> **Desigualdad de Chebyshev generalizada**
>
> Sea $X$ una VA con media finita $\mu$ y varianza finita $\sigma^2$. Entonces para $\epsilon > 0$ un número fijo, la probabilidad que $X$ difiera en a lo menos $\epsilon$ de su media, está acotada:
>
> $$
> P(\vert X - \mu \vert \geq \epsilon ) \leq \frac{\sigma^2}{\epsilon^2}
> $$
>
> O en términos del evento complementario: $P(\vert X - \mu\vert < \epsilon ) \geq 1 - \frac{\sigma^2}{\epsilon^2}$.

**Comentario**: Este es un límite ``laxo'' en el sentido de que **no** es muy restrictivo y por tanto no muy preciso o informativo.

## Ejemplo de $\{-1,0,1\}$ para Chebyshev I


>
> Si $X$ tiene tres posibles valores: $\{ -1, 0, 1 \}$, con probabilidades $\{ \frac{1}{18}, \frac{8}{9}, \frac{1}{18} \}$, respectivamente. ¿Cuál es la probabilidad $P(\vert X - \mu \vert \geq 3\sigma)$ y cómo se compara con el límite de Chebyshev?

* Recordar que
    $$E\left[ X \right] = \sum_{i=1}^{N}x_i P(x_i)$$
* También que
    $$\sigma_{X}^{2} = E\left[ \left( X- \overline{X} \right)^2 \right] = E[X^2] - E^2[X]$$
* Siendo que
    $$P(\vert W \vert \geq \epsilon ) \leq \frac{\sigma^2}{\epsilon^2}$$
* Pero una forma equivalente es
    $$P( \vert X - \mu_X \vert \geq k\sigma_X ) \leq \frac{1}{k^2}$$

---

La media y la varianza de la VA discreta se obtienen de la siguiente forma:

$$
E[X] = \sum_{i=1}^{3} x_i P(x_i) = (-1)\frac{1}{18} + (0)\frac{8}{9} + (1)\frac{1}{18} = 0
$$

$$
\mathsf{Var}[X] = \sum_{i=1}^{3} (x_i - E[X])^2 P(x_i) = (-1)^2 \frac{1}{18} + (0)^2 \frac{8}{9} + (1)^2 \frac{1}{18} = \frac{1}{9}
$$

Utilizando la definición provista de la desigualdad de Chebyshev, se obtiene

$$
P( \vert X - \mu_X \vert \geq k\sigma_X ) = P( \vert X - 0 \vert \geq 3 \frac{1}{3} ) \leq \frac{1}{3^2} = \frac{1}{9}
$$

---

Mientras tanto, utilizando la PDF propiamente, se puede encontrar la probabilidad $P( \vert X \vert \geq 1 )$ solicitada. Considerando que solo hay tres valores posibles de $X$, $\{ -1, 0, 1 \}$, los elementos de interés son $\{ -1, 1 \}$ cuyas probabilidades son $1/18 + 1/18 = 1/9$, igual que con Chebyshev.

<br>

En general, la desigualdad de Chebyshev será mucho menos restrictiva que el análisis de la PDF, pero en este caso de ejemplo resultaron iguales.

# Desigualdad de Markov

## Desigualdad de Markov

> **Desigualdad de Markov**
>
> Si $X$ es una VA con $f_X(x) = 0$ para $x < 0$, entonces $X$ es llamada una VA no-negativa, para la cual aplica la desigualdad de Markov:
>
> $$
> P(X \geq \epsilon) \leq \frac{E[X]}{\epsilon}
> $$

**Comentario**: En contraste con el límite de Chebyshev, que involucra tanto la media como la varianza, este límite requiere únicamente de la media de $X$.

## Prueba de la desigualdad de Markov

La consideración es ahora en relación con la definición del valor esperado (el *momento ordinario de primer orden*):

$$
\begin{aligned}
E[X] = \int_{0}^{\infty} x f_X(x) dx &\geq \int_{\epsilon}^{\infty} x f_X(x) dx \\
&\geq \int_{\epsilon}^{\infty} \epsilon f_X(x) dx = \epsilon \int_{\epsilon}^{\infty} f_X(x) dx \\
&= \epsilon P(X \geq \epsilon)
\end{aligned}
$$

## Ejemplo de los resistores de baja calidad

> **Planteamiento**
>
> Es posible asumir que en la manufactura de resistores eléctricos de baja calidad de 1000 $\Omega$, la resistencia promedio es en efecto de 1000 $\Omega$, según se determina por un análisis estadístico de mediciones, pero hay una gran variación alrededor de este valor. Si todos los resistores por encima de 1500 $\Omega$ deben descartarse, ¿cuál es la fracción máxima de resistores que terminarían por fuera?

* Recordar que
    $$P(X \geq \epsilon) \leq \frac{E[X]}{\epsilon}$$
