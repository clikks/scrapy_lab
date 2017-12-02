# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from github.models import engine, Repository
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class GithubPipeline(object):
    def process_item(self, item, spider):
    	item['update_time'] = 
        return item
