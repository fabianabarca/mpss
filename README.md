# Notas de clase de Modelos Probabilísticos de Señales y Sistemas

| Presentación | Descripción |
|---|---|
| 0 - Teoría de conjuntos y análisis combinatorio | Los “eventos” y “experimentos” que vamos a utilizar se modelan y analizan matemáticamente. Dos herramientas útiles para ello son la teoría de conjuntos, para relacionar y agrupar eventos, y el análisis combinatorio, para contar el número de posibles resultados de un experimento. |
| 1 - La probabilidad | La probabilidad es una rama de la matemática con inmensa aplicación práctica en muchas disciplinas: desde el quehacer personal y doméstico hasta grandes decisiones sociales. En nuestra disciplina es, además, fundamental para el análisis de... señales y sistemas. |
| 2 - Probabilidad conjunta, condicional y teorema de Bayes | Una gran cantidad de “experimentos” y cálculos de probabilidad cotidianos pueden ser descritos por medio de las herramientas de la probabilidad condicional y conjunta, el teorema de Bayes y los eventos independientes, que representan un conocimiento básico y útil de la probabilidad. |
| 3 - Eventos independientes y pruebas de Bernoulli | La independencia estadística es una simplificación útil en los cálculos de probabilidad. Implica que la ocurrencia de un evento no afecta la probabilidad de ocurrencia de otro evento independiente. La independencia de dos o más eventos es una propiedad del experimento y su determinación depende del conocimiento del mismo o de un análisis estadístico. |
| 4 - Variables aleatorias | Las variables aleatorias facilitan una manipulación numérica más robusta de los fenómenos aleatorios, y permiten extender el análisis a muchos más casos que los vistos hasta ahora. Herramientas como las funciones de densidad y de distribución acumulativa de probabilidad proveen descripciones completas de los modelos probabilísticos. |
| 5 - Funciones de distribución condicionales | Para las variables aleatorias también es posible modelar probabilidades de eventos condicionados a la ocurrencia de otros eventos. Esta relación de interdependencia está sujeta al experimento o fenómeno particular y una buena cantidad de situaciones reales obedecen a un modelado condicional como este. |
| 6 - Momentos de una variable aleatoria | El valor esperado y los “momentos” (su generalización) permiten caracterizar numéricamente el comportamiento o las tendencias de una variable aleatoria. |
| 7 - Funciones que dan momentos | A partir de una nueva función es posible generalizar la obtención de los momentos ordinarios de una variable aleatoria. Esta función es única para cada va. Hay dos tipos de estas funciones: la función generadora de momentos (MGF) y la función característica (CF). |
| 8 - Transformaciones de una variable aleatoria | Las transformaciones permiten determinar la función de densidad probabilística de una variable aleatoria Y a partir del conocimiento de otra X , relacionadas por la función Y = T(X) = g(X). Es común en situaciones donde el resultado de un proceso o la salida de un sistema depende de una entrada aleatoria. |
| 9 - Variables aleatorias múltiples | En muchos experimentos, las observaciones no son una sola cantidad, sino un grupo o familia de cantidades. Por tanto, se construyen vectores de variables aleatorias, llamados vectores aleatorios. |
| 10 - Momentos de variables aleatorias múltiples | Es posible determinar momentos asociados con dos o más variables aleatorias. La información que proveen, al igual que con las variables aleatorias individuales, son útiles como descriptores generales. |
| 11 - Transformaciones de variables aleatorias múltiples | Similar al caso de las variables aleatorias marginales, es posible “transformar” dos o más variables aleatorias conjuntas mediante funciones, y el objetivo es encontrar la función de densidad de las nuevas variables aleatorias conjuntas. |
| 12 - Teorema del límite central y otros | El teorema del límite central establece que la función de distribución probabilística de la suma o de las medias muestrales de un número grande de variables aleatorias aproxima a una distribución gaussiana (normal). |
| 13 - Procesos estocásticos | Los procesos aleatorios (o estocásticos) son los terceros “objetos aleatorios” que analizaremos. Incorporan una segunda variable independiente, el tiempo, que los hace útiles en la descripción de fenómenos cambiantes o dinámicos tales como las señales y los sistemas. |
| 14 - Ergodicidad y funciones de correlación | La ergodicidad establece la igualdad entre el promedio estadístico y el promedio temporal de un proceso aleatorio. Es una nueva forma de estacionaridad que simplifica el análisis del proceso aleatorio. |
| 15 - Características espectrales de procesos estocásticos | Cuando los procesos estocásticos describen señales (funciones unidimensionales en el tiempo), es posible analizarlos según sus características espectrales, es decir, relativas a la frecuencia. Esto es útil en aplicaciones de procesamiento de señales: sensores, audio, sistemas de control, comunicaciones, estabilidad de sistemas de potencia. |
| 16 - Respuesta de sistemas lineales a una señal aleatoria | En la interacción de señales y sistemas donde hay entradas aleatorias, es posible determinar cantidades útiles para el análisis, como la señal misma o la potencia de salida, conociendo las características determinísticas del sistema y características estadísticas de la entrada. |
| 17 - Proceso contador de Poisson | Un proceso aleatorio de Poisson describe el número de veces que algún evento ha ocurrido, como una función del tiempo o el espacio, y en donde los eventos ocurren en instantes o lugares al azar. |
| 18 - Cadenas de Markov de tiempo continuo | Muchos fenómenos del mundo real pueden ser modelados como una secuencia de transiciones de un estado a otro, donde cada transición tiene una incertidumbre asociada. Las cadenas de Markov proveen un modelo para información secuencial que permite que resultados futuros dependan de otros resultados previos. |
| 19 - Markov de tiempo continuo y el vector de estado estable | Luego de suficientes transiciones de estados, la probabilidad de ocurrencia de un estado, de entre todos los estados posibles, se estabiliza en un valor constante. A cada estado, por tanto, se le asigna una probabilidad de estado estable. |
| 20 - Cadenas de Markov de tiempo discreto | Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados. |
| 21 - Markov de tiempo discreto y el vector de estado estable | Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados. Luego de suficientes transiciones, y al alcanzar un “régimen permanente”, cada estado tiene una probabilidad definida. |
