#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import scrapy

class GithubRepoSpider(scrapy.Spider):
	name = 'githubrepo'
	def start_requests(self):
		repo_url = 'https://github.com/shiyanlou?page={}&tab=repositories'
		urls = (repo_url.format(i) for i in range(1,5))
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
		

	def parse(self,response):
		for repo in response.css('li.col-12'):
			yield {

			'name': repo.xpath('.//div[contains(@class, "mb-1")]/h3/a/text()').re_first('\s*(.+)'),
			'update_time': repo.css('div.mt-2 relative-time::attr(datetime)').extract_first()
				}
		

