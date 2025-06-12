# Vida útil de un componente y su repuesto

Sea $X_1$ una \textit{variable aleatoria} para el tiempo de vida de un componente. El componente puede sustituirse una única vez, y $X_2$ representa el tiempo de vida del repuesto. $X_1$ y $X_2$ son **iid** con distribución exponencial de parámetro $\lambda$. Por lo anterior, la PDF conjunta es

$$
f_{X_1,X_2}(x_1,x_2) = \lambda^2 e^{-\lambda(x_1 + x_2)} \quad \text{para} \quad x_1 > 0, x_2 > 0
$$

![Conjunta Vida Util](images/11_pdf_conjunta_vida_util_repuesto.svg)

Podríamos estar interesados en dos cantidades (transformaciones arbitrarias $u_1$ y $u_2$):

- La vida total del dispositivo $$Y_1 = u_1(X_1,X_2) = X_1 + X_2$$
- La proporción de la vida del primer componente a la vida total del dispositivo $$Y_2 = u_2(X_1,X_2) = \frac{X_1}{X_1 + X_2}$$

## Planteamiento
¿Cuál es la distribución conjunta de $Y_1$ y $Y_2$?

Por el teorema de transformación, escrito como

$$
f_{Y_1,Y_2}(y_1,y_2) = f_{X_1,X_2}[x_1 = v_1(y_1,y_2), x_2 = v_2(y_1,y_2)] \left\vert \mathsf{det}(\mathbf{M}) \right\vert
$$

Y dadas las funciones inversas 

- $x_1 = v_1(y_1,y_2) = y_1 y_2$
- $x_2 = v_2(y_1,y_2) = y_1(1 - y_2)$

de donde se obtiene también la región de la "imagen de la transformación", en $y_1 > 0, 0 < y_2 < 1$.

En una transformación bivariada se cumple que

$$
J(y_1,y_2) \triangleq \mathsf{det}(\mathbf{M}) \triangleq \frac{\partial (v_1,v_2)}{\partial(y_1,y_2)} \triangleq \mathsf{det} 
\begin{pmatrix}
\frac{\partial v_1}{\partial y_1} & \frac{\partial v_1}{\partial y_2} \\$0.5em]
\frac{\partial v_2}{\partial y_1} & \frac{\partial v_2}{\partial y_2}
\end{pmatrix}
$$

de donde, dados $v_1(y_1,y_2)$ y $v_2(y_1,y_2)$,

- $\frac{\partial v_1}{\partial y_1} = y_2$
- $\frac{\partial v_1}{\partial y_2} = y_1$
- $\frac{\partial v_2}{\partial y_1} = (1-y_2)$
- $\frac{\partial v_2}{\partial y_2} = -y_1$
y, por tanto,

$$
\mathsf{det}(\mathbf{M}) = \frac{\partial v_1}{\partial y_1} \cdot \frac{\partial v_2}{\partial y_2} - \frac{\partial v_1}{\partial y_2} \cdot \frac{\partial v_2}{\partial y_1} = -y_1 y_2 - y_1(1-y_2) = -y_1
$$

Finalmente, la nueva función de densidad viene de

$$
\begin{aligned}
    f_{Y_1,Y_2}(y_1,y_2) 
    & = f_{X_1,X_2}[x_1 = v_1(y_1,y_2), x_2 = v_2(y_1,y_2)] \left\vert \frac{\partial (v_1,v_2)}{\partial(y_1,y_2)} \right\vert \\
    & = \lambda^2 e^{-\lambda(y_1 y_2 + y_1(1 - y_2))} \vert -y_1 \vert = \lambda^2 y_1 e^{-\lambda(y_1)} \\
    & = \lambda^2 y_1 e^{-\lambda y_1} \cdot 1 \quad \text{para} \quad y_1 > 0, 0 < y_2 < 1
\end{aligned}
$$

donde se observa que no depende de $y_2$, y 1 está distribuido en $0 < y_2 < 1$.

![Transformadas](images/11_pdf_transformada.svg)

Se observa además que

- La distribución del tiempo de vida $X_1 + X_2$ se conoce como \textit{distribución gama}, con parámetros $\alpha = 2$ y $\beta = 2$.
- La proporción del tiempo de vida del componente original es uniforme entre 0 y 1.
- $Y_1$ y $Y_2$ son independientes entre sí.

# Ejemplo de transformación lineal

Sea $Z = X + Y$, y $W = X - Y$. Entonces

