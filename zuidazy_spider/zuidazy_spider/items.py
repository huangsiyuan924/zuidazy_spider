# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZuidazySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_title = scrapy.Field()
    movie_update_info = scrapy.Field()
    movie_score = scrapy.Field()
    movie_alias = scrapy.Field()
    movie_director = scrapy.Field()
    movie_starring = scrapy.Field()
    movie_type = scrapy.Field()
    movie_area = scrapy.Field()
    movie_lang = scrapy.Field()
    movie_release_year = scrapy.Field()
    movie_length = scrapy.Field()
    movie_source_last_update = scrapy.Field()
    movie_detail = scrapy.Field()
    movie_down_zuidam3u8 = scrapy.Field()
    movie_down_zuidall = scrapy.Field()
    movie_down_xunlei = scrapy.Field()
