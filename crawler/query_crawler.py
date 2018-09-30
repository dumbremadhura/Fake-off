from newspaper import Article
from urllib.parse import urlparse
# Class Crawler contains all of the spiders fror crawling purposes 


class Crawler:

    def crawl_data(self):
        print("Enter the link")
        url =  input()
        
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
            print("Article title")
            print(article.title)
            print("Article body")
            print(article.text)
        except:
            print("Invalid URL")

        

            

        

