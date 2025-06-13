# La matriz de transición de orden $t$

La matriz de transición $\Pi$ muestra las probabilidades de transición $\Pi_{i,j}$. Supóngase que se necesita encontrar probabilidades tales como:

\begin{equation*}
  P(X_{t+3} = j \mid X_{t} = i)
\end{equation*}

de que la partícula estará en estado $j$ tres saltos desde el estado actual $i$.

!!! note ""
    Si las probabilidades de transición de un paso $\Pi_{i,j}$ son las entradas de la matriz $\Pi$, ¿cómo puede encontrarse las probabilidades de tres pasos, y más generalmente, las probabilidades de $t$ pasos?

!!! tip "Matriz de transición de orden $t$"
    La matriz de transición de orden $t$ es $\Pi^{t}$, cuya entrada $(i, j)$ es:

    \begin{equation}
      \Pi_{i,j}^t = P(X_{t} = j \mid X_{0} = i)
    \end{equation} 

    que es la probabilidad de saltar de $i$ a $j$ en $t$ pasos.

La homogeneidad en el tiempo (el hecho de que las probabilidades de transición no dependan de $t$) implica que, no obstante el tiempo $\mu \geq 0$:

\begin{equation}
  P(X_{t+\mu} = j \mid X_{\mu} = i) = \Pi_{i,j}^{t}
\end{equation}

O sea, las probabilidades de transición de $t$ pasos dependen solamente de la diferencia de tiempo.

---

## Visualización de la transición de estados

Un algoritmo general se necesita para hallar la matriz de transición $\Pi^{t}$ de orden $t$ para cualquier matriz $\Pi$ de una cadena de Markov dada.

![Cadena de Markov de tiempo discreto](images/20_cadena_markov_discreta.svg)

Para hallar la matriz de transición de orden $t+1$ a partir de la de orden $t$, se usan las suposiciones de Markov básicas.

- Supóngase que la partícula empieza en estado $i$ en el tiempo 0, es decir, $X_0 = i$.
- Para que la partícula esté en el estado $j$ en el tiempo $t+1$, debe haber atravesado algún estado $k$ en el tiempo intermedio $t$, es decir, $X_0 = i \longrightarrow X_t = k \longrightarrow X_{t+1} = j$.

El objetivo es encontrar una expresión para $\Pi_{i,j}^{t+1}$.

\begin{equation*} 
\begin{aligned}
  \Pi_{i,j}^{t+1} & = P(X_{t+1} = j \mid X_{0} = i) \\
                  & = \sum_{k=0}^{N} P(X_{t+1} = j \text{ y } X_{t} = k \mid X_{0} = i) \\
               	  & = \sum_{k=0}^{N} P(X_{t+1} = j \mid X_{t} = k \text{ y } X_{0} = i)P(X_{t} = k \mid X_{0} = i) \\
                  & = \sum_{k=0}^{N} P(X_{t+1} = j \mid X_{t} = k)P(X_{t} = k \mid X_{0} = i) \\
                  & = \sum_{k=0}^{N} \Pi_{i,k}^{t} \Pi_{k,j} 
\end{aligned} 
\end{equation*}


- La primera igualdad es por definición de la matriz de transición de orden $t$.
- La segunda igualdad viene de particionar donde la partícula estaba en el tiempo $t$.
- La tercera igualdad viene de la regla de probabilidad condicional:
    \begin{equation*}
      P(A \cap B \mid C) = P(A \mid B \cap C)P(B \mid C)
    \end{equation*} 
- La cuarta igualdad usa la propiedad de Markov, donde la probabilidad de transición solo depende del estado anterior.
- La quinta igualdad se obtiene por definición de las matrices de transición y por la propiedad de homogeneidad.
