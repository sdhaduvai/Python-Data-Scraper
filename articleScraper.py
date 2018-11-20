import newspaper
import urllib
import bs4
import requests
import csv
import time
import os

ignore_keywords = ["entertainment", "sports", "video", "tech", "radio", "asia"]

"""
gets the links of every gun related article in breitbart.com and rushlimbaugh.com
"""
def get_all_articles():
    all_articles = []
    articles_to_read = []

    breitbart = newspaper.build("https://www.breitbart.com/", memoize_articles=False)
    for article in breitbart.articles:
        all_articles.append(article.url)
    

    filter_func = lambda s: "https://www.breitbart.com/" in s and not any(category in s for category in ignore_keywords)
    articles_to_read = [line for line in all_articles if filter_func(line)]
    
    count = 0
    page_no = 1
    minimum_no_of_articles = 10
    while(count < minimum_no_of_articles):
        response = requests.get("https://www.rushlimbaugh.com/archives/page/" + str(page_no) + "/")
        html = response.text
        soup = bs4.BeautifulSoup(html, "html.parser")

        content = soup.find_all(class_ = "entry-title")
        for element in content:
            link = element.find("a").get("href")
            if "gun" in link:
                count += 1
                articles_to_read.append(link)

        page_no += 1

    return articles_to_read