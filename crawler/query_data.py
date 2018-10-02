from crawler.query_crawler import Crawler

class Query_data:
    def __init__(self,url):
        self.url = url
    
    def get_data(self):

        mini_Crawler = Crawler()
 
        # return a list in the form 
        # [scheme,netloc,title,text,meta_keywords]
        crawled_data = mini_Crawler.crawl_query_data(self.url)

        api_news_data =[]

        if(crawled_data):
            # list[-1] denotes the last index of the list
            # list returned [scheme,netloc,title,text,meta_keywords]
            # [-1] is a list of all the keywords
            # returns a list of URLs
            URls = mini_Crawler.request_news_URLs(crawled_data[-1])

            for URL in URls:
                api_news_data.append(mini_Crawler.crawl_query_data(URL))
            
            return(crawled_data,api_news_data)
        else:
            print("Invalid URL")
            return None

        
        




        

