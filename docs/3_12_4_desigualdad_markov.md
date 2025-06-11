## La desigualdad de Chebyshev II

Es esperable que la probabilidad \(P(\vert W \vert \geq \epsilon)\) debería hacerse más grande conforme \(\sigma^2\) se hace más grande, puesto que los valores de \(W\) están más dispersos.

\begin{equation}
\begin{aligned}
\int_{w^2 \geq \epsilon^2} \frac{\epsilon^2}{\epsilon^2}f_W(w)\,\mathrm{d}w & \leq \int_{w^2 \geq \epsilon^2}\frac{w^2}{\epsilon^2}f_W(w)\,\mathrm{d}w \\
& \leq \int_{-\infty}^{\infty}\frac{w^2}{\epsilon^2}f_W(w)\,\mathrm{d}w \\
& = \frac{1}{\epsilon^2}\int_{-\infty}^{\infty} w^2 f_W(w)\,\mathrm{d}w \\
& = \frac{E[W^2]}{\epsilon^2} \\
P(\vert W \vert \geq \epsilon) & \leq \frac{\sigma^2}{\epsilon^2}
\end{aligned}
\end{equation}

---

- La primera desigualdad es porque el intervalo de integración contiene los puntos \(w\) donde \(w^2 \geq \epsilon^2\) y, por lo tanto, el integrando será mayor si \(\epsilon^2\) se reemplaza por \(w^2\).  
- La segunda desigualdad viene de aumentar el intervalo de integración de los puntos \(w\) donde \(w^2 \geq \epsilon^2,\) a la recta numérica de \(-\infty\) a \(+\infty\).  
- \(E[W^2]\) (el segundo momento ordinario) es igual en este caso a la varianza \(\sigma^2\) (el segundo momento central) porque la media es cero y \(\sigma^2 = E[W^2] - E^2[W]\).

!!! tip "Desigualdad de Chebyshev"
    Si \(E[W] = 0\) y dado cualquier número positivo \(\epsilon\), el evento que \(W\) difiera en por lo menos \(\epsilon\) de cero, está acotado por la probabilidad:

    \begin{equation}
    P(|W| \geq \epsilon) \leq \frac{\sigma^2}{\epsilon^2}
    \end{equation}

---

### **Generalización de la desigualdad de Chebyshev**

Si \(\mu = E[X] \neq 0\) pero \(W = X - \mu\), entonces \(E[W] = 0\), y el desarrollo anterior aplica a \(X\):

!!! tip "Desigualdad de Chebyshev generalizada"
    Sea \(X\) una variable aleatoria con media finita \(\mu\) y varianza finita \(\sigma^2\). Entonces para \(\epsilon > 0\) un número fijo, la probabilidad que \(X\) difiera en a lo menos \(\epsilon\) de su media, está acotada:

    \begin{equation}
    P(|X - \mu| \geq \epsilon) \leq \frac{\sigma^2}{\epsilon^2}
    \end{equation}

    O en términos del evento complementario:

    \begin{equation}
    P(|X - \mu| < \epsilon) \geq 1 - \frac{\sigma^2}{\epsilon^2}
    \end{equation}

**Comentario**: Este es un límite “laxo” en el sentido de que **no** es muy restrictivo y por tanto no muy preciso o informativo.

---

:material-pencil-box: **EJEMPLO**

!!! example "Ejemplo de \(\{-1, 0, 1\}\) para Chebyshev "
    Si \(X\) tiene tres posibles valores: \(\{ -1, 0, 1 \}\), con probabilidades \(\{ \frac{1}{18}, \frac{8}{9}, \frac{1}{18} \}\), respectivamente. ¿Cuál es la probabilidad \(P(\vert X - \mu \vert \geq 3\sigma)\) y cómo se compara con el límite de Chebyshev?

- Recordar que:

    \begin{equation}
    E[X] = \sum_{i=1}^N x_i P(x_i)
    \end{equation}

