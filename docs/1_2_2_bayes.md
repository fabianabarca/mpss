### Presentación

[2 - Probabilidad conjunta, condicional y teorema de bayes](https://www.overleaf.com/read/mpzrvppyvszr#9c9c90)

### Secciones
- Teorema de Bayes (16 - 32)

# Teorema de Bayes


!!! abstract Introducción

    Como uno de los resultados más útiles de la teoría de probabilidad, el teorema de Bayes permite *actualizar* el conocimiento o *recalcular* la probabilidad de un evento de interés cuando encontramos nueva evidencia de su ocurrencia.


!!! Question ""
    ❤ La prueba médica (la evidencia) resultó negativa, ¿cuál es la probabilidad de que realmente no tenga la enfermedad?


---

Sean $A$ y $B$ eventos en los que se asume inicialmente una dependencia de $B$ a la ocurrencia de $A$ tal que, si $P(A) \neq 0$,

$$
P(B \mid A) = \frac{P(B \cap A)}{P(A)}
$$

También existe una relación inversa en que, si $P(B) \neq 0$, se cumple que

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Del álgebra de conjuntos se sabe que $P(B \cap A) = P(A \cap B)$, y es posible igualar estas dos ecuaciones,resultando:



!!! Success Regla de la probabilidad condicional inversa:
    $$
    P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}
    $$







Una ecuación equivalente se obtiene de una sustitución de $P(B)$ en términos de una **probabilidad total**:

!!! example ""
    $$
    P(A_n \mid B) = \frac{P(B\mid A_n)P(A_n)}{P(B \mid A_1)P(A_1) + \cdots + P(B \mid A_N)P(A_N)}
    $$

donde $\{ A_n \}$ es una partición universal para $n = 1, 2, \ldots, N$.

!!! tip ""
    Una intuición importante de esta ecuación es que la ocurrencia de $B$ puede deberse a múltiples factores (en este caso, cualquiera entre $A_1,\ldots,A_N$), pero estamos interesados en la *relación* con **uno** de ellos en particular, $A_n$.

!!! note Nota
    Esta *relación* puede, o no, ser de **causalidad**.

### Definiciones:

!!! example ""
    $$
    P(A_n \mid B) = \frac{P(B\mid A_n)P(A_n)}{P(B \mid A_1)P(A_1) + \cdots + P(B \mid A_N)P(A_N)}
    $$

- **$P(A_n)$**: probabilidades *a priori*, dado que se conocen para cada evento ${ A_n }$ antes de la ejecución del experimento.
- **$P(B \mid A_n)$**: son *probabilidades condicionales directas* o *probabilidades de transición* en teoría de telecomunicaciones. Típicamente son conocidas antes de ejecutar el experimento.
- **$P(A_n \mid B)$**: probabilidades *a posteriori* o *condicionales inversas*, dado que se investigan después de la ejecución del experimento, cuando se obtiene un evento $B$.

---

!!! example **Ejemplo de incidencia de una enfermedad poco común**

    Se ha desarrollado un examen de diagnóstico para una enfermedad extraña que afecta solo a 1 de cada 1000 adultos. En análisis estadísticos médicos de clasificación binaria (*sí o no*) se define:

    ### Definiciones:
    - **Sensitividad**: Un resultado positivo implica que el individuo efectivamente tiene la enfermedad en el 99 \% de los casos (también llamada *probabilidad de detección*). Un resultado contrario es un **falso negativo**.
    
    - **Especificidad**: Un individuo sin la enfermedad dará resultado negativo 98 \% de las veces (también llamada *tasa negativa verdadera*). Un resultado contrario es un **falso positivo**.

    !!! Question ¿Cuál es la probabilidad de que el paciente sí tenga la enfermedad si el diagnóstico es positivo?
### Cálculo con el Teorema de Bayes:


![Árbol de probabilidad de Bayes](images/2_arbol_probs_ej_enfermedad.svg)




$$
\begin{aligned}
P(B \mid A) & = \frac{P(A\mid B)P(B)}{P(A \mid B)P(B) + P(A \mid \overline{B})P(\overline{B})} \\
& = \frac{(0.99) (0.001)}{(0.99) (0.001) + (0.02) (0.999)} \\
& = 0.0472 \approx 5\%
\end{aligned}
$$

