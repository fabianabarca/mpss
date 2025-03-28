# Instrucciones de edición

El proyecto utiliza [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) para mostrar el contenido como una página web, a modo de documentación.

## Ejecución del proyecto

Las [instrucciones de ejecución](https://squidfunk.github.io/mkdocs-material/getting-started/) de Material son útiles, sin embargo posiblemente se reduce a los siguientes pasos en la terminal de comandos:

**Nota**: ver la sección [sobre Git y el ambiente virtual de Python](#sobre-git-y-el-ambiente-virtual-de-trabajo).


1. Instalar el paquete [mkdocs-material](https://pypi.org/project/mkdocs-material/) con [pip](https://pypi.org/project/pip/) en el ambiente local de desarrollo de Python (por ejemplo, el instalado con [Anaconda](https://www.anaconda.com/download)):

```bash
pip install mkdocs-material
```

2. Clonar el proyecto (dentro del directorio deseado):

```bash
git clone https://github.com/fabianabarca/mpss.git
```

3. En el mismo directorio donde está el archivo `mkdocs.yml` dentro del repositorio local (`cd mpss/`), ejecutar MkDocs:

```bash
mkdocs serve
```

el cual correrá un servidor local con el sitio web disponible en http://127.0.0.1:8000/ (por defecto, aunque puede cambiar).

### Sobre Git y el ambiente virtual de trabajo

Podrían ser necesarios algunos pasos previos para usar Git y los paquetes de Python.

1. Instalar Git y Python.

2. Configurar las credenciales de Git en el sistema local, con los siguientes comandos:

```bash
git config --global user.name "Nombre Apellido"
```

```bash
git config --global user.email "correo@ejemplo.com"
```

Así quedará vinculado con la cuenta personal de GitHub

3. Crear un [ambiente virtual](https://docs.python.org/es/3.13/library/venv.html) de Python para instalar paquetes. Para esto, en el directorio raíz del proyecto (carpeta en donde está clonado el repositorio: `mpss/`, la misma donde está `mkdocs.yml`) ejecutar el comando:

```bash
python3 -m venv env
```

donde `env` es el nombre del entorno (si utiliza otro, recuerde agregarlo en el archivo `.gitignore`). Esto creará una carpeta `env/` con todos los archivos necesarios para correr los paquetes instalados de Python, que solo estarán disponibles cuando el ambiente virtual está activado.

Recordar **siempre**, antes de trabajar, activar el ambiente virtual de Python:

```bash
source env/bin/activate
```

Y para desactivar:

```bash
deactivate
```

## Edición del contenido

