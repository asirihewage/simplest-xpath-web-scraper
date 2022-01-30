"""
    simplest xpath web scraper
    @author: Asiri Hewage
"""
from Extractor import Extractor
from Data import data
# from Database import Database


def run():
    try:
        extractor = Extractor()
        # database = Database()
        for obj in data:
            res = extractor.extract(obj["url"], obj["xpaths"])
            # database.insert(res)
            print(res)
    except Exception as er:
        print(er)


if __name__ == '__main__':
    run()
