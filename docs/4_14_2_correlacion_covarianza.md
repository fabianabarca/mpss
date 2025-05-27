# Funciones de correlación y covarianza

!!! note "Introducción"
    Las funciones de correlación y covarianza cuantifican el grado de relación lineal entre un mismo proceso aleatorio en distintos de tiempo (*auto*) y entre dos procesos distintos (*cruzada*).

    Sus propiedades tienen interpretaciones importantes en el procesamiento de señales.

## Función de autocorrelación

!!! tip "Autocorrelación"
    La autocorrelación de un proceso aleatorio $X(t)$ es la correlación $E[X_1 X_2]$ de dos variables aleatorias $X_1 = X(t_1)$ y $X_2 = X(t_2)$ definidas por el proceso en tiempos $t_1$ y $t_2$. 

    \begin{equation}
      R_{XX}(t_1, t_2) = E[X(t_1)X(t_2)]
    \end{equation}

    Con $t_1 = t$ y $t_2 = t_1 + \tau$ 

    \begin{equation}
      R_{XX}(t, t+\tau) = E[X(t)X(t+\tau)]
    \end{equation}

Si $X(t)$ es estacionario en sentido amplio, $R_{XX}(t, t+\tau)$ es función únicamente de la diferencia $\tau = t_2 - t_1$, 

\begin{equation}
  R_{XX}(\tau) = E[X(t)X(t+\tau)]
\end{equation}

## Propiedades de la función de **autocorrelación**

1. El valor máximo de $R_{XX}(\tau)$ está en $\tau = 0$, por tanto está acotado en el origen.

    \begin{equation}
        \vert R_{XX}(\tau) \vert \leq R_{XX}(0)
    \label{E:autocorrelacion_valor_maximo}
    \end{equation}

2. La autocorrelación tiene simetría par.  

    \begin{equation}
        R_{XX}(-\tau) = R_{XX}(\tau)
    \label{E:autocorrelacion_simetria}
    \end{equation}

3. El valor máximo es igual a la media del cuadrado (o *valor cuadrático medio*), llamado también la **potencia del proceso**.

    \begin{equation}
        R_{XX}(0) = E[X^{2}(t)]
    \label{E:autocorrelacion_potencia}
    \end{equation}

4. Si $X(t)$ es ergódico sin componentes periódicos, y además $E[X(t)] = \overline{X} \neq 0$, entonces
  
    \begin{equation}
        \lim_{\vert \tau \vert \rightarrow \infty} R_{XX}(\tau) = \overline{X}^2
    \label{E:autocorrelacion_limite}
    \end{equation}

    - Si $X(t)$ es ergódico sin componentes periódicos, con media cero, entonces
  
    \begin{equation*}
        \lim_{\vert \tau \vert \rightarrow \infty}R_{XX}(\tau) = 0
    \end{equation*}

5. Si $X(t)$ tiene un componente periódico, entonces $R_{XX}(\tau)$ tendrá un componente periódico con el mismo periodo.

---
:material-pencil-box: **EJEMPLO**

!!! example "Propiedades de autocorrelación"
    Para un proceso estacionario $\text{WSS}$ y ergódico $\text{ERG}$, sin componentes periódicos, en 

    \begin{equation}
      R_{XX}(\tau) = 25 + \frac{4}{1 + 6\tau^2}
    \end{equation}
    
    encontrar el valor medio y la varianza del proceso.

![Gráfico de autocorrelación mostrando la función y su asíntota en 25](images/14_proceso_estacionario.svg)


La propiedad 4 establece que $\displaystyle \lim_{\vert \tau \vert \rightarrow \infty} R_{XX}(\tau) = \overline{X}^2$ y entonces

\begin{equation*}
  E[X(t)] = \overline{X} = \sqrt{25} = \pm 5
\end{equation*}

Nótese que tal propiedad solamente da la magnitud de $\overline{X}$ y no su signo. 

Con la definición de varianza y la propiedad 3 dada por $R_{XX}(0) = E[X^{2}(t)]$ entonces

\begin{equation*}
\begin{aligned}
\sigma_{X}^2 	& = E[X^2(t)] - (E[X(t)])^2 \\
  				& = R_{XX}(0) - \overline{X}^2 \\
  				& = 29 - 25 = 4
\end{aligned}
\end{equation*}

!!! note ""
    **Resultados:**  
    - Valor medio: $\overline{X} = \pm 5$  
    - Varianza: $\sigma_X^2 = 4$

---

## Función de correlación cruzada

!!! tip "Correlación cruzada"
    La función de correlación cruzada está definida por

    \begin{equation}
      R_{XY}(t,t+\tau) = E\left[ X(t)Y(t+\tau) \right]
      \label{E:correlacion_cruzada}
    \end{equation}

## Propiedades de la función de **correlación cruzada**

1. Si $X(t)$ y $Y(t)$ son conjuntamente estacionarios en sentido amplio, $R_{XY}(t,t+\tau)$ será independiente del tiempo absoluto:

    \begin{equation}
        R_{XY}(\tau) = E\left[ X(t)Y(t+\tau) \right]
        \label{E:correlacion_cruzada_estacionaria}
    \end{equation} 

2. Si $R_{XY}(t,t+\tau) = 0$, entonces $X(t)$ y $Y(t)$ son procesos ortogonales. 

3. Si los dos procesos son estadísticamente independientes, la función de correlación cruzada se convierte en: 

    \begin{equation}
        R_{XY}(t,t+\tau) = E[X(t)]E[Y(t+\tau)]
    \end{equation}

4. Si además de ser independientes, $X(t)$ y $Y(t)$ son *al menos* estacionarios en sentido amplio, 

    \begin{equation}
        R_{XY}(\tau) = \overline{X} \cdot \overline{Y}
    \end{equation}

    que es una constante. 

5. Si los procesos son *al menos* estacionarios en sentido amplio, entonces: 

    - $R_{XY}(-\tau) = R_{YX}(\tau)$
    - $\vert R_{XY}(\tau) \vert \leq \sqrt{R_{XX}(0)R_{YY}(0)}$ (media geométrica)
    - $\vert R_{XY}(\tau) \vert \leq \frac{1}{2}\left[ R_{XX}(0) + R_{YY}(0) \right]$ (media aritmética)

