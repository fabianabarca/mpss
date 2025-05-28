!!! Introducción

    Muchos fenómenos del mundo real pueden ser modelados como una secuencia de **transiciones** de un **estado** a otro, donde cada transición tiene una incertidumbre asociada.

# Definición de cadenas de Markov

## Ejemplos de "cadenas de Markov" I

* Un modelo simplista del tiempo atmosférico en un lugar está dado por la secuencia temporal {X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ...}, donde X<sub>i</sub> tiene los dos únicos valores 0 ("seco") y 1 ("lluvioso").

![](18_modelo_simplista_tiempo.svg)

* Los precios de las acciones de una empresa tienen una incertidumbre respecto a si el precio va a hacer una *transición* hacia un valor mayor o menor.

!!! note ""

    En ambos casos, las **transiciones** pueden modelarse de manera probabilística y es crucial el conocimiento del estado actual. Las cadenas o procesos de Markov son un modelo de *dependencia*.

## Ejemplos de "cadenas de Markov" II

**Otros ejemplos de aplicaciones**
* Predicción de cambios en la demanda de electricidad
* Modelado del movimiento de insectos
* Monitoreo del uso de camillas en hospitales
* Personas que cambian de servicio celular
* Monitoreo de patrones de navegación web para proveer anuncios personalizados

## La propiedad de Markov

* Las cadenas de Markov son **procesos estocásticos** que cumplen la *propiedad de Markov*.
* Informalmente, esta propiedad establece que los estados futuros dependen únicamente del estado actual, y no de la secuencia de estados para llegar ahí. De algún modo, “trunca la memoria”.

!!! note "Propiedad de Markov o de la falta de memoria"

    Formalmente, es una *probabilidad* condicional de la forma
    
    \begin{equation}
        P(X<sub>n</sub> = x | X<sub>0</sub>, ... , X<sub>n-1</sub>) = P(X<sub>n</sub> = x | X<sub>n-1</sub>), ∀n, ∀x
    \end{equation}

## Ejemplo de taxis en diferentes zonas de una ciudad I

Una ciudad tiene tres diferentes “zonas”, numeradas 1, 2 y 3, y los taxis operan en todas
las zonas.

![](18_estados_zonas.svg)

La probabilidad de que el próximo pasajero vaya hacia una zona particular depende de ¿Dónde abordó el taxi?

# Deducción a partir de la distribución exponencial

## La distribución exponencial como “tiempo de vida”

!!! note""

    La distribución exponencial es la típica caracterización de la probabilidad de los tiempos de espera (o “de vida”).

Si *T* es el tiempo de vida de un componente que está exponencialmente distribuido con parámetro α, entonces *T* tiene densidad

begin{equation}
  f_{T}(t) = 
  \begin{cases}
  0 					& t < 0 \\
  \alpha e^{-\alpha t} 	& t > 0 
  \end{cases}
\end{equation}

La media de *T* es el recíproco del parámetro α, *E*[T ] = 1/α .
* La variable aleatoria T tiene la *propiedad de falta de memoria*
* “No importa la antigüedad del componente, este opera como si fuera nuevo”.

## Propiedad de falta de memoria de la distribución exponencial

La propiedad de falta de memoria, matemáticamente, se escribe[^1] como

P(T>t+s|T>t) = P(T>s)

para tiempos *t*, *s* ≥ 0. También se tiene que

P(T>t) = e^(−αt)

para *t* ≥ 0 (porque *F<sub>T</sub>* (t) = 1 − e(−αt) ).

A partir de estas definiciones, se determinan dos casos específicos.

[^1]: Por ejemplo, T podría ser “el tiempo de espera de un autobús”, y s = 5 min y t = 30 min.

## Primer hecho I
### Densidad de la variable mínima de un conjunto de variables aleatorias