$$
\begin{aligned}
X &= \frac{Z + W}{2} \triangleq P(Z,W) \\
Y &= \frac{Z - W}{2} \triangleq Q(Z,W)
\end{aligned}
$$

Por tanto

$$
\vert J(z,w) \vert = \left\vert \mathrm{det} 
\begin{pmatrix}
\frac{\partial P}{\partial z} & \frac{\partial P}{\partial w} \\$0.5em]
\frac{\partial Q}{\partial z} & \frac{\partial Q}{\partial w}
\end{pmatrix}
\right\vert
= \left\vert \mathrm{det} 
\begin{pmatrix}
\frac{1}{2} & \frac{1}{2} \\$0.5em]
\frac{1}{2} & -\frac{1}{2}
\end{pmatrix}
\right\vert
= \frac{1}{2}
$$

y así

$$
\boxed{f_{Z,W}(z,w) = \frac{1}{2} f_{X,Y} \left( \frac{z+w}{2}, \frac{z-w}{2} \right)}
$$

# Ejemplo de transformación rotacional

Sea, para un ángulo fijo $\theta_0$,

$$
Z = X\cos \theta_0 + Y \sin \theta_0 \qquad
W = X\sin \theta_0 - Y\cos \theta_0
$$

y así

$$
\begin{aligned}
X &= Z\cos \theta_0 + W \sin \theta_0 \triangleq P(Z,W) \\
Y &= Z\sin \theta_0 - W\cos \theta_0 \triangleq Q(Z,W)
\end{aligned}
$$
por tanto

$$
\vert J(z,w) \vert = \left\vert \mathrm{det} 
\begin{pmatrix}
\frac{\partial P}{\partial z} & \frac{\partial P}{\partial w} \\$0.5em]
\frac{\partial Q}{\partial z} & \frac{\partial Q}{\partial w}
\end{pmatrix}
\right\vert
= \left\vert \mathrm{det} 
\begin{pmatrix}
\cos\theta_0 & \sin\theta_0 \\$0.5em]
\sin\theta_0 & -\cos\theta_0
\end{pmatrix}
\right\vert
= 1
$$

de forma que una transformación rotacional como la descrita no cambia la función de densidad conjunta.

# Ejemplo de transformación polar

Sea

$$
\begin{aligned}
R^2 &= X^2 + Y^2 & 0 \leq R \leq \infty \\
\Theta &= \tan^{-1}(Y/X) & -\pi < \Theta < \pi
\end{aligned}
$$

$$
X = R\cos\Theta \triangleq P(R,\Theta) \qquad
Y = R\sin\Theta \triangleq Q(R,\Theta)
$$

Luego,

$$
\vert J(r,\theta) \vert = \left\vert \mathrm{det} 
\begin{pmatrix}
\frac{\partial P}{\partial r} & \frac{\partial P}{\partial \theta} \\$0.5em]
\frac{\partial Q}{\partial r} & \frac{\partial Q}{\partial \theta}
\end{pmatrix}
\right\vert
= \left\vert \mathrm{det} 
\begin{pmatrix}
\cos\theta & -r\sin\theta \\$0.5em]
\sin\theta & r\cos\theta
\end{pmatrix}
\right\vert
= r
$$

de forma que

$$
\boxed{f_{R,\Theta}(r,\theta) = f_{X,Y}(r\cos\theta,r\sin\theta) r}
$$

# Distribución probabilística de la suma de variables aleatorias

## Suma de variables aleatorias

Se va a analizar el problema de hallar las funciones de densidad y distribución para una suma de variables aleatorias **estadísticamente independientes**.

## Suma de dos variables aleatorias

Sea $W$ una variable aleatoria igual a la suma de dos variables aleatorias independientes $X$ e $Y$: 

$$
W = X + Y
$$

**Nota**: $X$ pudiera representar una señal aleatoria de tensión e $Y$ pudiera representar ruido aleatorio. La suma $W$ pudiera representar entonces una tensión de señal más ruido, en algún receptor. 

La función de distribución de probabilidad que se busca está definida por:

$$
F_{W}(w) = P( W \leq w ) = P( X + Y\leq w )
$$

![dx/dy](images/11_dx_dy.svg)

La probabilidad correspondiente a un área elemental $\di{x}\di{y}$ en el plano $XY$ localizado en el punto $(x,y)$ es {\color{AzulUCR}{$f_{X,Y} \di{x}\di{y}$}}. Si se suma todas las probabilidades sobre la región donde $x+y \leq w$ se obtendrá $F_{W}(w)$:

