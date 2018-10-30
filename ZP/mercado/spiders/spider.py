# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.selector import HtmlXPathSelector
from mercado.items import *


VERBOSE = 0
WRITE = 1
MAX_FILE = 25000
CHANGE_URL = 500


class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	item_count_main = 0
	allowed_domain = ['www.zonaprop.com.ar']

	url_count = 0
	urls_max = 2
	file_count = 0
	file_id = 0

	filename = 'output_' 

	start_urls = ['https://www.zonaprop.com.ar/inmuebles.html']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[contains(@class, "pagination-action-next")]/a'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h4[@class="aviso-data-title"]')),
						   callback = 'parse_item')
			
	}
	def __init__(self, *a, **kw):   

		super(MercadoSpider, self).__init__(*a, **kw)
		

		print kw
		for key in kw:
			
			if key=='parametros':
				self.start_urls[0] = 'https://www.zonaprop.com.ar/' + kw[key] + '.html'
			if key=='archivo':			
				self.filename=kw[key]

	
	def parse_item(self, response):
		


		
		if True:

			data = MercadoItem()
			xpaths =MercadoXpathsAlt()

			if self.file_count > MAX_FILE:
				self.file_id+=1
				self.file_count=0


			if WRITE: file = open(self.filename + str(self.file_id) + '.csv' , 'a')

			if self.file_count == 0:
				if WRITE: 					
					for value in all_values:				
						
						file.write(str(value))						
						file.write(',')

		
			operacion = response.xpath(xpaths['tipo_operacion']).extract()
			precio = response.xpath(xpaths['precio_1']).extract()
		
			
			data['post_id'] = ""
			data['titulo'] = ""
			data['precio'] = ""
			data['moneda'] = ""
			data['provincia'] = ""

			data['barrio'] = ""
			data['localizacion'] = ""
			data['tipo_propiedad'] = ""
			data['tipo_operacion'] = ""
			data['superficie_total'] = ""

			data['superficie_cubierta'] = ""
			data['dormitorios'] = ""
			data['ambientes'] = ""
			data['banos'] = ""
			data['expensas'] = ""

			data['piso'] = ""
			data['departamentos_x_piso'] = ""
			data['pisos'] = ""
			data['tipo_departamento'] = ""
			data['disposicion'] = ""

			data['condiciones_especiales'] = ""
			data['tipo_vendedor'] = ""
			data['vendedor'] = ""
			data['fotos'] = ""
			data['latitud'] = ""

			data['longitud'] = ""
			data['cocheras'] = ""
			data['descripcion'] = ""
			data['apto_credito'] = ""
			data['con_aire'] = ""

			data['con_jardin'] = ""
			data['con_parrilla'] = ""
			data['con_pileta'] = ""
			data['apto_profesional'] = ""

			data['antiguedad'] = ""
			data['url'] = ""
			
			for item in operacion:
				if item.find("Venta") > -1 and item.find("Alquiler") > -1:

					data['tipo_operacion'] = "Venta y Alquiler"


				elif item.find("Venta") > -1:
					data['tipo_operacion'] = "Venta"
					if str(precio).find("onsultar") >-1:
						data['moneda'] = str(precio[0])
						data['precio']  = str(precio[0])
					else:
						data['moneda'] = str(precio[0]).split(' ')[0]
						data['precio']  = str(precio[0]).split(' ')[-1]

				elif item.find("Alquiler") > -1:
					data['tipo_operacion'] = "Alquiler"
					data['moneda'] = str(precio[0]).split(' ')[0]
					data['precio']  = str(precio[0]).split(' ')[-1]

				else:
					precio = response.xpath(xpaths['precio_2']).extract()
					data['tipo_operacion'] = "Emprendimiento"
					print " >>>> ", str(precio)
					data['moneda'] = str(precio[0]).split(' ')[0]
					data['precio']  = str(precio[0]).split(' ')[-1]

					if str(precio).find("onsultar") >-1:
						data['moneda'] = str(precio[0])
						data['precio']  = str(precio[0])
					else:
						data['moneda'] = str(precio[0]).split(' ')[0]
						data['precio']  = str(precio[0]).split(' ')[-1]
					
				
		

			data['titulo'] = str(response.xpath(xpaths['titulo']).extract()[0]).encode('utf-8')
			data['post_id'] = response.xpath(xpaths['post_id']).extract()[-1]
		
			data['vendedor'] = str(response.xpath(xpaths['vendedor'])).encode('utf-8')
			data['localizacion'] = str(response.xpath(xpaths['localizacion_1']).extract()[0]).encode('utf-8')
			
			if len (data['localizacion']) <5:
				data['localizacion'] = str(response.xpath(xpaths['localizacion_2']).extract()[0]).encode('utf-8')
				
			tipo = 	response.xpath(xpaths['tipo_propiedad']).extract()		
			for asd in tipo: print 'asd',asd

			if str(tipo).find("epartamento") > -1:
				data['tipo_propiedad'] = 'Departamento'
			elif str(tipo).find("ocal") > -1:
				data['tipo_propiedad'] = 'Local Comercial'
			elif str(tipo).find("errreno") > -1:
				data['tipo_propiedad'] = 'Terreno'
			elif str(tipo).find("Casa") > -1:
				data['tipo_propiedad'] = 'Casa'
			else:
				data['tipo_propiedad'] = 'Otro'



			data['expensas'] = response.xpath(xpaths['expensas']).extract_first()

			x = response.xpath(xpaths['items_atrib']).extract()
			y = response.xpath(xpaths['items_value']).extract()

			for z in range(len(x)):	
				for a,b in value_items:	
					key = 0							
					if x[z].find(a.decode('utf8')) > -1: # > 0 ?
						key=b	
			
					if key:
						data[key]=y[z]
						if VERBOSE:
							print x[z],'\t',data[key]


			descripcion_secundaria = response.xpath(xpaths['extra_items']).extract()

			
			for point  in descripcion_secundaria:
				if VERBOSE:
					print point
				key = 0
				keyword=""
				
				for a,b in check_items:
					if  a in point: # > 0 ?
						
						key=b
						keyword=a
				if key:
					data[key]='Si'
					if VERBOSE:
						print keyword,'\t',data[key]

			data['url'] = str(response.request.url)
							
				
			if VERBOSE: print '*'*50
			
					
			file.write('\r\n')
			for value in all_values:				
				
				file.write(str(data[value]).encode('utf-8').replace(',',' ').replace(';',' '))
				
				file.write(',')
		
			file.close()
			

			self.item_count += 1
			self.item_count_main += 1
			self.file_count += 1

			if self.item_count > CHANGE_URL:
				self.item_count == 0
				self.url_count +=1
				if self.url_count == self.urls_max:
					self.url_count = 0

				print
				print  "******** > ", self.start_urls
				print

			print '*'*50
			print "===>> Cantidad de elementos: " ,self.item_count_main, "*"		
			print "===>> Last URL : ",  str(response.request.url)
			print '*'*50
		else:
			print '*'*50
			print "===>> Cantidad de elementos: " ,self.item_count_main, "*"		
			print "===>> Last URL : ",  str(response.request.url)
			print '*'*50
			raise CloseSpider('item_exceeded')

			
		yield data
