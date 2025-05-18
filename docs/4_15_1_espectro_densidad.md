

!!! abstract  
    Cuando los procesos estocásticos describen *señales* (funciones unidimensionales en el tiempo), es posible analizarlos según sus características **espectrales**, es decir, relativas a la **frecuencia**.

    Esto es útil en aplicaciones de procesamiento de señales: sensores, audio, sistemas de control, comunicaciones, estabilidad de sistemas de potencia, etc.

## Espectro de densidad de potencia
!!! note ""
    El espectro de densidad de potencia de una señal aleatoria describe cómo se distribuye su potencia en todas las frecuencias.

- Esta es una descripción[^1] de \(X(t)\) en el **dominio de la frecuencia**.
- Por otra parte, las propiedades estadísticas de los procesos estocásticos, como las funciones de la media, la varianza, la autocovarianza, la autocorrelación, etc., son descripciones de \(X(t)\) en el **dominio del tiempo**.

[^1]: Conocida en inglés como PSD (*Power Spectral Density*).

!!! note ""
    **Premisa**  
    Es posible interpretar $X^2(t)$ como la "potencia instantánea" en $t$ contenida en el proceso aleatorio $X(t)$, que es una familia de funciones del tiempo.

En teoría de circuitos, la potencia disipada en un resistor es

\begin{equation}
    p_R(t) = i^2(t) R = v^2(t)/R
\end{equation}

## Definiciones preliminares 

- **Función muestra de $X(t)$:**  Sea $x_{T}(t)$ una porción de una función muestra $x(t)$ definida entre $-T$ y $T$, de modo que

    \begin{equation}
    x_{T}(t) = 
    \begin{cases}
    x(t) & -T < t < T \\
    0    & \text{fuera del intervalo}
    \end{cases}
    \end{equation}

![Función de muestra de $X(t)$](images/15_func_muestra_x_t.svg){ style="display:block;margin:auto;" width="1000" }


- **Área bajo la curva es finita:** Si $T$ es finito, *se supone* que $x_{T}(t)$ cumple

    \begin{equation}
    \int_{-T}^{T} \vert x_{T}(t) \vert ~\mathrm{d} t < \infty
    \end{equation}


- **Función en el dominio de la frecuencia:** $x_T(t)$ tiene una *transformada de Fourier* $X_{T}(\omega)$

    \begin{equation}
    X_{T}(\omega) = \int_{-\infty}^{\infty} x_{T}(t) ~ e^{-j\omega t} ~\mathrm{d} t = \int_{-T}^{T} x(t) ~ e^{-j\omega t} ~\mathrm{d} t
    \end{equation}

- **Energía $E(T)$ de $x_T(t)$:** En el intervalo $[-T,T]$ la energía contenida es

    \begin{equation}
    E(T) = \int_{-\infty}^{\infty}x_{T}^2(t) ~\mathrm{t} = \int_{-T}^{T}x^2 (t) ~\mathrm{d} t
    \end{equation}


- **Relación entre la energía en el tiempo y en la frecuencia:** La energía de $x_T(t)$ está relacionada con la de $X_{T}(\omega)$ por el *teorema de Parseval*, 

    \begin{equation}
    E(T) = \int_{-T}^{T}x^2 (t) ~\mathrm{d} t = \frac{1}{2\pi}\int_{-\infty}^{\infty}\vert X_{T}(\omega) \vert^2 ~\mathrm{d} \omega
    \end{equation}

- **Potencia promedio $P(T)$:** Al dividir ambas expresiones por $2T$, se obtiene la potencia promedio $P(T)$ en $x(t)$ sobre el intervalo $[-T,T]$: 

    \begin{equation}
    P(T) = \frac{1}{2T}\int_{-T}^{T}x^2(t) ~\mathrm{d} t = \frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\vert X_{T}(\omega) \vert^2}{2T} ~\mathrm{d} \omega
    \end{equation}

## Deducción 
En esta ecuación, $\vert X_{T}(\omega) \vert^2 / 2T$ es una densidad espectral de potencia porque de la integración sobre todo $\omega$ se obtiene la potencia.

\begin{equation}
P(T) = \frac{1}{2T}\int_{-T}^{T}x^2(t) ~\mathrm{d} t = \frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\vert X_{T}(\omega) \vert^2}{2T} ~\mathrm{d} \omega
\end{equation}

Sin embargo, no es todavía la función que necesitamos, por tres razones: 

1. No representa la potencia de una función muestra completa
2. Es la potencia en una sola función muestra y no representa a todo el proceso
3. $P(T)$ es realmente una variable aleatoria (y no un valor) con respecto al proceso aleatorio (por la aleatoriedad de las funciones muestra)

## Espectro de densidad de potencia II
!!! note ""
    Por lo anterior, la estrategia para encontrar la potencia promedio de $X(t)$ (denotada como $P_{XX}$) es hacer $P_{XX} = E[P(\infty)]$

\begin{equation}
 P_{XX} = \lim_{T \rightarrow \infty} \frac{1}{2T}\int_{-T}^{T}E[X^2(t)] ~\mathrm{d} t
\end{equation}
 
\begin{equation}
P_{XX} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\lim_{T \rightarrow \infty}\frac{E[\vert X_{T}(\omega) \vert^2]}{2T} ~\mathrm{d} t     
\end{equation}

De aquí se obtienen las dos importantes conclusiones siguientes.

## Potencia Promedio de un proceso estocástico

!!! tip "La potencia promedio $P_{XX}$ de un proceso estocástico""
    $P_{XX} = \lim_{T \rightarrow \infty} \frac{1}{2T}\int_{-T}^{T}E[X^2(t)] ~\mathrm{d} t = A\{E[X^2(t)]\}$


