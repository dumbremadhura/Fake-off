from crawler.query_data import Query_data

def main():

    print("Enter the URL")

    URL = input()

    user_query = Query_data(URL)
    

    # returns a tuple containing the crawled data from the link and data from the news api
    # crawled_data_and_api_data[0] gives data from the link 
    # crawled_data_and_api_data[1] gives a 2d list from the api data
    crawled_data_and_api_data = user_query.get_data()

    print(crawled_data_and_api_data[0][3])

if __name__ == "__main__":
    main()