### Presentación

# Funciones de covarianza

## Funciones de covarianza I

### Autocovarianza

> 💡 **Autocovarianza**  
> La función de autocovarianza (momento conjunto central de orden dos) de un proceso estocástico está definida por:
> 
> $$
> C_{XX}(t, t + \tau) = \mathbb{E}\left[(X(t) - \mathbb{E}[X(t)])(X(t + \tau) - \mathbb{E}[X(t + \tau)])\right]
> $$
> 
> equivalente a:
> 
> $$
> C_{XX}(t, t + \tau) = R_{XX}(t, t + \tau) - \mathbb{E}[X(t)]\mathbb{E}[X(t + \tau)]
> $$

---

## Funciones de covarianza II

### Covarianza cruzada
> 💡 **Covarianza cruzada**  
> La función de covarianza cruzada para dos procesos \( X(t) \) y \( Y(t) \) está definida por:
>
> $$
> C_{XY}(t, t + \tau) = \mathbb{E}\left[(X(t) - \mathbb{E}[X(t)])(Y(t + \tau) - \mathbb{E}[Y(t + \tau)])\right]
> $$
>
> o, alternativamente:
>
> $$
> C_{XY}(t, t + \tau) = R_{XY}(t, t + \tau) - \mathbb{E}[X(t)]\mathbb{E}[Y(t + \tau)]
> $$

---

## Funciones de covarianza III
>
> ℹ️ **Covarianza en procesos WSS**  
> Para procesos que son al menos conjuntamente estacionarios en sentido amplio (WSS), las covarianzas son:

$$
C_{XX}(\tau) = R_{XX}(\tau) - \bar{X}^2
$$

$$
C_{XY}(\tau) = R_{XY}(\tau) - \bar{X} \cdot \bar{Y}
$$

- La varianza de un proceso aleatorio está dada por la autocovarianza con $$( \tau = 0 )$$
- Para un proceso estacionario en sentido amplio, la varianza no depende del tiempo y está dada por:

$$
\sigma_X^2 = \mathbb{E}\left[(X(t) - \mathbb{E}[X(t)])^2\right] = R_{XX}(0) - \bar{X}^2
$$

---

## Funciones de covarianza IV

> ⚠️ **No correlación e independencia**  
> Para dos procesos aleatorios, si:

$$
C_{XY}(t, t + \tau) = 0
$$

entonces están **no correlacionados**, lo cual implica que:

$$
R_{XY}(t, t + \tau) = \mathbb{E}[X(t)] \cdot \mathbb{E}[Y(t + \tau)]
$$

> Se concluye que **procesos independientes son no correlacionados**,  
> pero el recíproco **no siempre es cierto** (aunque sí lo es para procesos conjuntamente gaussianos).

---
