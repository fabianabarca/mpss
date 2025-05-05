!!! abstract "Introducción"
    Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados.

    Luego de suficientes transiciones, y al alcanzar un "régimen permanente", cada estado tiene una probabilidad definida.

Como en el caso anterior (no discreto), supóngase que hay un número grande $N$ de partículas, cada una que salta de estado a estado entre los estados de $S$ guiados por la matriz de transición $\Pi$ de probabilidades de saltos.

- Si todas las $N$ partículas empiezan en el estado 0 en el tiempo $t = 0$, entonces después de un salto algunas permanecerán en el estado 0 (si $\Pi_{0,0} > 0$) y otras saltarán a otros estados. Se puede esperar $N\Pi_{0,j}$ partículas en el estado $j$ después de un salto.
- Por otro lado, supóngase que se distribuyen las $N$ partículas de modo que $N_{j}$ empiezan en el estado $j$ en el tiempo 0 para $j = 0, 1, 2, \ldots, N$.
- Dado que $N_{j}\Pi_{j,i}$ de aquellas partículas que empiezan en $j$ puede esperarse que salten al estado $i$, el número total de partículas que puede esperarse que estén en el estado $i$ después de un salto es:

\begin{equation}
\sum_{j=1}^{N} N_{j} \Pi_{j,i}
\end{equation}

- Pudiera suceder que este número es el mismo número $N_{i}$ de partículas que empezaron en el estado $i$ en el tiempo 0.

!!! note ""
    Cada una de las partículas podría cambiar estados, pero el número completo en el estado $i$ permanecerá constante. Si esto fuera cierto para cada estado $i \in S$, el sistema entero de $N$ partículas estaría en **estado estable**: por cada partícula que deja un estado, una la reemplazaría proveniente de otro estado.

En vez del número $N_{i}$ absoluto de partículas en estado $i$, 

\begin{equation}
  N_{i} = \sum_{j=0}^{N} N_{j}\Pi_{j,i}
\end{equation}

reestablézcase la ecuación en términos del número relativo $N_{i}/N$ de partículas en estado $i$.

Por tanto, es la probabilidad de que cualquier partícula ocupe el estado $i$

\begin{equation}
  N_{i}/N = \sum_{j=0}^{N} \left( N_{j}/N \right) \Pi_{j,i}
\end{equation}

Si este fuera el caso, el sistema entero de $N$ partículas estaría en el estado estable. 

Un vector de probabilidad $\phi$ representa el estado estable si

\begin{equation}
  \phi_{i} = \sum_{j=0}^{N} \phi_{j}\Pi_{j,i}
\end{equation}

o sea, si $\phi^{1} = \phi \cdot \Pi = \phi$. De esta forma, la probabilidad de que una partícula esté en el estado $i$ es la misma en el tiempo 1 como en el tiempo 0. 

Nótese que si $\phi$ tiene esta propiedad de *reproducirse a sí mismo* después de un salto, esto se cumplirá para todos los tiempos $t$: 

\begin{equation}
  \phi^{1} = \phi \Pi = \phi
\end{equation}

lo que implica

\begin{equation}
\begin{aligned}
  \phi^{2} &= \phi^{1} \Pi = \phi \Pi = \phi \\
  \phi^{3} &= \phi^{2} \Pi = \phi \Pi = \phi
\end{aligned} 
\end{equation}

y, en general, 

\begin{equation} 
\begin{aligned}
  \phi^{t} 	& = \phi^{t-1}\Pi \\
   			& = \phi \Pi \\
			& = \phi
\end{aligned} 
\end{equation}

!!! tip "Vector de probabilidad de estado estable"
    Cualquier vector de probabilidad con la propiedad $\phi = \phi \Pi$ es denominado un vector de probabilidad de estado estable. Si la partícula empieza en el estado $i$ con probabilidad $\phi_{i}$ por cada estado $i$, entonces en todo tiempo $t$, estará en el estado $i$ con probabilidad $\phi_{i}$.

## Procedimiento para hallar el vector de probabilidad de estado estable

Consta de dos pasos:

- Establecer y resolver estas ecuaciones:

\begin{equation}
\phi_{j} = \sum_{i=0}^{N} \phi_{i} \Pi_{i,j}
\end{equation}

   para $j = 0, 1, 2, \ldots, N$ o alternativamente, en notación matricial, $\phi = \phi \Pi$.

- Normalizar por medio de la ecuación:

\begin{equation}
\sum_{i=0}^{N} \phi_{i} = 1
\end{equation}

Notas:

