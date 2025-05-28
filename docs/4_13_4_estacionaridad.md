# Estacionaridad


- Un **proceso** aleatorio se convierte en una **variable** aleatoria cuando *el tiempo se fija* en un valor particular.  
- La **variable** aleatoria poseerá propiedades **estadísticas**, tales como valor medio, momentos, varianza, etcétera, relacionados con su función de densidad.  
- Si **dos variables** aleatorias se obtienen del proceso para dos instantes del tiempo, tendrán propiedades estadísticas (medias, varianzas, momentos conjuntos, etcétera) relacionadas con su función de densidad conjunta.


> **Un proceso aleatorio se dice que es _estacionario_ si todas sus propiedades estadísticas _no cambian con el tiempo_.**


Otros procesos son denominados **no estacionarios**.


---


## Estacionaridad de primer orden


Un proceso aleatorio es llamado estacionario de orden uno si su función de densidad de primer orden no cambia con un desplazamiento en el origen del tiempo. Es decir:


\[
f_{X}(x_1; t_1) = f_{X}(x_1; t_1 + \Delta)
\]


Esto debe ser cierto para cualquier valor de \( t_1 \) y cualquier número real \( \Delta \).  
Como consecuencia, \( f_{X}(x_1;t_1) \) es independiente de \( t_1 \) y el valor medio del proceso \( E[X(t)] \) es una constante:


\[
E[X(t)] = \overline{X} = \text{constante}
\]


Para probar lo anterior se calculan los valores medios de las variables aleatorias \( X_1 = X(t_1) \) y \( X_2 = X(t_2) \).


Para \( X_1 \):


\[
E[X_1] = E[X(t_1)] = \int_{-\infty}^{\infty} x_1 f_X(x_1; t_1) \, dx_1
\]


Para \( X_2 \):


\[
E[X_2] = E[X(t_2)] = \int_{-\infty}^{\infty} x_1 f_X(x_1; t_2) \, dx_1
\]


(Solo se ha cambiado el nombre de la variable de integración por conveniencia.)


Si ahora se considera \( t_2 = t_1 + \Delta \):


\[
\begin{aligned}
E[X(t_2)] &= \int_{-\infty}^{\infty} x_1 f_X(x_1; t_1 + \Delta) \, dx_1 \\
          &= \int_{-\infty}^{\infty} x_1 f_X(x_1; t_1) \, dx_1 \\
          &= E[X(t_1)] = E[X_1]
\end{aligned}
\]


Se concluye que:


\[
E[X(t_1 + \Delta)] = E[X(t_1)]
\]


lo cual implica que el valor esperado es constante porque \( t_1 \) y \( \Delta \) son arbitrarios.


---


## Estacionaridad de segundo orden


Un proceso es llamado estacionario de orden dos si su función de densidad de segundo orden cumple:


\[
f_X(x_1, x_2; t_1, t_2) = f_X(x_1, x_2; t_1 + \Delta, t_2 + \Delta)
\]


para todo \( t_1, t_2 \) y \( \Delta \).


Aquí aparece una nueva relación de interés:


\[
R_{XX}(t_1, t_2) = E[X(t_1)X(t_2)]
\]


A esto se le llama **autocorrelación de un proceso aleatorio** \( X(t) \), y en general es función de \( t_1 \) y \( t_2 \).


Una consecuencia importante de la ecuación anterior es que, para procesos estacionarios de segundo orden, la autocorrelación depende solo de la diferencia temporal:


\[
\tau = t_2 - t_1
\]


Por lo tanto:


\[
R_{XX}(t_1, t_1 + \tau) = E[X(t_1)X(t_1 + \tau)] = R_{XX}(\tau)
\]


---


## Estacionaridad en sentido amplio


Muchos problemas prácticos requieren conocer la función de autocorrelación y el valor medio de un proceso aleatorio. Estas soluciones se simplifican si dichas cantidades **no dependen del tiempo absoluto**.


La estacionaridad de segundo orden es suficiente para esto, pero suele ser más restrictiva de lo necesario.  
Por eso, se utiliza una forma más relajada llamada **estacionaridad en sentido amplio**:


\[
E[X(t)] = \overline{X} \quad (\text{constante})
\]


\[
E[X(t)X(t+\tau)] = R_{XX}(\tau)
\]


Esto se conoce como **WSS** (*Wide Sense Stationarity*).


### Estacionaridad conjunta


Dos procesos aleatorios \( X(t) \) y \( Y(t) \) son **conjuntamente estacionarios en sentido amplio** si:


1. Cada uno de ellos es estacionario en sentido amplio.  
2. Su función de **correlación cruzada**:


\[
R_{XY}(t_1, t_2) = E[X(t_1) Y(t_2)]
\]


solo depende de la diferencia temporal \( \tau = t_2 - t_1 \):


\[
R_{XY}(t, t+\tau) = E[X(t) Y(t+\tau)] = R_{XY}(\tau)
\]


---


## Ejemplo de estacionaridad en sentido amplio


Se demostrará que el proceso aleatorio


\[
X(t) = A \cos(\omega_0 t + \Theta)
\]


es estacionario en sentido amplio si \( A \) y \( \omega_0 \) son constantes y \( \Theta \) es una variable aleatoria **uniformemente distribuida** en el intervalo \( [0, 2\pi] \).


El valor medio es:


\[
E[X(t)] = \int_0^{2\pi} A \cos(\omega_0 t + \theta) \cdot \frac{1}{2\pi} \, d\theta = 0
\]


*(Aquí seguiría el cálculo de la función de autocorrelación para comprobar que depende solo de \( \tau \), completando así la verificación de WSS.)*
La función de autocorrelación con \( t_1 = t \) y \( t_2 = t + \tau \) se convierte\footnote{Se utiliza la identidad \(\cos(x) \cos(y) = \frac{1}{2} (\cos(x-y) + \cos(x+y))\).} en


\[
\begin{aligned}
 R_{XX}(t, t+\tau) &= E\left[ A \cos(\omega_0 t + \Theta) \cdot A \cos(\omega_0 t + \omega_0 \tau + \Theta) \right] \\
                   &= \frac{A^2}{2} E\left[ \cos(\omega_0 \tau) + \cos(2 \omega_0 t + \omega_0 \tau + 2 \Theta) \right] \\
                   &= \frac{A^2}{2} \cos(\omega_0 \tau)
\end{aligned}
\]


La función de autocorrelación depende solamente de \(\tau\) y el valor medio es una constante, por lo que \( X(t) \) es estacionario en sentido amplio.
## Estacionaridad en sentido estricto y de orden \(N\)


Un proceso aleatorio es estacionario de orden \(N\) si su función de densidad de orden \(N\) es invariante ante un desplazamiento en el origen temporal; es decir, si


\[
f_{X}(x_1, \ldots, x_N; t_1, \ldots, t_N) = f_{X}(x_1, \ldots, x_N; t_1 + \Delta, \ldots, t_N + \Delta)
\]


para todo \(t_1, \ldots, t_N\) y \(\Delta\). La estacionaridad de orden \(N\) implica estacionaridad a todos los órdenes \(k \leq N\). Un proceso estacionario a todo orden \(N = 1, 2, \ldots\) es denominado estacionario en sentido estricto.


---


## Videos y referencias en internet


- ▶️ **¿Qué es un proceso estocástico?**


  *Luis Rincón*, [https://youtu.be/Gngu2xp3exU](https://youtu.be/Gngu2xp3exU
