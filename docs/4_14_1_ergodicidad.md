!!! Introducción
    La ergodicidad establece la igualdad entre el promedio estadístico y el promedio temporal de un proceso aleatorio.

    Es una nueva forma de estacionaridad que simplifica el análisis del proceso aleatorio.

## Promedios en el tiempo
El promedio temporal de una función está definido con el nuevo operador

\begin{equation}
  A \left[~ f(t) ~\right] = \lim_{T \rightarrow \infty} \frac{1}{2T} \int_{-T}^{T} f(t)\, \mathrm{d}t
\end{equation}

donde $A$ se utiliza para denotar **promedio temporal** de una manera análoga al operador $E$ para el **promedio estadístico**. $f(t)$ es una función del tiempo cualquiera.

![](images/14_funcion_del_tiempo_cualquiera.svg)  

El valor $\overline{x} = A[x(t)]$ representa el promedio temporal de una función muestra. La función de autocorrelación temporal es denotada por $\mathcal{R}_{XX}(\tau) = A[x(t)x(t+\tau)]$. Estas funciones están definidas por

\begin{equation}
\begin{aligned}
  \overline{x} & = A[x(t)] \\
  			& = \lim_{T \rightarrow \infty} \frac{1}{2T}\int_{-T}^{T}x(t)\, \mathrm{d}t
\end{aligned}
\end{equation}

\begin{equation}
\begin{aligned}
  \mathcal{R}_{XX}(\tau) & = A[x(t)x(t+\tau)] \\
  			& = \lim_{T \rightarrow \infty} \frac{1}{2T} \int_{-T}^{T}x(t)x(t+\tau)\, \mathrm{d}t 
\end{aligned}
\end{equation}

Para cualesquiera función muestra $x(t)$ del proceso $X(t)$, estas dos últimas integrales simplemente producen dos números (para un valor fijo de $\tau$).   
 
![**Figura:** Ejemplo de un proceso aleatorio llamado "caminata aleatoria" (random walk).](images/14_camino_aleatorio.svg)  
**Figura:** Ejemplo de un proceso aleatorio llamado "caminata aleatoria" (random walk).  

Cuando se consideran todas las funciones muestra, $\overline{x}$ y $\mathcal{R}_{XX}(\tau)$ son realmente variables aleatorias. Tomando el valor esperado a ambos lados de las definiciones, suponiendo que la operación matemática de la esperanza puede llevarse al interior de la integral y suponiendo que $X(t)$ es un **proceso estacionario**, 

\begin{equation*}
    E[\overline{x}] = \overline{X} \qquad\qquad\qquad
    E[\mathcal{R}_{XX}(\tau)] = R_{XX}(\tau) 
\end{equation*}  

## Procesos ergódicos

!!! tip "Procesos ergódicos"
    Si se supone que $\overline{x}$ y $\mathcal{R}_{XX}(\tau)$ tienen varianzas nulas, es decir, que son constantes, se escribe entonces, 

    \begin{equation*}
    \begin{aligned}
    E[\overline{x}] & = \overline{x} = \overline{X} \\
    E[\mathcal{R}_{XX}(\tau)] & = \mathcal{R}_{XX}(\tau) = R_{XX}(\tau)
    \end{aligned}
    \end{equation*}

    Los promedios temporales $\overline{x}$ y $\mathcal{R}_{XX}(\tau)$ igualan a los promedios estadísticos. 

    **Los procesos para los que los promedios temporales igualan a los estadísticos se denominan ergódicos.**   

![**Figura:** Ejemplo de un proceso aleatorio llamado "ruido blanco" (white noise).](images/14_ruido_blanco.svg)  
**Figura:** Ejemplo de un proceso aleatorio llamado "ruido blanco" (white noise).

!!! note ""
    Ergodicidad es una forma muy restrictiva de estacionaridad y puede ser difícil probar que constituye una suposición razonable para cualquier situación física. Sin embargo, se asumirá que un proceso es ergódico a veces para *simplificar problemas*. 

**Ergodicidad conjunta**  
Dos procesos aleatorios son llamados conjuntamente ergódicos si son individualmente ergódicos y también tienen una función de correlación cruzada temporal que iguala la función de correlación cruzada estadística: 

\begin{equation}
  \mathcal{R}_{XY}(\tau) = \lim_{T \rightarrow \infty}\frac{1}{2T}\int_{-T}^{T}x(t)y(t+\tau)\, \mathrm{d}{t} = R_{XY}(\tau)
\end{equation}
