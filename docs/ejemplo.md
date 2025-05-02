## Sobre la transcripción

El objetivo de esta tarea es hacer una transcripción de los contenidos del curso Modelos Probabilísticos de Señales y Sistemas de las presentaciones hechas en LaTeX (Overleaf) para documentos en formato Markdown.

Esto tiene los siguientes objetivos:

- Explotar la versatilidad del formato Markdown para incluir nuevas formas de contenido multimedia.
- Crear una versión de página web del contenido, visible fácilmente desde celulares u otros medios, con MkDocs (esta misma página es un ejemplo).
- Crear presentaciones interactivas con Slidev. Las presentaciones PDF actuales son, por su naturaleza, estáticas.
- Crear un documento en LaTeX con los contenidos del curso pero en formato de libro de texto, utilizando los mismos archivos Markdown (`.md`) como fuente.

!!! tip "Transcripción de ejemplo"
    El documento [`5_21_1_markov_estado_estable.md`](5_21_1_markov_estado_estable.md) tiene la transcripción de la presentación 21 "El vector de probabilidad en estado estable".


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

Los textos, listas y otros similares siguen la [sintaxis básica de Markdown](https://www.markdownguide.org/basic-syntax/).

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

Hay variables, como $x_{1,2}$ o $b$, y ecuaciones en línea, como $a \neq 0$.

#### Cambios necesarios

Las presentaciones tienen algunas funciones especiales que es necesario adaptar aquí.

### Notas especiales ("cajas de colores")

En las presentaciones hay varias "cajas de colores" para resaltar ciertas informaciones y definiciones. Es posible transcribirlas en [admoniciones](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) de Markdown, cuyo formato es:

```markdown
!!! note

    Hola, soy una nota
```

que se convierte en:

!!! note

    Hola, soy una nota

#### Introducción de una presentación

Al inicio de cada presentación hay una breve reseña del tema. Esta misma reseña estará al inicio de la página transcrita en Markdown, como una *admonición*.

=== "LaTeX"

    ```latex
    \begin{frame}[plain,noframenumbering]
    \LARGE
    Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados.

    Luego de suficientes transiciones, y al alcanzar un ``régimen permanente'', cada estado tiene una probabilidad definida.
    \end{frame}
    ```

=== "Markdown"

    ```markdown
    !!! abstract
    Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados.

    Luego de suficientes transiciones, y al alcanzar un "régimen permanente", cada estado tiene una probabilidad definida.
    ```

y resulta en:

!!! abstract "Introducción"
    Cuando existe una cantidad definida de estados, es posible modelar las transiciones entre todos estos estados.

    Luego de suficientes transiciones, y al alcanzar un "régimen permanente", cada estado tiene una probabilidad definida.

#### Definiciones

Las presentaciones tiene definiciones que están dentro de un entorno llamado `bloque`, que será transcrito en una *admonición* tipo `tip`. Notar que hay un título de descripción.

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

#### Resultados con énfasis

Algunos resultados o frases tienen un énfasis (caja verde) con un entorno llamado `énfasis`.

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

#### Ejemplos o ejercicios

Los ejemplos (`\begin{framex}`) estarán totalmente contenidos dentro de una *admonición* de la siguiente forma:

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

!!! example "Llamadas telefónicas a una pizzería"
    La más famosa de las funciones de probabilidad es la *normal* (o *gaussiana*), que describe la noción de que las probabilidades de ocurrencia de un evento están concentradas de forma simétrica alrededor de un valor central.

Notas:

- Los ejemplos deben tener un título representativo
- El enunciado y el resultado final tendrán la forma de cita, con `>`.
- Actualmente el enunciado está dentro del entorno `planteamiento`.

### Uso de inteligencia artificial generativa

¡Por supuesto! ChatGPT, Gemini, DeepSeek, Claude o cualquier otro pueden ayudar a transformar el código de LaTeX en Markdown, solo hay que pedirlo. Pero ¡cuidado!, hay que revisar bien la sintaxis y los casos especiales y verificar su presentación en la documentación, para que sea fiel (totalmente fiel) a la presentación, especialmente con precisión de la matemática, etc.

### Gráficos

Notas:

- Las referencias dentro del texto a una figura (si las hubiese) con `\ref{label}` deben ser sustituidas por una descripción literal, como "la figura anterior" o "la figura siguiente", por ejemplo.

#### PGF/Ti*k*Z

La gran mayoría de los gráficos en las presentaciones son hechos con [PGF/Ti*k*Z](https://tikz.dev/), un poderoso paquete de diseño de imágenes.

El directorio `images/` tiene la versión SVG de todas las imágenes de todas las presentaciones y deben usarlas en su lugar respectivo. El formato es:

```markdown
![Descripción de la imagen](images/prueba.svg)
```

![Descripción de la imagen](images/prueba.svg)

#### Mermaid

[Mermaid.js](https://mermaid.js.org/) es ahora el formato más popular de creación de diagramas técnicos para documentación, soportado por GitHub y otras plataformas.

## Notas generales

- No todos los títulos de 
- Deben ignorar (y eliminar) las instrucciones
  - `\begin{frame} ... \end{frame}` (sin embargo sí hay que usar los títulos)
  - `\framebreak`
  - `\noindent`
- Los delimitadores de expresiones matemáticas deben ser `$` para variables o ecuaciones en línea y `\begin{equation} ... \end{equation}` (igual que LaTeX pero sin el `*` y sin indentación) para ecuaciones en bloque.