# Sección 1: Valor esperado de una función de variables aleatorias

El valor esperado de una función de variables aleatorias se define como el promedio ponderado de los valores que puede tomar esta función.

Para variables aleatorias discretas $X$ y $Y$, y una función $g(X, Y)$, el valor esperado se define como:

$$
E[g(X, Y)] = \sum_x \sum_y g(x, y) \cdot P_{X,Y}(x, y)
$$

Para variables aleatorias continuas:

$$
E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \cdot f_{X,Y}(x, y) \, \mathrm{d}x \, \mathrm{d}y
$$

**Ejemplo:**  
Si $X$ y $Y$ son independientes y uniformes en $[0,1]$, y $g(x,y) = x + y$, entonces:

$$
E[X + Y] = \int_0^1 \int_0^1 (x + y) \, \mathrm{d}x \, \mathrm{d}y = 1
$$


# Sección 2: Momentos conjuntos alrededor del origen

Los momentos conjuntos alrededor del origen miden el comportamiento combinado de dos variables aleatorias.

Se definen como:

$$
\mu'_{rs} = E[X^r Y^s]
$$

Estos momentos permiten analizar características como la dispersión y forma conjunta de la distribución. Por ejemplo:

- $\mu'_{10} = E[X]$: esperanza de $X$
- $\mu'_{01} = E[Y]$: esperanza de $Y$
- $\mu'_{11} = E[XY]$: producto esperado

**Ejemplo:**  
Si $f_{X,Y}(x,y) = 4xy$ para $(x, y) \in [0,1] \times [0,1]$, entonces:

$$
\mu'_{11} = E[XY] = \int_0^1 \int_0^1 xy \cdot 4xy \, \mathrm{d}x \, \mathrm{d}y = \frac{4}{9}
$$

---

# Sección 3: La correlación

La covarianza entre dos variables aleatorias mide cómo varían ambas respecto a sus medias.

Se define como:

$$
\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]
$$

**Criterios:**

- Si la covarianza es positiva, $X$ y $Y$ tienden a aumentar juntos.  
- Si es negativa, uno tiende a aumentar cuando el otro disminuye.  
- Si es cero, no hay relación lineal.

**No correlación:** Si $\text{Cov}(X, Y) = 0$, entonces no hay correlación lineal entre $X$ y $Y$, pero esto no implica independencia.

La correlación es la forma normalizada de la covarianza:

$$
\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

donde $\sigma_X$ y $\sigma_Y$ son las desviaciones estándar de $X$ y $Y$.

**Interpretación de $\rho_{X,Y}$:**

- $\rho_{X,Y} = 1$: correlación positiva perfecta  
- $\rho_{X,Y} = -1$: correlación negativa perfecta  
- $\rho_{X,Y} = 0$: sin correlación lineal

**Ejemplo:**  
Sea $X$ una variable uniforme en $[-1,1]$, y $Y = X^2$. Entonces:

$$
\text{Cov}(X, Y) = 0
$$

Pero $X$ y $Y$ no son independientes.
