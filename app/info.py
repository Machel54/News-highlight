from flask import render_template
from app import app
from requests import get_news,get_articles


# Views
@app.route('/')
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
	title = "News Highlight(ニュースハイライト)"

	return render_template('index.html',title = title, general_news = general_news, science_news = science_news, business_news = business_news,technology_news = technology_news, health_news = health_news, entertainment_news = entertainment_news, sports_news = sports_news)

    
@app.route('/news/<int:news_id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles))