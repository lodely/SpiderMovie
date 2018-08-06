# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 词条
    name = scrapy.Field()
    # 译名
    translateName = scrapy.Field()
    # 片名
    title = scrapy.Field()
    # 海报
    imgUrl = scrapy.Field()
    # 年代
    time = scrapy.Field()
    # 产地
    place = scrapy.Field()
    # 类别
    category = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 字幕
    subtitle = scrapy.Field()
    # 豆瓣评分
    dbScore = scrapy.Field()
    # 片长
    length = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    star = scrapy.Field()
    # 简介
    info = scrapy.Field()
    # 磁力链接
    magneticLink = scrapy.Field()
    # 下载地址
    downloadUrl = scrapy.Field()
    # 分类页面第一页url
    categoryURL = scrapy.Field()