$$
F_{W}(w) = \int_{-\infty}^{\infty}\int_{x = -\infty}^{w-y}f_{X,Y}(x,y)\di{x}\di{y}
$$

Como $X$ y $Y$ son independientes, es decir, $f_{X,Y}(x,y) = f_X(x) f_Y(y)$, entonces,

$$
F_{W}(w) = \int_{-\infty}^{\infty}f_{Y}(y)\int_{x=-\infty}^{w-y}f_{X}(x)\di{x}\di{y}
$$

Después de derivar, usando la regla de Leibniz, se obtiene la función de densidad:

$$
f_{W}(w) = \int_{-\infty}^{\infty}f_{Y}(y)f_{X}(w-y)\di{y}
$$

que describe una **integral de convolución**, por tanto: 

**La función de densidad de la suma...**
...de dos variables aleatorias estadísticamente independientes es la convolución de sus funciones de densidad individuales.

# Ejemplo de la suma de dos variables aleatorias

**Planteamiento**: Encuentre la función de densidad de $W = X + Y$ donde las densidades respectivas son:

$$
\begin{eqnarray*}
  f_{X}(x) & = & \left(\frac{1}{a}\right) \left[ u(x) - u(x-a) \right] \\
  f_{Y}(y) & = & \left(\frac{1}{b}\right) \left[ u(y) - u(y-b) \right]
\end{eqnarray*}
$$

con $0 < a < b$.

Este ejercicio se puede resolver mediante la integral de convolución o mediante el método de la transformada de Laplace. Se escoge este último método al notarse que ambas funciones de densidad están definidas a partir del origen, lo cual facilita un manejo algebraico del problema.

Se tiene entonces:

$$
\mathcal{L}\{ f_{X}(x) \} = \int_{0}^{a}\frac{1}{a}e^{-sx}dx 
$$
$$
= \left( \frac{1}{a} \right) \left. \frac{e^{-sx}}{-s} \right|_{0}^{a} 
$$
$$
= \left( \frac{1}{as} \right) \left[ 1 - e^{-as} \right] 
$$
$$
\mathcal{L}\{ f_{Y}(y) \} = \left( \frac{1}{bs} \right) \left[ 1 - e^{-bs} \right]
$$

La transformada de Laplace de una integral de convolución es igual al producto de las transformadas de Laplace de las funciones que conforman el integrando de tal integral. El próximo paso es entonces encontrar el producto de las dos transformadas de Laplace calculadas para luego encontrar la transformada de Laplace inversa y así hallar la nueva función de densidad, correspondiente a la nueva variable aleatoria $W$.

$$
\mathcal{L}\{f_{X}(x)\} \mathcal{L}\{f_{Y}(y)\} = \left( \frac{1}{ab}\right) \left( \frac{1}{s^2}\right) \left[ 1 - e^{-bs} - e^{-as} + e^{-(a+b)s} \right]
$$

Lo que sigue ahora es encontrar la transformada de Laplace inversa, para lo que es importante recordar la siguiente transformada:

$$
\mathcal{L}\{ t^n \} = \frac{n!}{s^n+1} 
$$

Se obtiene entonces:

$$
\begin{aligned}
f_W(w) &= \mathcal{L}^{-1} \{ \frac{1}{a b s^2} [ 1 - e^{-a s} - e^{-b s} + e^{-(a+b)s} ] \} \\ 
&= \frac{1}{ab} w\, \mathrm{u}(w) - \frac{1}{ab} (w - a) \mathrm{u}(w - a) - \frac{1}{ab} (w - b) \mathrm{u}(w - b) \\
&\quad + \frac{1}{ab} (w - a - b) \mathrm{u}(w - a - b)
\end{aligned}
$$

Nótese que se ha hecho cambios de variable para emplear correctamente la transformada de Laplace. Finalmente, dado que el resultado debe ser una función de densidad, una prueba que se puede hacer para probar si el resultado es correcto, es comprobar que el área bajo la curva de la nueva función es en efecto igual a la unidad.

# Suma de varias variables aleatorias

**La función de densidad de la suma de varias variables aleatorias**  
La función de densidad de \$ Y = X_1 + X_2 + \cdots + X_N \$, donde las \$ X_i \$ son variables aleatorias estadísticamente independientes entre sí, es la convolución de las \$ N \$ funciones de densidad individuales: 

$$
f_{Y}(y) = f_{X_N}(x_N) \ast f_{X_{N-1}}(x_{N-1}) \ast \cdots \ast f_{X_1}(x_1)
$$

