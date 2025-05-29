### Presentación

[18 - Cadenas de Markov en tiempo contínuo](https://www.overleaf.com/read/wmkypgnzztdn#38decd)

### Secciones
<h1 style="text-align: center;color: #004B87;">El proceso de nacimiento y muerte en tiempo continuo</h1>

---
<h2 style="text-align: right;color: #004B87;">El proceso de nacimiento y muerte en tiempo continuo I</h2>

"Nacimiento" y "muerte" es una analogía  tétrica que puede interpretarse también como "aparición y desaparición" o "llegada y salida"o "llegada" y "salida" o "unión" y "separación" o "haciendo fila y listo el trámite"...

![Llegada y salida de entidades](images/18_llegada_salida.svg){ style="display: block; margin: auto;" }


---
<h2 style="text-align: right;color: #004B87;">El proceso de nacimiento y muerte en tiempo continuo II</h2>


* Considérese una “máquina” que puede estar en cualquiera de varios estados en
cada instante de tiempo $t \geq 0$.
* El conjunto de estados posibles, el espacio de estados S, será siempre discreto:

$$
S = \{0, 1, 2, \ldots, N\} \quad \text{o} \quad S = \{0, 1, 2, \ldots\}
$$

* Al tiempo t, el estado de la máquina es denotado por $X_t$.

!!! note ""
    Por ejemplo, $X_t$ podría denotar el número de animales en una poza para beber.  
    El estado de la máquina es el número $X_t$ de animales al tiempo $t$.

---

<h2 style="text-align: right; color: #004B87;">Suposiciones básicas I</h2>
<h3 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte</h3>

**1.** Si al tiempo $t$ la máquina está en el estado $i$, permanece en ese estado por un  
tiempo aleatorio que es exponencialmente distribuido con parámetro $\Omega_i$.

- El tiempo de espera promedio en el estado $i$ es el recíproco $1 / \Omega_i$  
- $\Omega_i$ depende del estado $i$, pero no depende de otros estados anteriores  
- El estado $i$ pudiera ser **absorbente**: una vez que la máquina entra al estado $i$, permanecerá siempre ahí  
- En este caso, $\Omega_i = 0$ y el tiempo de espera promedio es $1 / \Omega_i \rightarrow \infty$


---
<h2 style="text-align: right; color: #004B87;">Suposiciones básicas II</h2>
<h3 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte</h3>

**2.** Cuando la máquina sale del estado $i$, cambia al estado $i + 1$ o al estado $i - 1$  
(habían 9 vacas, luego hay 8 si se va una, o 10 si llega otra). Sea

$$
\begin{align}
p_i &= P(\{\text{próximo estado es } i + 1 \mid \text{último estado es } i\}) \notag \\
q_i &= 1 - p_i \notag \\
    &= P(\{\text{próximo estado es } i - 1 \mid \text{último estado es } i\}) \tag{7}
\end{align}
$$



Entonces $p_i$ y $q_i$ dependen solamente del estado $i$ y no de otros detalles del proceso  
(tales como el tiempo $t$, la duración en $i$ o el estado antes de $i$).

---
<h2 style="text-align: right; color: #004B87;">Suposiciones básicas III</h2>
<h3 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte</h3>

![Diagrama de transición de estados en el proceso de nacimiento y muerte](images/18_estados_nacimiento_muerte.svg)

El proceso estocástico $\{X_t\}_{t=0}^\infty$ es un registro completo de los estados ocupados por la máquina para todos los tiempos $t \geq 0$.

---
<h2 style="text-align: right; color: #004B87;">Propiedad de la falta de memoria I</h2>
<h3 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte</h3>

Dado el presente estado $X_t$ del sistema al tiempo $t$, los estados futuros de la máquina no  
dependen de los estados pasados.

- En particular, si el estado al tiempo $t$ es $X_t = i$, entonces es completamente  
irrelevante si ha estado en el estado $i$ por varios años o si acaba de cambiar al  
estado $i$, para predecir cuándo se mudará del estado $i$.

---
<h2 style="text-align: right; color: #004B87;">Propiedad de la falta de memoria II</h2>
<h3 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte</h3>

- Dado que la distribución exponencial sigue la propiedad de la falta de memoria,  
  la máquina se comporta como si acabara de moverse al estado $i$ a pesar de qué tan  
  largo hubiera realmente ocupado el estado $i$.

- La distribución exponencial es la única distribución continua concentrada en  
  $[0, \infty[$ para los tiempos de espera que tiene esta propiedad.

Nótese que si $\Omega_i = 0$ para el estado $i$, entonces los valores de $p_i$, $q_i$ son innecesarios de especificar dado que la máquina no puede cambiar del estado $i$ una vez en él.

---
<h2 style="text-align: right; color: #004B87;">Proceso de nacimiento y muerte en tiempo continuo</h2>
<h3 style="text-align: right; color: #004B87;">Síntesis</h3>

Consiste de una máquina que puede cambiar entre estados en un espacio de estados $S$.

- $X_t$ denota el estado ocupado al tiempo $t$ para $t \geq 0$.

- La máquina permanece en el estado $i$ por un período de tiempo indeterminado  
  (llamado tiempo de espera o permanencia) que es exponencialmente distribuido  
  con parámetro $\Omega_i$ (tiempo de espera promedio $1 / \Omega_i$).

- Cuando la máquina cambia, cambia a los estados $i + 1$, $i - 1$ con probabilidades  
  respectivas $p_i$, $q_i = 1 - p_i$.