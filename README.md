# El Bosque Estéreo

## Capturas

### El Bosque Stereo (emisora)
<img src="/Capturas/01.PNG" alt="Inicio" width="200px" height="150px">  <img src="/Capturas/02.PNG" alt="Parrilla de programación" width="200px" height="150px">  <img src="/Capturas/03.PNG" alt="Login Administrativo" width="200px" height="150px">  <img src="/Capturas/04.PNG" alt="Modulo administrativo" width="200px" height="150px">  <img src="/Capturas/05.PNG" alt="Redes sociales y señal en VIVO" width="200px" height="150px"> 

## Instalación Python

Descargar python ultima versión 3.6 o mayor. Importante: En la instalación se debe seleccionar la opción "Añadir a variables del sistema"
Una vez instalado verificar la instalación de la siguiente manera:
  Abrir la ventana de comandos CMD en modo administrador y escribir el comando `python --version`
  Aparecerá entonces la versión de python instalada.
  
### Instalación Django

En la ventana de comandos CMD ingresar el comando `pip install django` (Ejecutar en modo administrador)
En las ultimas lineas de la instalación debe aparecer que se instaló correctamente


## Clonar Repositorio Git de Github

Muy importante clonar el repositorio para tener las ultimas actualizaciones, para guardar las modificaciones y que todos puedan tenerlas.

Instalar Git ( https://git-scm.com/downloads )

Una vez instalado abrir ventana de comandos CMD y poner el siguiente comando `git clone https://github.com/cizaquita1/ElBosque_Estereo`
Una vez descargado el repositorio, ir a la carpeta que lo contiene (donde se descargó)


## Configurando el proyecto

En la carpeta descargada ir a la ruta `ElBosque_Estereo/elbosque_estereo/elbosque_estereo/` para crear una copia del archivo `settings.py.dist` luego renombrar el archivo copia a `settings.py`


## Ejecutando el proyecto

Ir a la ruta `ElBosque_Estereo/elbosque_estereo/` y abrir la ventana de comandos CMD.
* Ejecutar `python manage.py migrate` para actualizar su base de datos local.
* Ejecutar `python manage.py createsuperuser` para crear un usuario administrador con el que accederan al panel principal.
* Ejecutar `python manage.py runserver` para correr el proyecto.


## Guardando cambios en el repositorio

Dentro de la carpeta del proyecto, ejecutar Gitbash con clic derecho -> Git Bash Here.
* Para asegurarte de que no hayan modificaciones creadas por otros, utiliza `git pull` o `git pull origin master` para luego proceder a crear las modificaciones que necesitas.
* Si creaste nuevos archivos dentro del repositorio, agregalos usando `git add .`
* Para guardar los cambios utiliza `git commit -am 'Comentario de la modificación o actualización lo que hiciste.'`
* Para subir los cambios a Github usa: `git push origin master` y pon tus credenciales de Github.

Si todo sale bien podrás acceder desde el navegador al aplicativo con la dirección http://127.0.0.1:8000

Por favor, si tienes algún inconveniente te ayudaré sin problema, por favor contáctame, estaré complacido en ayudar:
Telegram: https://t.me/Cizaquita

Salu2

