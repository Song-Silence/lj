from scrapy import Request, Spider
import json
from jsonpath import jsonpath


class IhgSpider(Spider):
    name = 'LJ'

    def start_requests(self):
        base_url = 'https://wh.lianjia.com/ershoufang/pg'
        for i in range(1, 2):
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
        print(response.xpath(
            '//ul[@class="sellListContent"]//div[@class="title"]/a/text()'))
        print(response.xpath(
            '//ul[@class="sellListContent"]//div[@class="positionInfo"]//text()'))
        print(response.xpath(
                  '//ul[@class="sellListContent"]//div[@class="houseInfo"]//text()'))
        print(response.xpath(
                        '//ul[@class="sellListContent"]//div[@class="followInfo"]//text()'))
        print(response.xpath(
            '//ul[@class="sellListContent"]//div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()'))
        print(response.xpath(
            '//ul[@class="sellListContent"]//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()'))
