from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import csv

keyword = 0
num_of_url = 0

driver = webdriver.Chrome('C:/Users/selap/PycharmProjects/ClickURL/chromedriver')
driver.implicitly_wait(3)

keyword_file = open('C:/Users/selap/PycharmProjects/ClickURL/data/30trends.txt', 'r')
url_file = open('C:/Users/selap/PycharmProjects/ClickURL/data/google_URL.csv', 'w', newline='')
wr = csv.writer(url_file, delimiter=',')

search = keyword_file.readlines()

for line in search:
    driver.get(line[:-1])
    t.sleep(2)
    page = 1

    while page < 12:
        try:
            elem = driver.find_element_by_tag_name('body')
            print(str(keyword) + " - " + str(page))
            urls = driver.find_elements_by_xpath("//h3[@class='r']/a")
            if not urls:
                continue
            else:
                wr.writerow(["DATA - " + str(keyword) + " - " + str(page)])
                for url in urls:
                    wr.writerow([url.get_attribute('href')])
                    num_of_url += 1
                    print("num_of_url = ", num_of_url)
                elem.send_keys(Keys.PAGE_DOWN)
                elem.send_keys(Keys.PAGE_DOWN)
                page += 1
                turn = 'Page ' + str(page)
                temp = driver.find_elements_by_xpath("//tr[@valign='top']/td/a")
                for i in temp:
                    if i.get_attribute('aria-label') == turn:
                        i.click()
                        break
                t.sleep(2)
        except:
            t.sleep(1)
    keyword += 1
