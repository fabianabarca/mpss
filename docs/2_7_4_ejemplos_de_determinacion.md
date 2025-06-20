### Presentación

[7 - Funciones que dan momentos](https://www.overleaf.com/read/cgwskrxfpkps#713512)

### Secciones
- Ejemplo de determinación de la función característica VIII-XII (18 - 24)

<<<<<<< HEAD
=======
\[
m_n = (-j)^n \frac{d^n}{d\omega^n} \Phi_Y(\omega)\bigg|_{\omega=0}
\]

---

## Ejemplo de determinación de la función característica IX

\[
m_2 = (-j)^2 \frac{d^2}{d\omega^2} \Phi_Y(\omega) \Big|_{\omega=0}
\]

\[
= -1 \cdot \frac{d^2}{d\omega^2} \left[
0.0062\,e^{j\omega1} + 0.1525\,e^{j\omega2} + 0.6826\,e^{j\omega3} + 0.1587\,e^{j\omega4}
\right] \Bigg|_{\omega=0}
\]

\[
= -1 \left[
(-0.0062)\,e^{j\omega1} + (-0.6100)\,e^{j\omega2} + (-6.1434)\,e^{j\omega3} + (-2.5392)\,e^{j\omega4}
\right]_{\omega=0}
\]

\[
m_2 = 9.2988
\]

---

## Ejemplo de determinación de la función característica X

**Confirmación con la definición directa:**

\[
E(Y^2) = \int_{-\infty}^{+\infty} y^2 f_Y(y)\,dy
\]

\[
= \int_{-\infty}^{+\infty} y^2 \left[
0.0062\,\delta(y - 1) +
0.1525\,\delta(y - 2) +
0.6826\,\delta(y - 3) +
0.1587\,\delta(y - 4)
\right] dy
\]

\[
= 0.0062 \cdot 1^2 +
0.1525 \cdot 2^2 +
0.6826 \cdot 3^2 +
0.1587 \cdot 4^2
\]

\[
= 0.0062 \cdot 1 +
0.1525 \cdot 4 +
0.6826 \cdot 9 +
0.1587 \cdot 16
\]

\[
E(Y^2) = 9.2988
\]

Resultado coincide con el obtenido por derivación de la función característica..

---

## Ejemplo de determinación de la función característica XI

**Cálculo de la media \( E[Y] \):**

\[
E[Y] = \int_{-\infty}^{+\infty} y f_Y(y)\,dy
\]

\[
= 0.0062 \cdot 1 + 0.1525 \cdot 2 + 0.6826 \cdot 3 + 0.1587 \cdot 4
\]

\[
E[Y] = 0.0062 + 0.3050 + 2.0478 + 0.6348 = 2.9938
\]

---

## Ejemplo de determinación de la función característica XII

El resultado \( E[Y] = 2.9938 \) tiene sentido porque es muy cercano a 3, donde está concentrada la mayor probabilidad según \( f_Y(y) \).

Entonces la **varianza** es:

\[
\sigma_Y^2 = E[Y^2] - (E[Y])^2 = 9.2988 - (2.9938)^2 = 0.3360
\]

Y la **desviación estándar**:

\[
\sigma_Y = \sqrt{0.3360} = 0.5796
\]

Esto indica una **dispersión baja**, lo cual concuerda con la fuerte concentración de valores alrededor de 3.
>>>>>>> 69a5172 (Transcripción de función característica)
