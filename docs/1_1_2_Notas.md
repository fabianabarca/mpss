## Definición axiomática según Kolgomorov II
### Defición y axiomas de la probabilidad

**Tercer axioma:**

  La probabilidad de la unión de eventos mutuamente excluyentes es igual a suma de la probabilidad de los eventos individuales

  
\begin{equation}
P\left( \bigcup_{n=1}^{N} A_{n}\right) = \sum_{n=1}^{N} P(A_{n})
\tag{5}
\label{E:terceraxioma}
\end{equation}

  En el caso especial para dos eventos, \( A \cap B = \emptyset \):

$$
P\left(A \cup B\right) = P(A) + P(B)
$$
  
  Un posible mnemónico es *PUSuP* (**P**robabilidad de la **U**nión es la **S**uma de las **P**robabilidades)


## Nota sobre los valores de la probabilidad
### Fuente común de errores a partir de la definición axiomática


\begin{equation}
\textit{primer axioma} \longrightarrow 0 \leq P(\cdot) \leq 1 \longleftarrow \textit{segundo axioma}
\end{equation}


- La medida de la probabilidad es mayor a cero
- La medida de la probabilidad es menor a uno

\begin{equation}
\boxed{P(A) = 0.42} \qquad \cancel{P(A) = - 0.42} \qquad \cancel{P(A) = 1.42}
\end{equation}


## Nota sobre álgebra de conjuntos y aritmética
### Fuente común de errores 


El tercer axioma es la unión de operaciones de álgebra de conjuntos y operaciones aritméticas:

\begin{equation}
P\left( \bigcup_{n=1}^{N} A_{n}\right) = \sum_{n=1}^{N} P(A_{n})
\end{equation}


- Los **eventos** tienen operaciones de **álgebra de conjuntos** pero no aritméticas (suma, resta, multiplicación, división).
- Las **probabilidades** son números (\(0 < P(\cdot) < 1\)) con **operaciones aritméticas**, pero no operaciones de unión, intersección, complemento.

\begin{equation}
\begin{matrix}
    \cancel{\overline{P(A)}} && \boxed{P(A) + P(B)} && \cancel{P(A + B)}  \\
    \boxed{P(\overline{A})} && \cancel{P(A) \cup P(B)} && \boxed{P(A \cup B)}  
\end{matrix}
\end{equation}

:material-pencil-box:
**EJEMPLO**

!!! example "Ejemplo del lanzamiento de dos dados" 


Observar la suma de dos dados que se lanzan

\[
\begin{array}{cccccc}
(1,1) & (1,2) & (1,3) & (1,4) & (1,5) & (1,6) \\
(2,1) & (2,2) & (2,3) & (2,4) & (2,5) & (2,6) \\
(3,1) & (3,2) & (3,3) & (3,4) & (3,5) & (3,6) \\
(4,1) & (4,2) & (4,3) & (4,4) & (4,5) & (4,6) \\
(5,1) & (5,2) & (5,3) & (5,4) & (5,5) & (5,6) \\
(6,1) & (6,2) & (6,3) & (6,4) & (6,5) & (6,6)
\end{array}
=
\begin{array}{cccccc}
2 & 3 & 4 & 5 & 6 & 7 \\
3 & 4 & 5 & 6 & 7 & 8 \\
4 & 5 & 6 & 7 & 8 & 9 \\
5 & 6 & 7 & 8 & 9 & 10 \\
6 & 7 & 8 & 9 & 10 & 11 \\
7 & 8 & 9 & 10 & 11 & 12
\end{array}
\]


¿Cuál es la probabilidad de estos eventos?

\[
\begin{aligned}
A &= \lbrace \text{suma} = 7 \rbrace \\
B &= \lbrace 8 < \text{suma} \leq 11 \rbrace \\
C &= \lbrace 10 < \text{suma} \rbrace
\end{aligned}
\]

Asumiendo que $(P(A_{ij}) = 1/36)$ y dado que los eventos $(A_{ij})$, $(i,j = 1, 2, \ldots, N = 6)$, son mutuamente excluyentes, estos deben satisfacer el tercer axioma.

\[
\begin{aligned}
P(A) &= P\left( \bigcup_{i = 1}^{6}A_{i,7-i} \right) = \sum_{i=1}^{6}P(A_{i,7-i}) \\ 
	&= 6\left( \frac{1}{36}\right) = \frac{1}{6}
\end{aligned}
\]

donde 6 es el número de elementos que satisfacen $\bigcup_{i = 1}^{6}A_{i,7-i}$ (observable en la tabla anterior) y 36 es el número de eventos posibles ($n(S)$, la cardinalidad del conjunto universal).


Con $(B)$, hay 9 elementos que satisfacen el requisito $(B = \lbrace 8 < \text{suma} \leq 11 \rbrace)$

