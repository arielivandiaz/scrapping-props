# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.ar']

	tipo_transaccion = "venta"
	tipo_propiedad = "departamentos"
	start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/venta/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[contains(@class,"--next")]/a'))),
		#Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="results-item article grid"]/div')),
		#					callback = 'parse_item', follow = False)
		#//div[contains(@id,'MLA')]
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[contains(@id,"MLA")]')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		ml_item['titulo'] = response.xpath('normalize-space(//li[@class="vip-title-breadcrumb"]/span/text())').extract_first()
		ml_item['precio'] = response.xpath('normalize-space(//article[@class="vip-price ch-price"]/strong/text())').extract()
		ml_item['localizacion'] = response.xpath('normalize-space(//h2[@class="map-location"]/text())').extract()
		
		#ml_item['tecnologia'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div/section[2]/ul/li[1]/span)').extract()
		#ml_item['tipo'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div/section[2]/ul/li[2]/span)').extract()
		#ml_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
		#ml_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		#ml_item['envio'] = response.xpath('normalize-space(//p[contains(@class, "shipping-method-title")]/text())').extract()
		#ml_item['ubicacion'] = response.xpath('normalize-space(//p[contains(@class, "card-description")])').extract()
		#ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		#imagenes del producto
		#ml_item['image_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
		#ml_item['image_name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		#info de la tienda o vendedor
		#ml_item['vendedor_url'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
		#ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		#ml_item['ventas_vendedor'] = response.xpath('normalize-space(//div[@class="feedback-title"]/text())').extract()
		self.item_count += 1
		if self.item_count > 50:
			raise CloseSpider('item_exceeded')
		yield ml_item
