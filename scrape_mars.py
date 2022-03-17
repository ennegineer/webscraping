from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape the Mars News Site and collect the latest News Title and Paragraph Text.
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the first list item
    latestNews = soup.find('div', class_='list_text')

    # Get the latest news title
    newsTitle = latestNews.find_all('div', class_='content_title')[0].text

    # Get the news text
    newsPara = latestNews.find_all('div', class_='article_teaser_body')[0].text

    # Visit spaceimages-mars.com for the image
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Grab the featured image URL
    headerimg = soup.find('div', class_='header')
    featured_image_url = url + headerimg.find_all('img')[1]['src']

    # Store data in a dictionary
    mars_data = {
        "news_title": newsTitle,
        "news_para": newsPara,
        "featured_image_url": featured_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
