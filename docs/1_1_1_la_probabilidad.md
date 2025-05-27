### ¿Qué es y para qué sirve la probabilidad?

> **La probabilidad es una *medida* de la certidumbre de ocurrencia de un evento.**

- Permite tomar decisiones en un Universo fundamentalmente incierto.
- Es útil para tratar de:
  - **adivinar el futuro**
  - **adivinar el pasado**
- No es posible saber lo que va a pasar, pero podemos **modelar y cuantificar** lo que podemos esperar, con base en lo que ya ha sucedido.

!(![alt text](images/4_covid_acumulado.svg))


---

### ¿Qué hace *aleatorio* a un fenómeno aleatorio? *(Nota al margen)*

Puede ser la física (a partir del principio de incertidumbre), o por ser un **sistema caótico** (extremadamente sensible a las condiciones iniciales), o por el **conocimiento imperfecto** del observador (el fenómeno podría ser predecible desde algún punto de vista, pero el observador no lo sabe).

---

## Aplicaciones de la probabilidad

---

### ¿Qué aplicaciones tiene la teoría de probabilidad?

- 🛈 Teoría de la información  
- 📶 Comunicaciones  
- 🧾 Reconocimiento de patrones  
- ⚙️ Producción industrial  
- 📈 Finanzas  
- 🏛 Política pública  
- 📚 Aprendizaje automático  
- ☁️ Meteorología  
- 🚑 Epidemias  
- 🔍 (...)

---

## Los conceptos de la probabilidad

---

### Definición clásica de Laplace

La probabilidad de un evento $A$ se define *a priori* (sin experimentación) como:

$$
\begin{aligned}
P(A) & = \frac{\text{Número de resultados favorables a }A}{\text{Número total de resultados posibles}} \\
     & = \frac{\lvert A \rvert}{\lvert S \rvert} = \frac{n(A)}{n(S)}
\end{aligned}
$$

En el caso de que todos los resultados (o *salidas*) son igualmente probables.

> **El operador $P(\cdot)$**  
> El operador $P(\cdot)$ es una *medida* de la certeza de la ocurrencia del evento $\cdot$ descrito.

---

### Ejemplo de la caja con bolas blancas y rojas I

 
> Considerar una caja con $n$ bolas blancas y $m$ bolas rojas. En este caso, hay dos resultados elementales: una bola blanca o una bola roja. ¿Cuál es la probabilidad de seleccionar una bola blanca?

$$
P(\text{seleccionar una bola blanca}) = \frac{n}{n+m}
$$

---

### Ejemplo de la divisibilidad por un número primo I

 
> Determine la probabilidad de que un número natural cualquiera es divisible por un número primo $n$.

- Si $n$ es un número primo, entonces cada $n$-ésimo número (empezando por $n$) es divisible por $n$.
- Por lo tanto, en $n$ enteros consecutivos hay un resultado favorable, y por tanto:

$$
P(\text{un número es divisible por un primo } n) = \frac{1}{n}
$$



### Deficiencias de la definición clásica de Laplace

$$
P(A) = \frac{\text{Número de resultados favorables a }A}{\text{Número total de resultados posibles}}
$$

- La probabilidad es utilizada para definir la probabilidad (referencia cíclica).
- No puede ser utilizado para situaciones donde los resultados no son igualmente probables.
- No puede ser utilizado para un número infinito de resultados posibles.

---

### Definición estadística de la probabilidad

> **Frecuencia relativa:**  
> Un experimento aleatorio se realiza muchas veces, entonces la probabilidad de un evento $A$ se define como:

> $$
> P(A) = \lim_{n \to \infty} \frac{n(A)}{n}
> $$

> Donde $n(A)$ es el número de ocurrencias de $A$ y $n$ es el número total de "experimentos" o "pruebas".

Este es un método común para determinación experimental de probabilidades.

---

### Otras probabilidades por frecuencia relativa I

#### Personas con obesidad

$$
\begin{aligned}
P(\text{ser obeso}) &= \frac{\text{Personas con obesidad}}{\text{Población mundial}} \\
&= \frac{725~039~900}{7~687~217~424} \approx 9.43\%
\end{aligned}
$$

#### Muertes por fumado

$$
\begin{aligned}
P(\text{morir por fumar}) &= \frac{\text{Muertes por fumado}}{\text{Muertes este año}} \\
&= \frac{805~310}{9~514~900} \approx 8.46\%
\end{aligned}
$$

> **¿Es correcto decir que tengo un 9.43% de probabilidades de ser obeso y 8.46% de morir por fumar?**

*Datos de http://www.worldometers.info/es/*

---

### Ejemplo de la divisibilidad por un número primo I


> Determine la probabilidad de que un número natural cualquiera sea divisible por un número primo *n*.

- Entre los enteros \( 1, 2, \dots, m \), los números \( n, 2n, \dots \) son divisibles por \( n \).
- Por lo tanto, hay \( \left\lfloor \frac{m}{n} \right\rfloor \) números divisibles por \( n \) entre 1 y \( m \). Entonces:

\[
P(\text{un número es divisible por un primo } n) =
\lim_{m \to \infty} \frac{ \left\lfloor \frac{m}{n} \right\rfloor }{m} = \frac{1}{n}
\]

---

En el caso anterior se resolvió “analíticamente”, en este caso “probando” todos los números.

---

### Deficiencias de la definición estadística de la probabilidad

$$
P(A) = \lim_{n\to\infty} \frac{n(A)}{n}
$$

- No se pueden realizar infinitos experimentos.
- No puede ser utilizado para un número infinito de resultados posibles.
- Asume eventos equiprobables.

---

### Definición axiomática según Kolmogorov I

> **Axioma:**  
> Proposición o enunciado tan evidente que no requiere demostración.

**Primer axioma:**

$$
P(A) \geq 0
$$

La "medida" asignada a un evento que denota su probabilidad es no negativa.

---

**Segundo axioma:**

$$
P(S) = 1
$$

La probabilidad de ocurrencia de un resultado que pertenece al conjunto universal es segura.

---

**Tercer axioma:**

$$
P\left( \bigcup_{n=1}^{N} A_n \right) = \sum_{n=1}^{N} P(A_n)
$$

En el caso especial para dos eventos, $A \cap B = \emptyset$:

$$
P(A \cup B) = P(A) + P(B)
$$

Un posible mnemónico es **PUSuP** (**P**robabilidad de la **U**nión es la **Su**ma de las **P**robabilidades)
