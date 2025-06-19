## Independencia y ortogonalidad

### Independencia y correlación

!!! tip "Independencia y correlación"
    La independencia estadística de $X$ y $Y$ es suficiente para garantizar que **no** están correlacionadas.

!!! note ""
    El recíproco de esta afirmación, que $X$ y $Y$ son independientes si no están correlacionadas, **no es necesariamente cierto**.  
    Una excepción importante: **variables gaussianas no correlacionadas sí son independientes**.

### Ortogonalidad

!!! tip "Ortogonalidad"
    Si $R_{XY} = 0$ para dos variables aleatorias $X$ y $Y$, estas se denominan ortogonales.

### En síntesis

- Si $R_{XY} = E[XY] = E[X]E[Y]$, entonces $X$ y $Y$ **no están correlacionadas**.
- La independencia, es decir, $f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$, **garantiza** que no estén correlacionadas, pero no a la inversa.
- Si $R_{XY} = 0$, las variables son **ortogonales**.

---

## Ejemplo de correlación y ortogonalidad

:material-pencil-box: **EJEMPLO**

!!! example "Correlación y ortogonalidad entre $X$ y $Y$"
    Sea $X$ una variable aleatoria con valor medio $\overline{X} = E[X] = 3$ y varianza $\sigma_X^2 = 2$, y sea $Y = -6X + 22$.

    Determinar si $X$ y $Y$ están correlacionadas y si son ortogonales.

1. Calculamos el segundo momento de $X$ alrededor del origen:

\begin{equation}
E[X^2] = \sigma_X^2 + \left( E[X] \right)^2 = 2 + 9 = 11
\end{equation}

2. Valor esperado de $Y$:

\begin{equation}
E[Y] = -6E[X] + 22 = -6 \cdot 3 + 22 = 4
\end{equation}

3. Producto cruzado:

\begin{equation}
\begin{aligned}
R_{XY} &= E[XY] \\
&= E[X(-6X + 22)] = E[-6X^2 + 22X] \\
&= -6E[X^2] + 22E[X] = -6(11) + 22(3) = 0
\end{aligned}
\end{equation}

!!! note ""
    $X$ y $Y$ **son ortogonales** porque $R_{XY} = 0$.  
    Sin embargo, **no están no correlacionadas** en el sentido de la media, ya que $E[X]E[Y] = 3 \cdot 4 = 12 \neq R_{XY}$.

!!! important ""
    Dos variables aleatorias pueden ser ortogonales incluso si una es función lineal de la otra: $Y = aX + b$.

---

## Momentos centrales conjuntos

### Definición

!!! tip "Momentos centrales conjuntos"
    Para dos variables aleatorias $X$ y $Y$:

    \begin{equation}
    \begin{aligned}
    \mu_{nk} &= E\left[ (X - \overline{X})^n (Y - \overline{Y})^k \right] \\
    &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x - \overline{X})^n (y - \overline{Y})^k f_{X,Y}(x,y) ~\mathrm{d}x ~\mathrm{d}y
    \end{aligned}
    \end{equation}

**Momentos importantes**:

- $\mu_{20} = E[(X - \overline{X})^2] = \sigma_X^2$
- $\mu_{02} = E[(Y - \overline{Y})^2] = \sigma_Y^2$

---

## Covarianza de dos variables aleatorias

!!! tip "Covarianza"
    La covarianza $C_{XY}$ es el momento central conjunto de orden (1,1):

    \begin{equation}
    \begin{aligned}
    C_{XY} &= E[(X - \overline{X})(Y - \overline{Y})] \\
    &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x - \overline{X})(y - \overline{Y}) f_{X,Y}(x,y) ~\mathrm{d}x ~\mathrm{d}y \\
    &= E[XY] - E[X]E[Y] = R_{XY} - E[X]E[Y]
    \end{aligned}
    \end{equation}

**Propiedades**:

1. Si $X$ y $Y$ son independientes o no correlacionadas: $C_{XY} = 0$  
2. Si $X$ y $Y$ son ortogonales: $C_{XY} = -E[X]E[Y]$  
   - Si además $E[X] = 0$ o $E[Y] = 0$, entonces $C_{XY} = 0$

---

## Coeficiente de correlación de Pearson

El coeficiente de correlación normalizado es:

\begin{equation}
\rho = \frac{\mu_{11}}{\sqrt{\mu_{20} \mu_{02}}} = \frac{C_{XY}}{\sigma_X \sigma_Y}
\end{equation}

También puede escribirse como:

\begin{equation}
\begin{aligned}
\rho &= \frac{E[(X - \overline{X})(Y - \overline{Y})]}{\sigma_X \sigma_Y} \\
&= E\left[ \frac{(X - \overline{X})}{\sigma_X} \cdot \frac{(Y - \overline{Y})}{\sigma_Y} \right]
\end{aligned}
\end{equation}

**Rango**: $-1 \leq \rho \leq 1$

### Visualización de casos especiales del coeficiente de correlación de Pearson

![Ejemplo: Ubicación del "centro de gravedad"](images/10_pearson.svg)

---

## Funciones características conjuntas

### Definición
La función característica conjunta de dos variables aleatorias $X$ y $Y$ está definida por: 


\begin{equation}
\Phi_{X,Y}(\omega_1, \omega_2) = E\left[ e^{j\omega_1 X + j\omega_2 Y} \right]
\end{equation}

donde $\omega_1, \omega_2$ son números reales. Una forma equivalente es:

\begin{equation}
\Phi_{X,Y}(\omega_1, \omega_2) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y) e^{j\omega_1 x + j\omega_2 y} ~\mathrm{d}x ~\mathrm{d}y
\end{equation}

Lo anterior es la transformada bidimensional de Fourier (con signos cambiados para $\omega_1, \omega_2$) de la función de densidad conjunta. De la transformada inversa de Fourier se tiene:

\begin{equation}
f_{X,Y}(x,y) = \frac{1}{(2\pi)^2} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \Phi_{X,Y}(\omega_1, \omega_2) e^{-j\omega_1 x - j\omega_2 y} ~\mathrm{d}\omega_1 ~\mathrm{d}\omega_2
\end{equation}

Con poner $\omega_2 = 0$ u $\omega_1 = 0$, se obtiene las funciones características de $X$ o $Y$, de $\Phi_{X,Y}(\omega_1, \omega_2)$. Estas se llaman funciones características marginales: 

- $\Phi_X(\omega_1) = \Phi_{X,Y}(\omega_1, 0)$
- $\Phi_Y(\omega_2) = \Phi_{X,Y}(0, \omega_2)$

Los momentos conjuntos $m_{nk}$ pueden hallarse de la función característica conjunta como sigue:

\begin{equation}
m_{nk} = \left. (-j)^{n+k} \frac{\partial^{n+k} \Phi_{X,Y}(\omega_1, \omega_2)}{\partial \omega_1^n ~\partial \omega_2^k} \right|_{\omega_1 = 0,~ \omega_2 = 0}
\end{equation}
