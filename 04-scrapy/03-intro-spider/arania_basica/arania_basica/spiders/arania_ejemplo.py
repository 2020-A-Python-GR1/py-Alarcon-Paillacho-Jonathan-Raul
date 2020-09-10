import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()


        precio = etiqueta_contenedora.css(
            'div > p.price_color::text'
        ).extract()

        stock = etiqueta_contenedora.css(
            'div > p.instock availability > i.icon-ok::text'
        ).extract()

        imagen = etiqueta_contenedora.css(
            'div > a > img.src::text'
        ).extract()

        print(titulos)
        print(precio)
        print(stock)
        print(imagen)