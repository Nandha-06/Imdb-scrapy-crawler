# IMDB Scraper

A Scrapy project to scrape movie information from IMDB.

## Project Structure

```
imdb_scraper/
├── imdb_scraper/
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── imdb_json_spider.py  # Spider to scrape IMDB movie data
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── movie_data.json  # Output file with scraped data
└── scrapy.cfg
```

## Spider Details

The `imdb_json_spider.py` spider extracts movie information from IMDB by parsing the JSON data embedded in the page. It extracts the following information:

- Title
- Year
- Rating
- Genres
- Plot
- Poster URL
- Directors
- Writers
- Stars

## How to Run

To run the spider and save the output to a JSON file:

```bash
cd imdb_scraper
scrapy crawl imdb_json_scraper -o movie_data.json
```

## Implementation Details

The spider works by:

1. Sending a request to the IMDB movie page
2. Extracting the JSON data from the `__NEXT_DATA__` script tag
3. Parsing the JSON to extract the relevant movie information
4. Yielding the extracted data

The spider uses a custom user agent and other settings to avoid being blocked by IMDB.

## Sample Output

```json
[
  {
    "title": "Leo",
    "year": 2023,
    "rating": 7.2,
    "genres": ["Action", "Crime", "Drama", "Thriller"],
    "plot": "Parthiban is a mild-mannered cafe owner who fends off a gang of murderous thugs and gains attention from a drug cartel claiming he was once a part of them.",
    "poster": "https://m.media-amazon.com/images/M/MV5BODFkZWQwZDAtZDNkYi00MWU1LTkyNmYtM2JjMTM5OTI0ZGQwXkEyXkFqcGc@._V1_.jpg",
    "directors": ["Lokesh Kanagaraj"],
    "writers": ["Lokesh Kanagaraj", "Rathna Kumar", "Deeraj Vaidy"],
    "stars": ["Joseph Vijay", "Sanjay Dutt", "Trisha Krishnan"]
  }
]
```