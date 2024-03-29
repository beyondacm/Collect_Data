# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnswerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    answer_id = scrapy.Field() 
    related_id = scrapy.Field()
    user_id = scrapy.Field()
    answer_voted = scrapy.Field()
    answer_content = scrapy.Field()
    
    #pass


class QuestionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    question_id = scrapy.Field()
    user_id = scrapy.Field()
    question_content = scrapy.Field()

    #pass

