# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

class SpiderMovieScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class MoviePipeline(object):

    def process_item(self, item, spider):

        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWD']
        db = settings['MYSQL_DB']
        c=settings['CHARSET']
        port=settings['MYSQL_PORT']
        #数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        #数据库游标
        cue=con.cursor()
        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步

        try:
            cue.execute("""insert into movies
                        (name, translateName, title, imgUrl, time, place, category, language, subtitle, dbScore, length, director, star, info, magneticLink, downloadUrl)
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        [item['name'],
                         item['translateName'],
                         item['title'],
                         item['imgUrl'],
                         item['time'],
                         item['place'],
                         item['category'],
                         item['language'],
                         item['subtitle'],
                         item['dbScore'],
                         item['length'],
                         item['director'],
                         item['star'],
                         item['info'],
                         item['magneticLink'],
                         item['downloadUrl'],
                         ])
            print("insert success")#测试语句

        except Exception as e:
            print('Insert error:',e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item