# Maker Shop (Proyecto SENA)

## Descripción

Maker Shop es una aplicación web desarrollada con el framework **Django**, 
como parte de un proyecto académico del *SENA*. 
Esta es la segunda versión del sistema, con diversas mejoras sobre la anterior.

El sistema está compuesto por tres módulos principales:

- *Proveedores:* Gestión y administración de proveedores.
- *Productos:* Registro, control e inventario de productos.
- *Usuarios (Consumidores):* Administración de usuarios y asignación de productos.

También cuenta con un sistema de *ayuda y soporte* a través 
de *correo electrónico (SMTP)* para mejorar la atención al usuario.


## Requisitos

- Python 3.12 o superior
- Django 5.1.2
- SQLite (por defecto, puedes configurar a tu gusto en settings.py)
- Servidor SMTP configurado (opcional)

## Licencia

Este proyecto se distribuye con fines educativos y puede ser reutilizado, 
adaptado y mejorado libremente dentro de entornos académicos.

## Autor

Miguel Medrano Pérez  
[GitHub: @Miguelmp28](https://github.com/Miguelmp28)


## Instalación

Sigue estos pasos para clonar el proyecto y ejecutarlo en tu entorno local:

```bash
# ---- Clonar el repositorio ------------
git clone https://github.com/Miguelmp28/django-app.git

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# ---- Ingresar al directorio del proyecto -----
cd appdjango

# ---- Insatalación de los requerimientos ------
pip install -r requirements.txt

# ---- Crea el super usuario --------
python manage.py createsuperuser

# ---- Crea migraciones -------
python manage.py makemigrations
python manage.py migrate 

# ---- Ejecución de la aplicacion -------
python manage.py runserver
