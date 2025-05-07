### Presentación

[10 - Momentos de las variables aleatorias múltiples](https://www.overleaf.com/read/kggsyrzbdrxc#998b1f)

### Secciones
- Valor esperado de una función de variables aleatorias (1 - 3)
- Momentos conjuntos alrededor del origen (4 - 5)
- Correlación (6 - 9)

# **Universidad de Costa Rica**  
## Facultad de Ingeniería  
### Escuela de Ingeniería Eléctrica  
### Curso: Modelos Probabilísticos para Ingeniería  
### Tema: Funciones de Variables Aleatorias y Correlación  
### Estudiante: Nicole Mena Porras  C14663  

### 6 de mayo de 2025  

---

# Sección 1: Valor esperado de una función de variables aleatorias 

1. El **valor esperado** de una función de variables aleatorias se define como el promedio ponderado de los valores que puede tomar esta función.

2. También, para las variables aleatorias discretas $X$ y $Y$, y una función $g(X, Y)$, el valor esperado está definido por:  
   $$
   E[g(X, Y)] = \sum_x \sum_y g(x, y) \cdot P_{X,Y}(x, y)
   $$

3. Para variables aleatorias continuas:  
   $$
   E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \cdot f_{X,Y}(x, y) \, dx \, dy
   $$



# Sección 2: Momentos conjuntos alrededor del origen 

4. Los **momentos conjuntos** alrededor del origen miden el comportamiento combinado de dos variables aleatorias. Esto se puede definir como:  
   $$
   \mu'_{rs} = E[X^r Y^s]
   $$

5. Estos momentos permiten analizar características como la dispersión y forma conjunta de la distribución. Por ejemplo:  
   - $\mu'_{10} = E[X]$: esperanza de $X$  
   - $\mu'_{01} = E[Y]$: esperanza de $Y$  
   - $\mu'_{11} = E[XY]$: producto esperado  



# Sección 3: La correlación 

6. La **covarianza** entre dos variables aleatorias mide cómo varían ambas respecto a sus medias, por ejemplo:  
   $$
   \text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]
   $$

7. Se tienen los siguientes criterios, si la covarianza es:  
   - Positiva → $X$ y $Y$ tienden a aumentar juntos.  
   - Negativa → uno tiende a aumentar cuando el otro disminuye.  
   - Cero → no hay relación lineal.  

8. La **correlación** se refiere a la forma normalizada de la covarianza:  
   $$
   \rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
   $$
   donde $\sigma_X$ y $\sigma_Y$ se refieren a las desviaciones estándar de $X$ y $Y$.

9. El valor de $\rho_{X,Y}$ está entre el rango de -1 y 1. Significado de los valores cercanos a:  
   - 1 → alta correlación positiva  
   - -1 → alta correlación negativa  
   - 0 → sin correlación lineal
