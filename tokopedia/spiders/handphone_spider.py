import scrapy
import logging

class HandphoneSpider(scrapy.Spider):
	name = 'tokopedia-handphone'
	allowed_domains = ['www.tokopedia.com', 'ta.tokopedia.com']
	download_delay = 1

	def __init__(self, max_items='', *args, **kwargs):
		super(HandphoneSpider, self).__init__(*args, **kwargs)
		self.item = 0
		self.max_items = 100
		self.page = 1

		# ob=5, refers to tokopedia filter option sort by "Review"
		self.base_url = "https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page={}"
		self.request_url = self.base_url.format(self.page)

	def start_requests(self):
		yield scrapy.Request(
            self.request_url,
            callback=self.parse
        )


	def parse(self, response):
		if self.item == self.max_items:
			return
		# products = response.xpath("//div[@class='css-bk6tzz e1nlzfl3']/a")
		products = response.xpath("//div[@class='css-bk6tzz e1nlzfl2']")
		for product in products:
			if self.item == self.max_items:
				return
				# break

			product_link = product.xpath("./a/@href").get()

			# Detail product page is forbidden by the host
			# Thus, can't get product description 
			# yield scrapy.Request(
			# 	url = product_link,
			# 	callback = self.parse_detail
			# 	)

			# Payload
			product_name = product.xpath(".//div[2]/div[2]/span[1]/text()").get()
			# product_description 
			product_image = product.xpath(".//div[2]/div[1]//div/div/img/@src").get()
			product_price = product.xpath(".//div[2]/div[2]/div/div/span/text()").get()
			for _ in range(5,0,-1): #looping from 5 to 1
				product_rating = product.xpath(f".//div[2]/div[2]/div[3]/div/img[{_}]/@src").get()
			merchant_name = product.xpath(".//div[2]/div[2]/div[2]/div/span[2]/text()").get()

			self.item += 1

			yield {
				"product_name": product_name,
				"product_image": product_image,
				"product_price": product_price,
				"product_rating": product_rating,
				"merchant_name": merchant_name,
			}

		self.page += 1
		yield scrapy.Request(
	        url = self.base_url.format(self.page),
	        callback = self.parse)
		return