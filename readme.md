# Scraping Propiedades
### Mercado Libre, ZonaProp, Argenprop

[![N|Solid](https://www.nexosmart.com.ar/images/logo-light-197x32.png)](https://nodesource.com/products/nsolid)

### Requerimientos

* [Python 2.7] 
* [Scrapy] - Instalable desde "pip install scrapy"
* [Pillow] - Instalable desde "pip install Pillow"
* Para Linux : es posible que sea necesario ejecutar el programa con permisos de superusuario



# MercadoLibre
Para correr el Scraping sobre Mercadolibre entrar a la carpeta ML y ejecutar el comando correspondiente:
```sh
$ sudo scrapy crawl mercado 
```  
Este ultimo comando escribe por defecto la salida en el archivo Output_0.csv. Si este archino no existe lo crea y si existe sigue escribiendo desde el final.

Para ejecutar una busqueda personalizada se pueden agregar parametros de la siguiente manera:
```sh
sudo scrapy crawl mercado -a start_from=66 -a propiedad=casas -a zona=bsas-gba-norte -a operacion=venta -a ciudad=escobar -a archivo=MLescobar -a vendedor=inmobiliaria 
```  
Todos los parametros son opcionales, para el caso de archivo si este no esta presente la salida siempre será en el archivo Output_0.csv. A continuación se listan estos parametros:
- start_from : Comienza la busqueda desde el item N°#, (no desde la pagina)
- propiedad : El parametro correspondiente a la categoria de "Inmueble" de MercadoLibre
 - zona El parametro correspondiente a la categoria de "Zona" de MercadoLibre, tal cual figura en la URL
- operacion : Correspondiente a venta, alquiler o alquiler-temporario
- ciudad :  Ciudad de busqueda tal cual esta escrita en la URL 
- archivo : Nombre del archivo de salida
- vendedor : Opción de "inmobiliaria" o "dueno-directo"



Otra forma de realziar un scrapping avanzado es usar los parametros propios de la URL de mercadolibre, agregando el argumento "parametros" seguido de los filtros utilizados.
Por ejemplo para realizar scrapping sobre la dirección "https://inmuebles.mercadolibre.com.ar/depositos-y-galpones/alquiler/buenos-aires-interior/bahia-blanca" y guardar la salida en un archivo llamado "galponesBahia.csv" el comando seria el siguiente:
```sh
sudo scrapy crawl mercado -a parametros=depositos-y-galpones/alquiler/buenos-aires-interior/bahia-blanca -a archivo=galponesBahia
```  
### Observaciones

>Mercadolibre no da acceso a la lista completa de propiedades, es posible obtener información de hasta 50 paginas, dependiendo de la carga de la categoria/servicio, más allá de eso MercadoLibre deja de proporcinar items para continuar la busqueda y te pide que realizes una busqueda avanzada para obtener más propiedades.

# Zonaprop

Para correr el scraping sobre Zonaprop entrar a la carpeta ZP y ejecutar el comando correspondiente:
```sh
$ sudo scrapy crawl mercado 
```  
Si se desea realziar una busqueda avanzada es necesario conocer la terminación de la URL correspondiente, por ejemplo para el caso de  "https://www.zonaprop.com.ar/inmuebles-capital-federal-entre-5-y-10-anos.html" el comando necesario es el siguinte:
```sh
$ sudo scrapy crawl mercado -a parametros=inmuebles-capital-federal-entre-5-y-10-anos -a archivo=scrapZonaProp
``` 


# Argenprop

Para correr el scraping sobre Argenprop entrar a la carpeta AP y ejecutar el comando correspondiente:
```sh
$ sudo scrapy crawl mercado 
```  

El parametro soportado para esta pagina es solamente el nombre del archivo de salida, el cual se puede especificar de la siguiente manera:
```sh
$ sudo scrapy crawl mercado -a archivo=scrapArgenprop
```  
Generando la salida de dados en el archivo "scrapArgenprop.csv", si este no existe se lo crea y si este existe se comienza a escribir sobre el final. En el caso de no utilizar el parametro archivo la salida por defecto es "Output_0.csv"



### Observaciones

> Este sitio tiene una key unicá para mostrar cada parametro de busqueda, por este motivo no se puede navegar por las distintas categorias. Si se desea realziar una busqueda avanzada se debera contemplar esta situación para cada caso de forma particular. En la versión actual esta contemplado las URL  de "Propiedades" y "Alquileres en Argentina". A tener en cuenta que los alquielres corresponden al 10% de las publicaciones en total.


