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
**Valor esperado de una función de variables aleatorias**

El PDF conjunto de la cantidad \( X \) de almendras y la cantidad \( Y \) de semillas de marañón (y la cantidad \( Z \) de maní) en un tarro de 1 kg es:
Sean los valores de \(x\) y \(y\) tales que:

- x está entre 0 y 1,
- y está entre 0 y 1,
- y la suma x + y es menor o igual que 1.

$$
f_{X,Y}(x, y) = 24xy
$$

En cualquier otro caso:

$$
f_{X,Y}(x, y) = 0
$$

Si 1 kg de almendras le cuesta a la compañía ₡6000, un kilogramo de semillas de marañón son ₡10.000 y 1 kg de maní cuesta ₡3.500.  
**¿Cuál es el costo esperado total del contenido del tarro?**
Sea la función del costo

$$
h(X, Y) = 6000X + 10000Y + 3500(1 - X - Y)
$$

Entonces,

$$
E[h(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} h(x, y)\, f_{X,Y}(x, y) \, dx\, dy
$$

Se reduce a:

$$
E[h(X, Y)] = \int_0^1 \int_0^{1-x} \left[6000x + 10000y + 3500(1 - x - y)\right] 24xy\, dy\, dx
$$

$$
= 7100
$$

que representa los costos esperados del contenido de la caja.



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

# Ejemplo de la ubicación del “centro de gravedad” I:

![Ejemplo: Gráfica de gravedad](./images/10_gravedad.svg)


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


# Ejemplo de correlación del tarro de nueces I
El PDF conjunto de la cantidad X de almendras, la cantidad Y de semillas de marañón y la cantidad Z de maní en un tarro de 1 kg está dado por:

Sea f_{X,Y}(x, y) = 24xy  en el dominio:
- x está entre 0 y 1,
- y está entre 0 y 1,
- y la suma x + y es menor o igual que 1.

¿Cuál es la correlación entre X y Y?


![Fórmula en blanco](https://latex.codecogs.com/svg.image?\color{white}R_{XY}=m_{11}=E[XY]=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy\,f_{X,Y}(x,y)\,dx\,dy)


$$
= \int_0^1 \int_0^{1-y} xy \cdot 24xy \, dx \, dy = 24 \int_0^1 y^2 \left( \int_0^{1-y} x^2 \, dx \right) dy
$$

$$
= \frac{24}{3} \int_0^1 y^2 (1 - y)^3 \, dy
$$

$$
= \frac{24}{3} \left[ -\frac{y^6}{6} + \frac{3y^5}{5} - \frac{3y^4}{4} + \frac{y^3}{3} \right]_0^1 = \frac{2}{15} \approx 0{,}13
$$