\[
\begin{aligned}
P(B) &= P\left\lbrace \left( \bigcup_{i = 3}^{6}A_{i,9-i} \right) \cup \left( \bigcup_{i = 4}^{6}A_{i,10-i} \right) \right. \\ 
& \qquad \left. \cup \left( \bigcup_{i = 5}^{6}A_{i,11-i} \right) \right\rbrace \\
&= 9\left( \frac{1}{36}\right) = \frac{1}{4}
\end{aligned}
\]


En $(C)$ es fácil observar que hay solo 3 resultados elementales coincidentes, por lo que:

\[
\begin{aligned}
P(C) &= 3\left( \frac{1}{36}\right) = \frac{1}{12}
\end{aligned}
\]

Adicionalmente,

\[
\begin{aligned}
P(B \cap C) &= 2\left( \frac{1}{36} \right) = \frac{1}{18} \\
P(B \cup C) &= \frac{10}{36} = \frac{5}{18}
\end{aligned}
\]

considerando que

\[
A = \lbrace \text{suma} = 7 \rbrace \qquad
B = \lbrace 8 < \text{suma} \leq 11 \rbrace \qquad
C = \lbrace 10 < \text{suma} \rbrace
\]

!!! note 

    Respuesta: La probabilidad de estos eventos es 5/18


## Consecuencias lógicas de la definición axiomática 
### Definición axiomática según Kolmogorov
 

Las siguientes conclusiones se siguen de los axiomas expuestos:

**1.** Dado que $( A \cup \overline{A} = S )$, usando el segundo axioma:

   
$$
P(A \cup \overline{A}) = P(S) = 1
$$
   

   pero $( A \cap \overline{A} = \emptyset )$, y utilizando el tercer axioma:

   
$$
\begin{aligned}
P(A \cup \overline{A}) &= P(A) + P(\overline{A}) = 1 \\
&\Rightarrow \boxed{P(\overline{A}) = 1 - P(A)}
\end{aligned}
$$

**2.** De forma similar, para cualquier \( A \), con \( A \cap \emptyset = \emptyset \), entonces:

   
   
$$
P(A \cup \emptyset) = P(A) + P(\emptyset)
$$


pero \( A \cup \emptyset = A \), y así debe cumplirse que: $\boxed{P(\emptyset) = 0}$


**3.** Si $A$ y $B$ no son mutuamente exclusivos, ¿cuál es la probabilidad $P(A \cup B)$?  
  Para resolverlo, se debe volver a expresar esa unión en términos de **conjuntos ME** (mutuamente excluyentes), de forma que se pueda utilizar el tercer axioma de la probabilidad.

\[
A \cup B = A \cup \overline{A}B \quad \text{ donde } \quad A \cap \overline{A}B = \emptyset
\tag{6}
\label{E:separacion}
\]


Utilizando el tercer axioma se tiene que

\[
P(A \cup B) = P(A \cup \overline{A}B) = P(A) + P(\overline{A}B)
\tag{7}
\label{E:ap3ax}
\]

pero también

\[
B = S \cap B = (A \cup \overline{A}) \cap B = AB \cup \overline{A}B
\tag{8}
\label{E:identidadB}
\]

Si \( AB \) y \(\overline{A}B\) son mutuamente excluyentes (ME), se aplica el tercer axioma \eqref{E:terceraxioma},

\[
\begin{aligned}
P(B) & = P(AB) + P(\overline{A}B) \\
P(\overline{A} B) & = P(B) - P(A B)
\end{aligned}
\]

y sustituyendo en (\ref{E:ap3ax}) entonces

\[
\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}
\]

---

![Unión de los conjuntos A y B](images/0_union_conjuntos.svg)


## Identidades útiles de la probabilidad


\[
P(\overline{A}) = 1 - P(A)
\]

\[
P(\emptyset) = 0
\]

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

:material-pencil-box:
**EJEMPLO**

!!! example "Ejemplo del lanzamiento de una moneda"

##Definición axiomática según Kolmogorov


Tirar una moneda "justa" indefinidamente y definir el evento \( A \) como

\[
A = \lbrace \text{escudo aparece, $\textit{eventualmente}$} \rbrace
\]

¿Cuál es \( P(A) \)?

La intuición dice que \( A \) es un evento con \( P(A) = 1 \). Sea

\[
\begin{aligned}
A_n &= \lbrace \text{escudo aparece por primera vez} \\ 
& \qquad \text{en el $n$-ésimo tiro} \rbrace \\
&= \lbrace ( \underbrace{C,C,C,\ldots,C}_{n-1},E ) \rbrace
\end{aligned}
\]


Si \(A_i \cap A_j = \emptyset\) para \(1\leq i,j \leq n\) (porque cada uno es una secuencia distinta, única):

\[
\begin{matrix}
A_1 && E \\[1mm]
A_2 && C & E \\
A_3 && C & C & E \\
A_4 && C & C & C & E \\
A_5 && C & C & C & C & E \\
\vdots \\
\end{matrix}
\]

se tiene entonces

\[
A = A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_i \cup \cdots = \bigcup_{n=1}^{\infty} A_i
\]

es decir: "en alguno pega", eventualmente.

!!!note ""
