from scrapy import Request, Spider
import json
from jsonpath import jsonpath
from lxml import html
from lianjia.items import LianjiaItem


class IhgSpider(Spider):
    name = 'LJ'

    def start_requests(self):
        base_url = 'https://wh.lianjia.com/ershoufang/pg'
        for i in range(1, 101):
            url = base_url + str(i)
            header = {
                'Host': 'wh.lianjia.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                '537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1', }
            yield Request(url=url, headers=header, method='GET')

    def parse(self, response):
        lianjia_item = LianjiaItem()
        new_text = response.xpath('//ul[@class="sellListContent"]/li')
        for item in new_text:
            text = item.extract()
            nodes = html.fromstring(text)
            title = nodes.xpath('//div[@class="title"]/a/text()')
            position = nodes.xpath('//div[@class="positionInfo"]//text()')
            house = nodes.xpath('//div[@class="houseInfo"]//text()')
            follow = nodes.xpath('//div[@class="followInfo"]//text()')
            total = nodes.xpath(
                '//div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()')
            unit = nodes.xpath(
                '//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')

            follow = follow[0].split('/')
            time = follow[1]
            follow = follow[0]
            if '一年前发布' in time:
                time = '360'
            elif '个月以前发布' in time:
                time = int(time.split('个月以前发布')[0])*30
            elif '天以前发布' in time:
                time = time.split('天以前发布')[0]
            follow = follow.split('人关注')[0]
            lianjia_item['title'] = title[0]
            lianjia_item['position'] = position[0]
            lianjia_item['follow'] = int(follow)
            lianjia_item['time'] = int(time)
            lianjia_item['total'] = float(total[0])
            unit = unit[0].replace('单价', '')
            unit = unit.replace('元/平米', '')
            lianjia_item['unit'] = float(unit)
            house_list = house[0].split('|')
            
            for i in range(7-len(house_list)):
                house_list.append('暂无数据')
            lianjia_item['houseIntroduction'], lianjia_item['houseRange'], lianjia_item['houseDirection'], lianjia_item[
                'houseDecorate'], lianjia_item['houseHeight'], lianjia_item['houseAge'], lianjia_item['houseType'] = house_list
            
            if '年建' in lianjia_item['houseAge']:
                lianjia_item['houseAge'] = lianjia_item['houseAge'].split('年建')[
                    0]
            else:
                lianjia_item['houseType'] = lianjia_item['houseAge']
                lianjia_item['houseAge'] = '暂无数据'

            yield lianjia_item
