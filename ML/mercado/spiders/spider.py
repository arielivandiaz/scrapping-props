# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.selector import HtmlXPathSelector
from mercado.items import *
import time 

VERBOSE = 0
WRITE = 1
MAX_FILE = 25000
CHANGE_URL = 500



class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	item_count_main = 0
	allowed_domain = ['www.mercadolibre.com.ar']

	
	propiedad=""
	operacion=""
	zona=""
	ciudad=""
	vendedor=""
	start_from=""
	archivo=""


	url_count = 0
	urls_max = 2
	file_count = 0
	file_id = 0
	flag_started =  0

	filename = 'output_' 

	start_urls = ['https://inmuebles.mercadolibre.com.ar']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[contains(@class,"--next")]/a'))),
		#Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="results-item article grid"]/div')),
		#					callback = 'parse_item', follow = False)
		#//div[contains(@id,'MLA')]
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[contains(@id,"MLA")]')),
							callback = 'parse_item', follow = False)
	}

	def __init__(self, *a, **kw):   

		super(MercadoSpider, self).__init__(*a, **kw)
		
		key_parametros = 0
		print kw
		for key in kw:
			
			if key=='propiedad':	
				print "--> Key detected", key, " ", kw[key]
				self.propiedad=kw[key]
		
			if key=='operacion':
				print "--> Key detected", key, " ", kw[key]
				self.operacion=kw[key]
	
			if key=='zona':
				print "--> Key detected", key, " ", kw[key]
				self.zona=kw[key]

			if key=='ciudad':
				print "--> Key detected", key, " ", kw[key]
				self.ciudad=kw[key]

			if key=='vendedor':
				print "--> Key detected", key, " ", kw[key]
				self.vendedor=kw[key]
	
			if key=='start_from':
				print "--> Key detected", key, " ", kw[key]
				self.start_from=kw[key]
			if key=='parametros':
				key_parametros= True

				#depositos-y-galpones/alquiler/buenos-aires-interior/bahia-blanca
			if key=='archivo':
				print "--> Key detected", key, " ", kw[key]
				self.filename=kw[key]

		if key_parametros:
			self.start_urls[0] = self.start_urls[0] + '/' + kw['parametros'] 
		else:
			if self.propiedad:
				self.start_urls[0] =  self.start_urls[0] +'/' + str(self.propiedad)
				print "STARTED FROM -> ", self.start_urls[0]
			if self.operacion:
				self.start_urls[0] =  self.start_urls[0] +'/' + str(self.operacion)
				print "STARTED FROM -> ", self.start_urls[0]
			if self.zona:
				self.start_urls[0] =  self.start_urls[0] +'/' + str(self.zona)
				print "STARTED FROM -> ", self.start_urls[0]
			if self.ciudad:
				self.start_urls[0] =  self.start_urls[0] +'/' + str(self.ciudad)
				print "STARTED FROM -> ", self.start_urls[0]
			if self.vendedor:
				self.start_urls[0] =  self.start_urls[0] +'/' + str(self.vendedor)
				print "STARTED FROM -> ", self.start_urls[0]
			if self.start_from:    
				self.start_urls[0] =  self.start_urls[0] +'/_Desde_' + str(self.start_from)
				print "STARTED FROM -> ", self.start_urls[0]
		if self.archivo:
			self.filename = self.archivo
			print "STARTED FROM -> ", self.start_urls[0]




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


			precio = response.xpath('normalize-space(//article[@class="vip-price ch-price"]/strong/text())').extract_first()
			
			if WRITE:
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

			if len(precio.split(' '))< 2:
				
				if VERBOSE:	
					print "URL: " + response.request.url

				xpaths = MercadoXpathsAlt()


				operacion = response.xpath(xpaths['tipo_operacion']).extract()
					

				for item in operacion:
					if item.find("enta") > -1:
						data['tipo_operacion'] = "Venta"
					elif item.find("emporario") > -1:
						data['tipo_operacion'] = "Alquiler Temporario"
					elif item.find("lquiler") > -1:
						data['tipo_operacion'] = "Alquiler"

				for item in operacion:
					if item.find("asa") > -1:
						data['tipo_operacion'] = "Casa"
					elif item.find("epartament") > -1:
						data['tipo_operacion'] = "Departamento"
					else:
						data['tipo_operacion'] = "Otro"


				data['post_id'] = str(response.request.url).split('MLA-')[-1].split('-')[0]

				data['moneda'] = response.xpath(xpaths['moneda']).extract_first()
				data['precio'] = response.xpath(xpaths['precio']).extract_first()
				data['titulo'] = response.xpath(xpaths['titulo']).extract_first()

				data['vendedor'] = response.xpath(xpaths['vendedor']).extract_first()
				data['localizacion'] = response.xpath(xpaths['localizacion_1']).extract_first() +' '+ response.xpath(xpaths['localizacion_2']).extract_first()
				#data['titulo'] = response.xpath(xpaths[''])
				#data['titulo'] = response.xpath(xpaths[''])

				x= response.xpath('//li[@class="specs-item"]/strong/text()').extract()
				y = response.xpath('//li[@class="specs-item"]/span/text()').extract()
				
				for z in range(len(x)):					
			
					for a,b in value_items:	

						key = 0	
						
						if x[z].find(a.decode('utf8')) > -1: # > 0 ?
							key=b
							
	
						if key:
							data[key]=y[z]
							if VERBOSE:
								print x[z],'\t',data[key]


				descripcion_secundaria = response.xpath('//ul[@class="attribute-list"]/li/text()').extract()


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

		

			else: # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
				xpaths = MercadoXpaths()


				operacion = response.xpath(xpaths['tipo_operacion']).extract()
					

				for item in operacion:
					if item.find("enta") > -1:
						data['tipo_operacion'] = "Venta"
					elif item.find("emporario") > -1:
						data['tipo_operacion'] = "Alquiler Temporario"
					elif item.find("lquiler") > -1:
						data['tipo_operacion'] = "Alquiler"

				for item in operacion:
					if item.find("asa") > -1:
						data['tipo_propiedad'] = "Casa"
					elif item.find("epartament") > -1:
						data['tipo_propiedad'] = "Departamento"
					else:
						data['tipo_propiedad'] = "Otro"


				data['post_id'] = str(response.request.url).split('MLA-')[-1].split('-')[0]

				data['moneda'] = precio.split(' ')[0]
				data['precio']  = precio.split(' ')[-1]

				data['vendedor'] = response.xpath(xpaths['vendedor']).extract_first()
				data['localizacion'] = response.xpath(xpaths['localizacion_1']).extract_first() +' '+ response.xpath(xpaths['localizacion_2']).extract_first()

				for item in cosntant_items:
					if xpaths[item] != '':
						data[item] = response.xpath(xpaths[item]).extract_first()
						if VERBOSE:
							print item," : ",data[item]
				

				

				if VERBOSE:
					print "Mondeda : ",data['moneda']
					print "Precio : ",data['precio']
				
				x= response.xpath('//li/span[@class="attribute-key"]/text()').extract()
				y = response.xpath('//li/span[@class="attribute-value"]/text()').extract()
				
				for z in range(len(x)):					
					key = 0
					for a,b in value_items:				
						if x[z].find(a.decode('utf8'))  > -1:
							key=b
					
					if key:
						data[key]=y[z]
						if VERBOSE:
							print x[z],'\t',data[key]
			
					

				if VERBOSE: print '*'*50

				descripcion_secundaria = response.xpath('//div[@class="description-content-secondary-group attribute-content"]/div/ul/li/text()').extract()


				for point  in descripcion_secundaria:
					if VERBOSE:
						print point
					key = 0
					keyword=""
					for a,b in check_items:
						if  a in point:
							if VERBOSE:
								print "ENCONTRADO '\t' !!! \t' !!!", key
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
				
				file.write(data[value].encode('utf-8').replace(',',' '))
				file.write(',')		
			
				
			file.close()

			self.item_count += 1
			self.item_count_main += 1
			self.file_count += 1

			if self.item_count > CHANGE_URL:
				self.item_count == 0
				self.url_count +=1
				time.sleep(60)
				if self.url_count == self.urls_max:
					self.url_count = 0
	

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
