import os
import newspaper
import time

import articleScraper
import articleReader
import articleWriter

# creates a directory to save all articles
dest_dir = "articles\gun_articles"
try:
    os.makedirs(dest_dir)
except OSError:
    pass # already exists

# gets all article links
articles = articleScraper.get_all_articles()

# list of dictionaries of passages
passages_dict_list = []

# list of dictionaries of documents
documents_dict_list = []

for article in articles:
    article = newspaper.Article(article)
    article.download()
    # waits until the article is successfully downloaded
    while article.download_state != 2: #ArticleDownloadState.SUCCESS is 2
        time.sleep(1)
    article.parse()
    articleReader.read_and_save(article, passages_dict_list, documents_dict_list)

articleWriter.write_passages_to_csv(passages_dict_list)
articleWriter.write_documents_to_csv(documents_dict_list)
print("DONE")