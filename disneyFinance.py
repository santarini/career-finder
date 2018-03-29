import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://jobs.disneycareers.com/search-jobs?k=finance&alp=6252001&alt=2')
time.sleep(5)

#posting count
listingCount = driver.find_element_by_xpath('//*[@id="search-results"]/h1').get_attribute('innerHTML')
listingCount = listingCount.split("finance", 1)[0]
pageCount = int(listingCount)/15

i = 0
while i <= pageCount:
    #create an html variable
    pageTable = driver.find_element_by_id('search-results').get_attribute('innerHTML')
    soup = bs.BeautifulSoup(pageTable, 'lxml')
    table = table = soup.find('table')
    for row in table.findAll('tr')[1:]:
        title = row.findAll('h2')[0].text
        facility = row.findAll('span')[0].text
        location = row.findAll('span')[1].text
        print(title + " " + facility + " " + location)
    nextButton = driver.find_element_by_link_text('Next')
    nextButton.click()
    i += 1
