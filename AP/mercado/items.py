# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

cosntant_items = ['titulo','localizacion']
test_items=['titulo','precio','localizacion']

items = ['provincia','barrio','localizacion','tipo_propiedad',
'tipo_operacion','condiciones_especiales',
'tipo_vendedor','vendedor','fotos','latitud','longitud','descripcion','','',
'','','','']

value_items =[['up. cubierta','superficie_cubierta']
            ,['up. descubierta','superficie_total']
            ,['ormitorios','dormitorios']
            ,['mbientes','ambientes']
            ,['baños','banos']
            ,['xpensas','expensas']
            ,['ant. pisos','pisos']
            ,['isposici','disposicion']
            ,['iso (unidad)','piso']
            ,['eptos. por piso','departamentos_x_piso']
            ,['ocheras','cocheras']
            ,['ipo de unidad','tipo_departamento']
            ,['xpensas','expensas']
            ,['antig','antiguedad']
            ,['pto Cr','apto_credito']  
           # ,['','']
            ]

check_items=[ #['Apto Cr','apto_credito']
             ['Aire acondicionado','con_aire']
            ,['Roof garden','con_jardin'] #Modificar, esta es una opcion
            ,['Jard','con_jardin'] #Modificar, esta es una opcion
            ,['arrilla','con_parrilla']
            ,['Pileta','con_pileta']
            ,['Apto Profesional','apto_profesional']
            #,['','']            
            ]

all_values = ['post_id','titulo','precio','moneda',   'provincia','barrio','localizacion','tipo_propiedad','tipo_operacion',
            'superficie_total','superficie_cubierta','dormitorios','ambientes','banos','expensas','piso','departamentos_x_piso',
            'pisos','antiguedad','tipo_departamento','disposicion','condiciones_especiales','tipo_vendedor','vendedor','fotos','latitud',
            'longitud','cocheras','descripcion','apto_credito','con_aire','con_jardin','con_parrilla','con_pileta','apto_profesional','url']

class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de la propiedad
    post_id = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    moneda = scrapy.Field()    
    provincia = scrapy.Field()

    barrio = scrapy.Field()
    localizacion = scrapy.Field()    
    tipo_propiedad = scrapy.Field()
    tipo_operacion = scrapy.Field()    
    superficie_total = scrapy.Field()

    superficie_cubierta = scrapy.Field()
    dormitorios = scrapy.Field()
    ambientes = scrapy.Field()
    banos = scrapy.Field()
    expensas = scrapy.Field()

    piso = scrapy.Field()
    departamentos_x_piso = scrapy.Field()
    pisos = scrapy.Field()
    tipo_departamento = scrapy.Field()
    disposicion = scrapy.Field()

    condiciones_especiales = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    vendedor = scrapy.Field()
    fotos = scrapy.Field()
    latitud = scrapy.Field()

    longitud = scrapy.Field()
    cocheras = scrapy.Field()
    descripcion = scrapy.Field()
    apto_credito = scrapy.Field()
    con_aire = scrapy.Field()
    
    con_jardin = scrapy.Field()
    con_parrilla = scrapy.Field()
    con_pileta = scrapy.Field()
    apto_profesional = scrapy.Field()
    
    antiguedad = scrapy.Field()
    url = scrapy.Field()


class MercadoXpathsAlt():
    
    post_id = '//div[@class="code-container"]/span/text()'
    titulo = 'normalize-space(//div[@class="address"]/h2/text())'
    precio = 'normalize-space(//div[@class="price"]/p/text())'

    barrio = ''
    localizacion = 'normalize-space(//h2[@class="ubicacion-description"])'       
    tipo_propiedad = 'normalize-space(//div[@class="address"]/p/text())'
    tipo_operacion = 'normalize-space(//div[@class="address"]/p/text())'    

    expensas = 'normalize-space(//p[@class="price-expensas"]/text())'

    vendedor = 'normalize-space(//div[@class="clearfix"]/div/div/p/a/text())' 


    items_atrib = '//div[@class="field"]/text()'
    items_value = '//div[@class="value"]/text()'

    extra_items = '//div[@class="field"]/text()'

    descripcion = 'normalize-space(//div[@id="aviso-description"]/text())'
  
    def __getitem__(self, item):
        return getattr(self, item)
