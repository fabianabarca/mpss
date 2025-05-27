## El teorema del límite central para sumas

!!! tip "Definición de la convergencia en la distribución"

    Considérese $X_1, \ldots, X_N$ variables aleatorias *independientes e idénticamente distribuidas* ($i.i.d.$), con media común $\mu_{X_i} = \mu$ y desviación estándar $\sigma_{X_i} = \sigma$. Sea además:

    $$
    S_N = X_1 + \cdots + X_N
    $$

    la **suma** de ellas. Según el teorema del límite central, $S_N \sim \mathcal{N}(N \mu, N \sigma^2)$ conforme $N \to \infty$. Alternativamente, si $Z$ es una distribución *normalizada* de $S_N$:

    $$
    Z = \frac{S_N - \mu_{S_N}}{\sigma_{S_N}} = \frac{S_N - N\mu}{\sigma \sqrt{N}}
    $$

    entonces $Z$ tiene una distribución $f_Z(z)$ que aproxima a $\mathcal{N}(0,1)$ conforme $N \to \infty$.

**Nota**: $\mathcal{N}(0,1)$ es una función de distribución gaussiana de media 0 y varianza 1, donde $\mathcal{N}$ alude a "normal".

---

## Visualización del teorema del límite central para sumas

### Caso 1: convolución de la función de densidad

$f_{S_N}(x_1,\ldots,x_N) = f_{X_1}(x_1) \ast \cdots \ast f_{X_N}(x_N)$

![](images/12_TLCconv.svg)

---

## Visualización del teorema del límite central para sumas

### Caso 2: simulación de la suma de datos aleatorios generados de $N$ va $X_i \sim \mathsf{exponencial}(1)$

![](images/12_TLCsuma.svg)

---

## Deducción de la media y desviación estándar para la suma de va

**Con respecto a la media de $S_N$**

$$
\begin{aligned}
E \left[S_N \right] & = E\left[ X_1 + X_2 + \cdots + X_N \right] \\
  					& = \mu + \mu + \cdots + \mu \\
  					& = N\mu
\end{aligned}
$$

Lo anterior se justifica porque $E[X_i] = \mu$.

**Con respecto a la desviación estándar de $S_N$**

$$
\begin{aligned}
{\sigma_{S_N}}^2 	& = E \left[ \left( S_N - \overline{S_N}\right)^2 \right] \\
               		& = E \left[ {S_N}^2 \right] - \left( E\left[ S_N \right] \right)^2
\end{aligned}
$$

De la última identidad, se conoce el segundo término, que es la media de $S_N$ al cuadrado. Con respecto al primer término,

$$
\begin{aligned}
  E\left[ {S_N}^2 \right] & = E\left[ \left( X_1 + X_2 + \cdots + X_N \right)^2 \right] \\
                      & = E\left[ (X_1 + X_2 + \cdots + X_N)(X_1 + X_2 + \cdots + X_N)\right] \\
                      & = E\left[ X_{1}^2 + X_1 X_2 + X_1 X_3 + \cdots X_1 X_N + \cdots + \ldots \right. \\
                      & \qquad \left. \ldots + X_N X_1 + X_N X_2 + \cdots + X_N X_{N-1} + X_{N}^2 \right] \\
                      & = \sum_{i=1}^N E[X_{i}^2] + \sum_{i=1}^N \sum_{j=1, j \neq i}^N E[X_i]E[X_j] \\
                      & =  N (\sigma^2 + \mu^2) + N(N-1)\mu^2 \\
                      & = N \sigma^2 + N\mu^2 + N^2\mu^2 - N\mu^2 \\
                      & = N\sigma^2 + N^2\mu^2
\end{aligned}
$$

Finalmente,

$$
\begin{aligned}
  {\sigma_{S_N}}^2 & = E \left[ {S_N}^2 \right] - \left( E\left[ S_N \right] \right)^2 \\
         	& = N\sigma^2 + N^2\mu^2 - N^2\mu^2 \\
        	& = N\sigma^2
\end{aligned}
$$

de donde se obtiene que la desviación estándar es $\sigma_{S_N} = \sigma \sqrt{N}$.

Así se plantea, como antes,

$$
Z = \frac{S_N - N\mu}{\sigma \sqrt{N}}
$$

---

## Ejemplo de los resistores en serie

