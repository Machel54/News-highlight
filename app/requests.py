from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']
articles_url = app.config['ARTICLES_BASE_URL']

#Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news']:
            news_results_list = get_news_response['news']
            news_results = process_news(news_results_list)


    return news_results

def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        description = news_item.get('description')
		url = news_item.get('url')
		category = news_item.get('category')
		language = news_item.get('language')
		country = news_item.get('country')

            news_object = News(id,title,description,url,category,country,language)
            news_results.append(news_object)

    return movie_results

# def get_articles(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_movies_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         news_results = None

#         if get_news_response['news']:
#             news_results_list = get_news_response['news']
#             news_results = process_news(news_results_list)


#     return news_results

# def process_news(news_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain news details

#     Returns :
#         news_results: A list of movie objects
#     '''
#     news_results = []
#     for news_item in news_list:
#         id = news_item.get('id')
#         description = news_item.get('description')
# 		url = news_item.get('url')
# 		category = news_item.get('category')
# 		language = news_item.get('language')
# 		country = news_item.get('country')

#             news_object = News(id,title,description,url,category,country,language)
#             news_results.append(news_object)

#     return movie_results

