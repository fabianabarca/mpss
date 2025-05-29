### Presentación

[7 - Funciones que dan momentos](https://www.overleaf.com/read/cgwskrxfpkps#713512)

### Secciones
- Ejemplo de determinación de la función característica VIII-XII (18 - 24)

# Ejemplo de determinación de la función característica

!!! note "Definición del problema"
    Se define una variable aleatoria discreta \( Y \) con la función de densidad:

$$
\begin{aligned}
f_Y(y) = & P\{ X \leq x_1 \} \delta(y - 1) + P\{ x_1 < X \leq x_2 \} \delta(y - 2) \\
         & + P\{ x_2 < X \leq x_3 \} \delta(y - 3) + P\{ x_3 < X < \infty \} \delta(y - 4)
\end{aligned}
$$

donde \( X \) es una variable aleatoria gaussiana de media 50 y desviación estándar \( \sigma = 10 \),  
con \( x_1 = 25 \); \( x_2 = 40 \) y \( x_3 = 60 \).


## Parte 1: Graficar \( f_Y(y) \)

Primero se normaliza:

$$
Z = \frac{X - 50}{10}
$$

![Distribución normal estandarizada](images/f_gauss_norm.svg)

Cálculo de probabilidades:

- \( P(X \leq 25) = F_Z(-2.5) = 0.0062 \)
- \( P(25 < X \leq 40) = F_Z(-1.0) - F_Z(-2.5) = 0.1525 \)
- \( P(40 < X \leq 60) = F_Z(1.0) - F_Z(-1.0) = 0.6826 \)
- \( P(60 < X) = 1 - F_Z(1.0) = 0.1587 \)

Verificación:  
\( 0.0062 + 0.1525 + 0.6826 + 0.1587 = 1 \)

Entonces:

$$
\begin{aligned}
f_Y(y) = & 0.0062 \, \delta(y-1) + 0.1525 \, \delta(y-2) \\
         & + 0.6826 \, \delta(y-3) + 0.1587 \, \delta(y-4)
\end{aligned}
$$

![Función de densidad discreta (PMF)](images/Captura.png)

## Parte 2: Calcular la función característica de \( Y \)

Por definición:

$$
\Phi_Y(\omega) = E[e^{j \omega Y}] = \int_{-\infty}^{\infty} f_Y(y) e^{j \omega y} \, dy
$$

Sustituyendo \( f_Y(y) \):

$$
\begin{aligned}
\Phi_Y(\omega) = & \int_{-\infty}^{\infty} [ 0.0062 \delta(y-1) + 0.1525 \delta(y-2) \\
                  & + 0.6826 \delta(y-3) + 0.1587 \delta(y-4) ] e^{j \omega y} \, dy
\end{aligned}
$$

### Nota sobre la delta de Dirac:

$$
\int_{-\infty}^{\infty} \delta(x - a) f(x) dx = f(a)
$$

Aplicando:

$$
\Phi_Y(\omega) = 0.0062 e^{j \omega} + 0.1525 e^{j 2\omega} + 0.6826 e^{j 3\omega} + 0.1587 e^{j 4\omega}
$$