* Supóngase que *T<sub>1</sub>*, *T<sub>2</sub>*, . . ., *T<sub>n</sub>* son variables aleatorias independientes, cada una
distribuida exponencialmente. Supóngase que *T<sub>i</sub>* tiene parámetro *α<sub>i</sub>*.
* Suponga *N* componentes que se “conectan” (o “inician su operación conjunta”) al tiempo *t* = 0.
* *T<sub>i</sub>* es el tiempo de vida del *i*-ésimo componente.
* Sea *M* el mínimo de todos los tiempos *T<sub>i</sub>* ’s de los componentes. *M* es el tiempo en que el primer componente falla.
* *M* es una variable aleatoria.

## Primer hecho II
### Densidad de la variable mínima de un conjunto de variables aleatorias

* Sea *t* ≥ 0. Entonces *M* = min{*T<sub>1</sub>*, . . . , *T<sub>N</sub>*} es más grande que *t* si y solo si **todo** Ti > t.

\begin{equation} 
\begin{aligned}
  P(M > t) & = P(\min\{T_{1}, T_{2}, \ldots, T_{N}\} > t) \\
  & = P(T_{1} > t, T_{2} > t, \ldots, T_{N} > t) \\
  & = e^{-\alpha_{1}t}\cdot e^{-\alpha_{2}t} \cdots e^{-\alpha_{N}t} \\
  & = e^{-(\alpha_{1} +\alpha_{2} + \ldots +\alpha_{N})t}
\end{aligned} 
\end{equation}

!!! note""

    *M* está exponencialmente distribuida con parámetro α<sub>1</sub> + α<sub>2</sub> + . . . + α<sub>N</sub> y valor medio 1/(α<sub>1</sub> + α<sub>2</sub> + . . . + α<sub>N</sub> ).

## Segundo hecho I
### Probabilidad de que un componente dado sea el que falle

Ante la pregunta,
    *¿Cuál es la probabilidad de que, cuando el primer fallo suceda, sea el componente
    j-ésimo?*

!!! note""

    La probabilidad de que entre las *N* variables aleatorias *T<sub>i</sub>* el mínimo sea *T<sub>j</sub>* está dada por la expresión

    \begin{equation}
        P(T_{j} = \min \{T_{1}, T_{2}, \ldots, T_{N}\}) = \frac{\alpha_{j}}{\alpha_{1} + \alpha_{2} + \cdots + \alpha_{N}}
    \end{equation}

## Segundo hecho II
### Probabilidad de que un componente dado sea el que falle

**Prueba para dos variables aleatorias**
Si *T<sub>1</sub>* y *T<sub>2</sub>* son independientes y distribuidos exponencialmente con parámetros
respectivos α y β: *f<sub>T1,T2</sub>* (*t<sub>1</sub>*, *t<sub>2</sub>*) = αe^(−α*t<sub>1</sub>*) βe^(−β*t<sub>2</sub>*) , para *t<sub>1</sub>*, *t<sub>2</sub>* > 0. Con *t<sub>1</sub>* y *t<sub>2</sub>*
correspondientes a *T<sub>1</sub>* y *T<sub>2</sub>*:

\begin{equation} 
\begin{aligned}
  P(T_{1} = \min\{T_{1}, T_{2}\}) & = P(T_{1} < T_{2}) \\
  	& = \iint_{T_1 < T_2} f_{T_{1}, T_{2}}(t_{1},t_{2}) \di{t_1} \di{t_2} \\
  	& = \int_{0}^{\infty}\int_{0}^{t_{2}}\alpha e^{-\alpha t_{1}}\beta e^{-\beta t_{2}} \di{t_1} \di{t_2} \\
  	& = \int_{0}^{\infty}(1 - e^{-\alpha t_{2}})\beta e^{-\beta t_{2}} \di{t_2} \\
 	& = 1 - \frac{\beta}{\alpha + \beta} = \frac{\alpha}{\alpha + \beta} 
\end{aligned} 
\end{equation}