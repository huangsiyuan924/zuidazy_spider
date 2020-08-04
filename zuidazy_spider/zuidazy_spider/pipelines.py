# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from zuidazy_spider.mysqlUtil import MysqlHelper


class ZuidazySpiderPipeline(object):

    def __init__(self):
        self.helper = MysqlHelper()

    def process_item(self, item, spider):
        movie_id = item["movie_id"]
        movie_title = item["movie_title"]
        movie_update_info = item["movie_update_info"]
        movie_score = item["movie_score"]
        movie_alias = item["movie_alias"]
        movie_director = item["movie_director"]
        movie_starring = item["movie_starring"]
        movie_type = item["movie_type"]
        movie_area = item["movie_area"]
        movie_lang = item["movie_lang"]
        movie_release_year = item["movie_release_year"]
        movie_length = item["movie_length"]
        movie_source_last_update = item["movie_source_last_update"]
        movie_detail = item["movie_detail"]
        movie_down_zuidam3u8 = item["movie_down_zuidam3u8"]
        movie_down_zuidall = item["movie_down_zuidall"]
        movie_down_xunlei = item["movie_down_xunlei"]

        self.helper.insert_spider("zuidazy_spider" , movie_id, movie_title, movie_update_info, movie_score, movie_alias, movie_director, movie_starring, movie_type, movie_area, movie_lang, movie_release_year, movie_length, movie_source_last_update, movie_detail, movie_down_zuidam3u8, movie_down_zuidall, movie_down_xunlei)

        return item