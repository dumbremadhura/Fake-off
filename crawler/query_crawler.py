from newspaper import Article
from urllib.parse import urlparse
from newsapi import NewsApiClient


class Crawler:
    '''
    Class Crawler contains all of the spiders and methods fror crawling purposes 
    '''


    def crawl_query_data(self,url):
        '''
        crawl_query_data(url) takes an URL as an argument and returns a (list) which contains information about the website
        list format: [scheme,name of the main website ,title,content,meta_keywords]

        :type url: string
        :param url: the URL of the website
        '''
        
        # Check if the URL provided is valid
        try:
            # initialize an object from the Article class and provide the URL in the constructor    
            article = Article(url)
            # Download and parse
            article.download()
            article.parse()

            # Scheme returns https ,http etc | str
            # Netloc returns the name of the main website | str
            # title returns the title and text returns the content | str
            # meta_keywords returns all the keywords from the meta | list
            return [urlparse(url).scheme,urlparse(url).netloc,article.title,article.text,article.meta_keywords]
        except Exception as e:
            print(e)
            # If the url is invalid return None (null)
            return(None)

        

    def request_news_URLs(self,list_of_keywords):

        '''
        request_news_URLs(list_of_keywords) takes in a list of keywords applies AND operation between them and queries it 
        with the help of news api and returns a maximum of 5 related Urls (list)

        :type list_of_keywords: list
        :param list_of_keywords: a python list of keywords to query the api

        '''

        # Init
        newsapi = NewsApiClient(api_key='3689abcc32e2468abb4eed31af2115c0')
        
        # query_string and list_of_URLs are initially kept empty and later adjusted accordingly
        query_string = ""

        list_of_URLs =[]

        # Do an AND operation between all the keywords add to query_string
        for i in range(0,len(list_of_keywords)):
            if(i >= len(list_of_keywords)-1):
                query_string = query_string + list_of_keywords[i]
                break
            else:
                query_string = query_string+ list_of_keywords[i] + " AND " 

        # returns dictionary on all the news articles documentation -> https://newsapi.org/docs/endpoints/everything
        all_articles = newsapi.get_everything(q=query_string)
        
        # parse for only thr url in the dctionary as the api restricts the content to only 260 characters for free users
        # and append them to the list of urls
        for i in range(0,len(all_articles["articles"])) :
            list_of_URLs.append(all_articles["articles"][i]["url"])
            if(len(list_of_URLs)>5):
                break

        
        #return a (list) of URLs

        return list_of_URLs


        
        


            

        

