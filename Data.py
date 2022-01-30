"""
    simplest xpath web scraper
    @author: Asiri Hewage
"""

data = [
    {
        "url": "https://www.technology.pitt.edu/blog/zoom10faq",
        "xpaths": [
            {
                "question": '//div[@class="field-item even"]/h2/text()',
                "answers": '//div[@class="field-item even"]/p/text()',
                "correct_answer": '//div[@class="field-item even"]/p[0]/text()'
            }
        ]
    },
    {
        "url": "https://www.socialsciencespace.com/2020/03/16-answers-to-your-questions-about-teaching-online/",
        "xpaths": [
            {
                "column_name1": "/img",
                "column_name2": "/p",
                "column_name3": "/a"
            }
        ]
    }
]