### Interpretación del teorema del límite central para sumas

Los resistores tienen una resistencia *nominal* y un porcentaje de *tolerancia*. Por ejemplo, un resistor de 330 ohm con una tolerancia del 5 % se espera que tenga una resistencia entre 313,5 y 346,5 ohm.

!!! note ""
          Considérense cinco resistores de 330 ohm, escogidos aleatoriamente de una población 
          con 5 % de tolerancia, y modélese la resistencia de cada una como una distribución 
          uniforme en $[313.5 \quad 346.5]$. Si son conectados en serie, ¿cuál es la distribución 
          de la resistencia $R$ del sistema, dada por $R = X_1 + \ldots + X_5$? Los $X_i$ son los 
          valores de resistencia (i.i.d.).


Una variable aleatoria uniformemente distribuida en $[a \quad b]$ tiene media $\mu = (a + b)/2$ y desviación estándar $\sigma = (b - a) / \sqrt{12}$. Para **cada resistencia**:

- la media es $E[X_i] = (313.5 + 346.5)/2 = 330~\Omega$, es decir, la resistencia nominal
- la desviación estándar es $\sigma = (346.5 - 313.5) / \sqrt{12} = 9.529~\Omega$

La resistencia **del sistema en serie** tiene una media y desviación estándar de

$$
\begin{aligned}
E[R] 	&= N\mu = 5 \cdot 330 = 1650~\Omega\\
SD[R] 	&= \sqrt{N} \sigma = \sqrt{5} \cdot 9.529 = 21.3~\Omega
\end{aligned}
$$


¿Cómo es la distribución de probabilidad de $R = X_1 + \ldots + X_5$? ¿Es $R$ también distribuido uniformemente? Una simulación de 10 000 instancias distintas de $R$ muestra:

![Distribución suma resistores](images/12_dist_resistores.svg)

que es una muy buena aproximación de $\mathcal{N}(\mu,\sigma) = \mathcal{N}(1650,21.3)$.

---

## Ejemplo de la revisión de formularios antes del mediodía
!!! Nota ""
          Hay 40 formularios por revisar. Por los años de experiencia, la persona que los revisa sabe
          que el tiempo requerido para revisar cada uno es una variable aleatoria con un valor esperado
          de 6 minutos y una desviación estándar de 6 minutos. Si los tiempos de revisión son 
          independientes y la persona inicia a las 7:50 a.m. revisando de forma continua, ¿cuál es la
          probabilidad de que termine antes de las 12:00 m.d.?

- Recordar que $Z = \frac{S_N - N\mu}{\sigma \sqrt{N}}$
- También que $f_Z(z) \rightarrow \mathcal{N}(0,1)$
- ¿Cuánto es $N$?
- ¿Cuánto es $\mu$?
- ¿Cuánto es $\sigma$?
- ¿Cuánto es el tiempo disponible?


Para este problema, se debe aplicar el teorema del límite central para sumas, puesto que se trabajará con la suma del tiempo de revisión de todos los formularios. De la información del enunciado:

- 40 formularios: $N = 40$
- Tiempo promedio de revisión por formulario: $\mu = 6$
- Desviación estándar: $\sigma = 6$

La persona comienza a las 7:50 a.m. y para terminar antes de las 12:00 m.d. deberá hacerlo en menos de 250 minutos. El objetivo es, por tanto, encontrar $P(S_N \leq 250)$, o de forma equivalente, $P(Z \leq Z_0)$, donde

$$
Z_0 = \frac{S_0 - N \mu}{\sigma \sqrt{N}} = \frac{250 - 40 \cdot 6}{6 \sqrt{40}} = 0.263
$$

Es decir,

$$
P \left( \frac{S_N-40\cdot6}{6 \sqrt{40}}\leq \frac{250-40\cdot6}{6 \sqrt{40}}\right)
$$

$$
P \left( Z \leq 0.263 \right)
$$

Utilizando la tabla para probabilidades acumulativas para valores positivos de $Z$, el valor más cercano a $0.263$ está dado para $0.26$.

!!! note ""

    $$
    P \left( Z \leq 0.263 \right) \approx P \left( Z \leq 0.26 \right) = 0.6026 \Rightarrow 60.26 \%
    $$

    La persona que revisa tiene un 60.26 % de probabilidad de completar la revisión de formularios antes del mediodía.



