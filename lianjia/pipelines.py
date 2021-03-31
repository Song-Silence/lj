# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class LianjiaPipeline:
    def __init__(self):
        self.db = pymysql.connect(
            host='192.168.1.43', user='test', password='123456', database='TEST')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO message(title, position, houseIntroduction, follow, total, unit, houseRange, houseDirection, houseDecorate, houseHeight, houseAge, houseType, time) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(
            item['title'], item['position'],  item['houseIntroduction'], item['follow'], item['total'], item['unit'], item['houseRange'], item['houseDirection'], item['houseDecorate'], item['houseHeight'], item['houseAge'], item['houseType'], item['time'])
        # print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
