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
	allowed_domain = ['www.argenprop.com']

	url_count = 0
	urls_max = 2
	file_count = 0
	file_id = 0

	filename = 'output_' 

	urls = [
			'https://www.argenprop.com/Propiedades/',
			'https://www.argenprop.com/Propiedades-Alquiler-Argentina/af_817Kaf_100000001KvnQVistaResultadosKvncQVistaGrilla'
			]
	start_urls = ['https://www.argenprop.com/Propiedades-Alquiler-Argentina/af_817Kaf_100000001KvnQVistaResultadosKvncQVistaGrilla']



	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="pagination-next"]/a'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="paginado-next"]/a'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//p[@class="address"]/a')),
						   callback = 'parse_item')
			
	}
	def __init__(self, *a, **kw):   

		super(MercadoSpider, self).__init__(*a, **kw)
		

		print kw
		for key in kw:

			if key=='archivo':			
				self.filename=kw[key]

	
	
	
	def parse_item(self, response):
		
		
		#if self.item_count_main <  50000: 
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
			

			operacion = response.xpath(xpaths['tipo_operacion']).extract()
			precio_aux = str(response.xpath(xpaths['precio']).extract())
			precio_aux_2 = []
			moneda_aux = []
			for a in precio_aux:
				if a.isdigit():
					precio_aux_2.append(a)
				else:
					moneda_aux.append(a)

			data['precio'] = ''.join(precio_aux_2) 
			data['moneda'] = str(''.join(moneda_aux)).replace(" .']",'').replace("[u'",'')

		
			

			for item in operacion:
				if item.find("enta") > -1:
					data['tipo_operacion'] = "Venta"
				elif item.find("lquiler") > -1:
					data['tipo_operacion'] = "Alquiler"
					
		

			data['titulo'] = str(response.xpath(xpaths['titulo']).extract()[0]).encode('utf-8')
			data['post_id'] = str(response.xpath(xpaths['post_id']).extract()[0]).encode('utf-8')
		
			data['vendedor'] = str(response.xpath(xpaths['vendedor']).extract()).replace("']",'').replace("[u'",'')
			data['localizacion'] = str(response.xpath(xpaths['localizacion']).extract()[0]).encode('utf-8')
			

				
			tipo = 	response.xpath(xpaths['tipo_propiedad']).extract()		
		
			if str(tipo).find("epartamento") > -1:
				data['tipo_propiedad'] = 'Departamento'
			elif str(tipo).find("ocal") > -1:
				data['tipo_propiedad'] = 'Local Comercial'
			elif str(tipo).find("errreno") > -1:
				data['tipo_propiedad'] = 'Terreno'
			elif str(tipo).find("casa") > -1:
				data['tipo_propiedad'] = 'Casa'
			else:
				data['tipo_propiedad'] = 'Otro'

	
			x = response.xpath(xpaths['items_atrib']).extract()
			y = response.xpath(xpaths['items_value']).extract()

			condiciones_especiales = []
		
			for z in range(len(y)):	

							

				for a,b in value_items:	
					key = 0							
					if x[z].find(a.decode('utf8')) > -1: # > 0 ?
						key=b	
				
					if key:
					
						data[key]=str(y[z]).replace(' ','').replace('\r\n','')
						if VERBOSE:
							print x[z],'\t',data[key]
					

			for point  in x:
				if VERBOSE:
					print point
				key = 0
				keyword=""
				
				for a,b in check_items:
					if  a in point: 
						
						key=b
						keyword=a
				if key:
					data[key]='Si'
					if VERBOSE:
						print keyword,'\t',data[key]
				condiciones_especiales.append(point)
			
			data['url'] = str(response.request.url)
			
			data['condiciones_especiales']=  str('/'.join(condiciones_especiales))		
			data['descripcion']	= str(response.xpath(xpaths['descripcion']).extract()).replace("']",'').replace("[u'",'')
				
			if VERBOSE: print '*'*50
			
			if WRITE: 	
				file.write('\r\n')			
				for value in all_values:				
					
					file.write(str(data[value]).replace(',',' ').encode('utf-8'))
					
					file.write(',')
			
				file.close()

			"""
			print '*'*50
			print self.item_count 
			print self.item_count_main 
			print self.file_count 

			if self.item_count > 3:
				self.item_count == 0
				self.url_count +=1
				if self.url_count == self.urls_max:
					self.url_count = 0
			
				self.start_urls = self.urls[self.url_count]
			print '*'*50
			""" 
			self.item_count += 1
			self.item_count_main += 1
			self.file_count += 1

			if self.item_count > CHANGE_URL:
				self.item_count == 0
				self.url_count +=1
				if self.url_count == self.urls_max:
					self.url_count = 0

			
				self.start_urls = self.urls[self.url_count]
				print
				print  "******** > ", self.start_urls
				print


		#if self.item_count > 3:

		else:

			
			raise CloseSpider('item_exceeded')

			
		yield data
