# -*- coding: utf-8 -*-
# scrapy crawl test
import re
import scrapy
from spider_movie_scrapy.items import SpiderMovieItem


class Dytt8Spider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/20180731/57174.html']
    category_urls = []
    movie_urls = []
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    }


    # 获取每部电影页面的url
    def parse(self, response):
        grid_view = response.css('.co_area2')
        content = grid_view.css('.co_content8 #Zoom p::text')
        # print('translateName: %s' % content[2])
        # print('title: %s' % content[3].strip())
        # print('time: %s' % content[4].strip())
        # print('placeOfOrigin: %s' % content[5].strip())
        # print('category: %s' % content[6].strip())
        # print('language: %s' % content[7].strip())
        # print('subtitle: %s' % content[8].strip())
        # print('dbScore: %s' % content[9].strip())
        # print('length: %s' % content[15].strip())
        # print('director: %s' % content[16].strip())

        # pattern = re.compile(r'主\s+演(.*?)◎简\s+介', re.S)
        # star = re.search(pattern, content).group(1)
        #
        # pattern1 = re.compile(r'简\s+介(.*)', re.S)
        # info = re.search(pattern, content).group(1)
        print(content)