!!! note ""


    La probabilidad de que el paciente **sí tenga la enfermedad** es del **5 %**… a pesar de que el resultado del examen fue positivo.

!!! question ¿Por qué es tan baja esta probabilidad, con una _sensibilidad_ de la prueba del 99 %?

---



### Otros valores comunes
- **Cuadro**: Otros valores de sensitividad y especificidad para algunos exámenes de enfermedades comunes

| Enfermedad            | Sensitividad | Especificidad |
|-----------------------|--------------|---------------|
| Cáncer de próstata   | 85 %         | 30 %          |
| Cáncer de mama       | 75 %         | 92 %          |
| Cáncer de colon      | 86 %         | 93 %          |
| COVID-19 BioMedomics | 89 %         | 91 %          |

---

!!! example **Ejemplo del apagón en el sistema eléctrico**

    Un barrio de Heredia experimenta un apagón. Una ingeniera de operación y mantenimiento de ESPH está cerca de ahí e inmediatamente sospecha de cuatro orígenes de la falla: ($A_1$) en la línea de transmisión Colima - Heredia, ($A_2$) en el transformador de la subestación de Heredia, ($A_3$) en la línea de distribución hacia San Pablo o en ($A_4$) el transformador del poste.


    > Sabe la ingeniera que ante una falla en el transformador de subestación siempre habrá una desconexión permanente. ¿Cuál es la probabilidad de que la causa de la desconexión permanente haya sido una falla en ($A_2$) el trafo de subestación?
    
    !!! note Nota
        Las protecciones del sistema eléctrico ejecutan dos operaciones ante una falla: o ($B$) una desconexión permanente o ($\overline{B}$) un "recierre" luego de un tiempo prudencial si la falla ha desaparecido.




    #### Los datos conocidos para el último mes son los siguientes:

    | Falla               | Casos | Recierre | Desconexión |
    |---------------------|-------|----------|--------------|
    | $A_1$ Línea de transmisión   | 3     | 2        | 1            |
    | $A_2$ Trafo de subestación   | 3     | 0        | 3            |
    | $A_3$ Línea de distribución  | 16    | 9        | 7            |
    | $A_4$ Trafo de poste         | 8     | 0        | 8            |

Para encontrar la probabilidad de cada falla, analizamos su frecuencia relativa con los datos provistos (se descartan aquí otros tipos de fallas). Por tanto


- $P(A_1) = 3/30 = 0.10$
- $P(A_2) = 3/30 = 0.10$
- $P(A_3) = 16/30 = 0.5333$
- $P(A_4) = 8/30 = 0.2666$


Sean $B = \{ \text{desconexión permanente} \}$ y $ \overline{B} = \{ \text{recierre} \}$. La probabilidad que buscamos es una proporción entre el evento de interés y todas las posibilidades juntas:





$$
\text{Probabilidad de que } A_2 \text{ sea la causa de } B = 
\frac{
\text{Probabilidad de que sucedan } A_2 \textbf{ y } B
}{
\text{Suma de las probabilidades de todas las combinaciones } A_n \textbf{ y } B
}
$$


y que puede expresarse como:

$$
P(A_2 \mid B) = \boxed{\frac{P(A_2 \cap B)}{P\left( \bigcup_{n=1}^{4} A_n \cap B \right)}} = \frac{P(A_2)P(B \mid A_2)}{P(B)}
$$


que es otra forma de escribir la regla de Bayes. La gráfica a continuación muestra los "caminos" posibles y el evento de interés está resaltado. 


![Árbol de caminos](images/2_caminos.svg)


Con \( P(B \mid A_1) = \frac{1}{3} = 0.3333 \), \( P(B \mid A_2) = 1 \), \( P(B \mid A_3) = \frac{7}{16} = 0.4375 \), \( P(B \mid A_4) = 1 \):


