from selenium import webdriver

#  Chrome浏览器
# browser = webdriver.Chrome()
# Firefox;浏览器
# browser = webdriver.Firefox()
# phantomjs
browser = webdriver.Phantomjs()
browser.get('http://www.google.cn/')
