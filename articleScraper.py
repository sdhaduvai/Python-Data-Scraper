import newspaper
import bs4
import requests

ignore_keywords = ["sports", "video", "radio", "asia"]

"""
gets the links of every gun related article in breitbart.com and rushlimbaugh.com
"""
def get_all_articles():
    all_articles = []
    articles_to_read = []

    count = 0
    page_no = 1
    max_page_no = 99
    minimum_no_of_articles = 0
    print("Searching for articles in breitbart.com")
    while(count < minimum_no_of_articles and page_no <= max_page_no):
        response = requests.get("https://www.breitbart.com/news/source/breitbart-news/page/" + str(page_no) + "/")
        html = response.text
        soup = bs4.BeautifulSoup(html, "html.parser")        

        content = soup.find_all(class_ = "article-content")
        for element in content:
            link = element.find("a").get("href")
            headline = element.find("a").contents[0]
            if "gun" in headline.lower():
                count += 1
                articles_to_read.append(link)
                print("On page: " + str(page_no) + ", found article: " + headline)

        page_no += 1
    
    print("\n*****\n")

    count = 0
    page_no = 4000
    minimum_no_of_articles = 20
    print("Searching for articles in rushlimbaugh.com")
    while(count < minimum_no_of_articles):
        response = requests.get("https://www.rushlimbaugh.com/archives/page/" + str(page_no) + "/")
        html = response.text
        soup = bs4.BeautifulSoup(html, "html.parser")

        content = soup.find_all(class_ = "entry-title")
        if(not content):
            print("No more articles to read")
            break
        for element in content:
            link = element.find("a").get("href")
            headline = element.find("a").contents[0]
            if "gun" in headline.lower():
                count += 1
                articles_to_read.append(link)
                print("On page: " + str(page_no) + ", found article: " + headline)

        page_no += 1

    return articles_to_read