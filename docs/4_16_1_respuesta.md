
[ ### Presentación ]: #

[16 - Respuesta de sistemas lineales a una señal aleatoria](https://www.overleaf.com/read/yfnrpxpcmvsz#5b73e6)

[ ### Secciones ]: #
[ - Respuesta del sistema (1 - 2) ]: #
[ - Valor cuadrático medio (2 - 6) ]: #

[ C12770: No logré dejar la línea horizontal que se encuentra sobre las variables que representan valores medios con \overline{}, usé \bar{} pero no quedó la misma línea. ]: #

# Respuesta del sistema y valor cuadrático medio

!!! abstract "Introducción"
    En la interacción de señales y sistemas donde hay entradas aleatorias, es posible determinar cantidades útiles para el análisis, como la señal misma o la potencia de salida, conociendo las características determinísticas del sistema y características estadísticas de la entrada.

[ # Respuesta del sistema ]: #

## Respuesta del sistema: convolución

Con $x(t)$ una señal aleatoria, la respuesta de cualquier red eléctrica, denotada por $y(t)$, está dada por la integral de convolución

\begin{equation}
\begin{aligned}
    y(t) & = \int_{-\infty}^{\infty} x(\xi) h(t - \xi) \, ~\mathrm{d} \xi \\
    & = \int_{-\infty}^{\infty} h(\xi) x(t - \xi) \, ~\mathrm{d} \xi \\
    & = x(t) * h(t)
\end{aligned} 
\end{equation}

donde $h(t)$ es la respuesta al impulso de la red. Se está suponiendo un sistema lineal e invariante con el tiempo (LIT).

![Diagrama del sistema lineal e invariante con el tiempo](images/16_sistema_LIT.svg)

La ecuación anterior es una operación sobre un miembro $x(t)$ del agregado del proceso estocástico $X(t)$ que produce un miembro del agregado de un nuevo proceso $Y(t)$. En general, para todo el proceso estocástico,

\begin{equation}
\begin{aligned}
    Y(t) & = \int_{-\infty}^{\infty} h(\xi) X(t - \xi) \, ~\mathrm{d} \xi \\
    & = X(t) * H(t)
\end{aligned} 
\end{equation}

[ ## Valor medio y cuadrático medio de la respuesta del sistema ]: #

## Valor medio de la respuesta del sistema

Si $X(t)$ es estacionario en sentido amplio (WSS), entonces

\begin{equation}
\begin{aligned}
    E[Y(t)] & = E\left[ \int_{-\infty}^{\infty} h(\xi) X(t - \xi) \, ~\mathrm{d} \xi \right] = \int_{-\infty}^{\infty} h(\xi) E[X(t - \xi)] \, ~\mathrm{d} \xi \\
    & = \bar{X} \int_{-\infty}^{\infty} h(\xi) \, ~\mathrm{d} \xi = \bar{Y} \quad \text{(constante)}
\end{aligned}
\end{equation}


Entonces el valor medio de $Y(t)$ iguala al valor medio de $X(t)$ multiplicado por el área bajo la curva de la respuesta al impulso.

## Nota al margen: Relación entre la integración y el valor esperado

Las operaciones de integración y de esperanza matemática son intercambiables, de modo que, para

\begin{equation}
\int_{t_{1}}^{t_{2}} E[|W(t)|] |h(t)| \, ~\mathrm{d} t < \infty
\end{equation}

donde $t_{1}$, $t_{2}$ son constantes reales que pueden ser infinitas, aplica que

\begin{equation}
E\left[ \int_{t_{1}}^{t_{2}} W(t) h(t) \, ~\mathrm{d} t \right] = \int_{t_{1}}^{t_{2}} E[W(t)] h(t) \, ~\mathrm{d} t
\end{equation}

donde $W(t)$ es alguna función acotada de un proceso aleatorio (sobre el intervalo $[t_{1}, t_{2}]$) y $h(t)$ es una función del tiempo, no aleatoria.

## Valor cuadrático medio de la respuesta del sistema

Para el valor cuadrático medio de $Y(t)$, se calcula

\begin{equation} 
\begin{aligned}
    E[Y^2(t)] & = E\left[ \int_{-\infty}^{\infty} h(\xi_{1}) X(t - \xi_{1}) \, ~\mathrm{d} \xi_{1} \int_{-\infty}^{\infty} h(\xi_{2}) X(t - \xi_{2}) \, ~\mathrm{d} \xi_{2} \right] \\
    & = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} E[X(t - \xi_{1}) X(t - \xi_{2})] h(\xi_{1}) h(\xi_{2}) \, ~\mathrm{d} \xi_{1} \, ~\mathrm{d} \xi_{2}
\end{aligned} 
\end{equation}

Si se supone que la entrada es estacionaria en sentido amplio:

\begin{equation}
E[X(t - \xi_{1}) X(t - \xi_{2})] = R_{XX}(\xi_{1} - \xi_{2})
\end{equation}

con lo que la ecuación se vuelve independiente de $t$:

\begin{equation} 
\begin{aligned}
    \bar{Y^2} & = E[Y^2(t)] \\
    & = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} R_{XX}(\xi_{1} - \xi_{2}) h(\xi_{1}) h(\xi_{2}) \, ~\mathrm{d} \xi_{1} \, ~\mathrm{d} \xi_{2}
\end{aligned} 
\end{equation}

---

:material-pencil-box: **EJEMPLO**

!!! example "Sistema con entrada de ruido blanco"
    Se encontrará $\bar{Y^2}$ para un sistema con ruido blanco gaussiano en su entrada. 

Aquí:

\begin{equation}
R_{XX}(\xi_{1} - \xi_{2}) = (\mathcal{N}_0 / 2) \delta(\xi_{1} - \xi_{2})
\end{equation}

donde $\mathcal{N}_0$ es una constante real positiva. Luego,

\begin{equation}
\bar{Y^2} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (\mathcal{N}_0 / 2) \delta(\xi_{1} - \xi_{2}) h(\xi_{1}) ~\mathrm{d} \xi_{1} h(\xi_{2}) ~\mathrm{d} \xi_{2}
\end{equation}

!!! note ""
    Se concluye que:

    \begin{equation}
    \bar{Y^2} = (\mathcal{N}_0 / 2) \int_{-\infty}^{\infty} h^2(\xi_{2}) \, ~\mathrm{d} \xi_{2}
    \end{equation}

    La potencia de salida se vuelve proporcional al área bajo el cuadrado de la curva de $h(t)$, en este ejemplo.

---