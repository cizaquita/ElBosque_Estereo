# El Bosque Estéreo


## Instalación Python

Descargar python ultima versión 3.6 o mayor. Importante: En la instalación se debe seleccionar la opción "Añadir a variables del sistema"
Una vez instalado verificar la instalación de la siguiente manera:
  Abrir la ventana de comandos CMD en modo administrador y escribir el comando `python --version`
  Aparecerá entonces la versión de python instalada.
  
### Instalación Django

En la ventana de comandos CMD ingresar el comando `pip install django` (Ejecutar en modo administrador)
En las ultimas lineas de la instalación debe aparecer que se instaló correctamente


## Clonar Repositorio Github

Muy importante clonar el repositorio para tener las ultimas actualizaciones y para guardar las actualizaciones y que todos puedan tenerlas.

Instalar Git ( https://git-scm.com/downloads )

Una vez instalado abrir ventana de comandos CMD y poner el siguiente comando `git clone https://github.com/cizaquita1/ElBosque_Estereo`
Una vez descargado el repositorio, ir a la carpeta que lo contiene (donde se descargó)

## Configurando el proyecto

En la carpeta descargada ir a la ruta `ElBosque_Estereo/elbosque_estereo/elbosque_estereo/` para crear una copia del archivo `settings.py.dist` luego renombrar el archivo copia a `settings.py`


## Ejecutando el proyecto

Ir a la ruta `ElBosque_Estereo/elbosque_estereo/` y abrir la ventana de comandos CMD.
Ejecutar `python manage.py migrate` para actualizar su base de datos local.
Ejecutar `python manage.py createsuperuser` para crear un usuario administrador con el que accederan al panel principal.
Ejecutar `python manage.py runserver` para correr el proyecto.

Si todo sale bien podrás acceder desde el navegador al aplicativo con la dirección http://127.0.0.1:8000

Por favor, si tienes algún inconveniente te ayudaré sin problema, por favor contáctame, estaré complacido en ayudar:
Telegram: https://t.me/Cizaquita
WhatsApp: https://api.whatsapp.com/api/send?phone=573138087811
e-mail: cristian[dot]izaquita[at]gmail[dot]com

Salu2

