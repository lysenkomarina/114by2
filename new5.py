from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://114.by/")
assert "Расписание автобусов в Республике Беларусь" in driver.title
place_from = driver.find_element_by_css_selector('[placeholder="введите откуда выезжаем"]')
place_from.clear()
place_from.send_keys("Минск АВ-Центральный")
place_where = driver.find_element_by_css_selector('[placeholder="введите куда приезжаем"]')
place_where.clear()
place_where.send_keys("Лида") 
service = driver.find_element_by_css_selector('[footer [href="\/item\/kak-polzovatsia-servisom\/"]]')
service.click()
time.sleep(1000)
driver.close()
