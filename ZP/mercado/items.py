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

value_items =[['Superficie total','superficie_total']
            ,['Superficie cubierta','superficie_cubierta']
            ,['Dormitorios','dormitorios']
            ,['Ambientes','ambientes']
            ,['Baños','banos']
            ,['Expensas','expensas']
            ,['Pisos','pisos']
            ,['Disposici','disposicion']
            ,['Piso (unidad)','piso']
            ,['Departamentos por piso','departamentos_x_piso']
            ,['Cocheras','cocheras']
            ,['Tipo de departamento','tipo_departamento']
            ,['Antig','antiguedad']
           # ,['','']
            ]

check_items=[ ['Apto cr','apto_credito']
            ,['Aire acondicionado','con_aire']
            ,['Roof garden','con_jardin'] #Modificar, esta es una opcion
            ,['Jard','con_jardin'] #Modificar, esta es una opcion
            ,['arrilla','con_parrilla']
            ,['Pileta','con_pileta']
            ,['Apto profesional','apto_profesional']
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


"""
class MercadoXpaths():
    
    post_id = ''
    titulo = 'normalize-space(//li[@class="vip-title-breadcrumb"]/span/text())'
    precio = 'normalize-space(//article[@class="vip-price ch-price"]/strong/text())'
    moneda = ''    
    provincia = ''

    barrio = ''
    localizacion = 'normalize-space(//div[@class="section-location"]/text())'    
    tipo_propiedad = ''
    tipo_operacion = ''    
    #superficie_total = ''

    #superficie_cubierta = ''
    #dormitorios = ''
    #ambientes = ''
    #banos = 'normalize-space(//span[@class="vip-product-info__attribute-value xh-highlight"]/text())'
    #expensas = ''

    #piso = ''
    departamentos_x_piso = ''
    #pisos = ''
    tipo_departamento = ''
    #disposicion = ''

    condiciones_especiales = ''
    tipo_vendedor = ''
    vendedor = 'normalize-space(//span[contains(@class,"profile-info-data profile-info-name-data")]/a/text())' 
    fotos = ''
    latitud = ''

    longitud = ''
    cocheras = ''
    descripcion = ''
    #apto_credito = ''
    #con_aire = ''
    
    #con_jardin = ''
    #con_parrilla = ''
    #con_pileta = ''
    #apto_profesional = ''
    descripcion_xpath= 'normalize-space(//div[@class="description-content-main-group attribute-content"])'
    descripcion2_xpath= 'normalize-space(//div[@class="description-content-secondary-group attribute-content"])'
    #normalize-space(//section[6]/div[1]/div[2])
    def __getitem__(self, item):
        return getattr(self, item)

"""
class MercadoXpathsAlt():
    
    post_id = '//span[@class="publisher-code"]/text()'
    titulo = '//div[@class="section-title"]/h1/text()'
    precio_1 = 'normalize-space(//div[@class="price-items"]/span/text())'
    precio_2 = 'normalize-space(//span[@class="data-price"]/b/text())'
    moneda = 'normalize-space(//span[contains(@class,"price-tag-symbol")]/text())'    
    #provincia = ''

    barrio = ''
    localizacion_1 = 'normalize-space(//div[@class="section-location"])'   
    localizacion_2 = 'normalize-space(//h2[@class="info-location"])'   
    tipo_propiedad = 'normalize-space(//ul[@class="breadcrumb"])'
    tipo_operacion = 'normalize-space(//div[@class="block-price block-row"]/div/text())'    
    #superficie_total = ''

    #superficie_cubierta = ''
    #dormitorios = ''
    #ambientes = ''
    #banos = 'normalize-space(//span[@class="vip-product-info__attribute-value xh-highlight"]/text())'
    expensas = 'normalize-space(//div[@class="block-expensas block-row"]/span/text())'

    #piso = ''
    #departamentos_x_piso = ''
    #pisos = ''
    #tipo_departamento = ''
    #disposicion = ''

    #condiciones_especiales = ''
    #tipo_vendedor = ''
    vendedor = '//div[@class="contact-phone-box"]/a/@title/text()' 


    items_atrib = '//ul[@class="section-icon-features"]/li/span/text()'
    items_value = '//ul[@class="section-icon-features"]/li/b/text()'

    extra_items = '//section[@class="general-section article-section"]/ul/li/h4/text()'
  
    def __getitem__(self, item):
        return getattr(self, item)
