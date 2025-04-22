## Sobre la transcripción

El objetivo de esta tarea es hacer una transcripción de los contenidos del curso Modelos Probabilísticos de Señales y Sistemas de las presentaciones hechas en LaTeX (Overleaf) para documentos en formato Markdown.

Esto tiene los siguientes objetivos:

- Utilizar la versatilidad del formato Markdown para incluir nuevas formas de contenido multimedia.
- Crear una versión de página web del contenido, visible fácilmente desde celulares u otros medios, con MkDocs (esta misma página es un ejemplo).
- Crear presentaciones interactivas con Slidev. Las presentaciones PDF actuales son, por su naturaleza, estáticas.
- Crear un documento en LaTeX con los contenidos del curso pero en formato de libro de texto, utilizando los mismos archivos Markdown (`.md`) como fuente.

### LaTeX vs. Markdown

Tanto LaTeX como Markdown son lenguajes de descripción de formato. Markdown, de hecho, es una versión de sintaxis simplificada de HTML.

Estas son algunas equivalencias:

| Formato | LaTeX | Markdown |
|---|---|---|
| *Cursiva* | `\textit{hola}` | `*hola*` |
| **Negrita** | `\textbf{hola}` | `**hola**` |
| Sección | `\section{Hola}` | `# Hola` |
| Subsección | `\subsection{Hola}` | `## Hola` |

## Elementos de la transcripción



### Textos

### Fórmulas

- Todas las fórmulas son escritas con notación de LaTeX.

Esta documentación utiliza [MathJax](https://www.mathjax.org/) para renderizar las fórmulas en el navegador. La notación es idéntica:

```latex title="LaTeX | Markdown"
\begin{equation}
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
```
que genera:

\begin{equation}
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}

#### Cambios necesarios

Las presentaciones tienen algunas funciones especiales que es necesario adaptar aquí. La más común es:

### Notas especiales ("cajas de colores")

En las presentaciones hay varias "cajas de colores" para resaltar ciertas informaciones y definiciones. Es posible transcribirlas en [admoniciones](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) de Markdown, cuyo formato es:

```markdown
!!! note

    Hola, soy una nota
```

que se convierte en:

!!! note

    Hola, soy una nota

#### Definición con `bloque`

Esto es

=== "LaTeX"

    ```latex
    \begin{bloque}{Definición de una variable aleatoria}
    Para un espacio de eventos $S$, una \textbf{variable aleatoria} es cualquier regla que asocia cada resultado elemental de $S$ con \textbf{un número}. Es decir, es una \textbf{función} cuyo dominio es el espacio (quizá abstracto) de eventos o muestras, y cuyo rango es algún subconjunto de los números reales.
    \end{bloque}
    ```

=== "Markdown"

    ```markdown
    !!! tip "Definición de una variable aleatoria"
        Para un espacio de eventos $S$, una **variable aleatoria** es cualquier regla que asocia cada resultado elemental de $S$ con **un número**. Es decir, es una **función** cuyo dominio es el espacio (quizá abstracto) de eventos o muestras, y cuyo rango es algún subconjunto de los números reales.
    ```

y resulta en:

!!! tip "Definición de una variable aleatoria"
    Para un espacio de eventos $S$, una **variable aleatoria** es cualquier regla que asocia cada resultado elemental de $S$ con **un número**. Es decir, es una **función** cuyo dominio es el espacio (quizá abstracto) de eventos o muestras, y cuyo rango es algún subconjunto de los números reales.


#### Resaltado con `énfasis`

Esto es

=== "LaTeX"

    ```latex
    \begin{enfasis}
    La más famosa de las funciones de probabilidad es la \textit{normal} (o \emph{gaussiana}), que describe la noción de que las probabilidades de ocurrencia de un evento están concentradas de forma simétrica alrededor de un valor central.
    \end{enfasis}
    ```

=== "Markdown"

    ```markdown
    !!! note
        La más famosa de las funciones de probabilidad es la *normal* (o *gaussiana*), que describe la noción de que las probabilidades de ocurrencia de un evento están concentradas de forma simétrica alrededor de un valor central.
    ```

y resulta en:

!!! note
    La más famosa de las funciones de probabilidad es la *normal* (o *gaussiana*), que describe la noción de que las probabilidades de ocurrencia de un evento están concentradas de forma simétrica alrededor de un valor central.

### Gráficos

#### PGF/Ti*k*Z

La gran mayoría de los gráficos en las presentaciones son hechos con [PGF/Ti*k*Z](https://tikz.dev/), un poderoso paquete de diseño de imágenes.

No es posible renderizar directamente desde

![Descripción](images/prueba.svg)

#### Mermaid

[Mermaid.js](https://mermaid.js.org/) es ahora el formato más popular de creación de diagramas técnicos para documentación, soportado por GitHub y otras plataformas.