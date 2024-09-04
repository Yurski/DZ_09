import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        # Парсинг цитат
        for quote in response.css('div.quote'):
            author_name = quote.css('small.author::text').get()
            author_url = quote.css('span small a::attr(href)').get()
            yield {
                'text': quote.css('span.text::text').get(),
                'author': author_name,
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            if author_url:
                author_url = response.urljoin(author_url)
                yield scrapy.Request(author_url, callback=self.parse_author, meta={'author_name': author_name})

        # Перехід на наступну сторінку
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        author_name = response.meta['author_name']
        birthdate = response.css('span.author-born-date::text').get()
        birthplace = response.css('span.author-born-location::text').get()
        description = response.css('div.author-description::text').get()

        yield {
            'name': author_name,
            'birthdate': birthdate,
            'birthplace': birthplace,
            'description': description,
        }
