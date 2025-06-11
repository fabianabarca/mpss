!!! note "Introducción"

    La función de densidad de probabilidad describe cómo se distribuye la probabilidad a lo largo de la recta real. Es la base para numerosos cálculos numéricos en el análisis probabilístico.

# Función de densidad de probabilidad \( f_X(x) \)


## Función de densidad continua

!!! important "Definición"

    La función de densidad \( f_X(x) \) es la derivada de la función de distribución acumulativa:


    $$
    f_X(x) = \frac{\mathrm{d}F_X(x)}{\mathrm{d}x}
    $$

    También se le llama **PDF** (*Probability Density Function*).

### Visualización

![Función acumulativa Rayleigh](images/f_cdf_rayleigh.svg)  
![Función de densidad Rayleigh](images/f_pdf_rayleigh.svg)

## Función de densidad discreta

!!! important "Definición"

    Para una variable discreta:

    $$
    \begin{aligned}
    f_X(x) &= \frac{\mathrm{d}}{\mathrm{d}x} \sum_{i=1}^{N}P(x_i)u(x - x_i) \\\\
    f_X(x) &= \sum_{i=1}^{N}P(x_i)\delta(x - x_i)
    \end{aligned}
    $$

    También se le llama **PMF** (*Probability Mass Function*).

### Visualización

![Función acumulativa discreta](images/f_cdf_discreta.svg)  
![PMF discreta](images/f_pmf_discreta.svg)

## Propiedades de \( f_X(x) \)


!!! tip "Propiedades básicas"

    1. \( f_X(x) \geq 0 \) para todo \( x \)
   
    2. Área total unitaria:
       $$\int_{-\infty}^{\infty} f_X(x)\,\mathrm{d}x = 1$$
    3. Probabilidad en un intervalo:
       $$P(x_1 < X \leq x_2) = \int_{x_1}^{x_2} f_X(x)\,\mathrm{d}x$$
    4. La función acumulativa se obtiene de la densidad:
       $$F_X(x) = \int_{-\infty}^{x} f_X(\xi)\,\mathrm{d}\xi$$

![Propiedades de la función de densidad](images/f_propiedades.svg)

