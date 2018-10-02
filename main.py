from crawler.query_data import Query_data

def main():

    print("Enter the URL")

    URL = input()

    user_query = Query_data(URL)

    user_query.get_data()

if __name__ == "__main__":
    main()