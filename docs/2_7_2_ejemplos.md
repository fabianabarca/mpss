  ---
:material-pencil-box: **EJEMPLO**

!!! example "Ejemplo para un $f_X(x)$ triangular"
    Para el siguiente pdf $f_X(x)$ triangular, determine la función característica, $\Phi_X(\omega)$, y la función generadora de momentos, $M_X(\nu)$, y a partir de ahí determine el primer momento ordinario (la media) y el segundo momento central (la varianza).
    
    | Gráfica | Expresión |
    | ------ | :----------: |
    |![PDF fx(x) Triangular](images/7_pdf_triangular.svg) | <br> <br> <br> <br> <br> <br>\( f_X(x) = \begin{cases} x & 0 \leq x < 1 \\ 2 - x & 1 \leq x < 2 \\ 0 & \text{el resto} \end{cases} \)|



**Pasos de la solución:**

**Función característica:**

\begin{equation}
 \begin{aligned}
    \Phi_X(\omega) &= E[e^{j\omega x}] \\
    &= \int_0^1 x\,e^{j\omega x}\,dx + \int_1^2 (2 - x)\,e^{j\omega x}\,dx \\
    &= e^{j\omega} \left[\frac{\sin(\omega/2)}{\omega/2}\right]^2
\end{aligned}
\end{equation}


**Función generadora de momentos:**

\begin{equation}
 \begin{aligned}
    M_X(s) &= E[e^{sx}] \\
    &= \int_0^1 x\,e^{sx}\,dx + \int_1^2 (2 - x)\,e^{sx}\,dx \\
    &= \frac{(e^s - 1)^2}{s^2}
\end{aligned}    
\end{equation}

**Primer momento ordinario usando la definición:**  

\begin{equation}
\begin{aligned}
    m_1 &= E[X] \\
    &= \int_{-\infty}^{\infty} x\,f_X(x)\,dx \\
    &= \int_0^1 xx\,dx + \int_1^2 x(2-x)\,dx \\
    &= \frac{x^3}{3} \bigg\rvert_0^1 + x^2 \bigg\rvert_1^2 - \frac{x^3}{3} \bigg\rvert_1^2 \\
    &= 1 \text{ (Tiene sentido por la simetría)}
\end{aligned}
\end{equation}

 **Segundo momento central usando la definición:**  

\begin{equation}
\begin{aligned}
    \sigma_X^2 &= E\left[ (X - \overline{X})^2 \right] \\
    &= E[X^2] - (E[X])^2 \\
    &= \int_{0}^{1} x^2\,x\,\mathrm{d}x + \int_{1}^{2} x^2\,(2-x)\,\mathrm{d}x - 1\ \\
    &= \frac{x^4}{4} \bigg\rvert_0^1 + \frac{2x^3}{3} \bigg\rvert_1^2 - \frac{x^4}{4} \bigg\rvert_1^2 - 1 \\
    &= \frac{1}{6}
\end{aligned}
\end{equation}


**Primer momento ordinario usando la MGF:**  

\begin{equation}
\begin{aligned}
    m_1 &= \frac{d}{ds}\left[\left(\frac{e^s-1}{s}\right)^2\right] \bigg\rvert_{s=0} \\
    &= 2 \left(\frac{e^s-1}{s}\right)\left(\frac{se^s-e^s+1}{s^2}\right) \bigg\rvert_{s=0} \\
    &= 2\,(1)\,(1/2)\ \\
    &= 1
\end{aligned}
\end{equation}

*Corresponde con el resultado anterior*

**Segundo momento central usando la MGF:**
  
\begin{equation}
\begin{aligned}
    \sigma_X^2 &= E\left[ (X - \overline{X})^2 \right] = E[X^2] - (E[X])^2 \\
    E[X^2] = \frac{d^2}{ds^2}\,M_X(s)\Bigg\rvert_{s=0} &= \frac{d^2}{ds^2}\left( 1 + \frac{s}{2!} + \frac{s^2}{3!} + \cdots + \frac{s^{n-1}}{n!} + \cdots \right)\Bigg\rvert_{s=0} \\
    &= \frac{d^2}{ds^2}\left( 1 + \cdots + \frac{s^2}{4} + \frac{2s^2}{6} + \cdots \right)\Bigg\rvert_{s=0} \\
    &= \frac{d^2}{ds^2}\left( 1 + \cdots + \frac{7s^2}{12} + \cdots \right)\Bigg\rvert_{s=0} = \frac{7}{6} \\ 
    \sigma_X^2 &= E[X^2] - (E[X])^2 = \frac{7}{6} - 1 = \frac{1}{6}
\end{aligned}
\end{equation}

*Corresponde con el resultado anterior*


!!! note ""
    En resumen: 

    **Función característica:**

    $$
    \Phi_X(\omega) = e^{j\omega} \left[\frac{\sin(\omega/2)}{\omega/2}\right]^2
    $$

    **Función generadora de momentos:**

    $$
    M_X(s) = \frac{(e^s - 1)^2}{s^2}
    $$

    **Primer momento ordinario usando la definición:**  

    $$
    m_1 = 1\quad
    $$

    **Segundo momento central usando la definición:**  

    $$
    \sigma_X^2 = \frac{1}{6}
    $$

    **Primer momento ordinario usando la MGF:**  

    $$
    m_1 = 1
    $$

    **Segundo momento central usando la MGF:**
    
    $$
    \sigma_X^2 = \frac{1}{6}
    $$



## Unicidad de las funciones que dan momentos

La **MGF** (*Moment Generating Function*, función generadora de momentos) y la **CF** (*Characteristic Function*, función característica) son únicas para cada distribución y representan **una descripción completa de la variable aleatoria**, tanto como lo son la **CDF** (*Cumulative Distribution Function*, función de distribución acumulativa) y la **PDF** (*Probability Density Function*, función de densidad probabilística).

|         | Uniforme           | Exponencial        | Rayleigh           | 
|:--------|:------------------:|:------------------:|:------------------:|
| **PDF** | \(\frac{1}{b-a}\)  | \(\lambda e^{-\lambda x}\)| \(\frac{x}{\sigma^2} e^{-x^2/(2\sigma^2)}\) |
| <br> **MGF** | \(\left\{ \begin{array}{ll} \frac{e^{\nu b} - e^{\nu a}}{\nu (b-a)} & \text{para } \nu \neq 0 \\[1mm] 1 & \text{para } \nu = 0 \end{array} \right.\) | <br> \(\frac{\lambda}{\lambda - \nu}, \quad \nu < \lambda\) | <br> \(1 + \sigma \nu e^{\sigma^2 \nu^2 / 2} \ldots\) |
| <br> **CF**  | \(\left\{ \begin{array}{ll} \frac{e^{j \omega b} - e^{j \omega a}}{j \omega (b-a)} & \text{para } \omega \neq 0 \\[1mm] 1 & \text{para } \omega = 0 \end{array} \right.\) | <br> \(\frac{\lambda}{\lambda - j \omega}\) | <br> \(1 - \sigma \omega e^{-\sigma^2 \omega^2 / 2} \ldots\) |
