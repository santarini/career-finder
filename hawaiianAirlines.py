import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4 as bs

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

#navigate to careers webpage
driver.get('https://rn11.ultipro.com/HAW1000/JobBoard/ListJobs.aspx')
time.sleep(1)

#figure out how many listings there are
listingCount = driver.find_element_by_xpath('//*[@id="PXForm"]/table[1]/tbody/tr/td/span[5]')
listingCount = listingCount.get_attribute('innerHTML')
pageCount = int(listingCount)/10

i = 1
while i < pageCount:
    #create an html variable
    pageHTML = driver.find_element_by_tag_name('html')
    pageHTML = pageHTML.get_attribute('innerHTML')
    soup = bs.BeautifulSoup(pageHTML, 'lxml')
    table = soup.findAll('table')[1]
    for row in table.findAll('tr')[1:]:
        postDate = row.findAll('td')[0].text
        requisitionNumber = row.findAll('td')[1].text
        title = row.findAll('td')[2].text
        department = row.findAll('td')[3].text
        city = row.findAll('td')[4].text
        state = row.findAll('td')[5].text
        partTime = row.findAll('td')[6].text
        print(postDate + " " + requisitionNumber + " " + title + " " + department + " " + city + " " + state + " " + partTime)
    ActionChains(driver).key_down(Keys.ALT).send_keys('n').perform()
    i += 1
