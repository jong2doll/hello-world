from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

url = 'https://www.naver.com/'

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe', options=options)
driver.get(url)

"""
selected_selector = driver.find_element_by_css_selector('div.home div.p a')
print("selected_selector.tag_name")
print(selected_selector.tag_name)
print("selected_selector.text")
print(selected_selector.text)
selected_selector.click()
"""

selected_tag_a = driver.find_element_by_css_selector('input#query')

selected_tag_a.send_keys('댕댕이')
selected_tag_a.send_keys(Keys.ENTER)
selected_tag_a = driver.find_element_by_css_selector('#lnb > div.lnb_group > div > ul > li:nth-child(2) > a')
selected_tag_a.click()

driver.execute_script('alert("멍멍!")')
print("test")

