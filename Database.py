"""
    simplest xpath web scraper
    @author: Asiri Hewage
"""

import pymongo


class Database:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["mydatabase"]
        self.mycol = self.mydb["customers"]

    def insert(self, data):
        x = self.mycol.insert_one(data)
        return x
