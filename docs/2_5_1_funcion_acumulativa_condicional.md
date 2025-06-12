

# Función acumulativa condicional I

Sea \( A \) el evento \( \{X \leq x\} \) de la variable aleatoria \( X \). La probabilidad \( P(X \leq x \mid B) \) se define como la *función acumulativa condicional* de \( X \), que se denota \( F_X(x \mid B) \),

\[
P(A \mid B) = P(X \leq x \mid B) \triangleq F_X(x \mid B) \tag{1}
\]

\[
F_X(x \mid B) = \frac{P\left[(X \leq x) \cap B\right]}{P(B)} = \frac{P(A \cap B)}{P(B)} = P(A \mid B) \tag{2}
\]

Aplicable a variables aleatorias discretas, continuas o mixtas.



---

# Función acumulativa condicional II

El evento conjunto \( \{X \leq x\} \cap B \) consiste de los resultados \( s \) tales que \( X(s) \leq x \) y \( s \in B \).

![Mapeo evento conjunto](images/5_mapeo_evento_conjunto.svg)




\[
\{s : X(s) \leq x \land s \in B\} = \{s_1, s_2, s_3\}
\]




---

# Propiedades de la función acumulativa condicional

Todas las propiedades de las funciones acumulativas ordinarias se aplican a \( F_X(x \mid B) \):

1️⃣ Similar a \( P(\emptyset) = 0 \):  
  \( F_X(-\infty \mid B) = 0 \)

2️⃣ Similar a \( P(S) = 1 \):  
  \( F_X(\infty \mid B) = 1 \)

3️⃣ Es una probabilidad:  
  \( 0 \leq F_X(x \mid B) \leq 1 \)

4️⃣ Es no decreciente:  
  \( F_X(x_1 \mid B) \leq F_X(x_2 \mid B) \) si \( x_1 < x_2 \)

5️⃣ Probabilidad de un segmento:  
\[
P\{x_1 < X \leq x_2 \mid B\} = F_X(x_2 \mid B) - F_X(x_1 \mid B)
\]

6️⃣ Continuidad por la derecha:  
  \( F_X(x^+ \mid B) = F_X(x \mid B) \)

---

# Ejemplo de un evento \( B \) discreto I

Si solo existen los resultados elementales \( B = \{b_1, b_2, b_3\} \) entonces puede existir una función acumulativa \( F_X(x \mid B) \) con tres parámetros distintos, a saber
![Mapeo evento conjunto](images/5_funcs_acum_condicionales.svg)


---

# Ejemplo de tres lanzamientos de monedas I

> Considere el experimento de tres lanzamientos de moneda (o el lanzamiento de tres monedas, que es equivalente porque son eventos independientes). Sea la *va* \( X \) “el número total de coronas” y sea el evento \( B = \{\text{más coronas que escudos}\} \).  
> Determine y esboce \( F_X(x \mid B) \).

El lanzamiento de monedas tiene ocho resultados distintos \( (2^3) \). El evento \( B \) es:

\[
B = \{\text{CCC, CCE, CEC, ECC}\}
\]

con \( P(B) = \frac{1}{2} \)



---

# Ejemplo de tres lanzamientos de monedas II

Considere el evento conjunto \( \{X \leq x\} \cap B \) y la definición

\[
F_X(x \mid B) = \frac{P(\{X \leq x\} \cap B)}{P(B)}
\]

Si \( X \) es “el número total de coronas” y \( B = \{\text{más coronas que escudos}\} \), entonces:

| \( x \) | \( \{X \leq x\} \cap B \)                            | \( P(\{X \leq x\} \cap B) \) | \( F_{X \mid B} \) |
|--------|------------------------------------------------------|------------------------------|--------------------|
| 0      | \( \{\text{EEE}\} \cap B = \emptyset \)              | 0                            | 0                  |
| 1      | \( \{\text{CEE, ECE, EEC, EEE}\} \cap B = \emptyset \) | 0                            | 0                  |
| 2      | \( \{\text{CCE, CEC, ECC}\} \)                        | 3/8                          | 3/4                |
| 3      | \( \{\text{CCC, CCE, CEC, ECC}\} = B \)               | 4/8                          | 1                  |

---

# Ejemplo de tres lanzamientos de monedas III
![Mapeo evento conjunto](images/5_espacio_eventos_moneda.svg)


> **Figura:** Espacio de eventos del experimento de tres lanzamientos de moneda, junto con los eventos \( X \), “el número total de coronas” y \( B = \{\text{más coronas que escudos}\} \), es decir,  
> \( B = \{\text{CCC, CCE, CEC, ECC}\} \)



---

# Ejemplo de tres lanzamientos de monedas IV

Entonces,

\[
F_X(x \mid B) =
\begin{cases}
0 & x < 2 \\
3/4 & 2 \leq x < 3 \\
1 & 3 \leq x
\end{cases}
\]

mientras que,

\[
F_X(x) =
\begin{cases}
0 & x < 0 \\
1/8 & 0 \leq x < 1 \\
1/2 & 1 \leq x < 2 \\
7/8 & 2 \leq x < 3 \\
1 & 3 \leq x
\end{cases}
\]


---

# Ejemplo de tres lanzamientos de monedas V
![Mapeo evento conjunto](images/5_func_acum_monedas.svg)


> \( X \) es “el número total de coronas” y \( B = \{\text{más coronas que escudos}\} \)



