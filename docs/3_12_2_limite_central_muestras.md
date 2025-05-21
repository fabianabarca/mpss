## Teorema del límite central para medias de muestras

### Definición de la convergencia en la media

Si $\{ X_i \}_{i=1}^N$ es una **muestra** de $N$ elementos de una **población**, su **media muestral** es $\overline{X_N} = S_N/N = \mu_N$, donde $S_N = X_1 + X_2 + \cdots + X_N$. Se puede considerar (2) para hacer 

\begin{equation*}
\frac{S_N - N\mu}{\sigma \sqrt{N}} \cdot \frac{1/N}{1/N} = \frac{\overline{X_N} - \mu}{\sigma / \sqrt{N}}
\end{equation*}

!!! tip "Definición de convergencia en la media"
    Sean $X_1, \ldots, X_N$ una muestra de variables aleatorias $i.i.d.$ de una **población** con media común $\mu$ y desviación estándar $\sigma$ y con una **media de la muestra** $\overline{X_N}$. Entonces

    \begin{equation}
    Z = \frac{\overline{X_N} - \mu}{\sigma / \sqrt{N}}
    \label{E:media_muestras}
    \end{equation}

    aproxima $\mathcal{N}(0,1)$ conforme $N \rightarrow \infty$. Equivalentemente, $\overline{X_N} \sim \mathcal{N}(\mu, \sigma^2/N)$

### Visualización del teorema del límite central para medias de muestras

Aunque una **población** tenga una distribución con media $\mu = E[X]$, una **realización** o **muestra** de esta distribución tendrá casi siempre un valor ligeramente distinto.

!!! example "Ejemplo de una distribución uniforme"

    Sea $X \sim \mathsf{unif}(0,1)$ con $\mu = E[X] = \mathbf{0.5}$. Sea además $X_i$ **una muestra** de esta distribución con 500 elementos y con una media estadística de $\mu_{X_i} = 0.5138 \neq 0.5$.


    ![](images/12_TLCmuestra.svg)

Al hacer una simulación de $N$ muestras se obtienen $N$ medias distintas $\mu_{X_i}$. ¿Cómo se distribuyen estos valores alrededor de $\mu$ y cómo cambia la distribución según $N$?

![](images/12_TLCmedias.svg)

!!! note ""

    Entre más grande es $N$ más "agrupados" están los valores de la media de la muestra $\overline{X_N} = \mu_N$ alrededor de la "media verdadera" de la población, $\mu$.


![](images/12_grupos_dots.svg)  ![](images/12_medias_muestras.svg) 

:material-pencil-box: **EJEMPLO**

!!! example "Número de visitas mensuales al cajero automático"

    Suponga que el número de veces que un cliente utiliza el cajero automático de un banco en un mes es una variable aleatoria con un valor medio de 3,2 y una desviación estándar de 2,4. El banco conoce estos datos con exactitud pues puede monitorear cada visita de la **población** de sus miles de clientes.

    !!! note ""
         
        Si se selecciona aleatoriamente una muestra de 100 clientes, ¿qué tan probable es que el promedio de veces que el cajero es utilizado en la **muestra** exceda 3,5? 

    La probabilidad solicitada es $P(\overline{X_N} > 3.5)$, donde $\overline{X_N}$ es el valor medio de la muestra. La muestra es grande ($N = 100$ clientes) y por tanto la distribución de $\overline{X_N}$ se puede aproximar a una distribución normal.

    \begin{equation*}
    P(\overline{X_N} > 3.5) \approx P \left( Z > \frac{3.5 - \mu}{\sigma/\sqrt{N}} \right) = P \left( Z > \frac{3.5 - 3.2}{0.24} \right) = 1 - F_{Z}(1.25) = 0.1056
    \end{equation*}

    La probabilidad es pequeña porque la muestra es grande y la desviación estándar de la muestra es muy pequeña, de solo 0,24, de forma tal que la media de una muestra de 100 personas se acerca ``bastante'' a la media de la población de quizá miles de personas.