# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class SpiderMovieScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class MoviePipeline(object):
    def process_item(self,item,spider):
        '''
        将爬取的信息保存到mysql
        '''
        # 将item里的数据拿出来
        name = item['name']
        translateName = item['translateName']
        title = item['title']

        # 和本地的newsDB数据库建立连接
        db = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            port='3306',
            user='root',  # 自己的mysql用户名
            passwd='root',  # 自己的密码
            db='spider_movie',  # 数据库的名字
            charset='utf8',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)

        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "INSERT INTO movies(name,translateName,title) \
                  VALUES ('%s', '%s', '%s')" % (name,translateName,title)
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
        return item