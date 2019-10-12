import unittest
from models import news
News = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class 
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(BBC,'Ineos 159','Eliud Kipchoge super human','bbc.com','general','U.K')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))   

if __name__ == '__main__':
    unittest.main()