- También que:

    \begin{equation}
    \sigma^2_X = E\left[(X - \overline{X})^2\right] = E[X^2] - E^2[X]
    \end{equation}

- Siendo que:

    \begin{equation}
    P(|W| \geq \epsilon) \leq \frac{\sigma^2}{\epsilon^2}
    \end{equation}

- Pero una forma equivalente es:

    \begin{equation}
    P(|X - \mu_X| \geq k \sigma_X) \leq \frac{1}{k^2}
    \end{equation}

---

La media y la varianza de la VA discreta se obtienen de la siguiente forma:

\begin{equation}
E[X] = \sum_{i=1}^{3} x_i P(x_i) = (-1)\frac{1}{18} + (0)\frac{8}{9} + (1)\frac{1}{18} = 0
\end{equation}

\begin{equation}
\mathsf{Var}[X] = \sum_{i=1}^{3} (x_i - E[X])^2 P(x_i) = (-1)^2 \frac{1}{18} + (0)^2 \frac{8}{9} + (1)^2 \frac{1}{18} = \frac{1}{9}
\end{equation}

Utilizando la definición provista de la desigualdad de Chebyshev, se obtiene

\begin{equation}
P( \vert X - \mu_X \vert \geq k\sigma_X ) = P( \vert X - 0 \vert \geq 3 \cdot \frac{1}{3} ) \leq \frac{1}{3^2} = \frac{1}{9}
\end{equation}

---

!!! note "" 
    Mientras tanto, utilizando la PDF propiamente, se puede encontrar la probabilidad \(P( \vert X \vert \geq 1 )\) solicitada. Considerando que solo hay tres valores posibles de \(X\), \(\{ -1, 0, 1 \}\), los elementos de interés son \(\{ -1, 1 \}\) cuyas probabilidades son \(1/18 + 1/18 = 1/9\), igual que con Chebyshev.
    En general, la desigualdad de Chebyshev será mucho menos restrictiva que el análisis de la PDF, pero en este caso de ejemplo resultaron iguales.

---

### **Desigualdad de Markov**
!!! tip "Desigualdad de Markov"
    Si \(X\) es una variable aleatoria con \(f_X(x) = 0\) para \(x < 0\), entonces \(X\) es llamada una variable aleatoria no-negativa, para la cual aplica la desigualdad de Markov:

    \begin{equation}
    P(X \geq \epsilon) \leq \frac{E[X]}{\epsilon}
    \end{equation}

**Comentario**: En contraste con el límite de Chebyshev, que involucra tanto la media como la varianza, este límite requiere únicamente de la media de \(X\).

---

### **Prueba de la desigualdad de Markov**

La consideración es ahora en relación con la definición del valor esperado (el *momento ordinario de primer orden*):

\begin{equation}
\begin{aligned}
E[X] = \int_{0}^{\infty} x\, f_X(x)\,\mathrm{d}x &\geq \int_{\epsilon}^{\infty} x\, f_X(x)\,\mathrm{d}x \\
&\geq \int_{\epsilon}^{\infty} \epsilon\, f_X(x)\,\mathrm{d}x = \epsilon \int_{\epsilon}^{\infty} f_X(x)\,\mathrm{d}x \\
&= \epsilon P(X \geq \epsilon)
\end{aligned}
\end{equation}

---

:material-pencil-box: **EJEMPLO**

!!! example "Ejemplo de los resistores de baja calidad"
    Es posible asumir que en la manufactura de resistores eléctricos de baja calidad de 1000 \(\Omega\), la resistencia promedio es en efecto de 1000 \(\Omega\), según se determina por un análisis estadístico de mediciones, pero hay una gran variación alrededor de este valor. Si todos los resistores por encima de 1500 \(\Omega\) deben descartarse, ¿cuál es la fracción máxima de resistores que terminarían por fuera?

- Recordar que:

    \begin{equation}
    P(X \geq \epsilon) \leq \frac{E[X]}{\epsilon}
    \end{equation}

