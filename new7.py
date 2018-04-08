from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://114.by/")
assert "Расписание автобусов в Республике Беларусь" in driver.title
place_from = driver.find_element_by_css_selector('[placeholder="введите откуда выезжаем"]')
place_from.clear()
place_from.send_keys("Минск")
time.sleep(1)
chose_element = driver.find_element_by_xpath("//div[@id='id_tabs']/form[@class='form-route']/div/div[1]/ul[@class='list-group']/li[2]")
chose_element.click()
place_where = driver.find_element_by_css_selector('[placeholder="введите куда приезжаем"]')
place_where.clear()
place_where.send_keys("Лида") 
time.sleep(2)
chose_element2 = driver.find_element_by_css_selector('.form-route [class="col-sm-12 col-md-4"]:nth-of-type(3) .list-group-item:nth-of-type(1) [href]')
chose_element2.click()
poisk = driver.find_element_by_css_selector('[class="col-sm-12 hidden-md hidden-lg"] [type]')
poisk.click()
time.sleep(1000)
driver.close()
