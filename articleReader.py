import newspaper
import time
import os
import re

# keywords to look for in the articles
keywords = ["gun rights", "gun control", "gun policy", "gun regulation"]

""" 
downloads the article into our computer
@param article: article to download 
""" 
def save_article(article):
    dest_dir = "articles\gun_articles"
    title = article.title  
    # removes any special characters from the title  
    cleanString = re.sub('\W+',' ', title)
    path = os.path.join(dest_dir, cleanString)
    f = open(path+".txt", 'w', encoding = 'utf-8')
    f.write(article.text)
    f.close

"""
inserts the document entry into the documents_dict_list
@param article: article to scan
@param documents_dict_list: list of all document_dicts
@param keyword: keyword on which the document was obtained
"""
def insert_into_documents_dict(article, documents_dict_list, keyword):
    document_dict = dict.fromkeys(['document id', 'keyword', 'document title', 'document publication date', 'document path', 'word count', 'url'])
    document_dict['document id'] = article.title
    document_dict['keyword'] = keyword
    document_dict['document title'] = article.title 
    document_dict['document publication date'] = article.publish_date
    document_dict['document path'] = "articles\gun_articles\\" + re.sub('\\n','', article.title)
    document_dict['word count'] = len(article.text.split())
    document_dict['url'] = article.url

    try:
        if documents_dict_list[-1]['document id'] != document_dict['document id']:  
            documents_dict_list.append(document_dict)
    except:
        documents_dict_list.append(document_dict)

"""
checks each sentence in the article for keywords and makes an entry in the passage_dict if found
@param article: article to scan
@param passages_dict_list: a list of dictioanries to store passages
"""
def save_passages(article, passages_dict_list):
    sentences = article.text.split(".")
    for i, sentence in enumerate(sentences):
        for keyword in keywords:
            if keyword in sentence.lower():
                # dictionary 
                passages_dict = dict.fromkeys(["passage id", "document id", "keyword", "content", "prior-context", "after-context", "url"])
                passages_dict["passage id"] = "passage " + str(i)
                passages_dict["document id"] = article.title
                passages_dict["keyword"] = keyword
                passages_dict["content"] = re.sub('\\n','', sentence)
                passages_dict["prior-context"] = re.sub('\\n','', sentences[i-1])
                passages_dict["after-context"] = re.sub('\\n','', sentences[i+1])
                passages_dict['url'] = article.url
                
                passages_dict_list.append(passages_dict)

"""
scans the article for keywords and saves the article if any keyword is found
@param article: article to scan 
@param passages_dict_list: a list of dictionaries for storing passages
@param documents_dict_lists: a list of dictionaries for storing documents
"""   
def read_and_save(article, passages_dict_list, documents_dict_list):
    sentences = article.text.split(".")
    for i, sentence in enumerate(sentences):
        for keyword in keywords:
            if keyword in sentence.lower():
                save_article(article)
                save_passages(article, passages_dict_list)
                insert_into_documents_dict(article, documents_dict_list, keyword)
                return
