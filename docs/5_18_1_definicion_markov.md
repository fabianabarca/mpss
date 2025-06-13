# Definición de cadenas de Markov

## Ejemplos de "cadenas de Markov"

* Un modelo simplista del tiempo atmosférico en un lugar está dado por la secuencia temporal {X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ...}, donde X<sub>i</sub> tiene los dos únicos valores 0 ("seco") y 1 ("lluvioso").

![](/docs/images/18_modelo_simplista_tiempo.svg)

* Los precios de las acciones de una empresa tienen una incertidumbre respecto a si el precio va a hacer una *transición* hacia un valor mayor o menor.

!!! note ""

    En ambos casos, las **transiciones** pueden modelarse de manera probabilística y es crucial el conocimiento del estado actual. Las cadenas o procesos de Markov son un modelo de *dependencia*.

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

    Formalmente, es una *probabilidad condicional* de la forma

    \[
        P(X_n = x \mid X_0, \dots, X_{n-1}) = P(X_n = x \mid X_{n-1}), \quad \forall n, \forall x
    \]


## Ejemplo de taxis en diferentes zonas de una ciudad I

Una ciudad tiene tres diferentes “zonas”, numeradas 1, 2 y 3, y los taxis operan en todas
las zonas.

![](/docs/images/18_estados_zonas.svg)

La probabilidad de que el próximo pasajero vaya hacia una zona particular depende de ¿Dónde abordó el taxi?

# Deducción a partir de la distribución exponencial

## La distribución exponencial como “tiempo de vida”

!!! note ""

    La distribución exponencial es la típica caracterización de la probabilidad de los tiempos de espera (o “de vida”).

Si *T* es el tiempo de vida de un componente que está exponencialmente distribuido con parámetro α, entonces *T* tiene densidad

\[
f_{T}(t) =
\begin{cases}
  0 & \text{si } t < 0 \\
  \alpha e^{-\alpha t} & \text{si } t > 0
\end{cases}
\]

La media de *T* es el recíproco del parámetro $\alpha$, $E[T] = \frac{1}{\alpha}$.
* La variable aleatoria T tiene la *propiedad de falta de memoria*
* “No importa la antigüedad del componente, este opera como si fuera nuevo”.

## Propiedad de falta de memoria de la distribución exponencial

La propiedad de falta de memoria, matemáticamente, se escribe como

\[
P(T > t + s \mid T > t) = P(T > s)
\]

para tiempos \( t, s \geq 0 \). También se tiene que

\[
P(T > t) = e^{-\alpha t}
\]

para \( t \geq 0 \) (porque \( F_T(t) = 1 - e^{-\alpha t} \)).

A partir de estas definiciones, se determinan dos casos específicos.

[^1]: Por ejemplo, T podría ser “el tiempo de espera de un autobús”, y s = 5 min y t = 30 min.

## Primer hecho
### Densidad de la variable mínima de un conjunto de variables aleatorias

* Supóngase que *T<sub>1</sub>*, *T<sub>2</sub>*, . . ., *T<sub>n</sub>* son variables aleatorias independientes, cada una
distribuida exponencialmente. Supóngase que *T<sub>i</sub>* tiene parámetro *α<sub>i</sub>*.
* Suponga *N* componentes que se “conectan” (o “inician su operación conjunta”) al tiempo *t* = 0.
* *T<sub>i</sub>* es el tiempo de vida del *i*-ésimo componente.
* Sea *M* el mínimo de todos los tiempos *T<sub>i</sub>* ’s de los componentes. *M* es el tiempo en que el primer componente falla.
* *M* es una variable aleatoria.

* Sea *t* ≥ 0. Entonces *M* = min{*T<sub>1</sub>*, . . . , *T<sub>N</sub>*} es más grande que *t* si y solo si **todo** \(T_i > t\).

\[
\begin{aligned}
  P(M > t) &= P\left( \min\{T_{1}, T_{2}, \ldots, T_{N}\} > t \right) \\
  &= P(T_{1} > t, T_{2} > t, \ldots, T_{N} > t) \\
  &= e^{-\alpha_{1}t} \cdot e^{-\alpha_{2}t} \cdots e^{-\alpha_{N}t} \\
  &= e^{-(\alpha_{1} + \alpha_{2} + \ldots + \alpha_{N})t}
\end{aligned}
\]

!!! note ""

    *M* está exponencialmente distribuida con parámetro \(α_1 + α_2 + . . . + α_N\) y valor medio \(1/(α_1 + α_2 + . . . + α_N\)).

## Segundo hecho
### Probabilidad de que un componente dado sea el que falle

Ante la pregunta,
    *¿Cuál es la probabilidad de que, cuando el primer fallo suceda, sea el componente j-ésimo?*

!!! note ""

    La probabilidad de que entre las *N* variables aleatorias *T<sub>i</sub>* el mínimo sea *T<sub>j</sub>* está dada por la expresión

    \[
    P\left( T_{j} = \min \{T_{1}, T_{2}, \ldots, T_{N}\} \right) = \frac{\alpha_{j}}{\alpha_{1} + \alpha_{2} + \cdots + \alpha_{N}}
    \]

**Prueba para dos variables aleatorias**

Si \( T_1 \) y \( T_2 \) son independientes y distribuidos exponencialmente con parámetros respectivos \( \alpha \) y \( \beta \): \(f_{T_1, T_2}(t_1, t_2) = \alpha e^{-\alpha t_1} \beta e^{-\beta t_2}, \quad \text{para } t_1, t_2 > 0.
\)

Con \( t_1 \) y \( t_2 \) correspondientes a \( T_1 \) y \( T_2 \):

\[
\begin{aligned}
P\left( T_1 = \min\{T_1, T_2\} \right) &= P(T_1 < T_2) \\
&= \iint_{T_1 < T_2} f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2 \\
&= \int_{0}^{\infty} \int_{0}^{t_2} \alpha e^{-\alpha t_1} \beta e^{-\beta t_2} \, dt_1 \, dt_2 \\
&= \int_{0}^{\infty} \left( 1 - e^{-\alpha t_2} \right) \beta e^{-\beta t_2} \, dt_2 \\
&= 1 - \frac{\beta}{\alpha + \beta} = \frac{\alpha}{\alpha + \beta}.
\end{aligned}
\]