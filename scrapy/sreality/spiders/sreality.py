#!/usr/bin/env python
# coding: utf-8

import json
import scrapy

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&locality_region_id=10&per_page=500"]

    def parse(self, response):
        data = response.json()
        data_list = []
        for item in data["_embedded"]["estates"]:
            yield {
                "title": item['name'],
                "links": item["_links"]["images"]
            }
                
