import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://boh.taleo.net/careersection/2/jobsearch.ftl?lang=en&portal=101430233')
time.sleep(10)

#figure out how many listings there are

pageHTML = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
soup = bs.BeautifulSoup(pageHTML, 'lxml')
contentCount = soup.find("span", {"id": "currentPageInfo"}).text
contentCount = contentCount.split("of ", 1)[1]
pageCount = int(contentCount)/25

i = 0
while i <= pageCount:
    pageHTML = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
    soup = bs.BeautifulSoup(pageHTML, 'lxml')
    contentCount = soup.find("span", {"id": "currentPageInfo"}).text
    contentCount = contentCount.split("of ", 1)[1]
    table = soup.find("table", {"id": "jobs"})
    for row in table.findAll('tr')[1:]:
        requisitionTitle = row.findAll('span')[0].text
        location = row.findAll('span')[1].text
        jobNumber = row.findAll('span')[2].text
        print(requisitionTitle + "|" + location + "|" + jobNumber)
    nextButton = driver.find_element_by_id('next')
    nextButton.click()
    time.sleep(3)
    i +=1
