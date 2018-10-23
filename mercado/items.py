# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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

    #titulo = scrapy.Field()
    #modelo = scrapy.Field()
    #marca = scrapy.Field()
    #tecnologia = scrapy.Field()
    #tipo = scrapy.Field()
    #precio = scrapy.Field()
    #condicion = scrapy.Field()
    #envio = scrapy.Field()
    #ubicacion = scrapy.Field()
    #opiniones = scrapy.Field()

    #imagenes
    #image_urls = scrapy.Field()
    #images = scrapy.Field()
    #image_name = scrapy.Field()


    #info de la tienda o vendedor
    #vendedor_url = scrapy.Field()
    #tipo_vendedor = scrapy.Field()
    #ventas_vendedor = scrapy.Field()
