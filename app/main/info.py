from flask import render_template,redirect,url_for
from . import main
from ..requests import get_news,get_articles

# Info
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data 
    '''
    general_news = get_news('general')
    science_news = get_news('science')
    business_news = get_news('business')
    technology_news = get_news('technology')
    health_news = get_news('health')
    entertainment_news = get_news('entertainment')
    sports_news = get_news('sports')
    sources_news = get_news('category')
    title = "News Highlight(ニュースハイライト)"

    return render_template('index.html',title = title, sources = sources_news)

@main.route('/news/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('articles.html',title = title, articles = articles)
	
