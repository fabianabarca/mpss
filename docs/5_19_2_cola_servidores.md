### Presentación

[19 - Vector de probabilidad de estado estable](https://www.overleaf.com/read/cpfydpqvyxzs#8095ae)

### Secciones


## Cola de un solo servidor 

:material-pencil-box: **EJEMPLO**

!!! example "La cola de un solo servidor "
    Encuentre el vector de probabilidad $\phi$ de estado estable para la cola de un servidor.

    Usando los valores de $\Omega_i$, $p_i$, $q_i$ de este ejemplo:
    - $\Omega_{i-1}p_{i-1} = \lambda$
    - $\Omega_i q_i = \nu$
    
Para todo $i \geq 1$:

$$
\phi_i = \frac{\Omega_{i-1}p_{i-1}}{\Omega_i q_i} \phi_{i-1} = \frac{\lambda}{\nu} \phi_{i-1}
$$

Por lo tanto:

$$
\phi_i = \frac{\lambda}{\nu} \phi_{i-1} = \left( \frac{\lambda}{\nu} \right)^2 \phi_{i-2} = \cdots = \left( \frac{\lambda}{\nu} \right)^i \phi_0
$$




Para $i = 0, 1, 2, \ldots$, la normalización implica que:

$$
\sum_{i=0}^{\infty} \phi_i = \phi_0 \sum_{i=0}^{\infty} \left( \frac{\lambda}{\nu} \right)^i = 1
$$

Utilizando la fórmula de la serie geométrica:

$$
\phi_0\sum_{i=0}^{\infty} \left( \frac{\lambda}{\nu} \right)^i = \phi_0\frac{1}{1 - \frac{\lambda}{\nu}}
$$

para $\frac{\lambda}{\nu} < 1$.



Si $\frac{\lambda}{\nu} \geq 1.$, la condición de normalización no se satisface. 

!!! note ""
    Para que exista un estado estable, la tasa de partidas $\nu$ debe ser mayor que la de llegadas $\lambda$.De otra orma, al cola tiende a hacerse más grande y no alcanza una estabilidad  

---
:material-pencil-box: **EJEMPLO**
!!! example "La cola de un solo servidor con $\lambda < \nu$ "
    Para la cola de un servidor con $\lambda < \nu$, encuentre la longitud esperada de la cola en estado estable.



En el estado estable, la longitud $L$ de la cola es $i$ con probabilidad $\phi_i$, para $i = 0, 1, 2, \ldots$  
Nótese que la variable aleatoria $X = L + 1$ está geométricamente distribuida.

Para $j \geq 1$:

$$
P(X = j) = P(L = j - 1) = \phi_{j-1} = (1 - q) q^{j - 1}
$$

Donde:

$$
q = \frac{\lambda}{\nu}
$$


De esta forma, la esperanza de $X$ es:

$$
E[X] = \sum_{j=0}^{\infty} j (1 - q) q^{j - 1}
     = \sum_{j=0}^{\infty} j q^{j - 1}
     = \sum_{j=0}^{\infty} j q^j
$$

Utilizando que:

$$
\sum_{j=0}^{\infty} j q^j = \frac{q}{(1 - q)^2}
\quad \Rightarrow \quad
E[X] = \frac{1}{1 - q} = \frac{\nu}{\nu - \lambda}
$$

Entonces:

$$
E[L] = E[X - 1] = \frac{\lambda}{\nu - \lambda}
$$

!!! note ""
    La longitud esperada de la cola de un servidor para $\lambda < \nu$ es:  
    $\boxed{\dfrac{\lambda}{\nu - \lambda}}$

---

!!! note "Nota"
    Se utiliza el resultado:

    $$
    \sum_{j=0}^{\infty} j x^{j - 1} = \frac{1}{(1 - x)^2}
    $$

    para $-1 < x < 1$.

    También se usa la ecuación:

    $$
    \sum_{j=0}^{\infty} jx^j = \frac{x}{(1 - x)^2}
    $$

    para $-1 < x < 1$.





## Cola de un infinito número de servidores

:material-pencil-box: **EJEMPLO**

!!! example "La cola de un infinito número de servidores "

    Encuentre el vector $\phi$ de probabilidad de estado estable para la cola con infinito número de servidores.

---

Si se usan los valores de $\Omega_i$, $p_i$, $q_i$ de tal ejemplo:

$$
\Omega_{i-1}p_{i-1} = \frac{((i-1)\nu + \lambda)\lambda}{(i-1)\nu + \lambda} = \lambda
$$

$$
\Omega_i q_i = \frac{(i\nu + \lambda)i\nu}{i\nu + \lambda} = i\nu
$$

Por consiguiente:

$$
\phi_i = \frac{\Omega_{i-1}p_{i-1}}{\Omega_i q_i} \phi_{i-1} = \frac{\lambda}{i\nu} \phi_{i-1}
$$



Si $i = 1, 2, \ldots$, esta relación puede usarse recursivamente:

$$
\begin{aligned}
\phi_i &= \frac{\lambda}{i\nu} \phi_{i-1} \\
       &= \frac{\lambda}{i\nu} \cdot \frac{\lambda}{(i-1)\nu} \phi_{i-2} \\
       &\quad \vdots \\
       &= \frac{1}{i!} \left( \frac{\lambda}{\nu} \right)^i \phi_0
\end{aligned}
$$



Si se usa normalización:

$$
1 = \sum_{i=0}^{\infty} \phi_i = \phi_0 \sum_{i=0}^{\infty} \frac{(\lambda/\nu)^i}{i!} = \phi_0 e^{\lambda/\nu}
$$

Por lo tanto, $\phi_0 = e^{-\lambda/\nu}$. En conclusión, para la cola con infinito número de servidores, las probabilidades de estado estable son:

!!! note ""

    $$
    \phi_i = \frac{(\lambda/\nu)^i}{i!} e^{-\lambda/\nu}, \quad i = 0, 1, 2, \ldots
    $$


!!! note "Nota"
    Las probabilidades en estado estable para la cola con infinito número de servidores están distribuidas de acuerdo a Poisson con parámetro $\frac{\lambda}{\nu}$. Consecuentemente, la longitud esperada de la cola con infinito de servidores es $\frac{\lambda}{\nu}$. El estado estable siempre esxiste: esto tiene sentido porque hay un infinito número de servidores.

---
## 90 % del tiempo con $N$ o menos clientes

:material-pencil-box: **EJEMPLO**

!!! example "90 % del tiempo con $N$ o menos clientes "

    Para la cola con infinito número de servidores con tasa de arribo $\lambda$ y tiempo medio de servicio $1/\nu$,  
    encuentre el número $N$ más pequeño de modo que **el 90 % del tiempo** habrá $N$ o menos clientes en el estado estable.


En el estado estable, la probabilidad de $i$ clientes es:

$$
\phi_i = \frac{(\lambda/\nu)^i}{i!} e^{-\lambda/\nu}
$$



Si bien $\sum_{i=0}^{\infty} \phi_i = 1$, $N$ es el entero más pequeño que satisface:

$$
\phi_0 + \phi_1 + \cdots + \phi_N \geq 0.90
$$

$$
\sum_{i=0}^{N} \phi_i = \sum_{i=0}^{N} \frac{(\lambda/\nu)^i}{i!} e^{-\lambda/\nu} \geq 0.90
$$


Nótese que el valor de $N$ depende solamente de la razón $\lambda/\nu$.Se muestra el Cuadro 1 con valores de $\lambda/\nu$ contra $N$. El resultado es interesante: el número esperado de clientes para la cola con infinito número de servidores $\lambda/\nu$, pero solamente un poco más que este número de clientes estará presente 10% del tiempo.

| $\lambda/\nu$ | $N$ | $\lambda/\nu$ | $N$ |
|--------------:|----:|--------------:|----:|
| 0.5           | 1   | 20            | 26  |
| 2             | 2   | 50            | 59  |
| 5             | 8   | 100           | 113 |
| 10            | 14  |               |     |

*Cuadro: Número $N$ más pequeño para que el 90 % del tiempo haya $N$ o menos clientes en el estado estable.*

---