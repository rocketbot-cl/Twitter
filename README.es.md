# Twitter
  
Conectarse a Twitter, listar los tweets de la timeline, actualizar el estado y buscar palabras  

*Read this in other languages: [English](README.md), [Español](README.es.md).*

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



## Overview


1. Conectar con Twitter  
Conectar con tu cuenta de Twitter utilizando tus credenciales

2. Enviar Tweet  
Enviar un tweet usando un mensaje y opcionalmente un ID de un tweet para responder

3. Buscar tweet  
Dada una palabra o texto, con o sin filtros, buscarlo mediante la API de Twitter

4. Obtener menciones  
Se obtiene una lista de menciones que se hayan hecho a la cuenta

5. Obtener ID de usuario  
Obtiene el ID de un usuario

6. Obtener timeline de usuario  
Se obtiene el timeline de un usuario

7. Retweetear  
Retweetea un tweet

8. Obtener información de un tweet  
Obtiene información de un tweet a partir de su ID  




----
### OS

- windows
- mac
- linux

### Dependencies
- [**tweepy**](https://pypi.org/project/tweepy/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)