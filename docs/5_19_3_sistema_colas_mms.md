# El sistema de colas M/M/s

!!! note ""

    Un sistema M/M/s tiene un proceso de llegada y de servicio tipo Markov (de ahí la M) y un número $s$ de servidores.


En un sistema M/M/s, las llegadas son descritas por un proceso de Poisson con parámetro $\\lambda$. Cada uno de los $s$ servidores tiene un tiempo de servicio exponencial con parámetro $\\nu$.  
El proceso $X(t) = i$ (notación abreviada $X_t$) describe el estado del sistema al tiempo $t$ para $S = \\{0, 1, \\dots \\}$ (es decir, $i \\geq 0$).


Únicamente con $\rho = \lambda/(s \nu) < 1$ el sistema alcanza un estado estacionario, donde:

$$
\Omega_0 = \lambda \hspace{1.5cm} \Omega_{i \rightarrow i-1} = 
\begin{cases} 
i \nu & \text{para } 0 < i < s \\
s \nu & \text{para } i \geq s
\end{cases}
$$

$$
\phi_0 = \left[ \sum_{k=0}^{s-1} \frac{(s \rho)^k}{k!} + \frac{(s \rho)^s}{s!(1-\rho)} \right]^{-1}
$$

$$
\phi_i =
\begin{cases}
\displaystyle \frac{(s \rho)^i}{i!} \phi_0 & \text{para } i < s \\
\displaystyle \frac{s^s \rho^i}{s!} \phi_0 & \text{para } i \geq s
\end{cases}
$$

## Notación alternativa M/M/c

En algunas referencias es posible encontrar esta notación equivalente:

$$
\pi_0 = \left[\left(\sum_{k=0}^{c-1} \frac{(c\rho)^k}{k!} \right) + \frac{(c\rho)^c}{c!(1 - \rho)}\right]^{-1}
$$

$$
\pi_k =
\begin{cases}
\pi_0 \dfrac{(c\rho)^k}{k!} & \text{para } 0 < k < c \\
\pi_0 \dfrac{(c\rho)^k c^{c-k}}{c!} & \text{para } k \geq c
\end{cases}
$$

donde $c$ es el número de servidores, $k$ es el estado (o número de clientes en el sistema), $\pi_k$ es la probabilidad en estado estable y $\rho = \lambda/(c \nu)$.


Asimismo, es posible describir el número promedio de clientes en el sistema como:

$$
L = \frac{\lambda}{\nu} + \frac{\rho (s \rho)^s}{s!(1 - \rho)^2} \phi_0
$$

Y el número promedio de clientes en una fila (cuando todos los servidores están ocupados), dado como:

$$
L_q = \frac{\rho (s \rho)^s}{s!(1 - \rho)^2} \phi_0 = L - \frac{\lambda}{\nu}
$$

## Parámetros del sistema

Para una corriente de arribo de Poisson con parámetro $\lambda$ y un tiempo de servicio exponencial con parámetro $\nu$, con un solo servidor $s = 1$, las probabilidades de estado estable son:

$$
\Omega_0 = \lambda \hspace{1.5cm} \Omega_{i \rightarrow i-1} = \nu
$$

$$
\phi_0 = 1 - \frac{\lambda}{\nu} = 1 - \rho
$$

$$
\phi_i = \left( 1 - \frac{\lambda}{\nu} \right) \left( \frac{\lambda}{\nu} \right)^i = (1 - \rho) \rho^i
$$


El número promedio de clientes en el sistema es:

$$
L = \frac{\rho}{1 - \rho} = \frac{\lambda}{\nu - \lambda}
$$

Y el número promedio de clientes en una fila (cuando el servidor está ocupado) es:

$$
L_q = \frac{\lambda^2}{\nu(\nu - \lambda)} = \frac{\rho^2}{1 - \rho}
$$

### Ejemplos de un servidor web


!!! example ""

    Un servidor web es modelado como un sistema M/M/1 con una tasa de arribo de 2 solicitudes por minuto.  
    Se desea tener 3 solicitudes o menos en fila (más una que está siendo atendida) el 99% del tiempo.  
    ¿Qué tan rápido debe ser el servicio? $\nu$ es solicitudes atendidas por minuto.

El estado $i$ es el número de clientes en el sistema. La longitud de la fila es $L_q = i - 1$ (en virtud de la solicitud que está siendo atendida en $s = 1$ servidores). Es posible encontrar:

$$
P(\text{5 o más clientes en el sistema}) = \sum_{i=5}^{\infty} (1 - \rho) \rho^i = 1 - \sum_{i=0}^{4} (1 - \rho) \rho^i = \rho^5
$$

que depende de $\rho = \frac{\lambda}{\nu}$ y del parámetro de servicio $\nu$ buscado.

De los datos del problema: $\lambda = 2$. Para tener una fila de 3 o menos clientes el 99% del tiempo se necesita:

$$
P(5 \text{ o más clientes en el sistema}) = \left( \frac{\lambda}{\nu} \right)^5 \leq 0.01
$$
$$
\nu^5 \geq \frac{\lambda^5}{0.01} = \frac{2^5}{0.01} = 3200 \quad \Rightarrow \nu \geq 5.024
$$


## Teorema del límite

Suponga las siguientes condiciones para el proceso de nacimiento y muerte:

!!! note ""

    1️⃣ $p_0 = 1$  
    2️⃣ $0 < p_i < 1$ para $i = 1, 2, \dots$  
    3️⃣ $q_N = 1$ si $S = \{0, 1, 2, \dots, N\}$  
    4️⃣ $\Omega_i > 0$ para $i \in S$

Suponga que $\phi$ es un vector de probabilidad que satisface:

$$
\phi_i = \left( \frac{\Omega_{i-1} p_{i-1}}{\Omega_i q_i} \right) \phi_{i-1}
$$

para i = 1,2,...


Entonces:

1️⃣ Dado cualquier vector de probabilidad inicial $\rho$,

$$
P(X_t = i \mid \text{vector inicial } \rho) \to \phi_i
$$

cuando $t \rightarrow \infty$ para cada $i \in S$.

2️⃣ Si el vector de probabilidad inicial es $\rho$ = $\phi$, entonces

$$
P(X_t = i \mid \text{vector inicial } \phi) = \phi_i 
$$

para todo $t \geq 0$ para $i \in S$.

*Primer resultado*
Sin importar el estado inicial en el tiempo $t = 0$, el proceso se hallará en el estado $i$ con probabilidad $\phi_i$ conforme $t$ se hace grande.

*Segundo resultado*
Si $\phi$ se usa como el vector inicial de probabilidad, entonces $\phi$ será el vector de probabilidad para todo tiempo $t \geq 0$.

Las condiciones del teorema sobre $\Omega_i, p_i, q_i$ son esenciales: ningún estado es absorbente y cualquier estado puede alcanzarse desde cualquier otro estado.

### Videos y referencias en internet

- *¿Qué es una cadena de Markov?*  
  Luis Rincón  
  [https://youtu.be/Trf9P7DnOHQ](https://youtu.be/Trf9P7DnOHQ)

- *Origin of Markov chains | Journey into information theory | Computer Science*  
  Khan Academy Labs  
  [https://youtu.be/Ws63I3F7Moc](https://youtu.be/Ws63I3F7Moc)
