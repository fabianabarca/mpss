## Pruebas de Bernoulli o pruebas repetidas I.

### Definición

**Pruebas de Bernoulli**

Un tipo de experimento en el que solo hay **dos resultados posibles** en cualquier prueba.

- Sea $A$ el evento elemental que tiene uno de los dos resultados posibles como su elemento. $\overline{A}$ es el otro (y único) posible evento elemental.

- Se repetirá el experimento básico $N$ veces, y se calculará la probabilidad de que $A$ suceda $k$ veces (no necesariamente consecutivas, sino en cualquier orden).

- Los eventos elementales son estadísticamente independientes. 

- El evento $A$ ocurre en cualquier ensayo con probabilidad:
$$
\boxed{P(A) = p}
$$

- El evento $\overline{A}$ entonces tiene la probabilidad complementaria:

    $$
    \boxed{P(\overline{A}) = 1 - p = q}
    $$
---
## Pruebas de Bernoulli o pruebas repetidas II.


- Ejemplo: después de $N$ ensayos del experimento básico, una secuencia posible (de muchas) es el evento $A$ ocurriendo $k$ veces seguidas, seguido por el evento $\overline{A}$ ocurriendo $N-k$ veces. Puesto que se asumió la independencia estadística de los ensayos, la probabilidad de esta secuencia particular es:

$$
\begin{aligned}
& \underbrace{P(A)P(A) \cdots P(A)}_{k \text{ eventos } A} \underbrace{P(\overline{A}) P(\overline{A})\cdots P(\overline{A})}_{N-k \text{ eventos } \overline{A}} \\
&= p^{k}(1 - p)^{N - k}
\end{aligned}
$$

- Hay otras secuencias que dan $k$ eventos $A$ y $N-k$ eventos $\overline{A}$. Por la independencia estadística, la *probabilidad* de cada una de estas *secuencias* es la misma.
---
## Pruebas de Bernoulli o pruebas repetidas III.

- Del análisis combinatorio, el número de maneras de tomar $k$ objetos de una colección de $N$ objetos es:

$$
\binom{N}{k} = \frac{N!}{k!(N-k)!} = \complement_{k}^{N} = {}_N\mathrm{C}_k
$$

La cantidad $\binom{N}{k}$ se conoce como *coeficiente binomial*.

Se obtiene entonces la, así llamada, *distribución binomial*:

$$
\begin{aligned}
P(k) &= P\{\text{$A$ ocurre exactamente $k$ veces}\} \\
     &= \binom{N}{k}p^{k}(1 - p)^{N - k}
     \\
&= (\text{el número de combinaciones}) \times (\text{la probabilidad de cada una})
\end{aligned}
$$

---

!!! example "Ejemplo de transmisión binaria de datos y errores I"
    Un dato binario (0 o 1) se envía por una línea de transmisión con una probabilidad de error de 0.001. Si 1000 bits son enviados, ¿cuál es la probabilidad de que haya... 

1. ...exactamente 5 errores:

$$
P(\{\text{exactamente 5 errores}\}) = \binom{1000}{5}(0.001)^5 (0.999)^{995}
$$


2. ...o entre 2 y 5 errores?

$$
P(\{\text{entre 2 y 5 errores}\}) = \sum_{k=2}^{5} \binom{1000}{k}(0.001)^k (0.999)^{1000-k}
$$


---
## Hay un problema con los números grandes

- ¡Los factoriales son difíciles de evaluar!
- Las potencias de muy alto orden también son difíciles de calcular.

Por eso existen dos aproximaciones de la distribución binomial que hacen más práctica su aplicación y su cálculo numérico $^1$:

a) Aproximación de De Moivre-Laplace  
b) Aproximación de Poisson



---

## a) Aproximación de De Moivre-Laplace

### Aproximaciones de las pruebas de Bernoulli

**Fórmula de Stirling**

Una aproximación de los factoriales de la forma:

$$
m! \approx (2\pi m)^{\frac{1}{2}} m^{m} e^{-m}
$$

para \( m \) grande. Entonces,

$$
\boxed{
\binom{N}{k}p^{k}(1 - p)^{N - k} \approx \frac{1}{\sqrt{2\pi N p (1-p)}} \exp \left[ -\frac{(k - N p)^2}{2 N p (1-p)} \right]
}
$$

Aplica para $N$, $k$, $(N-k)$ grandes, $k$ cerca de $Np$ tales que sus desviaciones de $Np$ (más arriba o más abajo) son pequeñas en magnitud relativas tanto a $Np$ como a $N(1-p)$.

---

## b) Aproximación de Poisson
### Aproximaciones de las pruebas de Bernoulli

Esta aproximación es más sencilla de evaluar, pero tiene algunas restricciones adicionales. Si se cumple que:

- $k$ es pequeño  
- $N$ y por tanto $(N-k)$ son grandes  
- $p\ll 1$ y además $Np = \lambda \approx 1$

Entonces la expresión a continuación es una aproximación de la prueba de Bernoulli,

$$
\boxed{
P(k) = \binom{N}{k}p^{k}(1 - p)^{N - k} \approx \frac{\lambda^k}{k!} e^{-\lambda}
}
$$


llamada *distribución de Poisson* (aquí sin demostración).

---
## Interpretación de la aproximación de Poisson
### Aproximaciones de las pruebas de Bernoulli

La *distribución de Poisson* describe situaciones enumerables como el número de personas en una fila durante un intervalo de tiempo.

Por ejemplo, si la tasa de llegada es $\lambda$ entonces la probabilidad de que hay $k$ personas en la fila está dada por 

$$
\boxed{
P(k) = \frac{\lambda^k}{k!} e^{-\lambda}
}
$$
---
!!! example "Ejemplo de transmisión binaria de datos y errores I"
    Un dato binario (0 o 1) se envía por una línea de transmisión con una probabilidad de error de 0.001. Si 1000 bits son enviados, ¿cuál es la probabilidad de que haya... 

Verificar en este ejemplo que:

- $k$ es pequeño: $k = 5$  
- $N$ y $(N-k)$ son grandes: $N = 1000$ y $(N-k) = 995$  
- $p \ll 1$ y además $Np = \lambda \approx 1$, que son: $p = 0.001$ y $Np = 1000 \cdot 0.001 = 1$

Entonces aplica la distribución de Poisson:

$$
P(k) = \frac{\lambda^k}{k!} e^{-\lambda}
$$

---

!!! example "Ejemplo de transmisión binaria de datos y errores II"
    Entonces, ¿cuál es la probabilidad de que haya...

1. ...exactamente 5 errores:

$$
\begin{aligned}
P(\{\text{exactamente 5 errores}\}) &\approx \frac{1^5 e^{-1}}{5!} \\
&= 0.003065 \approx 0.3\%
\end{aligned}
$$

2. ...o entre 2 y 5 errores?

$$
\begin{aligned}
P(\{\text{entre 2 y 5 errores}\}) &\approx \frac{1^2 e^{-1}}{2!} + \frac{1^3 e^{-1}}{3!} + \frac{1^4 e^{-1}}{4!} + \frac{1^5 e^{-1}}{5!} \\
&= 0.26365 \approx 26.4\%
\end{aligned}
$$

!!! note ""
    Computacionalmente, estas aproximaciones son mucho más sencillas de calcular.