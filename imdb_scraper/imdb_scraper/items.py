# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from typing import List, Optional, Union

class Info(scrapy.Item):
    """
    Item class for storing scraped IMDB Top 250 movie data.
    """
    title = scrapy.Field()        # Movie title
    movie_rank = scrapy.Field()   # Current rank on the Top 250 list
    release_year = scrapy.Field() # Release year
    movie_length = scrapy.Field() # Movie duration in seconds
    rating = scrapy.Field()       # IMDB rating
    vote_count = scrapy.Field()   # Number of votes
    description = scrapy.Field()  # Movie plot/summary

class ImdbScraperItem(scrapy.Item):
    """
    Item class for storing scraped IMDB movie data.
    """
    # Basic Information
    title = scrapy.Field()  # Movie title
    year = scrapy.Field()   # Release year
    rating = scrapy.Field()  # IMDB rating
    runtime = scrapy.Field()  # Movie duration
    plot = scrapy.Field()    # Movie plot/summary
    isAdult = scrapy.Field()  # Whether the content is adult-oriented
    
    # People
    stars = scrapy.Field()  # Main cast/actors
    cast = scrapy.Field()   # Full cast list
    directors = scrapy.Field()  # Movie directors
    writers = scrapy.Field()    # Screenwriters
    
    # Production
    production_companies = scrapy.Field()  # Production companies
    genres = scrapy.Field()     # Movie genres
    
    # Financial Information
    ProductionBudget = scrapy.Field()  # Movie's production budget
    worldwideGross = scrapy.Field()    # Worldwide box office gross
    lifetimeGross = scrapy.Field()     # Lifetime box office gross
    openingWeekendGross = scrapy.Field()  # Opening weekend box office gross
    
    # Additional Metadata
    reviews = scrapy.Field()  # Number of reviews
    
    # URL and timestamp
    url = scrapy.Field()  # Source URL
    timestamp = scrapy.Field()  # When the item was scraped