!!! note ""
    $$
    \begin{aligned}
    P(A_2 \mid B) &= \frac{P(A_2)P(B\mid A_2)}{P(A_1)P(B \mid A_1) + P(A_2)P(B \mid A_2) + P(A_3)P(B \mid A_3) + P(A_4)P(B \mid A_4)} \\
    &= \frac{(0.1)(1)}{(0.1)(0.3333) + (0.1)(1) + (0.5333)(0.4375) + (0.2666)(1)} \\
    &= 0.1579
    \end{aligned}
    $$

que representa una probabilidad quizá más baja de lo esperado. A pesar de que una falla en el transformador de subestación **siempre** provoca una desconexión permanente (y el consiguiente apagón), no son fallas comunes, y por eso su probabilidad sigue siendo baja. En este problema las probabilidades más alta son las de fallas de líneas de distribución $P(B \mid A_3) = 0.3684$ (expuestas a ramas, choques, etc.) y los trafos de poste $P(B \mid A_4) = 0.4210$, que son menos casos pero siempre implican desconexión.

---

!!! example **Ejemplo de los distribuidores de jocotes**


    Tres distribuidores de frutas, $A$, $B$ y $C$, entregan jocotes a un supermercado. Un día la inspección de producto encuentra, con cierto alborozo, una "guápil" (dos jocotes que nacieron juntos) en un contenedor donde están todos los jocotes de todos los distribuidores, revueltos e indistinguibles entre sí. En este lote de producto, $A$ entregó (aproximadamente) 800 jocotes, $B$ 700 y $C$ 500. En estudios previos se ha determinado que la incidencia de guápiles en cada distribuidora es del 1\% en $A$, del 2\% en $B$ y del 5\% en $C$. 

    !!! question ¿Cuál es la probabilidad de encontrar una guápil? Si una guápil es encontrada, ¿cuál es la probabilidad de que vino de $C$?


Sean $P(A)$, $P(B)$ y $P(C)$ las probabilidades de encontrar un jocote de los distribuidores $A$, $B$ y $C$, respectivamente. No son equiprobables, sino que están obtenidas por frecuencia relativa de la forma:

$$
\begin{aligned}
P(A) &= \frac{800}{800 + 700 + 500} = \frac{800}{2000} = 0,4 \\ P(B)&= \frac{700}{2000} = 0,35 \\ P(C) &= \frac{500}{2000} = 0,25 \\ \\
\end{aligned}
$$

La probabilidad de encontrar una guápil, $P(G)$, es la probabilidad total dada por:

$$
\begin{aligned}
P(G) &= P(A) P(G \mid A) + P(B) P(G \mid B) + P(C) P(G \mid C) \\
     &= 0.4 \cdot 0.01 + 0.35 \cdot 0.02 + 0.25 \cdot 0.05 \\
     &= 0.0235 = 2.35\%
\end{aligned}
$$



La probabilidad condicional inversa de que si una guápil fue encontrada esta vino del distribuidor $C$, $P(C \mid G)$, viene dada por el teorema de Bayes como:


!!! note ""
    $$
    \begin{aligned}
    P(C \mid G) &= \frac{P(C) \cdot P(G \mid C)}{P(G)} \\
                &= \frac{\mathbf{P(C)} \cdot \mathbf{P(G \mid C)}}{P(A) \cdot P(G \mid A) + P(B) \cdot P(G \mid B) + \mathbf{P(C)} \cdot \mathbf{P(G \mid C)}} \\
                &= \frac{0.25 \cdot 0.05}{0.0235} = 0.5319 = 53.2\%
    \end{aligned}
    $$




Observar (resaltado) como la probabilidad de que la guápil vino de $C$ es una proporción con las probabilidades de que venga de los otros distribuidores.

---

## Videos y referencias en internet

- **[Probability Part 2: Updating Your Beliefs with Bayes](https://youtu.be/oZCskBpHWyk)**  
  *CrashCourse* https://youtu.be/oZCskBpHWyk

- **[Bayes theorem, and making probability intuitive](https://youtu.be/HZGCoVF3YvM)**  
  *3Blue1Brown* https://youtu.be/HZGCoVF3YvM

- **[The quick proof of Bayes' theorem](https://youtu.be/U_85TaXbeIo)**  
  *3Blue1Brown* https://youtu.be/U_85TaXbeIo
