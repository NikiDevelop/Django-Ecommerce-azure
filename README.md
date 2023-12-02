# Django Ecommerce Deploy Azure
----------------------------------------------------------

Una guía como hacer un deploy en Azure y como preparar los archivos static de Django para desplegarla.

# Preparamos el proyecto para el Deploy
Tenemos que entender que Django no sirve los archivos static por eso tenemos que hacer una serie de cosas, le tenemos que decir donde se encuentran los archivos static a la hora de hacer el deploy.
Te voy a guiar paso a paso como hacerlo, mi mes de prueba en Azure se terminó.

Instalamos `Whitenoise `.
```
$ pip install whitenoise
```
Nos dirigimos a settings y lo agregamos en `MIDDLEWARE`

```
MIDDLEWARE = [
'whitenoise.middleware.WhiteNoiseMiddleware',
...
]
```
Ahora hay que decirle donde se encuentran los archivos static y media. Nos dirigimos a settings y agregamos el path.
Cambia `DEBUG = False `.<br>
En `ALLOWED_HOSTS` por ahora agregamos un `*` que luego agregaremos nuestro dominio de la aplicación.
```
ALLOWED_HOSTS = [*]
```

```
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
	BASE_DIR / 'static'	
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = BASE_DIR / 'staticfiles'

```
Nos dirigimos a urls.py del proyecto, donde tienes la configuración del proyecto y agregamos el `urlpatterns` e importamos static.

```
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),      
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
Algo así debería quedarte. Y ya por último necesitamos ejecutar `collectstatic` cuando ya tengamos toda la configuración y tengamos nuestros archivos static listos para el deploy. 

```
$ python manage.py collectstatic

```
Ejecutamos `freeze requirements`
```
$ pip freeze > requirements.txt
```
Ya tenemos el proyecto listo para hacer el deploy.<br>
Ve a GitHub y create un nuevo repositorio, y vamos a subir nuestro proyecto desde VsCode.
Ahora tenemos que subir nuestro proyecto a GitHub.

```
$ git init
$ git add .
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/tu_usuario/prueba.git
$ git push -u origin main

```

# Vamos con Azure
Nos dirigimos a ["Portal de Azure"](https://portal.azure.com/) tendrás que crearte una cuenta nueva.<br>
• Tienes un mes gratis para probar los productos de Azure.<br>
• Te pedirán ingresar una tarjeta de crédito para comprobar tu identidad pero no te cobraran nada.<br>

Después de que te hayas registrado tendría que salirte algo así.

![Screenshot 2023-12-01 at 16-45-36 Microsoft Azure](https://github.com/NikiDevelop/NikiDevelop/assets/105102619/ad6453da-06ce-4c9f-aca1-96e4a6d4fc62)
<br><br>
Creamos un nuevo `+ Crear un nuevo recuerso` aquí el nombre que le ponga no importa, puedes ponerle el nombre del proyecto. <br> 
Ahora le damos a `Aplicación web` y le damos a crear.

![Captura](https://github.com/NikiDevelop/NikiDevelop/assets/105102619/eebf8c17-8b84-4f7d-863d-462a04ac4bad)
<br><br>
Nos saldrá la suscripción que tenemos.<br>
- `Grupo de recursos` el que hemos creado al principo o creamos uno nuevo con el nombre que queramos. <br>
- `Nombre` le ponemos el nombre que queramos que será la url ejemplo: `Django-prueba`.azurewebsites.net<br>
- `Publicar` Código en mi caso.<br>
- `Pila del entorno...` elegimos el lenguaje de nuestra app, en mi caso Python y la versión que tengas. Para ver la versión de Python `python --version`
- `Región` Te recomiendo que elijas la más cercana.
Te debería quedar algo así y le damos a `Revisar y crear`
![Capturasssss](https://github.com/NikiDevelop/NikiDevelop/assets/105102619/8077cfa9-7fe3-492e-b745-ffaf12c9a78c)
<br><br>
Nos dirigimos a `Implementacion`. Nos logueamos con nuestra cuenta de `GitHub` para que nos salga nuestro proyecto y lo seleccionemos. Le damos a `Revisar y crear`<br>
Azure nos habrá creado una carpeta con un archivo `.github/workflows`/`main_prueba.yml`, Azure automáticamente nos ha creado esta carpeta con un archivo `yml`.<br>
Esperamos un momento para que Azure termine de realizar todo lo necesario para que nuestra aplicación este lista.<br>
Nos saldrá un botón que pondrá `Ir al recurso`, le damos.<br>
Refrescamos la página varias veces. A la derecha nos sale `Dominio predeterminado:.....` ahí es donde está alojada nuestra aplicación le damos y esperamos.<br>
Por último nos dirigimos a settings de nuestro proyecto y nos vamos a `ALLOWED_HOSTS` y ponemos nuesta url.
```
ALLOWED_HOSTS = ['Django-prueba.azurewebsites.net']
```
Realizamos el push a `GitHub` con los cambios. Asegurate que estes poniendo bien tu branch en mi caso es main. 
```
$ git pull origin main
$ git add .
$ git commit -m "add allowed hosts"
$ git push origin main
```
Nos dirigimos a Azure en `Introducción` y le damos a `Reinicar` y esperemas un rato y nos aplicación ya tendría que estar visible. <br><br>

## Ejecutar el proyecto
Lo primero creamos un entorno virtual.

```
$ python -m venv env
```

Tenemos que activar nuestro entorno virtual, tendremos que desplazarnos a la carpeta scripts.
```
$ cd env/scripts
```
Activamos nuestro entorno virtual.
```
$ .\activate
```
Ya tendríamos activado nuestro entorno virtual, debería salirte a la izquierda en color verde (env), eso quiere decir que está activado ya.

Ahora tenemos que regresar a nuestra carpeta del archivo, para eso utilizamos el siguiente comando por dos veces para regresar.
```
$ cd .. 
```
Ahora pasaremos a instalar las dependencias del proyecto.
```
$ pip install -r requirements.txt
```
Por último, ya solo te queda hacer las migraciones.
```
$ python manage.py makemigrations
```
```
$ python manage.py migarate
```
```
$ python manage.py runserver
```
Para poder agregar nuevas imágenes tendrás que crearte un usuario. Rellena los datos que te pide, como nombre de usuario,
el email lo puedes dejar en blanco si quieres dándole a enter y por último introduce una contraseña y repítela.
```
$ python manage.py createsuperuser
```

Espero que os guste mi proyecto.
Cualquier sugerencia o participación que quieras aportar es bienvenida.
