# -*- coding: utf-8 -*-
# scrapy crawl dytt8
import re
import scrapy
from spider_movie_scrapy.items import SpiderMovieItem


class Dytt8Spider(scrapy.Spider):
    name = 'dytt8'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net']
    # 存放分类页面url
    category_urls = []
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    }

    # 返回第一次response
    def start_requests(self):
        # 获取分类
        return [scrapy.Request(url=self.start_urls[0],callback=self.parse)]

    # 获取每个分类页面的url
    def parse(self, response):
        # 获取前十个分类
        grid_contain = response.css('.contain ul li')[:10]
        for data in grid_contain:
            value = data.css('a::attr(href)').extract_first()
            se = re.search(r'.*?(/html.*)', value).group(1)
            url = 'http://www.dytt8.net' + se
            self.category_urls.append(url)
        # print(self.category_urls)
        item = SpiderMovieItem()
        for url in self.category_urls[:1]:
            # 传递当前请求的url
            item['categoryURL'] = url
            request = scrapy.Request(item['categoryURL'], callback=self.category_parse)
            request.meta['item'] = item
            yield request

    # 该分类页面
    def category_parse(self, response):
        # 获取该分类总页面数
        # value = response.css('.co_area2 .co_content8 .x td::text').extract_first()
        # totalPage = re.search(r'共(\d+)页', value).group(1)

        # 获取当前请求的url
        item = response.meta['item']
        resurl = response.url

        # 获取每页的url
        allPage = response.css('.co_area2 .co_content8 .x select option')
        totalPageUrl = []
        for p in allPage:
            pageUrl = p.css('option::attr(value)').extract_first()
            totalPageUrl.append(pageUrl)
        # print(totalPageUrl)

        # 重新组装每页url
        for page in totalPageUrl:
            new_url = resurl.replace('index.html', page)
            # print(new_url)
            yield scrapy.Request(url=new_url, callback=self.page_parse)


    # 获取每部电影页面的url
    def page_parse(self, response):
        # 存放电影页面url
        movie_urls = []
        grid_view = response.css('.co_area2 .co_content8 ul table').extract()
        for data in grid_view:
            pattern = re.compile(r'<b>.*?a\shref="(.*?html)"\sclass=.*?</a>', re.S)
            da = re.search(pattern, data).group(1)
            url = 'http://www.dytt8.net' + da
            movie_urls.append(url)
        # 抓取每部电影详细信息
        for movie_detail in movie_urls:
            yield scrapy.Request(url=movie_detail, callback=self.movie_detail_parse)

    # 获得电影的详细信息
    def movie_detail_parse(self, response):
        grid_view = response.css('.co_area2')
        name = grid_view.css('.title_all h1 font::text').extract_first()
        imgUrl = grid_view.css('.co_content8 #Zoom p img::attr(src)').extract_first()
        content = grid_view.css('.co_content8 #Zoom p::text').extract()
        magneticLink = grid_view.css('.co_content8 #Zoom p a::attr(href)').extract_first()
        downloadUrl = grid_view.css('.co_content8 #Zoom table td a::attr(href)').extract_first()

        # print(content)
        # 存入数据库
        item = SpiderMovieItem()
        item['name'] = name
        item['imgUrl'] = imgUrl
        item['magneticLink'] = magneticLink
        item['downloadUrl'] = downloadUrl

        # item['actor'] = content[0].strip()
        item['translateName'] = content[2].strip()
        item['title'] = content[3].strip()
        item['time'] = content[4].strip()
        item['placeOfOrigin'] = content[5].strip()
        item['category'] = content[6].strip()
        item['language'] = content[7].strip()
        item['subtitle'] = content[8].strip()
        item['dbScore'] = content[9].strip()
        item['length'] = content[15].strip()
        item['director'] = content[16].strip()
        # item['star'] = content[0].strip()
        # item['info'] = content[0].strip()
        yield item







