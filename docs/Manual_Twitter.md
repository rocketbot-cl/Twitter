



# Twitter
  
Connect to Twitter, list tweets from timeline, update status, and search words  
  
![banner](/docs/imgs/Banner_Twitter.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



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
