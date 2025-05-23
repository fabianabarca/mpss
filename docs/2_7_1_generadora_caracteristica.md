###
# Funciones que dan momentos

!!! Introducción
    A partir de una nueva función es posible generalizar la obtención de los momentos ordinarios de una variable aleatoria. Esta función es única para cada va.

    Hay dos tipos de estas funciones: la función generadora de momentos (MGF) y la función característica (CF), que se obtienen con la ayuda de dos personajes conocidos...

# Función generadora de momentos, $M_{X}(\nu)$
!!! tip "Función generadora de momentos de una **va** $X$"
    Está definida por:

    \begin{equation}
    \begin{aligned}
    M_{X}(\nu) 	& = E\left[ e^{\nu X}\right] \\
                    & = \int_{-\infty}^{\infty}f_{X}(x) e^{\nu x} ~\mathrm{d} x
    \end{aligned}
    \end{equation}

    donde $\nu$ es un número real con $-\infty < \nu < \infty$. Si se sustituye $\nu$ por $s$ entonces esta función sería la \textbf{transformada de Laplace} con signo cambiado de $s$.

## Relación de los momentos con $M_{X}(\nu)$

El $n$-ésimo momento ordinario de la variable aleatoria $X$ se obtiene a partir de la $n$-ésima derivada de $M_{X}(\nu)$ con respecto a $\nu$, evaluada en $\nu = 0$:

\begin{equation}
m_n = \left. \frac{d^n}{d\nu^n} M_X(\nu) \right|_{\nu = 0}
\label{momentos}
\end{equation}

Para comprender por qué esta es una ``función generadora de momentos'', será posible expander la función $e^{\nu X}$, de la siguiente forma:


\begin{equation}
\begin{aligned}
  M_{X}(\nu) 	& = E\left[ e^{\nu X}\right] \\
          		& = \int_{-\infty}^{\infty} \left[e^{\nu x}\right] f_{X}(x)~\mathrm{d} x \\
                & = \int_{-\infty}^{\infty} \left[ 1 + \frac{\nu x}{1!} + \frac{\nu^2 x^2}{2!} + \frac{\nu^3 x^3}{3!} + \cdots \right] f_{X}(x) ~\mathrm{d} x \\
                & = \int_{-\infty}^{\infty} 1 f_{X}(x) ~\mathrm{d} x + \int_{-\infty}^{\infty} \frac{\nu x}{1!} f_{X}(x) ~\mathrm{d} x \\ &\qquad + \int_{-\infty}^{\infty} \frac{\nu^2 x^2}{2!} f_{X}(x) ~\mathrm{d} x + \int_{-\infty}^{\infty} \frac{\nu^3 x^3}{3!} f_{X}(x) ~\mathrm{d} x + \cdots \\
\end{aligned}
\end{equation}

Y replanteando ahora, en términos del valor esperado,

\begin{equation}
\begin{aligned}
M_X(\nu) & = E\left[1 + \frac{\nu X}{1!} + \frac{\nu^2 X^2}{2!} + \frac{\nu^3 X^3}{3!} + \cdots \right] \\
	& = E\left[1\right] + \frac{\nu }{1!}E\left[X\right] + \frac{\nu^2}{2!}E\left[ X^2\right] + \frac{\nu^3}{3!}E\left[ X^3\right] + \cdots  \\
\end{aligned}
\end{equation}

Es claro que haciendo la $n$-ésima derivada con respecto a $\nu$ y evaluando en $\nu = 0$, se obtiene, por ejemplo,

\begin{equation*}
\begin{aligned}
& \frac{d^2}{d\nu^2}{\left\lbrace 1 + \frac{\nu }{1!}E\left[X\right] + \frac{\nu^2}{2!}E\left[X^2\right] + \frac{\nu^3}{3!}E\left[X^3\right] + \cdots \right\rbrace_{\nu=0}}{\nu} \\
& = \left\lbrace 0 + 0 + E\left[X^2\right] + \nu E\left[ X^3\right] + \cdots \right\rbrace_{\nu=0} = E\left[ X^2\right]
\end{aligned}
\end{equation*}

