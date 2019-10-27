# -*- coding: utf-8 -*-
import scrapy


class Parcer1Spider(scrapy.Spider):
    name = 'parcer1'
    allowed_domains = ['https://bookmaker-ratings.ru']
    start_urls = ['https://bookmaker-ratings.ru/review/obzor-bukmekerskoj-kontory-ligastavok/all-feedbacks/']

    def parse(self, response):
        for block in response.css('#feedbacks-list .single'):
            yield {
                'user_name': block.css('.namelink::text').get(),
                'review_date': block.css('.date::text').get(),
                'review_description': block.css('.use-default-ui p::text').get(),
                 }

        # next_page = response.css('.pager-item nth::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
