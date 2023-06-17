# Entrega Del Proyecto Final

## Crear web similar a un blog
---
✔ Se deberá entregar de manera individual. Crearás una aplicacion web (ej. estilo blog) programada en Python en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.

✔ La entrega se realizará enviando el link de Github, y en el readme de Github deberá estar el nombre completo del participante y una descripción de lo realizado.

✔ En el github debe haber un video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos.

✔ Contar con algún acceso visible a la vista de"Acerca de mñi" donde se contará acerca de los dueños de la página manejado en la url about/. (En castellano un "acerca de mí" que hable un poco del creador del proyecto).

✔ Contar con algún acceso visible a la vista (por ej. de blogs que pueden alojarse en la url pages/ es decir un html que permite listar todos los registros de la base de datos).

✔ Acceder a una pantalla que contendrá las páginas. Al clickear en "Leer más" o "Detalle" debe navegar al detalle de la page (ej. mediante una url pages(< pageId >)). (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).

✔ Para crear, editar o borrar las fotos debes estar registrado como administrador.

✔ Al menos debe haber dos modelos que contengan texto, número, fecha y una imagen (mínimo y obligatorio, puede tener más).

✔ Piezas sugeridas, no hace falta que estén todas, pero tiene que haber por lo menos un CRUD completo y el módulo de Login debe ser sólido:

NavBar, home, about pages, login, logout, signup.
Create, update, delete, detail, update.

*Requisitos base*

✔ Tener una app de registro donde se puedan registrar usuario. Un usuario está compuesto por email - contraseña - nombre de usuario.

✔ Tener una app de login en la url /login/ la cual permite loguearse con los datos de administrador o de usuario normal.

✔ Contar con un admin en url admin/ donde se puedan manejar las apps y los datos en las apps.

---

## Descripción
#
Repositorio correspondiente a la entrega del proyecto final curso Python de Coderhouse.

Nombre: Eduardo José Palacios Beltrán.

Video demostración: https://youtu.be/CWGqWuHSAjY

---

## Requisitos mínimos para ejecutar el código
#
    1. Visual Studio Code
    2. Git


---
## Instrucciones para ejecutar el proyecto
#
Para el correcto funcionamiento del proyecto se recomienda seguir las instrucciones a continuación:

`Generación del proyecto en repositorio local`

- Creación de carpeta del proyecto

Se recomienda crear una carpeta en el ordenador donde se vaya a ejecutar el proyecto. Posteriormente se debe abrir dicha carpeta en el editor de código Visual Studio Code.

- Ubicar la carpeta del proyecto en la terminal

Mediante el comando cd se debe ubicar la carpeta generada.

- Clonar repositorio desde Github

Se debe clonar el repositorio alojado en Github. Para ello se debe ejecutar el siguiente comando en la terminal del VSC:

> git clone https://github.com/PalaciosBeltran/Coder_Python_Proyecto_Final.git

`Preparación del entorno del proyecto`

- Crear un entorno virtual

Se debe generar un entorno virtual donde se instalarán las dependencias requeridas para el proyecto. 

>python -m venv .venv

- Instalar Django en el entorno virtual

Se procede a instalar Django en el entorno virtual creado en el paso anterior.

>pip install Django

- Activar el entorno virtual

Una vez ubicado en la carpeta del proyecto, carpeta donde debe encontrarse el entorno virtual llamado .venv se debe ejecutar el siguiente comando en la terminal para empezar a trabajar en el proyecto:

> .\venv\scripts\activate

`Ejecución del proyecto`

Una vez instaladas las dependencias y el entorno virtual requerido, procederemos a ejecutar nuestro proyecto de desarrollo web mediante el siguiente comando:
>python manage.py runserver

Una vez se inicia el servidor se puede ingresar a la web desarrollada en el puerto http://127.0.0.1:8000/

`Pruebas de funcionamiento`

Se recomienda ver el video demostración (https://youtu.be/CWGqWuHSAjY) con todas las pruebas realizadas con una base de datos ya cargada y todas y cada una de las funciones que puede realizar el blog desarrollado.


