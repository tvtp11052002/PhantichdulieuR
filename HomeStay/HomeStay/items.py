# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomestayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Homestay_name = scrapy.Field()
    Address = scrapy.Field()
    Review = scrapy.Field()
    Restaurant_nearby = scrapy.Field()
    number_images_Traveler = scrapy.Field()
    Review_number = scrapy.Field()
    Great_for_walker = scrapy.Field()
    Attractions = scrapy.Field()
    Travel_types = scrapy.Field()
    Price_range = scrapy.Field()
    Room_number = scrapy.Field()
    number_room_dining = scrapy.Field()
    number_room_suite = scrapy.Field()
    pass