---

En este problema tenemos una distribución no-negativa (no hay valores negativos de resistencia eléctrica), y disponemos únicamente de la media y no de la varianza de la distribución, entonces aplica la desigualdad de Markov.

\begin{equation}
P(X \geq \epsilon) = P(X \geq 1500) \leq \frac{E[X]}{\epsilon} = \frac{1000}{1500} = \frac{2}{3}
\end{equation}

!!! note ""

    Es posible, aun así, que la proporción de resistencias descartadas sea menor. Bastaría con conocer la distribución para tener más certeza.



---

### **Ley de los grandes números I**

Sea \(\{X_i\}_{i=1}^N\) una muestra aleatoria. Los \(X_i\) son variables aleatorias idénticamente distribuidas e independientes IID con media común \(\mu\) y varianza \(\sigma^2\). Se espera intuitivamente que la media de la muestra, \(\overline{X_N},\) debería ser cercana a la media de la población \(\mu\) para \(N\) grande. Esto es:

\begin{equation}
\lim_{N \rightarrow \infty} \overline{X_N} = \lim_{N \rightarrow \infty} \frac{S_N}{N} = \mu
\end{equation}

donde \(S_N = X_1 + \ldots + X_N\) es la suma.

---

### **Ley de los grandes números II**

Sea \(\epsilon > 0\) un número fijo. Por la independencia de la secuencia \(X_1, \ldots, X_N\) en la muestra aleatoria, se cumple que:

\begin{equation}
E[S_N] = N\mu \qquad \sigma_{S_N}^2 = N\sigma^2
\end{equation}

La desigualdad de Chebyshev aplicada a \(S_N\) establece que:

\begin{equation}
P(\vert S_N - N\mu \vert \geq N\epsilon ) \leq \frac{\sigma_{S_N}^2}{(N\epsilon)^2} = \frac{N\sigma^2}{N^2\epsilon^2} = \frac{\sigma^2}{N\epsilon^2}
\end{equation}

En términos de la media \(\overline{X_N}\) de la muestra:

\begin{equation}
\begin{aligned}
P(\vert \overline{X_N} - \mu \vert \geq \epsilon ) &= P\left( \left\vert \frac{S_N}{N} - \mu \right\vert \geq \epsilon  \right) \\
&= P(\vert S_N - N\mu \vert \geq N\epsilon ) \leq \frac{\sigma^2}{N\epsilon^2}
\end{aligned}
\end{equation}

Para \(N \rightarrow \infty\) la cota de la derecha en la última ecuación tiende a 0 y entonces:

---

### **Ley de los grandes números — Definición**

!!! tip "Ley de los grandes números"
    Sea \(\left\{ X_i \right\}_{i=1}^{N}\) una muestra aleatoria con media común \(\mu\) y varianza \(\sigma^2\). Sea

    \begin{equation}
    S_N = X_1 + \cdots + X_N
    \end{equation}

    Entonces

    \begin{equation}
    P\left( \left| \frac{S_N}{N} - \mu \right| \geq \epsilon \right) \to 0
    \end{equation}

    conforme \(N \to \infty\) para cualquier \(\epsilon > 0\).

---

### **Del rigor en la ciencia — Jorge Luis Borges**

En aquel Imperio, el arte de la cartografía logró tal perfección que el mapa de una sola provincia ocupaba toda una ciudad, y el mapa del Imperio, toda una provincia. Con el tiempo, estos mapas desmesurados no satisficieron y los colegios de cartógrafos levantaron un mapa del Imperio, que tenía el tamaño del Imperio y coincidía puntualmente con él.

Menos adictas al estudio de la cartografía, las generaciones siguientes entendieron que ese dilatado mapa era inútil y no sin impiedad lo entregaron a las inclemencias del sol y los inviernos. En los desiertos del oeste perduran despedazadas ruinas del mapa, habitadas por animales y por mendigos; en todo el país no hay otra reliquia de las disciplinas geográficas.