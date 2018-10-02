from crawler.query_crawler import Crawler

class Query_data:
    def __init__(self,url):
        self.url = url
    
    def get_data(self):

        mini_Crawler = Crawler()

        crawled_data = mini_Crawler.crawl_query_data(self.url)

        if(crawled_data):
            # list[-1] denotes the last index of the list
            # list returned [scheme,netloc,title,text,meta_keywords]
            # [-1] is a list of all the keywords
            print("crawled_data from 2")
            print(crawled_data[-1])
            # returns a list of URLs
            mini_Crawler.request_news_URLs(crawled_data[-1])
        else:
            print("Invalid URL")

        
        




        

