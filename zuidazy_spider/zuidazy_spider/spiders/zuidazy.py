# -*- coding: utf-8 -*-
import scrapy
import os

from zuidazy_spider.items import ZuidazySpiderItem


class ZuidazySpider(scrapy.Spider):
    name = 'zuidazy'
    allowed_domains = ['zuidazy4.com']
    start_urls = ['http://zuidazy4.com/']

    def __init__(self):
        self.base_url = "http://zuidazy4.com"
        # 文件不存在
        if os.path.exists("check_point"):
            try:
                with open("check_point", "r") as f:
                    self.next_page_id = int(f.read())
            except:
                # 文件内容不规范
                self.next_page_id = 1
        else:
            self.next_page_id = 1

    def parse(self, response):
        print(self.next_page_id)
        self.next_page_id += 1
        next_page_url = "http://zuidazy4.com/?m=vod-index-pg-" + str(self.next_page_id) + ".html"
        # 影片详情页url列表
        movies_url_list = response.xpath('//span[@class="xing_vb4"]/a/@href').extract()
        for movie_url in movies_url_list:
            # 影片详情页的完整url
            yield scrapy.Request(
                url=self.base_url + movie_url,
                callback=self.parse_movie_detail
            )

        with open("check_point", "w") as f:
            f.write(str(self.next_page_id))
        yield scrapy.Request(
            url=next_page_url,
            callback=self.parse
        )

    def parse_movie_detail(self, response):
        # 电影id, 唯一标识码
        movie_id = response.url.split("id-")[1].split(".html")[0]
        # 影片名称
        movie_title = response.xpath('//div[@class="vodh"]/h2/text()').extract_first().replace("'", "\"")
        # 影片资源更新最新信息
        movie_update_info = response.xpath('//div[@class="vodh"]/span/text()').extract_first()
        # 影片评分
        movie_score = response.xpath('//div[@class="vodh"]/label/text()').extract_first()
        # 影片别名
        movie_alias = response.xpath('//div[@class="vodinfobox"]/ul/li[1]/span/text()').extract_first()
        if movie_alias is not None:
            movie_alias = movie_alias.replace("'", "\"")
        # 导演
        movie_director = response.xpath('//div[@class="vodinfobox"]/ul/li[2]/span/text()').extract_first()
        if movie_director is not None:
            movie_director = movie_director.replace("'", "\"")
        # 主演
        movie_starring = response.xpath('//div[@class="vodinfobox"]/ul/li[3]/span/text()').extract_first()
        if movie_starring is not None:
            movie_starring = movie_starring.replace("'", "\"")
        # 影片类型
        movie_type = response.xpath('//div[@class="vodinfobox"]/ul/li[4]/span/text()').extract_first()
        # 地区
        movie_area = response.xpath('//div[@class="vodinfobox"]/ul/li[5]/span/text()').extract_first()
        # 语言
        movie_lang = response.xpath('//div[@class="vodinfobox"]/ul/li[6]/span/text()').extract_first()
        # 上映年份
        movie_release_year = response.xpath('//div[@class="vodinfobox"]/ul/li[7]/span/text()').extract_first()
        # 片长
        movie_length = response.xpath('//div[@class="vodinfobox"]/ul/li[8]/span/text()').extract_first()
        # 影片资源最新更新时间
        movie_source_last_update = response.xpath('//div[@class="vodinfobox"]/ul/li[9]/span/text()').extract_first()
        # 影片介绍
        movie_detail = response.xpath('//span[@class="more"]/text()').extract_first().replace("'", "\"")
        # 影片m3u8资源链接
        movie_down_zuidam3u8 = "\n".join(response.xpath('//div[@id="play_1"]/ul/li/text()').extract())
        movie_down_zuidall = "\n".join(response.xpath('//div[@id="play_2"]/ul/li/text()').extract())
        movie_down_xunlei = "\n".join(response.xpath('//div[@id="down_1"]/ul/li/text()').extract())
        item = ZuidazySpiderItem()
        item["movie_id"] = movie_id
        item["movie_title"] = movie_title
        item["movie_update_info"] = movie_update_info
        item["movie_score"] = movie_score
        item["movie_alias"] = movie_alias
        item["movie_director"] = movie_director
        item["movie_starring"] = movie_starring
        item["movie_type"] = movie_type
        item["movie_area"] = movie_area
        item["movie_lang"] = movie_lang
        item["movie_release_year"] = movie_release_year
        item["movie_length"] = movie_length
        item["movie_source_last_update"] = movie_source_last_update
        item["movie_detail"] = movie_detail
        item["movie_down_zuidam3u8"] = movie_down_zuidam3u8
        item["movie_down_zuidall"] = movie_down_zuidall
        item["movie_down_xunlei"] = movie_down_xunlei
        yield item

