# Simplest xpath web scraper
Simples web scraper created using Python3
- extract data using multiple xpaths from multiple urls
- save response in MongoDB
- exceptions and error handling
- only for basic web sraping work from static HTML web pages

## setup Data.py for each url with xpath
```json
    {
        "url": "https://www.technology.pitt.edu/blog/zoom10faq",
        "xpaths": [
            {
                "questions": '//div[@class="field-item even"]/h2/text()',
                "answers": '//div[@class="field-item even"]/p/text()',
                "correct_answer": '//div[@class="field-item even"]/p[0]/text()'
            }
        ]
    }
```
## setup mongodb database connection string
```python
myclient = pymongo.MongoClient("mongodb://host:port/") # or add the connection url
mydb = myclient["database"]
mycol = mydb["collection"]
```

## install python dependancies
```commandline
pip3 install -r requirements.txt
```

## run
```commandline
python3 main.py
```

## response
 ![Simplest xpath web scraper](47dcf6e5-0d63-4824-9135-e2b4171a171f.jfif)

### Author : Asiri Hewage