import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' #Heredado # este el nombre de la araña

    allowed_domains = [ # Esto es heredado y es un override
        'un.org' 
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    #vamos a definir reglas 
    regla_uno = ( # Esto es una tupla
        Rule(
            LinkExtractor(),
            callback= 'parse_page' # Nombre de la funcion a ejecutar para parsear
        ),
        # Segundo parámetro vacío 
    )

    #rules = regla_uno # Heredado, aquí vamos a agregar las reglas
    

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ), callback = 'parse_page'
        ),
        # Parametro vacío
    )

    rules = regla_dos

    #la Clase
    def parse_page(self, response):
        lista_programas = response.css('div.field-items>div.field-item>h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+' ,encoding = 'utf-8') as archivo:
                archivo.write(agencia + '\n')