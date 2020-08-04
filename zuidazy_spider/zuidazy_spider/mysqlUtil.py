'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 04/08/2020 9:47 PM
@Software: PyCharm
@File    : mysqlUtil.py
@Email   : huangsiyuan924@gmail.com
'''
import pymysql





class MysqlHelper():

    def __init__(self):
        # 连接MySQL
        self.db = pymysql.connect("localhost", "root", "asdasdasd", "test")
        # 创建cursor对象
        self.cursor = self.db.cursor()

        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS zuidazy_spider(
                        movie_id INT PRIMARY KEY, -- 电影id
                        movie_title VARCHAR(100) NOT NULL, -- 影片名称
                        movie_update_info VARCHAR(20), -- 影片资源更新最新信息
                        movie_score FLOAT(2, 1), -- 影片评分
                        movie_alias VARCHAR(300), -- 影片别名
                        movie_director VARCHAR(200), -- 导演
                        movie_starring VARCHAR(300), -- 主演
                        movie_type VARCHAR(20), -- 影片类型
                        movie_area VARCHAR(20), -- 地区
                        movie_lang VARCHAR(20), -- 语言
                        movie_release_year INT(4), -- 上映年份
                        movie_length SMALLINT, -- 片长
                        movie_source_last_update DATETIME, -- 影片资源最新更新时间
                        movie_detail TEXT, -- 影片介绍
                        movie_down_zuidam3u8 MEDIUMTEXT, -- 影片m3u8资源链接
                        movie_down_zuidall MEDIUMTEXT,
                        movie_down_xunlei MEDIUMTEXT
                        )
        ''')

    def insert_spider(self,
                         table_name,
                         movie_id,
                         movie_title,
                         movie_update_info,
                         movie_score,
                         movie_alias,
                         movie_director,
                         movie_starring,
                         movie_type,
                         movie_area,
                         movie_lang,
                         movie_release_year,
                         movie_length,
                         movie_source_last_update,
                         movie_detail,
                         movie_down_zuidam3u8,
                         movie_down_zuidall,
                         movie_down_xunlei
                         ):
        sql = "INSERT INTO %s(movie_id, movie_title, movie_update_info, movie_score, movie_alias, movie_director, movie_starring, movie_type, movie_area, movie_lang, movie_release_year, movie_length, movie_source_last_update, movie_detail, movie_down_zuidam3u8, movie_down_zuidall, movie_down_xunlei) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (table_name, movie_id, movie_title, movie_update_info, movie_score, movie_alias, movie_director, movie_starring, movie_type, movie_area, movie_lang, movie_release_year, movie_length, movie_source_last_update, movie_detail, movie_down_zuidam3u8, movie_down_zuidall, movie_down_xunlei)
        self.cursor.execute(sql)
        self.db.commit()
    def close(self):
        self.db.close()
