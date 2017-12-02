# -*- coding: utf-8 -*-
import scrapy
from github.items import RepoItem

class ShiyanloureposSpider(scrapy.Spider):
    name = 'shiyanlourepos'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    @property
    def start_urls(self):
    	return ('https://github.com/shiyanlou?page={}&tab=repositories'.format(i) for i in range(1,5))

    def parse(self, response):
    	for repo in response.css('li.col-12'):
	        yield RepoItem({
	        	'name': repo.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first('\s*(.+)'),
	        	'update_time': repo.css('div.mt-2 relative-time::attr(datetime)').re('([\d-]+).([\d:]+)')
	        	})
