# Twitter
  
Conectarse a Twitter, listar los tweets de la timeline, actualizar el estado y buscar palabras 

*Read this in other languages: [English](Manual_Twitter.md), [Español](Manual_Twitter.es.md).*
  
![banner](imgs/Banner_Twitter.png)

## Como usar este modulo
### Primeramente debemos tener en claro que la cuenta de Twitter a utilizar debe tener el perfil con los datos completo y llevar un tiempo utilizandola, sino sera un poco mas complicado aplicar para tener habilitado el uso de la API. Revisar el siguiente link para mas informacion: https://developer.twitter.com/en/apply-for-access
1. Iniciaremos sesion en nuestra cuenta de Twitter y luego iremos al siguiente link https://developer.twitter.com/en/docs/twitter-api
2. Dentro de la pantalla principal, en la seccion "Twitter API" haremos click en el boton que se encuentra debajo y se llama "Sign Up"
3. Luego en el dashboard, deberemos crear un proyecto haciendo click en "Create Project". Deberemos colocar titulo, descripcion y otros datos mas para crear el proyecto.
4. Despues de crear el proyecto, nos apareceran algunas claves, de las cuales debemos copiar y guardar las que dicen API Key y API Secret Key.
5. Como ultimo paso, debemos generar los tokens. Para ello se debe ir a la seccion de Project App y hacer click en el icono con forma de llave que tiene de nombre "Keys and Tokens". 
6. Generamos el Access Token y el Access Token Secret, los copiamos y los guardamos.


## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conectar con Twitter
  
Conectar con tu cuenta de Twitter utilizando tus credenciales
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API KEY|Colocar el API KEY que generamos en nuestra cuenta|eYSmJLqazCAXxFOrMogNa1322|
|API KEY Secret|Colocar el API KEY Secret que generamos en nuestra cuenta|Qvi0tuylMfrzJOJxO5Rp2Y5cSGWMHevITBwG0Oj2199Vo5Tdbr|
|Access Token|Colocar el Access Token que generamos en nuestra cuenta|Jc7bsx5UaQFewwvKHava6PBGkaZqdn0HSvp7Jg30dBQyy5ZZOB|
|Access Token Secret|Colocar el Access Token Secret que generamos en nuestra cuenta|Qvi0tuylMfrzJOJxO5Rp2Y5cSGWMHevITBwG0Oj2199Vo5Tdbr|
|Resultado|Variable donde guardaremos nuestro resultado. Si la conexion es exitosa retornara True, caso contraria sera False|result|

### Enviar Tweet
  
Enviar un tweet usando un mensaje y opcionalmente un ID de un tweet para responder
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Mensaje|En este campo debemos colocar el mensaje a enviar|Hola amigo! Tanto tiempo|
|Tweet ID|En caso de querer responder un tweet o un hilo, debemos colocar el ID de ese tweet|1461077245825531907|
|Resultado|Variable donde guardaremos nuestro resultado. Retorna el link del tweet enviado|result|

### Buscar tweet
  
Dada una palabra o texto, con o sin filtros, buscarlo mediante la API de Twitter
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Buscar|Se debe colocar el texto o palabra a buscar|Noticias importantes|
|Cantidad|Indicamos la cantidad de tweets a devolver. Por defecto devuelve 10|10|
|Idioma|Indicamos el idioma en el que se desea realizar la busqueda|es|
|Tipo de resultado|Puede ser recent, mixed o popular. Dejar vacio para traer por defecto|recent|
|Resultado|Variable donde guardaremos nuestro resultado. Retorna una lista de diccionario que tiene link, autor y mensaje del tweet|result|

### Obtener menciones
  
Se obtiene una lista de menciones que se hayan hecho a la cuenta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Cantidad|Indicamos la cantidad de tweets a devolver. Por defecto devuelve 10|10|
|Resultado|Variable donde guardaremos nuestro resultado. Retorna una lista de diccionario que tiene link, autor y mensaje del tweet|result|

### Obtener ID de usuario
  
Obtiene el ID de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario de Twitter|Indica el usuario de Twitter del cual queremos obtener el ID|rocketbot_es|
|Resultado|Variable donde guardaremos nuestro resultado. Retorna una lista de diccionario que tiene link, autor y mensaje del tweet|result|

### Obtener timeline de usuario
  
Se obtiene el timeline de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de usuario|Indicamos el ID del usuario del cual queremos obtener el timeline|1234567890|
|Cantidad|Indicamos la cantidad de tweets a devolver. Por defecto devuelve 10|10|
|Incluir retweets|Indicamos si queremos incluir los retweets en el resultado|True|
|Resultado|Variable donde guardaremos nuestro resultado. Retorna una lista de diccionario que tiene link, autor y mensaje del tweet|result|

### Retweetear
  
Retweetea un tweet
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del tweet|Indica el ID del tweet que quieres retweetear|1461077245825531907|

### Obtener información de un tweet
  
Obtiene información de un tweet a partir de su ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del tweet|Indica el ID del tweet que quieres retweetear|1461077245825531907|
|Variable |Variable donde se almacenará el resultado|result|
