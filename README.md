# :computer: Creating a http server with python :computer: 

## ¿Qué es un protocolo informático? ##

En informática y telecomunicaciones, hablamos de un protocolo para referirnos a un sistema de normas que regulan la comunicación entre dos o más sistemas que se transmiten información a través de diversos medios físicos.

Dicho en otras palabras, los protocolos son lenguajes o códigos de comunicación entre sistemas informáticos, definidos en base a una sintaxis, una semántica y una sincronización, así como de métodos de recuperación de errores.

## ¿Qué es el protocolo http?

El Protocolo de transferencia de hipertexto (HTTP) es un protocolo para información distribuida, colaborativa e sistemas informaticos de hipermedia. HTTP ha sido utilizado por la "World-Wide Web global iniciative" de información desde 1990. La primera versión de HTTP, denominado HTTP/0.9, era un protocolo simple para la transferencia de datos sin procesar a través de Internet. Es como el código que se establece para que el computador solicitante y el que contiene la información solicitada puedan “hablar” un mismo idioma a la hora de transmitir información por la red.

Ademas este protocolo forma parte de la capa 7 del modelo OSI, la capa de aplicacion, en la cual participan tanto el protocolo http com los protocolos FTP, DNS, entre otros mas.

## ¿Para qué sirve el protocolo http?

En si http, es un lenguaje que media entre las peticiones del cliente y las respuestas del servidor en la Internet, para permitir una comunicación fluida y en un mismo “lenguaje”. Considerando que la Internet es poco más que una compleja red de intercambio de información entre computadores a distancia, este tipo de herramientas digitales son clave en establecer las bases para ordenar y facilitar la transmisión de la información.

## ¿Cómo funciona el protocolo http?

El funcionamiento del http se basa en un esquema de petición-respuesta entre el servidor web y el usuario o cliente que realiza la solicitud de transmisión de datos.
De esta manera el servidor brinda una respuesta estructurada de modo puntual y dotada de una serie de metadatos, que establecen las pautas para el inicio, desarrollo y cierre de la transmisión de la información. Estos son los “métodos de petición”, es decir, los comandos que disparan la ejecución de recursos determinados, cuyos archivos residen en el servidor.

## ¿Que metodos tiene el protocolo http?

HTTP define un conjunto de métodos de petición para indicar la acción que se desea realizar para un recurso determinado. Cada uno de ellos implementan una semántica diferente, pero algunas características similares son compartidas por un grupo de ellos. Los metodos son los siguientes:

- ### GET

El método GET  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.

- ### POST

El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

- ### HEAD

El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.

- ### PUT

El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

- ### DELETE
El método DELETE borra un recurso en específico.

- ### CONNECT
El método CONNECT establece un túnel hacia el servidor identificado por el recurso.

- ### OPTIONS
El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.

- ### TRACE
El método TRACE  realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.

- ### PATCH
El método PATCH  es utilizado para aplicar modificaciones parciales a un recurso.

## ¿Qué es una session en http?

En los protocolos basados en el modelo cliente-servidor, como es el caso del HTTP, una sesión consta de tres fases:

1-El cliente establece una conexión TCP (o la conexión correspondiente si la capa de transporte corresponde a otro protocolo).

2-El cliente manda su petición, y espera por la respuesta. 

3-El servidor procesa la petición, y responde con un código de estado y los datos correspondientes.

A partir del protocolo HTTP/1.1 la conexión, no se cierra al finalizar la tercera fase, y el cliente puede continuar realizando peticiones. Esto significa que la segunda y tercera fase, pueden repetirse cualquier número de veces.

## ¿Qué son las cookies?

Una cookie HTTP, cookie web o cookie de navegador es una pequeña pieza de datos que un servidor envía a el navegador web del usuario. El navegador guarda estos datos y los envía de regreso junto con la nueva petición al mismo servidor. Las cookies se usan generalmente para decirle al servidor que dos peticiones tienen su origen en el mismo navegador web lo que permite, por ejemplo, mantener la sesión de un usuario abierta. Las cookies permiten recordar la información de estado en vista a que el protocolo HTTP es un protocolo sin estado.

Las cookies se utilizan principalmente con tres propósitos:

- Gestión de Sesiones

- Personalización

- Rastreo

## ¿Como se utiliza el cache en http?

El rendimiento de los sitios web y las aplicaciones puede mejorarse significativamente al reutilizar los recursos previamente obtenidos. Los cachés web reducen la latencia y el tráfico de red y, por lo tanto, reducen el tiempo necesario para mostrar una representación de un recurso. Al hacer uso del almacenamiento en caché HTTP, los sitios web se vuelven más sensible.

## ¿Qué es https?

Para usar HTTPS con su nombre de dominio, debe instalar un certificado SSL o TLS en su sitio web. Es posible que su host web (proveedor de hosting web) ofrezca seguridad HTTPS, o bien usted puede solicitar un certificado SSL/TLS a las autoridades certificadoras y, luego, instalarlo por su cuenta. Es posible que los certificados SSL/TLS deban renovarse periódicamente.

## ¿Como conseguir que nuestro dominio tenga el certificado https?

Por HTTPS se entiende HyperText Transfer Procotol Secure o Protocolo Seguro de Transferencia de Hipertexto, que no es más que la versión segura del HTTP, es decir, una variante del mismo protocolo que se basa en la creación de un canal cifrado para la transmisión de la información, lo cual lo hace más apropiado para ciertos datos de tipo sensible (como claves y usuarios personales). Cada servidor tiene su propio proceso para instalar y actualizar certificados SSL/TLS. Para instalarlo hay que averiguar qué servidor usa su sitio web y seguir las instrucciones para instalar y actualizar el certificado.

Los siguientes servicios de Google emiten, instalan y renuevan automáticamente los certificados SSL/TLS sin costo adicional:

- Google Sites

- Google Mi Negocio

- Blogger

- Firebase

## ¿Qué es un servidor web o servidor HTTP?

Un servidor web o servidor HTTP es un programa informático que procesa una aplicación del lado del servidor, realizando conexiones bidireccionales o unidireccionales y síncronas o asíncronas con el cliente y generando o cediendo una respuesta en cualquier lenguaje o aplicación del lado del cliente. El código recibido por el cliente es renderizado por un navegador web. Para la transmisión de todos estos datos suele utilizarse algún protocolo. Generalmente se usa el protocolo HTTP para estas comunicaciones, perteneciente a la capa de aplicación del modelo OSI.

## ¿Que es Flask?

Flask es una aplicacion de framework web, la cual se usa principalmente para empezar en esta area de manera facil y sencilla dentro de los contextos de Python.

## ¿Que vamos a hacer en estas practica?

Vamos a crear un servidor web mediante la herramienta de Python en el cual cada usuario pueda conectarse y agregar una nueva palabra a una oracion creada entre muchos usuarios conectados

 Inspirado en https://flask.palletsprojects.com/en/2.1.x/quickstart/
 
 En un cmd:
   - pip install flask
   - set FLASK_APP=Servidor
   - flask run --host=0.0.0.0
   
 En el browser, entrar a http://localhost:5000
 
 ## Bibliografia
 
>https://concepto.de/protocolo-informatico/

>https://concepto.de/http/

>https://developer.mozilla.org/es/docs/Web/HTTP

>https://flask.palletsprojects.com/en/2.1.x/quickstart/


