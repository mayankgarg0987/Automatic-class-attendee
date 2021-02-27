from selenium import webdriver
import time

driver=webdriver.Chrome()

# opening the target website
driver.get('https://cuchd.blackboard.com')

# entering username and password
searchbox=driver.find_element_by_xpath('//*[@id="user_id"]')
searchbox.send_keys('...')    # YOUR USERNAME GOES HERE
searchbox=driver.find_element_by_xpath('//*[@id="password"]')
searchbox.send_keys('...')    # YOUR PASSWORD GOES HERE

# time.sleep(1)
# 2 seconds delay
cookieButton=driver.find_element_by_xpath('//*[@id="agree_button"]')
cookieButton.click()

# clicking on sign-in button
searchButton=driver.find_element_by_xpath('//*[@id="entry-login"]')
searchButton.click()

time.sleep(10)
# clicking on the link to enter in the class
classLink=driver.find_element_by_xpath('//*[@id="course-link-_19145_1"]/h4').click()

time.sleep(8)
# clicking on 'join session'
joinSession=driver.find_element_by_xpath('//*[@id="sessions-list-dropdown"]/span').click()

time.sleep(1)
# clicking on 'course room'
courseRoom=driver.find_element_by_xpath('//*[@id="sessions-list"]/li/a/span').click()
