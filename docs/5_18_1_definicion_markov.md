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

Si T es el tiempo de vida de un componente que está exponencialmente distribuido con parámetro α, entonces T tiene densidad

begin{equation}
  f_{T}(t) = 
  \begin{cases}
  0 					& t < 0 \\
  \alpha e^{-\alpha t} 	& t > 0 
  \end{cases}
\end{equation}

La media de T es el recíproco del parámetro α, E[T ] = 1/α .
* La variable aleatoria T tiene la *propiedad de falta de memoria*
* “No importa la antigüedad del componente, este opera como si fuera nuevo”.
