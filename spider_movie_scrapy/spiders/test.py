# -*- coding: utf-8 -*-
# scrapy crawl test
import re
import scrapy
from spider_movie_scrapy.items import SpiderMovieItem


class Dytt8Spider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/20180528/56912.html']
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

        name = grid_view.css('.title_all h1 font::text').extract_first()
        imgUrl = grid_view.css('.co_content8 #Zoom p img::attr(src)').extract_first()
        # content = grid_view.css('.co_content8 #Zoom p::text').extract()
        magneticLink = grid_view.css('.co_content8 #Zoom p a::attr(href)').extract_first()
        downloadUrl = grid_view.css('.co_content8 #Zoom table td a::attr(href)').extract_first()

        content = grid_view.css('.co_content8 #Zoom').extract_first()
        # print(content)

        translateName = re.search(r'译\s+名(.*?)<br>', content).group(1)
        title = re.search(r'片\s+名(.*)', content).group(1)
        # time = re.search(r'年\s+代(.*)', content).group(1)
        # place = re.search(r'(产\s+地|国\s+家)(.*?)<br>', content).group(2)
        # category = re.search(r'类\s+别(.*)', content).group(1)
        # language = re.search(r'语\s+言(.*)', content).group(1)
        # subtitle = re.search(r'字\s+幕(.*)', content).group(1)
        # dbScore = re.search(r'豆瓣评分(.*)', content).group(1)
        # length = re.search(r'片\s+长(.*)', content).group(1)
        # director = re.search(r'导\s+演(.*)', content).group(1)
        #
        # pattern = re.compile(r'主\s+演(.*).*?简\s+介', re.S)
        # star = re.search(pattern, content).group(1)
        # info = re.search(r'简\s+介.*?<br><br>(.*?)<br>', content).group(1)

        print('translateName: %s' % translateName.strip())
        print('title: %s' % title.strip())
        # print('time: %s' % time.strip())
        # print('place: %s' % place.strip())
        # print('category: %s' % category.strip())
        # print('language: %s' % language.strip())
        # print('subtitle: %s' % subtitle.strip())
        # print('dbScore: %s' % dbScore.strip())
        # print('length: %s' % length.strip())
        # print('director: %s' % director.strip())
        # print('star: %s' % star.strip())
        # print('info: %s' % info.strip())
        # 存入数据库
        item = SpiderMovieItem()
        item['name'] = name
        # item['imgUrl'] = imgUrl
        # item['magneticLink'] = magneticLink
        # item['downloadUrl'] = downloadUrl
        #
        item['translateName'] = translateName.strip()
        item['title'] = title.strip()
        # item['time'] = time.strip()
        # item['place'] = place.strip()
        # item['category'] = category.strip()
        # item['language'] = language.strip()
        # item['subtitle'] = subtitle.strip()
        # item['dbScore'] = dbScore.strip()
        # item['length'] = length.strip()
        # item['director'] = director.strip()
        # item['star'] = star.strip()
        # item['info'] = info.strip()

        # translateName = re.search(r'译\s+名(.*?)<br>', content).group(1)
        # title = re.search(r'片\s+名(.*?)<br>', content).group(1)
        # time = re.search(r'年\s+代(.*?)<br>', content).group(1)
        # place = re.search(r'(产\s+地|国\s+家)(.*?)<br>', content).group(2)
        # category = re.search(r'类\s+别(.*?)<br>', content).group(1)
        # language = re.search(r'语\s+言(.*?)<br>', content).group(1)
        # subtitle = re.search(r'字\s+幕(.*?)<br>', content).group(1)
        #
        # length = re.search(r'片\s+长(.*?)<br>', content).group(1)
        # director = re.search(r'导\s+演(.*?)<br>', content).group(1)

        # print(content)
        # 存入数据库
        # item = SpiderMovieItem()
        # item['name'] = name
        # item['imgUrl'] = imgUrl
        # item['magneticLink'] = magneticLink
        # item['downloadUrl'] = downloadUrl
        #
        # item['translateName'] = translateName.strip()
        # item['title'] = title.strip()
        # item['time'] = time.strip()
        # item['place'] = place.strip()
        # item['category'] = category.strip()
        # item['language'] = language.strip()
        # item['subtitle'] = subtitle.strip()
        # item['length'] = length.strip()
        # item['director'] = director.strip()


        # try:
        #     dbScore = re.search(r'豆瓣评分(.*?)<br>', content).group(1)
        #     pattern = re.compile(r'主\s+演(.*?)<br><br>', re.S)
        #     star = re.search(pattern, content).group(1)
        #     info = re.search(r'简\s+介.*?<br><br>(.*?)<br>', content).group(1)

            # item['dbScore'] = dbScore.strip()
            # item['star'] = star.strip()
            # item['info'] = info.strip()
        # except Exception:
        #     pass










