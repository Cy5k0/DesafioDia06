# Desafío - Mostrando contenido dinámico

Este proyecto es una aplicación web desarrollada en Django que permite mostrar información de empleados de una institución en una página web. Los nombres de los empleados están almacenados en una lista de Python, y se muestran en un template HTML. El número de empleados a mostrar es indefinido.

## Características

- Desarrollada en Django.
- Muestra los nombres de empleados desde una lista de Python.
- El número de empleados no está limitado, se pueden agregar tantos como sea necesario.
- Uso de templates HTML para la visualización de la información.

### Instalación Inicial

- Creación de entorno virtual
  `desafiodia06>python -m venv venv06`

- Activación entorno virtual
  `source env/bin/activate  # En Linux/MacOS`
  `env\Scripts\activate  # En Windows `
- Instalación de las dependencias del proyecto
  `pip install django #lo que tuve que hacer yo`
  `pip install -r requirements.txt` (por si se necesitara)
- Creación de proyecto
  `django-admin startproject project_d06 .`
- Creación de aplicación
  `django-admin startapp webapp`

### Ejecución

`python manage.py migrate`
`python manage.py runserver`
`http://localhost:8000/app/`

### Autor

[Francisco Colomer Bonometti](https://github.com/Cy5k0)
