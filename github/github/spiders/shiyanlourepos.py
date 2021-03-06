# -*- coding: utf-8 -*-
import scrapy
from github.items import RepoItem

class ShiyanloureposSpider(scrapy.Spider):
    name = 'shiyanlourepos'
    # allowed_domains = ['github.com']
    # start_urls = ['http://github.com/']

    @property
    def start_urls(self):
    	return ('https://github.com/shiyanlou?page={}&tab=repositories'.format(i) for i in range(1,5))

    def parse(self, response):
    	for repo in response.css('li.col-12'):
            item = RepoItem()
            item['name'] = repo.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first('\s*(.+)')
            item['update_time'] = repo.css('div.mt-2 relative-time::attr(datetime)').re('([\d-]+).([\d:]+)')
            repo_url = response.urljoin(repo.xpath('.//div[contains(@class, "mb-1")]/h3/a/@href').extract_first())
            request = scrapy.Request(repo_url, callback=self.parse_repo)
            request.meta['item'] = item
            yield request

    def parse_repo(self, response):
        item = response.meta['item']
        data_list = response.css('li span.num::text').re('\s*(\d+)\s*')
        item['commits'] = int(data_list[0])
        item['branches'] = int(data_list[1])
        item['releases'] = int(data_list[2])
        yield item
	        # yield RepoItem({
	        	# 'name': repo.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first('\s*(.+)'),
	        	# 'update_time': repo.css('div.mt-2 relative-time::attr(datetime)').re('([\d-]+).([\d:]+)'),
                # repo_url = repo.
	        	# })
