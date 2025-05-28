!!! Introducción
    Muchos fenómenos del mundo real pueden ser modelados como una secuencia de **transiciones** de un **estado** a otro, donde cada transición tiene una incertidumbre asociada.

## Ejemplos de "cadenas de Markov" I

* Un modelo simplista del tiempo atmosférico en un lugar está dado por la secuencia temporal {X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ...}, donde X<sub>i</sub> tiene los dos únicos valores 0 ("seco") y 1 ("lluvioso").

![](18_modelo_simplista_tiempo.svg)

* Los precios de las acciones de una empresa tienen una incertidumbre respecto a si el precio va a hacer una *transición* hacia un valor mayor o menor.

!!! note ""
    En ambos casos, las **transiciones** pueden modelarse de manera probabilística y es crucial el conocimiento del estado actual. Las cadenas o procesos de Markov son un modelo de *dependencia*.

## Ejemplos de "cadenas de Markov" II

