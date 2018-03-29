import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://chp.tbe.taleo.net/chp02/ats/careers/jobSearch.jsp?act=redirectCws&cws=1&org=FHB')
time.sleep(5)

#figure out how many listings there are
searchButton = driver.find_element_by_name('tbe_cws_submit')
searchButton.click()
time.sleep(3)

#posting count
listingCount = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/b').get_attribute('innerHTML')
pageCount = int(listingCount)/100

i = 0
while i < pageCount:
    #create an html variable
    pageHTML = driver.find_element_by_tag_name('html')
    pageHTML = pageHTML.get_attribute('innerHTML')
    soup = bs.BeautifulSoup(pageHTML, 'lxml')
    table = table = soup.find('table', id="cws-search-results")
    for row in table.findAll('tr')[1:]:
        title = row.findAll('td')[0].text
        location = row.findAll('td')[1].text
        department = row.findAll('td')[2].text
        print(title + " " + location + " " + department)
    nextButton = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td[4]/input')
    nextButton.click()
    i += 1
