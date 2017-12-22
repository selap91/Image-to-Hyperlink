from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t

driver = webdriver.Chrome('C:/Users/selap/PycharmProjects/ClickURL/chromedriver')
driver.implicitly_wait(3)

# get url
driver.get('https://trends.google.co.kr/trends/hottrends')
t.sleep(4)
html = driver.page_source
elem = driver.find_element_by_tag_name('body')

# open trend keywords during 1 year
days = 0
while days < 30:
    try:
        print(days)
        elem.send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_xpath("//div[@class='more-link-container']/div[@onclick='control.moreData()']").click()
        days += 1
    except:
        t.sleep(1)

test = driver.find_elements_by_xpath("//div[@class='hottrends-single-trend-title-container']/a")

# create csv file
f = open('C:/Users/selap/PycharmProjects/ClickURL/data/30trends.txt', 'w')

for s in test:
    print(s.get_attribute('href'))
    f.write(s.get_attribute('href')+'\n')
