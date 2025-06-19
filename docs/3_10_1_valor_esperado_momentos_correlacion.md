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
Para dos variables aleatorias  X  y  Y  se denotan por mₙₖ = E[XⁿYᵏ]
 y se definen por:

![Fórmula blanca](https://latex.codecogs.com/svg.image?\color{white}m_{nk}=\mathbb{E}\left[X^nY^k\right]=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}x^n&space;y^k&space;f_{X,Y}(x,y)\,&space;dx&space;\,&space;dy)

### Casos especiales

- ![m_n0](https://latex.codecogs.com/svg.image?\color{white}m_{n0}=\mathbb{E}[X^n]) son los momentos ![m_n](https://latex.codecogs.com/svg.image?\color{white}m_n) de ![X](https://latex.codecogs.com/svg.image?\color{white}X)
- ![m_0k](https://latex.codecogs.com/svg.image?\color{white}m_{0k}=\mathbb{E}[Y^k]) son los momentos de ![Y](https://latex.codecogs.com/svg.image?\color{white}Y)
- ![n+k](https://latex.codecogs.com/svg.image?\color{white}n&plus;k) es el orden de los momentos. Ejemplo: 
  ![m_02](https://latex.codecogs.com/svg.image?\color{white}m_{02}), 
  ![m_20](https://latex.codecogs.com/svg.image?\color{white}m_{20}), 
  ![m_11](https://latex.codecogs.com/svg.image?\color{white}m_{11}) 
  son los momentos de segundo orden de ![X](https://latex.codecogs.com/svg.image?\color{white}X) y ![Y](https://latex.codecogs.com/svg.image?\color{white}Y)
- ![m_01](https://latex.codecogs.com/svg.image?\color{white}m_{01}=\mathbb{E}[Y]=\overline{Y}) y 
  ![m_10](https://latex.codecogs.com/svg.image?\color{white}m_{10}=\mathbb{E}[X]=\overline{X}) 
  son los valores esperados de ![Y](https://latex.codecogs.com/svg.image?\color{white}Y) y ![X](https://latex.codecogs.com/svg.image?\color{white}X), y son las coordenadas del centro de gravedad de la función 
  ![f_XY](https://latex.codecogs.com/svg.image?\color{white}f_{X,Y}(x,y))

**Ejemplo de la ubicación del “centro de gravedad” I:**

![Ejemplo: Gráfica de gravedad](./images/10_gravedad.svg)


# Sección 3: La correlación

La covarianza entre dos variables aleatorias mide cómo varían ambas respecto a sus medias.

El momento de segundo orden  m₁₁ = E[XY] es denominado la **correlación** de X y  Y.  
Recibe el símbolo especial Rₓᵧ por su importancia.

$$
R_{XY} = m_{11} = E[XY] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy \, f_{X,Y}(x, y) \, dx \, dy
$$

### Interpretaciones posibles

- “La correlación es el grado en el cual dos o más cantidades están linealmente asociadas”.
- Pero (fundamental) **“correlación no implica causalidad”**.


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