Es decir, está dada por *el promedio temporal de su segundo momento ordinario*, que es también $R_{XX}(0)$.

**Caso del proceso estacionario**

Para un proceso que es a lo menos estacionario en sentido amplio $E[X^2(t)] = \overline{X^2}$, una constante, con lo que $P_{XX} = \overline{X^2}$.

## Densidad espectral de potencia de un proceso estocástico

!!! tip "Densidad espectral de potencia"
    \begin{equation}
    \mathcal{S}_{XX}(\omega) = \lim_{T \rightarrow \infty}\frac{E[\vert X_{T}(\omega) \vert^2]}{2T} \end{equation}


De aquí, $P_{XX}$ puede obtenerse con una integración en el dominio de la frecuencia como

\begin{equation}
    P_{XX} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\mathcal{S}_{XX}(\omega) ~\mathrm{d} \omega
\end{equation}

## Relación de Parseval


Sean \(f(t)\stackrel{\mathcal F}{\longleftrightarrow} F(\omega)\) y
\(g(t)\stackrel{\mathcal F}{\longleftrightarrow} G(\omega)\) pares de Fourier, entonces:




\begin{equation}
    \begin{aligned}
	& \int_{-\infty}^{\infty} f(t) \overline{g}(t) ~\mathrm{d} t \\ 
	& = \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} F(\omega) e^{-j2\pi \omega t} ~\mathrm{d} \omega \right] \left[ \int_{-\infty}^{\infty} G(\omega') e^{j2\pi \omega' t} ~\mathrm{d} \omega' \right] ~\mathrm{d} t \\
	& = \int_{-\infty}^{\infty} F(\omega) \int_{-\infty}^{\infty} G(\omega') \left[ \int_{-\infty}^{\infty} e^{j2\pi (\omega' - \omega) t} ~\mathrm{d} t \right] ~\mathrm{d} \omega' ~\mathrm{d} \omega \\
    & = \int_{-\infty}^{\infty} F(\omega) \left[ \int_{-\infty}^{\infty} G(\omega') \delta(\omega' - \omega) ~\mathrm{d} \omega' \right] ~\mathrm{d} \omega \\
    & = \int_{-\infty}^{\infty} F(\omega) \overline{G}(\omega) ~\mathrm{d} \omega \\
    \end{aligned}
\end{equation}

donde $\overline{z}$ es el complejo conjugado.

---

:material-pencil-box: **EJEMPLO**

!!! example "Ejemplo de la potencia promedio de un proceso aleatorio I"
    Considere el proceso estocástico

    \begin{equation}
    X(t) = A\cos\left( \omega_{0}t + \Theta \right)
    \end{equation}

    donde $A$ y $\omega_{0}$ son constantes reales y $\Theta$ es una variable aleatoria uniformemente distribuida en el intervalo $[0, \frac{\pi}{2}]$. ¿Cuál es la potencia promedio $P_{XX}$ en $X(t)$?


La potencia promedio es el promedio temporal del valor cuadrático medio, que se calcula a continuación. 

Recordar la identidad trigonométrica $\cos^2(x)= \frac{1}{2} (1 + \cos(2x))$


\begin{equation}
\begin{aligned}
  E[X^2(t)] & = E[A^2 \cos^2 \left( \omega_{0}t + \Theta \right)] \\
        & = E\left[ \frac{A^2}{2} +  \frac{A^2}{2}\cos\left( 2\omega_{0}t + 2\Theta \right) \right] \\
        & = \frac{A^2}{2} + \frac{A^2}{2}\int_{0}^{\frac{\pi}{2}}\frac{2}{\pi}\cos\left( 2\omega_{0}t + 2\theta \right) ~\mathrm{d} \theta \\
        & = \frac{A^2}{2} + \left( \frac{A^2}{2} \right)\left( \frac{2}{\pi} \right)\left. \frac{\sin(2\omega_{0}t + 2\theta)}{2} \right\vert_{0}^{\frac{\pi}{2}} \\
        & = \frac{A^2}{2} + \frac{A^2}{\pi}\left\{ \frac{\sin(2\omega_{0}t + \pi)}{2} - \frac{\sin(2\omega_{0}t)}{2} \right\} \\
        & = \frac{A^2}{2} + \frac{A^2}{\pi}\left[ \frac{-2\sin(2\omega_{0}t)}{2} \right] \\
        & = \frac{A^2}{2} - \frac{A^2}{\pi}\sin(2\omega_{0}t)
\end{aligned}
\end{equation}

El promedio temporal de la función anterior es:

\begin{equation}
\begin{aligned}
  A\left[ E[X^2(t)] \right] &= \lim_{T \rightarrow \infty}\frac{1}{2T}\int_{-T}^{T}\left[ \frac{A^2}{2} - \frac{A^2}{\pi}\sin(2\omega_{0}t) \right] ~\mathrm{d} t \\
  &= \lim_{T \rightarrow \infty}\frac{1}{2T}\left\{ \frac{A^2}{2}(2T) + \left. \left[ \frac{A^2}{\pi}\frac{\cos(2\omega_{0}t)}{2\omega_{0}} \right]\right\vert_{-T}^{T} \right\} \\
  &= \lim_{T \rightarrow \infty} \left\lbrace \frac{1}{2T}\left( \frac{A^2}{2}2T \right) + \frac{1}{2T}\frac{A^2}{2\omega_{0}\pi}\left[ \cos(2\omega_{0}T) - \cos(-2\omega_{0}T) \right] \right\rbrace \\
  P_{XX} &= \frac{A^2}{2}
\end{aligned}
\end{equation}

!!! note ""
    $P_{XX} = \frac{A^2}{2}$

---

:material-lightning-bolt: Es equivalente a elevar al cuadrado el valor efectivo $V_{RMS} = A/\sqrt{2}$ de la onda.c