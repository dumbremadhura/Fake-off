from crawler.query_crawler import Crawler

class Query_data:
    '''
    class Query_data contains aggregated methods from different classes and provides a single method for a particular operation 
    '''

    def __init__(self,url):
        '''
        :type url:string
        :param url: the URL of the website
        '''
        self.url = url
    
    def get_data(self):
        '''
        this methods extracts the contents from the given link in the class constructor and uses its keywords
        to extract urls from the api
        then it uses those URLs to get content from those URLs
        this method returns a tuple where at 0 position is the content from the link and at 1 position is the content from
        related URLs
        '''
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
            return(None)

        
        




        

