import unittest
from app.models import News,Articles
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class 
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Ineos 159','Eliud Kipchoge super human','bbc.com','general','U.K','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))   
