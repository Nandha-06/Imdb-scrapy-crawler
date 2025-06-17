import scrapy
import json

class ImdbJsonSpider(scrapy.Spider):
    name = 'imdb_scraper'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/title/tt1745960/']

    def parse(self, response):
        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()
        json_data = json.loads(raw_data)
        data = json_data['props']['pageProps']['aboveTheFoldData']
        mainColumnData = json_data['props']['pageProps']['mainColumnData']

        yield {
            'title': data['titleText']['text'],
            'Released_Year': data['releaseYear']['year'],
            'stars': [edge['node']['name']['nameText']['text'] for edge in data['castPageTitle']['edges']],
            'rating': data['ratingsSummary']['aggregateRating'],
            'runtime': data['runtime']['displayableProperty']['value']['plainText'],
            'reviews': data['reviews']['total'],
            'production_companies': [e['node']['company']['companyText']['text'] for e in mainColumnData['production']['edges']],
            'genres': [g['text'] for g in data['genres']['genres']],
            'plot': data['plot']['plotText']['plainText'],
            'cast': [actor['node']['name']['nameText']['text'] for actor in mainColumnData['cast']['edges']],
            'directors': [c['name']['nameText']['text'] for d in mainColumnData['directors'] for c in d.get('credits', [])],
            'writers': [c['name']['nameText']['text'] for w in mainColumnData['writers'] for c in w.get('credits', [])],
            'isAdult': data['isAdult'],
            'ProductionBudget': "${:,}".format(mainColumnData['productionBudget']['budget']['amount']) if mainColumnData['productionBudget'] else None,
            'worldwideGross': "${:,}".format(mainColumnData['worldwideGross']['total']['amount']),
            'lifetimeGross': "${:,}".format(mainColumnData['lifetimeGross']['total']['amount']) if mainColumnData['lifetimeGross'] else None,
            'openingWeekendGross': "${:,}".format(mainColumnData['openingWeekendGross']['gross']['total']['amount']) if mainColumnData['openingWeekendGross'] else None
        }