- El paso 1 anterior involucra la solución de $N+1$ ecuaciones para $N+1$ incógnitas $\phi_{0}, \phi_{1}, \phi_{2}, \ldots, \phi_{N}$. Siempre habrá redundancia: una de las ecuaciones será una combinación lineal de las otras.
- La ecuación del paso 2 es realmente la $(N+1)$-ésima.
- En otras palabras: el primer paso, aunque define un sistema de $N+1$ ecuaciones, solamente $N$ de ellas son linealmente independientes, por lo que se necesita del paso 2 para proveer la $(N+1)$-ésima ecuación para poder encontrar las $N+1$ incógnitas, que definirán los componentes del vector de probabilidad de estado estable.

---

:material-pencil-box: **EJEMPLO**

!!! example "Vector de probabilidad de estado estable con dos estados"
    Encuentre el vector de probabilidad de estado estable de la cadena de Markov mostrada en la figura siguiente. 

    ![Vector de probabilidad de estado estable](images/21_diagrama_saltos_0-1.svg)

Aplica que: 

\begin{equation} 
\begin{aligned}
\phi & = \phi \Pi \\
(\phi_{0}, \phi_{1}) & = (\phi_{0}, \phi_{1}) \Pi \\
\, & = (\phi_{0}, \phi_{1}) \left[ \begin{array}{cc}
\frac{1}{2} & \frac{1}{2} \\
1   & 0 
\end{array} \right] \\
\phi_{0} & = \frac{1}{2}\phi_{0} + \phi_{1} \\
\phi_{1} & = \frac{1}{2}\phi_{0} 
\end{aligned}
\end{equation}

Las dos últimas ecuaciones son realmente la misma: $\phi_{1} = \frac{1}{2}\phi_{0}$. A continuación se usa la condición de normalización: 

\begin{equation}
1 = \phi_{0} + \phi_{1} = \phi_{0} + \frac{1}{2}\phi_{0} = \frac{3}{2}\phi_{0}
\end{equation}


!!! note ""
    De esta forma se concluye que $\phi_{0} = 2/3, \phi_{1} = 1/3$. Por consiguiente, dos terceras partes del tiempo, la partícula se encontrará en el estado 0 y una tercera parte del tiempo se encontrará en el estado 1.

---

:material-pencil-box: **EJEMPLO**

!!! example "Vector de probabilidad de estado estable con tres estados"
    Considere la cadena de Markov de la siguiente figura. Encuentre el vector de probabilidad de estado estable $\phi$.

    ![Vector de probabilidad de estado estable](images/21_diagrama_saltos_0-1-2.svg) 

Se construye primero la matriz de transición $\Pi$: 

\begin{equation}
\Pi = \left[ \begin{array}{ccc}
0 & \frac{1}{2} & \frac{1}{2} \\
0 & \frac{2}{3} & \frac{1}{3} \\
\frac{1}{3} & \frac{2}{3} & 0
\end{array} \right]
\end{equation}

\begin{equation} 
\begin{aligned}
(\phi_{0}, \phi_{1}, \phi_{2}) & = (\phi_{0}, \phi_{1}, \phi_{2}) \left[ \begin{array}{ccc}
0 & \frac{1}{2} & \frac{1}{2} \\
0 & \frac{2}{3} & \frac{1}{3} \\
\frac{1}{3} & \frac{2}{3} & 0
\end{array} \right] \\
\phi_{0} & = \frac{1}{3}\phi_{2} \\
\phi_{1} & = \frac{1}{2}\phi_{0} + \frac{2}{3}\phi_{1} + \frac{2}{3}\phi_{2} \\
\phi_{2} & = \frac{1}{2}\phi_{0} + \frac{1}{3}\phi_{1}
\end{aligned} 
\end{equation}

lo cual genera, 

\begin{equation} 
\begin{aligned}
-3\phi_{0} + \phi_{2} & = 0 \\
3\phi_{0} - 2\phi_{1} + 4\phi_{2} & = 0 \\
3\phi_{0} + 2\phi_{1} - 6\phi_{2} & = 0
\end{aligned} 
\end{equation}

Si se suma la segunda y la tercera ecuaciones, resulta en $6\phi_{0} - 2\phi_{2} = 0$, que es esencialmente la misma primera ecuación, de donde se puede decir que la tercera ecuación es redundante. De las primeras dos ecuaciones se tiene que, 

\begin{equation} 
\begin{aligned}
\phi_{2} & = 3\phi_{0} \\ 
\phi_{1} & = \frac{15}{2}\phi_{0} 
\end{aligned} 
\end{equation}

Toca ahora usar la condición de normalización: 

\begin{equation}
1 = \phi_{0} + \phi_{1} + \phi_{2} = \left( 1 + \frac{15}{2} + 3\right) \phi_{0} = \frac{23}{2}\phi_{0}
\end{equation}

!!! note ""
    Por consiguiente, $\phi_{0} = \frac{2}{23}, \phi_{1} = \frac{15}{23}, \phi_{2} = \frac{6}{23}$.

---
