# backendTodoAppInterView
Repositorio para el backend desarrollado en DRF para la prueba Todo App

# Proyecto Backend TodoApp

Este proyecto es el backend para una aplicación de tareas (`TodoApp`), desarrollado con Django y Django REST Framework. Proporciona una API para la gestión de tareas.

## Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)

## Características

- **Autenticación**: Gestión de usuarios y autenticación mediante tokens.
- **Gestión de Tareas**: Crear, editar, eliminar y listar tareas.
- **Filtrado y Ordenación**: Ordenar y filtrar tareas por estado y fecha de actualización.

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior
- Django REST Framework 3.12 o superior
- asgiref==3.8.1
- Django-cors-headers==4.4.0
- djangorestframework==3.15.2
- psycopg2-binary==2.9.9
- python-decouple==3.8
- sqlparse==0.5.1
- tzdata==2024.1
- 
## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/meliodas024/backendTodoAppInterView.git
   cd nombre_del_repositorio
2. **Crear un Entorno Virtual:**
python -m venv env
3. **Activar el Entorno Virtual:**

En Windows:
env\Scripts\activate
En macOS/Linux:
source env/bin/activate
4. **Instalar Dependencias:**
pip install -r requirements.txt

5. **Configurar Variables de Entorno:**

Renombra el archivo .env.example a .env y configura las variables de entorno necesarias. Asegúrate de proporcionar los valores correctos para tu entorno.
SECRET_KEY=tu_clave_secreta_aqui
DEBUG= True o False en producción
DB_NAME=nombre_de_tu_base_de_datos
DB_USER=usuario_de_tu_base_de_datos
DB_PASSWORD=contraseña_de_tu_base_de_datos
DB_HOST=host_de_tu_base_de_datos (por defecto 'localhost')
DB_PORT=puerto_de_tu_base_de_datos (por defecto '5432')

6.**Realizar Migraciones:**

python manage.py migrate

7. **Iniciar el Servidor:**
python manage.py runserver
El servidor estará disponible en http://127.0.0.1:8000/.
