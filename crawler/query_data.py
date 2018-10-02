from crawler.query_crawler import Crawler

class Query_data:
    def __init__(self,url):
        self.url = url
    
    def get_data(self):

        mini_Crawler = Crawler()

        crawled_data = mini_Crawler.crawl_query_data(self.url)

        print(crawled_data)

        print(crawled_data[-1][0])

        mini_Crawler.request_news(crawled_data[-1])
        




        

