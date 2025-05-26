### Presentación

[20 - Cadenas de Markov en tiempo discreto](https://www.overleaf.com/read/jmzgnjrhfhnj#806886)

### Secciones
- Cadenas de Markov en tiempo discreto (1 - 18)

## Condiciones
* Considérese un sistema que puede estar en cualquiera de varios estados.
* El conjunto de estados es denominado el espacio de estados *S* y se supondrá en general que *S = {0, 1, 2, ..., N}*.
* Supóngase ahora que una \emph{partícula} es libre de saltar entre los estados del espacio de estados *S*. Su localización al tiempo *t* es *X<sub>t</sub>*.
* De esta forma se tiene un proceso estocástico $\{X_{t}\}_{t=0}^{\infty}$.
* La localización *X<sub>t</sub>* se mide solamente en los **tiempos discretos** *t* = 0, 1, 2, ....
* *X<sub>0</sub>* es la localización en el tiempo* 0*.

## Suposiciones 
!!! tip "Propiedad de Markov"
    Suponga que la partícula está en el estado *i* en el tiempo *t*. La probabilidad que brinque a otro estado *j* depende solamente de *i*. Matemáticamente, sea *i, j, i<sub>{t-1}</sub>, ..., i<sub>0</sub> ∈ S*. Entonces para cualquier tiempo $t$:

    \begin{equation*}
    \begin{aligned}
    & P(X_{t+1} = j \mid X_{t} = i, X_{t-1} = i_{t-1}, \ldots, X_{0} = i_{0}) \\
    & \qquad = P(X_{t+1} = j \mid X_{t} = i)
    \end{aligned}
    \end{equation*}

    Es decir, el futuro (tiempo *t+1*), dado el presente (tiempo *t*), es independiente del pasado (tiempos *t-1, ..., 0*). La probabilidad anterior es la probabilidad de transición o de salto del estado *i* al estado *j*.

Las probabilidades de transición descritas son:

- **Independientes de los estados pasados** una vez que se conoce donde la partícula está ahora. 
- **Independientes de *t*** el momento en que hace la transición.

!!! tip "Homogeneidad en Tiempo"
    \begin{equation}
    P(X_{t+1} = j \mid X_{t} = i) = \Pi_{i,j}
    \end{equation}

    
    *Π<sub>i, j</sub>* es la probabilidad de transición del estado *i* al estado *j*

!!! tip "Cadena de Markov de tiempo discreto homogénea"
    Consiste de una partícula que salta en cada unidad de tiempo entre estados en un espacio de estados *S*. *X<sub>t</sub>* denota el estado ocupado en el tiempo *t* para *t = 0, 1, 2, ...*

Si la partícula está en el estado *i* al tiempo *t*, estará en el estado *j* en el tiempo *t+1* (sin importar los estados ocupados antes del tiempo *t*) con probabilidad 

\begin{equation}
\Pi_{i,j} = P(X_{t+1} = j \mid X_{t} = i)
\end{equation}

:material-pencil-box: **EJEMPLO 1**

!!! example "Cadena de Markov de tiempo discreto"
    Sea *S = {0, 1}* con probabilidades de transición dadas por: 

    \begin{equation}
    \Pi_{0,0} = 1/3 \qquad \Pi_{0,1} = 2/3 \qquad \Pi_{1,0} = 1/4 \qquad \Pi_{1,1} = 3/4 
    \label{paulista}
    \end{equation}

    Su representación gráfica es:

    <p align="center">
    ![Cadena de Markov de tiempo discreto.](images/20_cadena_markov_discreta.svg)
    </p>

:material-pencil-box: **EJEMPLO 2**

!!! example "Cadena de Markov de tiempo discreto"
    Sea *S = {0, 1}* con probabilidades de transición dadas por: 

    También se suele representar la misma información dada en la ecuación

    \begin{equation*}
    \Pi_{0,0} = 1/3 \qquad \Pi_{0,1} = 2/3 \qquad \Pi_{1,0} = 1/4 \qquad \Pi_{1,1} = 3/4
    \end{equation*}

    pero de forma matricial:

    \begin{equation}
    \Pi = \left[ \begin{array}{ll}
    1/3 & 2/3 \\
    1/4 & 3/4 
    \end{array} \right]
    \end{equation}

Hay una manera estándar de escribir las probabilidades de salto *Π<sub>i, j</sub>* como una matriz, a la que se le llama la matriz de transición *Π*. El elemento en su *i*-ésima fila y *j*-ésima columna es *Π<sub>i, j</sub>*, la probabilidad que la partícula salte de *i* a *j*. 

\begin{equation}
  \Pi = \left[ \begin{array}{ccccc}
  \Pi_{0,0} & \Pi_{0,1} & \Pi_{0,2} & \cdots & \Pi_{0,N} \\
  \Pi_{1,0} & \Pi_{1,1} & \Pi_{1,2} & \cdots & \Pi_{1,N} \\
  \vdots    & \vdots    & \vdots    & \ddots & \vdots    \\
  \Pi_{N,0} & \Pi_{N,1} & \Pi_{N,2} & \cdots & \Pi_{N,N}  
  \end{array}
  \right]
\end{equation}

Nótese que la *i*-esima fila de la matriz *Π* muestra las probabilidades de salto **del** estado *i*, la *j*-ésima columna muestra las probabilidades de salto **al** estado *j*.

!!! tip "Matriz de transición"
    Sea *Π* una matriz de transición de una cadena de Markov. Entonces, 

    - *0 \leq Π<sub>i, j</sub> \leq 1* para todo *i, j* en el espacio de estados *S*.
    - *Π* tiene filas que suman 1: 
  
    \begin{equation}
    \sum_{j = 0}^N \Pi_{i,j} = \sum_{j =0}^{N} P(X_{t+1} = j \mid X_{t} = i) = 1
    \end{equation}

## Cadena de Markov de tres estados

:material-pencil-box: **EJEMPLO 1**
!!! example "Cadena de Markov de tiempo discreto"
    En una cadena de Markov hay tres estados: *S = {0, 1, 2}*. Del estado 0 la partícula salta a los estados 1 o 2 con una idéntica probabilidad de 1/2. Del estado 2, la partícula debe saltar al estado 1. El estado 1 es absorbente: una vez que la partícula entre al estado 1, no puede salirse. Dibuje el diagrama y escriba la matriz de transición.

    \begin{equation*}
     \Pi = \left[ \begin{array}{ccc}
    0 & 1/2 & 1/2 \\
    0 & 1   & 0   \\
    0 & 1   & 0
    \end{array}
    \right]
    \end{equation*}

    Su representación gráfica es:

    <p align="center">
    ![Cadena de Markov de tiempo discreto.](images/20_estados_0-1-2.svg)
    </p>

!!! tip "Estado absorbente"
    El estado *i* es absorbente si *Π<sub>i, j</sub> = 1*.

Interpretado como ``la probabilidad de pasar del estado *i* al mismo estado *i* es del 100 %''.

:material-pencil-box: **EJEMPLO 3**
!!! example "Un paseo aleatorio sobre *S = {0, 1, 2, ..., N}*"
    De cualquiera de los estados **interiores** *1, 2, ..., N-1*, la partícula salta a la derecha al estado *i+1* con probabilidad *p* y hacia la izquierda al estado *i-1* con probabilidad *q = 1 - p*. Es decir, para *1 \leq i \leq N-1*,

    \begin{equation*}
    \Pi_{i,i+1} = p, \qquad \Pi_{i,i-1} = q, \qquad \Pi_{i,j} = 0 \text{ para $j \neq i\pm 1$}
    \end{equation*}

    ¿Cuál es la matriz de transición y el diagrama de saltos?

    Esto corresponde al siguiente juego: tire una moneda; si sale escudo, entonces gana un colón; si sale corona, entonces pierde un colón. En cada tiro se salta al estado *i+1* con probabilidad *p* o al estado *i-1* con probabilidad *q*, con *i* colones al presente.  A este ``juego'' se le conoce como **la ruina del apostador**.

    !!! note ""
        Pueden considerarse tres casos diferentes acerca de la conducta de la partícula en los estados frontera 0 y *N*.
    
    **Caso 1:** Ambos estados frontera podrían ser **absorbentes**, en cuyo caso se tendría,

    \begin{equation*}
    \Pi_{0,0} = 1 \qquad \Pi_{N,N} = 1
    \end{equation*}

    \begin{equation*}
    \Pi = \left[ \begin{array}{cccccccc}
    1 & 0 & 0 & 0 & \cdot & \cdot & \cdot & 0 \\
    q & 0 & p & 0 & \cdot & \cdot & \cdot & 0 \\
    0 & q & 0 & p & \cdot & \cdot & \cdot & 0 \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
    0 & 0 & 0 & 0 & \cdot & q     & 0     & p \\
    0 & 0 & 0 & 0 & \cdot & \cdot & \cdot & 1
    \end{array}
    \right]
    \end{equation*}

    Esto corresponde a las situaciones en que el juego acabó dado que se quedó sin dinero o si se ha ganado el dinero de los oponentes.

    **Caso 2:** Ambos estados frontera podrían ser **reflectores**, en cuyo caso se tendría,

    \begin{equation*}
    \Pi_{0,1}  = 1 \qquad \Pi_{N,N-1} = 1
    \end{equation*}

    Esto corresponde al caso cuando mi oponente me da uno de sus colones cuando quedo con los bolsillos vacíos, o inversamente. Y que siga el juego.

    **Caso 3:** Los estados frontera podrían ser **parcialmente reflectores**, en cuyo caso se tendría,

    \begin{equation*}
    \Pi_{0,0} = r, \quad \Pi_{0,1} = 1 - r, \quad \Pi_{N,N} = s, \quad \Pi_{N,N-1} = 1 - s 
    \end{equation*}

    La correspondiente matriz de transición estaría dada por 

    \begin{equation*}
    \Pi = \left[ \begin{array}{ccccccccc}
    r & 1- r & 0 & 0 & 0 & \cdot & \cdot & \cdot & 0 \\
    q & 0    & p & 0 & 0 & \cdot & \cdot & \cdot & 0 \\
    0 & q    & 0 & p & 0 & \cdot & \cdot & \cdot & \cdot \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
     0 & 0    & 0 & 0 & 0 & \cdot & q     & 0     & p \\
     0 & 0    & 0 & 0 & 0 & \cdot & \cdot & 1 - s & s
    \end{array}
    \right]
    \end{equation*}

    El caso 3 incluye los dos casos anteriores para valores particulares de *r* y *s*.

    <p align="center">
    ![Cadena de Markov de tiempo discreto.](images/20_paseo_aleatorio.svg)
    </p>

:material-pencil-box: **EJEMPLO 4**
!!! example "Proceso de renovación"
    Considérese un componente cuya edad puede ser 0 o 1 o 2 ...

    * Edad 0 significa *acabado de instalar*. Supóngase que no importa qué tan viejo el componente es, se estropeará durante el próximo intervalo de tiempo con probabilidad *q* o continuará operando con probabilidad *p = 1 - q*. Así, el componente sigue la propiedad de la carencia de memoria.
    * El espacio de estados es *S = \{0, 1, 2, ...}* y el estado del sistema es la edad del componente instalado. Suponga que tan pronto como el componente se averíe, es reemplazado instantáneamente y entonces el estado del sistema se vuelve cero. La transición del estado 0 al estado 0 ocurre si el componente recién instalado se avería inmediatamente.

    \begin{equation*}
    \Pi = \left[ \begin{array}{ccccccc}
    q & p & 0 & 0 & \cdot & \cdot & \cdot \\
    q & 0 & p & 0 & 0 & \cdot & \cdot \\
    0 & q & 0 & p & 0 & \cdot & \cdot \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot   
    \end{array}
    \right]
    \end{equation*}

    * Véase que el espacio de estados *S*, en este caso, si bien discreto, tiene infinitamente muchos estados.
    * Este modelo recibe también el nombre de modelo de nacimiento o de desastre. Algunas aplicaciones son evidentes: tiempos de vida de componentes. Hay una que no es tan obvia: las noticias se apilan en una pizarra de avisos a una razón más o menos constante hasta que alguien decide tirarlas todas.
    * El estado del sistema es el número de días desde la última vez que la pizarra fue limpiada. Si la limpieza de la pizarra se hace aleatoriamente, independiente de cuantas noticias haya o del tiempo desde la última limpieza, la pizarra será limpiada en la próxima unidad de tiempo con una probabilidad constante *q*.

