# Instrucciones de edición

El proyecto utiliza [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) para desplegar el contenido como una página web, a modo de documentación.

## Ejecución del proyecto

Las [instrucciones de ejecución](https://squidfunk.github.io/mkdocs-material/getting-started/) de Material son útiles, sin embargo posiblemente se reduce a tres pasos en la terminal de comandos:

1. Configurar las credenciales de Git en el sistema local, con los siguientes comandos
```bash
git config --global user.name "Nombre Apellido"
```
```bash
git config --global user.email "your-email@example.com"
```
De forma que quede vinculado con su cuenta de Github

2. Crear un [ambiente] de python para poder ejecutar la instalación de librerías, para ello sitúese en el directorio raíz del proyecto (carpeta en donde copió el repositorio) y ejecute el comando:

```bash
python3 -m venv nombre_de_su_entorno
```
El nombre no es importante, puede elegir el de su preferencia. Recuerde **siempre**, antes de trabajar, activar el ambiente de python, de lo contrario se generarán errores. Para ello utilice el siguiente comando

```bash
source mi_entorno/bin/activate
```


3. Instalar el paquete [mkdocs-material](https://pypi.org/project/mkdocs-material/) con [pip](https://pypi.org/project/pip/) en el ambiente local de desarrollo de Python (por ejemplo, [Anaconda](https://www.anaconda.com/download)):

```bash
pip install mkdocs-material
```


4. Clonar el proyecto (dentro del directorio deseado):

```bash
git clone https://github.com/fabianabarca/mpss.git
```

5. En el mismo directorio donde está el archivo `mkdocs.yml` dentro del repositorio local (`cd mpss/`), ejecutar MkDocs:

```bash
mkdocs serve
```

el cual correrá un servidor local con el sitio web disponible en http://127.0.0.1:8000/ (por defecto, aunque puede cambiar).

## Edición del contenido