el segundo momento ordinario.
!!! example "Ejemplo de la varianza para una distribución exponencial"
    !!! note ""
        Sea una variable aleatoria $X$ con una distribución exponencial de parámetro $\lambda$, con $f_X(X) = \lambda e^{- \lambda x}$, y además una función generadora de momentos dada por:

        \begin{equation}
            M_X(\nu) = \frac{\lambda}{\lambda - \nu}
        \end{equation}

        Verifique que la varianza es $\sigma_X^2 = 1/\lambda^2$.
    
    Si $\sigma_X^2 = m_2 - m_1^2$, entonces 

    \begin{equation*}
    \begin{aligned}
    m_1 & = \left. \frac{d}{d\nu}{\frac{\lambda}{\lambda - \nu}}{\nu} \right|_{\nu = 0} \\
        & = \left. \frac{\lambda}{(\lambda - \nu)^2} \right|_{\nu = 0} = \frac{1}{\lambda}
    \end{aligned}
    \end{equation*}

    Y además

    \begin{equation*}
    \begin{aligned}
    m_2 & = \left.\frac{d^2}{d\nu^2}{\frac{\lambda}{\lambda - \nu}}{\nu} \right|_{\nu = 0} \\
        & = \left. \frac{2\lambda}{(\lambda - \nu)^3} \right|_{\nu = 0} = \frac{2}{\lambda^2}
    \end{aligned}
    \end{equation*}

    Por lo que

    \begin{equation*}
    \begin{aligned}
    \sigma_X^2  & = m_2 - m_1^2 \\
                & = \frac{2}{\lambda^2} - \left( \frac{1}{\lambda} \right)^2 = \frac{1}{\lambda^2}
    \end{aligned}
    \end{equation*}

# Función característica, $\Phi_{X}(\omega)$

!!! tip "Función característica de una variable aleatoria $X$"

    Está definida por 

    \begin{equation}
    \Phi_{X}(\omega) = E\left[ e^{j\omega X}\right]
    \end{equation}

    \noindent
    donde $j = \sqrt{-1}$. Esta es una función del número real $-\infty < \omega < \infty$ y es la \textbf{transformada de Fourier} (con el signo de $\omega$ cambiado) de $f_{X}(x)$: 

    \begin{equation}
    \Phi_{X}(\omega) = \int_{-\infty}^{\infty}f_{X}(x)e^{j\omega x} ~\mathrm{d} x
    \label{caracteristica}
    \end{equation}
Este detalle de la función característica permite usar las tablas de la transformada de Fourier así como la teoría respectiva. 

Por otro lado, si $\Phi_{X}(\omega)$ es conocida, $f_{X}(x)$ puede calcularse de la transformada inversa de Fourier (con el signo de $x$ cambiado)

\begin{equation}
  f_{X}(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\Phi_{X}(\omega)e^{-j\omega x} ~\mathrm{d} \omega
\end{equation}

Con la derivación de (\ref{caracteristica}) $n$ veces con respecto a $\omega$ y con $\omega = 0$ en la derivada, el $n$-ésimo momento ordinario de $X$ está dado por

\begin{equation}
\boxed{m_{n} = \left. (-j)^{n} \frac{d}{d\omega}{\Phi_{X}(\omega)}\right|_{\omega = 0}} 
\end{equation}

La magnitud máxima de una función característica es uno y ocurre en $\omega = 0$; es decir, 

\begin{equation}
  | \Phi_{X}(\omega)| \leq \Phi_{X}(0) = 1 
\end{equation}

## Diferencias entre función característica (CF) y función generadora de momentos (MGF)

- La principal desventaja de la función generadora de momentos es que puede no existir para todas las variables aleatorias y todos los valores de $\nu$. No obstante, si $M_{X}(\nu)$ existe para todos los valores de $\nu$ en un vecindario de $\nu = 0$, los momentos están dados por la ecuación (\ref{momentos}).
    
- Una ventaja de usar $\Phi_{X}(\omega)$ para hallar momentos es que $\Phi_{X}(\omega)$ existe siempre, de modo que los momentos pueden encontrarse si $\Phi_{X}(\omega)$ es conocida, siempre que sus momentos y derivadas existan. 

