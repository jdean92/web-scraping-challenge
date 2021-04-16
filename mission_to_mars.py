from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def scrape_that():
    scrape_site = "https://redplanetscience.com/"
    
    browser.visit(scrape_that)

    html = browser.html

    soup = bs (html, 'html.parser')
    #display (soup)

    title_title = soup.find_all ("div", class_="content_title")
    #title_title

    title_title = title_title[3].text
    #title_title

    para_finder = soup.find_all ("div", class_="article_teaser_body")
    #para_finder

    para_finder = para_finder[3].text
    #para_finder


    get_pic = "https://spaceimages-mars.com/"
    browser.visit(get_pic)

    html = browser.html

    soup = bs (html, 'html.parser')
    #display (soup)

    print_image = soup.find("a",class_="showimg fancybox-thumbs")["href"]
    #print (print_image)

    url = get_pic+print_image
    #print (url)

    get_data = "https://galaxyfacts-mars.com/"
    html_read = pd.read_html(get_data)
    #display (html_read)

    table = html_read[1]
    #table

    table.colums=["facts","value"]
    back_html = table.to_html(index=False)
    #back_html


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)
    soup = bs(browser.html, 'html.parser')

    links = soup.find_all('a', class_='itemLink')

    image_data = []
    for l in links:
        try:
            browser.visit(url + l['href'])
            time.sleep(1)
            soup = bs(browser.html, 'html.parser')
            hemisphere_title = soup.find('h2', class_='title')
            hemisphere_link = soup.find('img', class_='wide-image')['src']
            hemisphere_dict = {'title': hemisphere_title.get_text(), 'img_url': hemisphere_link}
            image_data.append(hemisphere_dict)
        except TypeError:
            #print('Error')

    hemisphere_image_urls = []
    for element in image_data:
        if element not in hemisphere_image_urls:
            hemisphere_image_urls.append(element)
        
    hemisphere_image_urls





