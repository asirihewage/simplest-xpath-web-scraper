"""
    simplest xpath web scraper
    @author: Asiri Hewage
"""
from lxml import html
import requests


class Extractor:
    def __init__(self):
        self.r = None
        self.tree = None
        self.xpaths = None

    def extract(self, url, xpaths):
        """
        :return:
        """
        res = []
        data = []
        ret = {}

        self.r = requests.get(url)
        self.tree = html.fromstring(self.r.content)

        for key, obj in enumerate(xpaths):
            for column_name, xpath in obj.items():
                value = self.tree.xpath(xpath)
                res = {
                    column_name: value
                }
                data.append(res)

            ret["url"] = url
            ret["data"] = data

        return ret
