import scrapy
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector

class ImdbTop250Spider(scrapy.Spider):
    name = 'imdb_top_250'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']
    
    def __init__(self, *args, **kwargs):
        super(ImdbTop250Spider, self).__init__(*args, **kwargs)
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def parse(self, response):
        # Use Selenium to load the page and handle dynamic content
        self.driver.get(response.url)
        
        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ipc-metadata-list'))
        )
        
        # Scroll to load all movies (loading 250 movies)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait to load page
            time.sleep(2)
            
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
            # Check if we've found all 250 movies
            movie_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')
            if len(movie_elements) >= 250:
                break
        
        # Parse the page source with Scrapy
        sel = Selector(text=self.driver.page_source)
        
        # Extract movie links
        movie_links = sel.css('li.ipc-metadata-list-summary-item a.ipc-title-link-wrapper::attr(href)').getall()
        
        # Clean and yield the links
        for link in movie_links:
            # Convert relative URL to absolute URL
            full_url = response.urljoin(link.split('?')[0])  # Remove query parameters
            yield {
                'movie_url': full_url,
                'movie_id': link.split('/')[2]  # Extract IMDb ID from URL
            }
    
    def closed(self, reason):
        # Close the browser when spider is closed
        self.driver.quit()
