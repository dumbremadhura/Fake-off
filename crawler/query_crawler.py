from newspaper import Article
from urllib.parse import urlparse
from newsapi import NewsApiClient
# Class Crawler contains all of the spiders fror crawling purposes 


class Crawler:



    def crawl_query_data(self,url):
        
        
        # Check if the URL provided is valid
        try:
            # Prints the scheme http, https etc
            print("Sceheme used")
            print(urlparse(url).scheme)
            # Prints out the main domain of the website
            print("Content Provider")
            print(urlparse(url).netloc)
            # initialize an object from the Article class and provide the URL in the constructor    
            article = Article(url)
            # Download and parse
            article.download()
            article.parse()
            article.nlp()
            print("Article title")
            print(article.title)
            print("Article body")
            print(article.text)
            print("meta keywords")
            print(article.meta_keywords)
            return [urlparse(url).scheme,urlparse(url).netloc,article.title,article.text,article.meta_keywords]
        except:
            # If the url is invalid return None (null)
            return(None)

        

    def request_news(self,list_of_keywords):

        # Init
        newsapi = NewsApiClient(api_key='3689abcc32e2468abb4eed31af2115c0')
        
        query_string = ""

        for keyword in list_of_keywords:
            query_string = query_string+ keyword + " " 

        # returns dictionary
        all_articles = newsapi.get_everything(q=query_string)
        
        # parse for only thr url in the dctionary as the api restricts the content to only 260 characters for free users
        for i in range(0,5):
            print(all_articles["articles"][i]["url"])
        


            

        

